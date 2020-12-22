﻿# Youtube Scraper

Scrape Youtube Page without an API key. 

#to find html tags and use them to scrape data
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#to Convert a Python's list, dictionary or Numpy array to a Pandas data frame.
import pandas as pd 

#to Convert a Pandas data frame to Excel File.
import openpyxl



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
