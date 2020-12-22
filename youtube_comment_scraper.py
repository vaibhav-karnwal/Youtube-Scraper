import time
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup 
from requests_html import HTMLSession, HTML
from lxml.etree import ParserError
from credential import url

#list of elements to scrape
name_links=[]
names=[]
comment_dates=[]
votes=[]
comments=[]

#function to scroll from 0 position to end position
def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        time.sleep(.5)

        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(7)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

#calling chrome driver 
driver = webdriver.Chrome()
driver.get(f"{url}")
       
time.sleep(1)

scroll_to_bottom(driver)

page_source = driver.page_source

#scraping html page data 
soup = BeautifulSoup(page_source, 'lxml')
section=soup.findAll('ytd-comment-thread-renderer',attrs={'class':'style-scope ytd-item-section-renderer'})
for a in section:

    #for scraping user link
    link=a.find('a',attrs={'id':'author-text'})
    name_link=link['href']
    name_links.append(name_link)

    #for scraping user name
    name=a.find('span',attrs={'class':'style-scope ytd-comment-renderer'})
    names.append(name.get_text(strip=True))
    
    #for scraping date and time of comment
    comment_date=a.find('a', attrs={'class':"yt-simple-endpoint style-scope yt-formatted-string"})
    comment_dates.append(comment_date.get_text(strip=True))
    
    #for scraping vote of comment
    vote=a.find('span', attrs={'id':'vote-count-middle'})
    if(len(vote) == 0):
        vote ="0"
    votes.append(vote.get_text(strip=True))
     
    #for scraping comment
    comment_text=a.find('div',{'id':'content'})  
    comments.append(comment_text.get_text(strip=True))

#Appending all the list data to a pd dataframe 
df = pd.DataFrame({'Names':names,'comment dates':comment_dates,'User':name_links,'Votes':votes,'Comments':comments })
df.to_excel("comments_detail.xlsx",sheet_name='Sheet_name_1')   