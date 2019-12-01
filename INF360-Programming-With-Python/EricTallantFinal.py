# INF360 - Programming with Python
# Eric Tallant
# Midterm Project


"""
ONION ARTICLE FEED
Pulls 5 newest article headlines from the front page of the onion.
A dictionary is built that hold the title and url for each article
Display a menu with the titles to the user
User then selects an article number
Go to that article, pull the body, and display the text to the user

modules: requests, lxml, re, bs4, textwrap, twilio, schedule

install commands:
pip3 install beautifulsoup4
pip3 install textwrap
pip3 install twilio
pip3 install schedule
"""


import requests
import lxml
import re
from bs4 import BeautifulSoup
import textwrap
from twilio.rest import Client
import schedule


# use requests to pull the html from a url
def get_html(url):
    r1 = requests.get(url)
    return r1.content


# remove <tagName> and </tagName> from code
def remove_tags(tagName, code):
    # use a regex to split the html tags from the string
    codeReg = re.split('<' + re.escape(tagName) + '|">|</' + re.escape(tagName), str(code))

    # the text we want is the 3rd item in the list
    return codeReg[2]


# pull the href from an a tag
def extract_href(theUrl):
    # use a regex to extract the href url
    urlReg = re.split('href=\"|\">', str(theUrl))

    # the text we want is the 2nd item in the list
    return urlReg[1]


# print out 70 _ characters with whitespace on top and bottom
def page_break():
    print('\n' + '_' * 70 + '\n\n')


# wordwrap and print text with textwrap's default setting of 70 characters per line
def pretty_article(text):
    # pull out any comment lines in the html
    cleanText = re.sub("(<.*?>)", "", text)

    # use textwrap to separate body into list
    wrapper = textwrap.wrap(cleanText)

    # print each list item on new line
    for line in wrapper:
        print(line)


# there is an initial load time to grab the url's html. display a wait message
print('Retrieving new articles, please wait...\n')

# grab all of the html from the onion home page
homepage = get_html('https://www.theonion.com/')

# make a soup to parse homepage so that python can understand it
soup1 = BeautifulSoup(homepage, 'lxml')

# find every article title in the latest article div on the page
# these are organized by date so it will pull them in order from most recent
articles = soup1.find_all('h2', class_='leHuzq')

# listings is a dictionary that will hold all of the titles and urls
listings = {
    '1': {
        'title': '', 'url': ''
    },
    '2': {
        'title': '', 'url': ''
    },
    '3': {
        'title': '', 'url': ''
    },
    '4': {
        'title': '', 'url': ''
    },
    '5': {
        'title': '', 'url': ''
    }
}

# iterate through each article
# in each article add a value for title and url to listing
for article in range(0, 5):
    listings[str(article + 1)]['title'] = remove_tags('h2', articles[article])
    listings[str(article + 1)]['url'] = extract_href(articles[article].parent)


print('\nHere are the 5 most recent articles from The Onion')
page_break()

# loop through each article that homepage finds and print the result
for title in range(0, 5):
    titleText = remove_tags('h2', articles[title])
    urlText = extract_href(articles[title].parent)
    print(str(title + 1) + ': "' + titleText + '"\n')

page_break()


# print out full article until user no longer wishes to do so
while True:
    chooseArticle = input('Choose the number of the article you would like to read: ')

    print('Finding article... ')

    while not(0 < int(chooseArticle) < 6):
        chooseArticle = input('Please choose between 1 and 5: ')

    selectedArticle = get_html(listings[chooseArticle]['url'])
    soup2 = BeautifulSoup(selectedArticle, 'lxml')

    # try to search for the body of the article
    # if there is no body, remove_tags will return a bad index
    # in that case, send user link to the article
    try:
        articleText = remove_tags('p', soup2.find('p', class_='hJpRRP'))
        print('\n' + listings[chooseArticle]['title'] + '\n')
        pretty_article(articleText)
        page_break()
    except IndexError:
        print('This article has no text! Check it out on the web here:\n' + listings[chooseArticle]['url'])
        page_break()

    # ask user if they are finished reading
    askUser = input('Would you like to read another? (Y/N): ')
    if askUser.lower() == 'n' or askUser.lower() == 'no':
        print('\nThanks for reading!')
        break


"""
SMS FEED
The below code is for a daily sms feed 
after the user inputs their Twilio account details and a preferred time,
they will get a daily message with a new article
"""


askSMS = input('I can text you new articles every day at noon while this process runs. Interested? (Y/N)')

# prompt intro message if yes, otherwise exit program
if askSMS.lower() == 'y' or askSMS.lower() == 'yes':
    print('''
Great! 
Because there are mischievous people out there, you will need a Twilio account for this to work.
If you don't have an account, please sign up at https://www.twilio.com/login to get started.
''')
else:
    print('Kk, goodbye!')
    exit()

# get account info from Twilio
accountSID = input('Enter your account SID: ')
authToken = input('Enter your Auth Token: ')
twilioCli = Client(accountSID, authToken)
myTwilioNumber = input('Enter your Twilio number in format +15551234567: ')
myCellNumber = input('Enter you cellphone number in format +15551234567: ')

# set a daily action at noon using schedule 
schedule.every().day.at("12:00").do(
    # create and send message
    message=twilioCli.messages.create(
        body='\nHere is your latest article from The Onion:\n' + listings[chooseArticle]['url'],
        from_=myTwilioNumber,
        to=myCellNumber
    )
)
