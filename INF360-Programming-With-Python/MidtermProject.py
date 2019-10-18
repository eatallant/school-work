# INF360 - Programming with Python
# Eric Tallant
# Midterm Project

# PROJECT IDEA BLOCK ****ERASE THIS BEFORE TURNING IN*****
# imports: requests
# 
# User enters a website that they want info from. Use requests to verify that this is a real address
# if it is, get some kind of info, else give an error


import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.theonion.com/'

r1 = requests.get(url)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'lxml')

coverpage_news = soup1.find_all('h1', class_='leHuzq')

print(coverpage_news)
