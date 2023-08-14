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
from luu_function import driver, local, data, Logging, ValidateFailResultAndSystem



    

def access_menu_asset(domain_name):
   

    Logging("------------------------------------------------------B. Menu Asset------------------------------------------------------")
    driver.get(domain_name + "/asset/admin/category")
    time.sleep(3)
    Logging("-------------- Write Category Asset --------------")
    time.sleep(2)
    category_name_asset = driver.find_element_by_xpath(data["asset"]["txt_category_name_asset"])
    category_name_asset.send_keys(data["asset"]["name_category_asset"])
    Logging("1. Input Category Name successfully")
    input_description_asset = driver.find_element_by_xpath(data["asset"]["txt_description"])
    input_description_asset.send_keys(data["asset"]["content_description_category_asset"])
    Logging("2. Input Description successfully")
    click_org = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["org_user_asset"]))).click()
    Logging("3. Click User/Group  successfully")
    time.sleep(3)
    search_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["txt_search_dept_asset"])))
    search_dept.send_keys(data["asset"]["dept_name_search_asset"])
    search_dept.send_keys(Keys.RETURN)
    time.sleep(3)
    select_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["asset_select_user_1"]))).click()
    time.sleep(3)
    Logging("4. Click user successfully")
    add_user= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["icon_add_user_asset"]))).click() 
    time.sleep(2)
    Logging("5. Click Icon Add user successfully")
    btnt_save_add_user= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["btn_save_add_user"]))).click() 
    time.sleep(2)
    Logging("6. Click button Add user successfully")
    time.sleep(1)
    select_permisssion = Select(driver.find_element_by_xpath(data["asset"]["click_permisson_asset"]))
    select_permisssion.select_by_visible_text("Read/Write")
    Logging("7. Select  Permissison successfully")
    time.sleep(1)
    btn_save_add_category= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["btn_save_category"]))).click() 
    time.sleep(2)
    Logging("8. Click button Save successfully")
    time.sleep(1)
    btn_close_add_category= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["btn_close_asset_category"]))).click() 
    time.sleep(2)
    Logging("9. Click button Close successfully")
    time.sleep(1)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["select_folder_parent_asset"])))
    element.location_once_scrolled_into_view
    time.sleep(2)
    click_folder_parent= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["asset"]["select_folder_parent_asset"])))
    if click_folder_parent.is_displayed():
        Logging("Write Category Asset =>--------- PASS")
    else:
        Logging("Write Category Asset =>--------- FAIL")


    Logging("-------------- Write Category-Sub folder Asset --------------")

    









    time.sleep(2)
    #end_time = time.time()
    #loading_time = end_time - start_time
    #Logging(end_time - start_time)
    time.sleep(3)
    
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)
time.sleep(1)

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






