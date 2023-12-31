import time, json, random, openpyxl
import logging
from selenium import webdriver
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
from openpyxl import Workbook
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import pathlib
from pathlib import Path
import os
from sys import platform
import NQ_function
from framework_NQ import *
from NQ_login_function import driver, data, ValidateFailResultAndSystem, Logging, TesCase_LogResult#, TestlinkResult_Fail, TestlinkResult_Pass

#chrome_path = os.path.dirname(Path(__file__).absolute())+"\\chromedriver.exe"

n = random.randint(1,3000)
m = random.randint(3000,6000)
now = datetime.now()

def new_co_manage(domain_name):
    # driver.get(domain_name + "projectnew/projects")
    Logging(" ")
    PrintGreen('============ Menu Comanage ============')
    # Commands.Wait20s_ClickElement(data["new_comanage"]["comanage"])
    # time.sleep(10)
    # Commands.Wait20s_ClickElement(data["new_comanage"]["admin"])
    try:
        admin = Waits.Wait20s_ElementLoaded(data["new_comanage"]["admin"])
        if admin.is_displayed():
            Logging("- Account admin")
            admin.click()
            Logging("- Click setting admin") 
            admin_execution()
    except:
        Logging("- Account user")

#def manager():

def manager_add_status():
    text_status = data["new_comanage"]["manager_status"]["input_name"] + str(n)
    try:
        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_status"]["status"])
        time.sleep(3)
        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_status"]["button_add"])
        Logging("> Add new manager_status")
        Commands.Wait20s_InputElement(data["new_comanage"]["manager_status"]["input_status"], text_status)
        Commands.Wait20s_InputElement(data["new_comanage"]["manager_status"]["input_description"], text_status)
        Logging("- Input name - description")
        time.sleep(5)

        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_status"]["button_save"])

        Logging("=> Manager status have been create")
        time.sleep(5)
    
        Logging("** Check Manager status have been create")
        manager_status = Waits.Wait20s_ElementLoaded("//*[@id='wrap-content-project']//div[contains(@class, 'column') and contains(., '" + text_status + "')]")
        time.sleep(5)
        if manager_status.is_displayed():
            Logging("=> Manager status have been create")
            TesCase_LogResult(**data["testcase_result"]["new_comanage"]["status"]["pass"])
        else:
            Logging(">> Manager status have been create fail")
            TesCase_LogResult(**data["testcase_result"]["new_comanage"]["status"]["fail"])
            ValidateFailResultAndSystem("<div>[new_comanage]manager_status have been create fail </div>")
        time.sleep(5)

    except:
        pass

    return text_status

def manager_delete_status(text_status):
    Commands.ScrollDown
    try:
        Logging("** Delete status")
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//div[contains(@class, 'column') and contains(., '" + text_status + "')]//following-sibling::div//button[2]")
        Logging("- Select status to delete")
        Waits.Wait20s_ElementLoaded(data["new_comanage"]["manager_status"]["notify"])
        Logging("=> Delete status success")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_status"]["pass"])
        time.sleep(5)
    except:
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_status"]["fail"])
        pass

def manager_add_worktype():
    text_worktype = data["new_comanage"]["manager_worktype"]["input_name"] + str(n)
    try:
        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_worktype"]["worktype"])
        time.sleep(3)
        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_worktype"]["button_add"])
        Commands.Wait20s_InputElement(data["new_comanage"]["manager_worktype"]["input_status"], text_worktype)
        time.sleep(3)
        Commands.Wait20s_ClickElement(data["new_comanage"]["manager_worktype"]["button_save"])
        Logging("=> Create work type")
        time.sleep(3)

        Logging("** Check work type have been create")
        work_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='wrap-content-project']//div[contains(@class, 'column') and contains(., '" + text_worktype + "')]")))
        if work_type.is_displayed():
            Logging("=> Work type have been create")
            TesCase_LogResult(**data["testcase_result"]["new_comanage"]["work_type"]["pass"])
        else:
            Logging("=> Work type have been create fail")
            TesCase_LogResult(**data["testcase_result"]["new_comanage"]["work_type"]["fail"])
            ValidateFailResultAndSystem("<div>[Comanage]Work type have been create fail </div>")
            time.sleep(5)
    except:
        pass

    return text_worktype

