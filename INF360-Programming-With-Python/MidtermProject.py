# INF360 - Programming with Python
# Eric Tallant
# Midterm Project

# PROJECT IDEA BLOCK ****ERASE THIS BEFORE TURNING IN*****
# imports: requests
# 
# Pulls new article headlines from the front page of the onion.
# User then selects an article number and the body of that article is queried and displayed


import requests
import lxml
import re
from bs4 import BeautifulSoup

url = 'https://www.theonion.com/'


r1 = requests.get(url)
homepage = r1.content

soup1 = BeautifulSoup(homepage, 'lxml')

# this will find every article title in the new article div on the page
articles = soup1.find_all('h1', class_='leHuzq')
articleLink = soup1.find_all('a', class_='sc-1out364-0')


for title in range(len(articles)):
  print(articleLink[title])
  print(articles[title])

# loop through each article that homepage finds and print the result
for title in range(len(articles)):

  # use a regex to remove the html tags from the string
  titleText = re.split('<|>', str(articles[title]))
  print(str(title + 1) + ': "' + titleText[2] + '"\n')










