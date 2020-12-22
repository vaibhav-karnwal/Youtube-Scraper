# Youtube Scraper

#Import Modules

<p>import time </p>
<p>import pandas as pd</p>
<p>import openpyxl</p>
<p>from selenium import webdriver</p>
<p>from selenium.webdriver.chrome.options import Options</p>
<p>from bs4 import BeautifulSoup </p>
<p>from requests_html import HTMLSession, HTML</p>
<p>from lxml.etree import ParserError</p>
<p>from credential import url</p>

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
				 
	
FOR PERSONAL USE ONLY: 
The Change Color Chrome Application is for non-commercial use only. You may not attempt to download.

## Screenshots

<img src="detail.PNG">

Feel free to contribute to fix any problems, or to submit an issue!
