import time, json, random
import logging
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException,NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
#from random import randint
import re,sys
#from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import luu_log_in,board_setting,project_setting,contact_setting,approval_admin,resource_add_category,builder_setting_admin,editor
#from luu_function import execution_log, fail_log, error_log, Logging,testcase_log
from luu_function import execution_log,Logging,testcase_log



def Luu_Execution(domain_name):
    error_menu = []
    #error_screenshot = []

    '''
    try:
        luu_log_in.log_in_domain(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_log_in.log_in_domain")
    '''
    
    

    try:
        board_setting.access_menu_board(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("board_setting.access_menu_board")
    
    try:
        project_setting.access_menu_project(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("project_setting.access_menu_project")
    
    try:
        contact_setting.access_menu_contact(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("contact_setting.access_menu_contact")
    
    try:
        approval_admin.access_menu_approval(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("approval_admin.access_menu_approval")
    
    try:
        resource_add_category.access_menu_resource(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("resource_add_category.access_menu_resource")
    
    try:
        builder_setting_admin.admin_menu_menubuilder(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("builder_setting_admin.admin_menu_menubuilder")

    try:
        builder_setting_admin.write_menu_menubuilder(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("builder_setting_admin.write_menu_menubuilder")
    
    

    try:
        editor.editor_menu_task(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("editor.editor_menu_task")
    
    luu_log = {
        "execution_log": execution_log,
        #"fail_log": fail_log,
        #"error_log": error_log,
        "error_menu": error_menu
    }

    return luu_log

def Luu_My_Execution(domain_name):
    
    luu_log_in.log_in_domain(domain_name)
    # board_setting.access_menu_board(domain_name)
    # project_setting.access_menu_project(domain_name)
    # contact_setting.access_menu_contact(domain_name)
    # approval_admin.access_menu_approval(domain_name)
    # resource_add_category.access_menu_resource(domain_name)
    # builder_setting_admin.admin_menu_menubuilder(domain_name)
    # builder_setting_admin.write_menu_menubuilder(domain_name)
    # editor.editor_menu_task(domain_name)


    luu_log = {
        "execution_log": execution_log,
        #"fail_log": fail_log,
        #"error_log": error_log
    }

    return luu_log
    

#Luu_My_Execution("http://tg01.hanbiro.net/ngw/app/#")

