from selenium import webdriver
from bs4 import BeautifulSoup
from Selenium.webdriver.chrome.service import Service
from csv

#initialize the chrome web driver 
driver = webdriver.chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#Fetching the web page 

#

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table element 
table = soup.find(id= 'simpleTable')

if table:
    #Extact column headers
 headers = [] 