def manager_delete_worktype(text_worktype):
    try:
        Logging("** Delete work type")
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//div[contains(@class, 'column') and contains(., '" + text_worktype + "')]//following-sibling::div//button[2]")
        Logging("- Select work type to delete")
        Waits.Wait20s_ElementLoaded(data["new_comanage"]["manager_worktype"]["notify"])
        Logging("=> Delete work type success")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_work_type"]["pass"])
        time.sleep(5)
    except:
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_work_type"]["fail"])
        pass

def manager_folder():
    project = data["new_comanage"]["managar_folders"]["project_name"] + str(n)
    try:
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["folder"])
        Logging("- Manager Folders")
        time.sleep(5)
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_add"])
        Commands.Wait20s_InputElement(data["new_comanage"]["managar_folders"]["input_project"], project)
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_confirm"])
        Logging("- Add folder successfully")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["folder"]["pass"])
        time.sleep(5)
    except:
        Logging("- Fail to add folder")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["folder"]["fail"])
        pass
    return project

def manager_subfolder(project):
    project_sub = data["new_comanage"]["managar_folders"]["project_name_sub"] + str(n)
    project_edit = data["new_comanage"]["managar_folders"]["project_name_edit"] + str(n)
    try:
        time.sleep(5)
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//span[contains(., '" + project + "')]")
        
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_add_sub"])
        Commands.Wait20s_InputElement(data["new_comanage"]["managar_folders"]["input_project"], project_sub)
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_confirm"])
        Logging("- Add sub folder")
        Waits.Wait20s_ElementLoaded(data["new_comanage"]["manager_status"]["notify"])
        time.sleep(5)
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//div[contains(@class, 'bd-b') and contains(., '" + project_sub + "')]//following-sibling::div//button[1]")
        
        Commands.Wait20s_Clear_Click_InputElement(data["new_comanage"]["managar_folders"]["input_project"], project_edit)
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_confirm"])
        time.sleep(5)
        Logging("- Edit name of folder")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["sub_folder"]["pass"])
        time.sleep(5)
    except:
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["sub_folder"]["fail"])
        pass
    return project, project_edit

def delete_sub_folder(project_edit):
    project = data["new_comanage"]["managar_folders"]["project_name"] + str(n)
    try:
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//span[contains(., '" + project + "')]//following-sibling::span")
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//span[contains(., '" + project_edit + "')]")
        Logging("- Select sub project")
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//li[3]//button")
        Logging("- Choose delete project")
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_confirm"])
        Logging("- Delete sub folder")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_sub_folder"]["pass"])
    except:
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_sub_folder"]["fail"])
        pass

def delete_folder(project):
    try:
        time.sleep(5)
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//span[contains(., '" + project + "')]")
        time.sleep(5)
        Commands.Wait20s_ClickElement("//*[@id='wrap-content-project']//li[3]//button")
        Commands.Wait20s_ClickElement(data["new_comanage"]["managar_folders"]["button_confirm"])
        Logging("- Delete folder")
        
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_folder"]["pass"])
    except:
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["delete_folder"]["fail"])
        pass

def admin_execution():

    try:
        text_status = manager_add_status()
    except:
        text_status = None

    if bool(text_status) == True:
        try:
            manager_delete_status(text_status)
        except:
            Logging(">> Can't continue execution")
            pass
    else:
        Logging(">> Manager status have been create fail")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["manager_status"]["fail"])
        pass

    try:
        text_worktype = manager_add_worktype()
    except:
        text_worktype = None

    if bool(text_worktype) == True:
        try:
            manager_delete_worktype(text_worktype)
        except:
            Logging(">> Can't continue execution")
            pass
    else:
        Logging("=> Work type have been create fail")
        TesCase_LogResult(**data["testcase_result"]["new_comanage"]["work_type"]["fail"])

    try:
        project = manager_folder()
    except:
        project = None

    if bool(project) == True:
        try:
            project_edit = manager_subfolder(project)
        except:
            Logging(">> Can't continue execution")
            pass 

        try:
            delete_sub_folder(project_edit)
        except:
            Logging(">> Can't continue execution")
            pass 

        try:
            delete_folder(project)
        except:
            Logging(">> Can't continue execution")
            pass    
    else:
        Logging(">> Folder create fail")
