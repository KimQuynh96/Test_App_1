import time, json, random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from random import randint
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import luu_function
from luu_function import local, data, Logging, ValidateFailResultAndSystem
from luu_function import driver


driver.implicitly_wait(5)
driver.set_window_size(1024, 600)
driver.maximize_window()

    

def log_in_domain(domain_name):
    '''
    #now = datetime.now()
    if platform == "linux" or platform == "linux2":
        driver = webdriver.Chrome("/usr/bin/chromedriver")
    else:
        driver = webdriver.Chrome(local + "\\chromedriver.exe")
    '''
       
    # A. LOG IN
    Logging("----------------------------------------------------------LOG IN-------------------------------------------------")
    Logging("1. Access Log in page")
    driver.maximize_window()
    #driver.get(data["login_page"])
    driver.get(domain_name)
    #start_time = time.time()
    driver.implicitly_wait(50)
    username = driver.find_element_by_id("log-userid")
    username.send_keys(data["hanbiro_user"])
    Logging("2. Input ID ")    
    frame_element = driver.find_element_by_id("iframeLoginPassword")
    driver.switch_to.frame(frame_element)
    password = driver.find_element_by_id("p")
    password.send_keys(data["hanbiro_password"])
    driver.switch_to.default_content()
    Logging("3. Input Password ")  
    submit = driver.find_element_by_id("btn-log")
    submit.send_keys(Keys.RETURN)
    Logging("4. Enter Login  ")
    driver.implicitly_wait(5)



    # Define login status
    try:
        log_in_alert = driver.find_element_by_xpath("//i[@class='ace-icon fa fa-warning orange bigger-110']")
        if log_in_alert.is_displayed():
            if  "The ID or password you entered is incorrect.(2)" or "You do not have permission to access."  in driver.page_source:
                Logging("5. Fail to log in with alert:" + log_in_alert.text)
                Logging("5. Test case status: fail")
                exit(0)
            elif log_in_alert.text == "false":
                Logging("5. Fail to log in with alert:" + log_in_alert.text)
                Logging("5. Test case status: fail")
                exit(0)
    except WebDriverException:
        Logging("5. Log In successfully ")
    time.sleep(1)
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["turn_off"]))).send_keys(Keys.RETURN)
        print("- Close pop up Successfully")
    except:
        print("- Don't show pop up")
    time.sleep(1)

    # Langugae is used


    if 'Notifications' in driver.page_source :
        Logging("2. English language is used")
    else:
        Logging("2. Other Languages")
        click_avatar = driver.find_element_by_xpath("//img")
        click_avatar.click()
        time.sleep(5)
        click_setting = driver.find_element_by_xpath(data["sidebar_settings"])
        click_setting.click()
        click_list_language = driver.find_element_by_xpath("//div[@id='sidebar_settings']/div/select")
        click_list_language.click()
        select_lang = Select(driver.find_element_by_xpath("//select[@id='set-lang']"))
        select_lang.select_by_visible_text("English")
        apply=driver.find_element_by_xpath("//button[@class='btn btn-sm btn-primary']")
        apply.click()



    

    

def is_Displayed(driver,xpath):
    try:
        driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    
def so(total):
    num = re.sub(r'\D', "", total)
    return int(num)



'''

with open(local+'\\'+'luu_board.txt','w') as board:
    domain="http://qa.hanbiro.net"
    access_menu_board(domain,board)



result=open(local+'\\result.txt','r')
file_result=result.read()
Logging(file_result)

'''






