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
from luu_function import driver, local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Yellow,Red,Green,Commands



    

def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Contact------------------------------------------------------")
    driver.get(domain_name + "/addrbook/list/org_0/")
    time.sleep(1)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["contact"]["admin_contact"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin


def contact_create_folder(domain_name):
    
    time.sleep(3)
    Logging("------------------------------------------------------C. Menu Contact------------------------------------------------------")
    #driver.get(domain_name + "/addrbook/list/org_0/")  
   
    '''
    search_dept = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["textbox_search_dept_contact"])))
    search_dept.send_keys(data["contact"]["dept_name_search"])
    search_dept.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["loading_dialog"])))
    select_user = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_01"])))
    select_user.click()
    select_user_2 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_02"])))
    select_user_2.click()
    select_user_3 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_03"])))
    select_user_3.click()
    
    '''

    try:
        Commands.Wait10s_ClickElement(data["contact"]["hide_list_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["setting_contact"])
        time.sleep(2)
        Logging("2. Click list My Company successfully")  
        Commands.Wait10s_ClickElement(data["contact"]["folder_my_contacts"])  
        Commands.Wait10s_InputElement(data["contact"]["textbox_folder_name"],data["contact"]["folder_title"])
        time.sleep(2)
        Commands.Wait10s_InputElement(data["contact"]["textbox_description"],data["contact"]["title_description"])
        Logging("6. Input Description successfully" + " :  " +  data["contact"]["title_description"] )
        Commands.Wait10s_ClickElement(data["contact"]["turn_on_share"]) 
        Commands.Wait10s_ClickElement(data["contact"]["click_org_contact"])
        time.sleep(1)

        try:
            Commands.Wait10s_ClickElement(data["contact"]["share_invite_user_dept"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["click_icon_add_user"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["save_add_user"])
            Logging("7. Select user Share successfully")
            try:
                check_add_user_share = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_add_user_contact"])))
                Logging("8. Add User successfully")
                time.sleep(1)
            except WebDriverException:
                Logging("Add User Share => Fail")
        except WebDriverException:
            Commands.Wait10s_ClickElement(data["contact"]["home_contact_add_user"])
        time.sleep(1)
        try:
            Commands.Selectbox_ByVisibleText(data["contact"]["select_permission"],data["contact"]["select_per_contact"])
            Logging("8. Select  Permissison successfully")
            time.sleep(1)
        except WebDriverException:
            Logging(" => Not show invite users")
            #Commands.Wait10s_ClickElement(data["contact"]["home_contact_add_user"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["save_folder_my_contact"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("9. Save folder successfully")
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["show_folder_contact"])))
        Logging(Green("Show Folder Contact successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_folder_contact"]["pass"])
    except WebDriverException:
        Logging("14. Delete User Managers Fail")
        Logging(Red("Show Folder Contact Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Show Folder Contact successfully </div>")
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_folder_contact"]["fail"])


def contact_create_subfolder(domain_name):    

    Logging("---------------- Write SubFolder My Contact----------------")
    try:
        Commands.Wait10s_ClickElement(data["contact"]["click_list_my_contact"])
        Commands.Wait10s_ClickElement(data["contact"]["select_parent_folder_contact"])
        time.sleep(1)
        Logging("10. Select Parent folder successfully")
        Commands.Wait10s_InputElement(data["contact"]["input_sub_folder_contacts"],data["contact"]["subfolder_name"])
        Logging("11. Input subfolder Name successfully" + " :  " + data["contact"]["subfolder_name"] )
        Logging("11. Save Subfolder successfully")
        Commands.Wait10s_ClickElement(data["contact"]["save_subfolder_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("12. Save folder successfully")
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
        time.sleep(2)
        try:
            select_sub_folder_contact = driver.find_element_by_xpath(data["contact"]["show_sub_folder"])
            Logging(Green("Write SubFolder My Contact => PASS"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["write_subfolder_contact"]["pass"])
        except WebDriverException:
            Logging(Red("Write SubFolder My Contact => FAIL"))
            ValidateFailResultAndSystem("<div>[Contact]Write SubFolder My Contact </div>")
            TestCase_LogResult(**data["testcase_result"]["contact"]["write_subfolder_contact"]["fail"])
    except WebDriverException:
        Logging("Not show folder parent")


    Logging("---------------- Delete SubFolder My Contact----------------")

    try:
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["select_subfolder_contact_delete"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_icon_delete_subfolder_contact"])
        Commands.Wait10s_ClickElement(data["contact"]["click_ok_button"])
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        time.sleep(1)
        Logging("13. Delete Subfolder successfully")
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
        time.sleep(1)
        TestCase_LogResult(**data["testcase_result"]["contact"]["delete_subfolder_contact"]["pass"])
    except WebDriverException:
        Logging("Not show subfolder ")
        TestCase_LogResult(**data["testcase_result"]["contact"]["delete_subfolder_contact"]["pass"])
        Logging(Red("1.Delete SubFolder My Contact =>  FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Write SubFolder My Contact </div>")
        TestCase_LogResult(**data["testcase_result"]["contact"]["delete_subfolder_contact"]["fail"])
    time.sleep(1)

def contact_edit_folder(domain_name):    
    Logging("---------------- Edit Folder My Contact---------------")
    try:
        Commands.Selectbox_ByVisibleText(data["contact"]["edit_permisssion_contacts"],data["contact"]["edit_permission_contact"])
        #select_permisssion = Select(driver.find_element_by_xpath(data["contact"]["edit_permisssion_contacts"]))
        #select_permisssion.select_by_visible_text("Read/Write")
        Commands.Wait10s_ClickElement(data["contact"]["save_folder_contact_edit"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("14. Edit folder successfully")
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        Logging(Green("Edit Folder Board successfully => PASS"))
    except WebDriverException:
        Logging(Red("Edit Folder Board Fail => FAIL"))
       

def contact_delete_folder(domain_name):    
    Logging("---------------- Delete  Folder Parent---------------")
    try:
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_icon_delete_subfolder_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_ok_button"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("15. Delete folder Parent successfully")
        time.sleep(4)
    except WebDriverException:
        Logging(Red("Delete folder => FAIL"))



    
def contact_manager_folder(domain_name):

    Logging("----------------------------------- Manage Company Folders-----------------------------------")
    driver.refresh()
    time.sleep(10)
    try:
        Commands.Wait10s_ClickElement(data["contact"]["admin_contact"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_manager_company_folder"])
        time.sleep(4)
        Logging("1. Click  Manage Company Folders successfully")
        Commands.Wait10s_ClickElement(data["contact"]["folder_public_contact"])
        Logging("2. Click  Public Contact successfully")
        Commands.Wait10s_InputElement(data["contact"]["textbox_folder_name"],data["contact"]["folder_title"])
        time.sleep(2)
        Logging("----------------------------------- Share Folder -----------------------------------")
        Commands.Wait10s_ClickElement(data["contact"]["check_radio_share"])
        Logging("1.Click Radio Share =>Pass")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
        Logging("2.Click Organization =>Pass")
        time.sleep(2)
        try:
            Commands.Wait10s_ClickElement(data["contact"]["select_dept_manager_company"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_manager"])
            time.sleep(2)
            try:
                check_add_user_manager = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_add_user_manager_in_org"])))
                Logging("8. Add User successfully")
                time.sleep(1)
            except WebDriverException:
                Logging("Add User Share => Fail")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["btn_save_add_user_mana"])
        except WebDriverException:
            Commands.Wait10s_ClickElement(data["contact"]["home_contact_add_user_manager"])
        time.sleep(1)
        try:
            Commands.Selectbox_ByVisibleText(data["contact"]["click_list_permission"],data["contact"]["select_permisson"])
            Logging("8. Select  Permissison successfully")
            time.sleep(1)
        except WebDriverException:
           Logging(" => Not show User to manage")

        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_manager_folder"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("9. Save folder successfully")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
        Commands.scroll_view(data["contact"]["pull_the_scroll_bar_view"])
        time.sleep(1)
        try:
            follder_manager_company = driver.find_element_by_xpath(data["contact"]["pull_the_scroll_bar_view"])
            Logging(Green("Create Manage Company Folders => PASS"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["manager_company_contact"]["pass"])
        except WebDriverException:
            Logging(Red("Create Manage Company Folders => FAIL"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["manager_company_contact"]["fail"])
        time.sleep(1)  
    except WebDriverException:
        Logging(Red("Manage Company Folders => FAIL"))



def contact_manager_edit_folder(domain_name):
    Logging("----------------------------------- Edit Folder -----------------------------------")
    try:
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["contact"]["pull_the_scroll_bar_view"])
        time.sleep(3)
        Commands.Wait10s_InputElement(data["contact"]["txt_about_folder"],data["contact"]["content_about_folder"])
        Logging("1. Input Content successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_manager_folder"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
        Logging("2. Save folder successfully")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
        Commands.scroll_view(data["contact"]["pull_the_scroll_bar_view"])
        time.sleep(1)
        try:
            follder_manager_company = driver.find_element_by_xpath(data["contact"]["pull_the_scroll_bar_view"])
            Logging(Green("Edit Folder => PASS"))
        except WebDriverException:
            Logging(Red("Edit Folder => FAIL"))
    except WebDriverException:
        Logging(Red("Not show folder Edit "))
        


def contact_manager_delete_folder(domain_name):    
    Logging("----------------------------------- Delete Manage Company Folders-----------------------------------")
    try:
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["pull_the_scroll_bar_view"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_delete_folder_company"])
        driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_ok_delete_folder_manager"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        time.sleep(1)
        Logging("=> Delete Manage Company Folders => PASS")
        time.sleep(4)
    except WebDriverException:
        Logging(Red("Delete Manage Company Folders=> FAIL"))




def contact_setting_general(domain_name):

    Logging("----------------------------------- Admin Settings - General-----------------------------------")
    Logging("----------------------------------- 1. General - Display Organization Contacts -----------------------------------")

    try:
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
        Logging("1. Click Admin Settings successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["select_view_contact_list"])
        Logging("2. Click Display Organization Contacts : LIST  successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
        Logging("3. Click Display Organization Contacts : LIST  successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        Logging("4. Click Close  successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["select_my_company"])
        Logging("5. Click My Company successfully")
        driver.refresh()
        time.sleep(9)
        if 'A new version is available! Do you want to update?' in driver.page_source :
            Commands.Wait10s_ClickElement(data["contact"]["btn_update_version"])
            #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["contact"]["btn_update_version"])))
            #update_verion = driver.find_element_by_xpath(data["contact"]["btn_update_version"])
            #update_verion.click()
            Logging("=> Update Version =>  SHOW")
            time.sleep(6)
            driver.get(domain_name + "/addrbook/list/org_0/")
            time.sleep(3)
        else:
            Logging("=> Update Version =>  Not show")
        if 'Name' in driver.page_source :
            Logging(Green("=> Select Display Organization Contacts : LIST =>  PASS"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["pass"])
        else:
            Logging(Red("=> Select Display Organization Contacts : LIST =>  FAIL"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["fail"])
        time.sleep(2)
        try:
            click_admin_settings = driver.find_element_by_xpath(data["contact"]["click_admin_setting"])
            Logging("Show Setting ")
        except WebDriverException:
            Logging("Not Show setting")
            Commands.Wait10s_ClickElement(data["contact"]["admin_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
        Commands.Wait10s_ClickElement(data["contact"]["select_view_contact_photo"])
        time.sleep(2)
        Logging("6. Click Display Organization Contacts : PHOTO  successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        Logging("7. Click Close  successfully")
        time.sleep(2)

    except WebDriverException:
        Logging(Red("Display Organization Contacts=> FAIL"))


def contact_setting_general_hide_my_contact(domain_name):
    Logging("----------------------------------- 1. General - Hide My Contact -----------------------------------")
    try:
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["hide_my_contacts"])
        Logging("7. Click Hide My Contacts  successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        Commands.Wait10s_ClickElement(data["contact"]["manage_favorites"])
        Logging("1. Click Manage Favorites successfully")
        driver.refresh()
        time.sleep(8)
        if 'A new version is available! Do you want to update?' in driver.page_source :
            Commands.Wait10s_ClickElement(data["contact"]["btn_update_version"])
            Logging("=> Update Version =>  SHOW")
            time.sleep(5)
            driver.get(domain_name + "/addrbook/list/org_0/")
            time.sleep(3)
        else:
            Logging("=> Update Version =>  Not show")
        time.sleep(2)
        try:
            check_data_hide_my_contact = driver.find_element_by_xpath(data["contact"]["check_data_hide_my_contact"])
            Logging(Green("Hide My Contact => PASS"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["pass"])
        except WebDriverException:
            Logging(Red("Hide My Contact => FAIL"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["fail"])
        Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
        time.sleep(1)
        Logging("1. Click Admin Settings successfully")
        Commands.Wait10s_ClickElement(data["contact"]["hide_my_contacts"])
        time.sleep(1)
        Logging("2. Click Hide My Contacts  successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        time.sleep(1)
    except WebDriverException:
        Logging("7. Click Close  successfully")

def contact_setting_general_public_contact_manager(domain_name):
    
    Logging("----------------------------------- Admin Settings - Public Contacts Manager-----------------------------------")
    
    try:
        Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
        Logging("1. Click Organization successfully")
        Commands.Wait10s_ClickElement(data["contact"]["select_user_public_dept"])
        '''
        search_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["txt_search_user_public"])))
        search_dept.send_keys(data["contact"]["dept_name_search"])
        search_dept.send_keys(Keys.RETURN)
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["loading_dialog"])))
        select_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_public"]))).click()
        '''
        Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_public"])
        time.sleep(5)
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_public"])
        Logging("2. Select user Public successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_public_contact"])
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        Logging("=> Select Public Contacts Manager => PASS")
        time.sleep(3)
    

        time.sleep(3)
        Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["icon_delete_all_user_public"])
        time.sleep(5)

        '''
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public_delete"])))
        element.location_once_scrolled_into_view
        time.sleep(1)
        select_user_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public_delete"]))).click()
        Logging("3. Select user Public successfully")
        icon_delete_user = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["icon_remove_user_public"]))).click()
        '''

        Logging("4. Click icon remove user successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_public"])
        Logging("5. click save successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_public_contact"])
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
        time.sleep(2)


    except WebDriverException:
        Logging("=> Public Contacts Manager=> Fail")

def contact_manage_favorites(domain_name):
    Logging("----------------------------------- Manage Favorites-----------------------------------")


    try:
        Commands.Wait10s_ClickElement(data["contact"]["manage_favorites"])
        Logging("1. Click Manage Favorites successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["icon_add_favorites_list"])
        Logging("2. Click icon Favorites List successfully")
        time.sleep(2)
        Commands.Wait10s_InputElement(data["contact"]["txt_folder_name_favorites"],data["contact"]["folder_name_favorites_list"])
        Logging("3. Input Folder Name Favorites successfully")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["click_icon_org"])
        Logging("4. Click Organization successfully")
        time.sleep(4)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_favorites_contact_global3"])))
            Logging("=> Domain Global3")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["select_dept_favorites_contact_gloabl3"])
        except WebDriverException:
            Logging("=>NOT Domain Global3")
            Commands.Wait10s_ClickElement(data["contact"]["select_dept_favorites_contact"])
        try:
            Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_favorites"])
            try:
                check_add_user_manager = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_add_user_favorites_in_org"])))
                Logging("8. Add User successfully")
            except WebDriverException:
                Logging("NOt show user in Dept")
                Commands.Wait10s_ClickElement(data["contact"]["home_contact_add_user_manager_favarites"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_favorites"])
        except WebDriverException:
            Commands.Wait10s_ClickElement(data["contact"]["home_contact_add_user_manager_favarites"])
        time.sleep(1)
        
        Logging("5. Select user Favorites successfully")
        Commands.Wait10s_InputElement(data["contact"]["txt_description_add_folder"],data["contact"]["content_description_add_folder"])
        Logging("6. Input Description successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_contact_favorites"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_favorites"])
        Logging("7. Save Folder Manage Favorites successfully")
        time.sleep(1)
        if 'Contact Favorites' in driver.page_source :
            Logging(Green("=> Manage Favorites =>  PASS"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["contact_favorites"]["pass"])
        else:
            Logging(Red("=> Manage Favorites =>  FAIL"))
            TestCase_LogResult(**data["testcase_result"]["contact"]["contact_favorites"]["fail"])
    except WebDriverException:
        Logging("Manage Favorites => Fail")

    Logging("-----------------------------------Delete Manage Favorites-----------------------------------")
    try:
        Commands.Wait10s_ClickElement(data["contact"]["select_folder_favorites_delete"])
        Logging("1. Click Folder Favorites Delete successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_delete_folder_favorites"])
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_ok_folder_favorites"])
        Logging("3. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_favorites"])
        Logging("4. Click button Close successfully")
        Logging("5. Delete Manage Favorites successfully")
        time.sleep(1)
    except WebDriverException:
        Logging("5. Delete Manage Favorites Fail")

def access_menu_contact(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)
    
    if admin == True:
        try:
            result_folder_parent = True
            contact_create_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)

        if result_folder_parent == True :
            try:
                contact_create_subfolder(domain_name)
                Logging("create folder successfully")
            except WebDriverException:
                Logging("fail to create subfolder")
            time.sleep(1)
            try:
                contact_edit_folder(domain_name)
                Logging("Edit folder successfully")
            except WebDriverException:
                Logging("Edit Folder Fail")
            time.sleep(1)
            try:
                contact_delete_folder(domain_name)
                Logging("Delete folder successfully")
            except WebDriverException:
                Logging("fDelete folder Fail")
            time.sleep(1)


        
    else:
        Logging("Account is not admin")
        try:
            contact_create_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)
        try:
            contact_create_subfolder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create subfolder")
        time.sleep(1)
        try:
            contact_edit_folder(domain_name)
            Logging("Edit folder successfully")
        except WebDriverException:
            Logging("Edit Folder Fail")
        time.sleep(1)
        try:
            contact_delete_folder(domain_name)
            Logging("Delete folder successfully")
        except WebDriverException:
            Logging("fDelete folder Fail")
        time.sleep(1)
    


    if admin == True:
        
        
        
        
        try:
            contact_manager_folder(domain_name)
            Logging("Create Manager folder successfully")
        except WebDriverException:
            Logging("Fail to Manager folder")
        time.sleep(1)
        



        try:
            contact_manager_edit_folder(domain_name)
            Logging("Edit Manager folder successfully")
        except WebDriverException:
            Logging("Edit Manager folder Fail")

        time.sleep(1)

        try:
            contact_manager_delete_folder(domain_name)
            Logging("Delete Manager folder successfully")
        except WebDriverException:
            Logging("Delete Manager folder Fail")

        time.sleep(1)

        
    else:
        Logging("1. Create Manager folder => Account is not admin")





    if admin == True:
        try:
            contact_setting_general(domain_name)
            Logging("Create Settings General  successfully")
        except WebDriverException:
            Logging("Settings General")
        time.sleep(1)


        try:
            contact_setting_general_hide_my_contact(domain_name)
            Logging("Create Settings General - Hide My Contact successfully")
        except WebDriverException:
            Logging("Create Settings General - Hide My Contact Fail")
        time.sleep(1)


        try:
            contact_setting_general_public_contact_manager(domain_name)
            Logging("Create Settings General - Hide My Contact successfully")
        except WebDriverException:
            Logging("Create Settings General - Hide My Contact Fail")
        time.sleep(1)


    else:
        Logging("2. Create Settings General  => Account is not admin")
    

    if admin == True:
        try:
            contact_manage_favorites(domain_name)
            Logging("Create Manage Favorites successfully")
        except WebDriverException:
            Logging("Fail to Manage Favorites")
    else:
        Logging("Account is not admin")
        try:
            contact_manage_favorites(domain_name)
            Logging("Create Manage Favorites successfully")
        except WebDriverException:
            Logging("Fail to Manage Favorites")

    





    time.sleep(2)
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






