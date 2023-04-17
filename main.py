from __future__ import with_statement
from datetime import date
import subprocess
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setting up the webdriver with headless Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

print("Enter the site you want to scrape. (with http)")
site = input(">_ ")

print ("Scraping "+ site)

# Navigating to the webpage with dynamically generated content
url = site
driver.get(url)

# Getting the page source after JavaScript has executed
html_content = driver.page_source

# Creating the BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Finding all the links on the page
links = soup.find_all('a')

# Printing the link text and URLs
for link in links:
    print(link.get('href'))

# Screenshot the page
today = date.today()
filename = 'scraped_screenshots/screenshot-{}.png'.format(today.strftime('%Y-%m-%d'))
driver.save_screenshot(filename)

# Saving scraped text
today = date.today()
filename = 'scraped_text/scraped-{}.txt'.format(today.strftime('%Y-%m-%d'))
with open(filename, 'w') as file:
    file.write(str(soup))

# Closing the webdriver instance
driver.quit()



