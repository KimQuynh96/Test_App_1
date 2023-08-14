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
import time
import pathlib
from pathlib import Path
import os
from sys import platform
import luu_function
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Red,Yellow,Green,Commands
from luu_function import driver
# Page



def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------Menu Resource------------------------------------------------------")
    driver.get(domain_name + "/resource/list/list_0/")
    time.sleep(1)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["add_resource"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin


def resource_add_category(domain_name):
    
    #driver.get(domain_name + "/resource/list/list_0/")
    #access_menu_menu_resource = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["resource"]["menu_resource"])))
    #access_menu_menu_resource.click()
    
    Logging("1. Access Menu Resource successfully")
    Logging("--------------------- Add Category Conference Room   ---------------------")
    try:
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["add_resource"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_add_resource"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus"])
        Logging("3.Click Icon Plus successfully")
        Commands.Wait10s_ClickElement(data["resource"]["select_type"])
        Logging("4.Select Type Category successfully")
        Commands.Wait10s_ClickElement(data["resource"]["select_type"])
        Logging("4.Select Type Category successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_category_name"],data["resource"]["input_category_name"])
        Logging("5. Input Category Name successfully" + " :  " + data["resource"]["input_category_name"])
        Commands.Wait10s_ClickElement(data["resource"]["btn_save_resource_name"])
        time.sleep(1)
        Logging("A. Add Category Conference Room successfully")
        Commands.scroll_view(data["resource"]["pull_the_scroll_bar"])
        time.sleep(2)
        #forder_hanbiro_room = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["resource"]["select_category_add"])))
        Logging(Green("Add Category Hanbiro Room =>-------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_room"]["pass"])
    except WebDriverException:
        Logging(Red("Add Category Hanbiro Room =>-------- FAIL"))
        ValidateFailResultAndSystem("<div>[Resource]Add Category Conference Room </div>")
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_room"]["fail"])




    try:
        Logging("--------------------- Add Category Vehicle   ---------------------")
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus"])
        Logging("1.Click Icon Plus successfully")
        Commands.Wait10s_ClickElement(data["resource"]["select_type_vehicle"])
        Logging("2.Select Type Category successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_category_name"],data["resource"]["input_category_name_vehicle"])
        Logging("3. Input Category Name successfully" + " :  " + data["resource"]["input_category_name_vehicle"])
        Commands.Wait10s_ClickElement(data["resource"]["btn_save_resource_name"])
        Logging("A. Add Category Vehicle successfully")
        Commands.scroll_view(data["resource"]["pull_the_scroll_bar"])
        time.sleep(2)
        Logging(Green("Add Category Vehicle =>--------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_vehicle"]["pass"])
    except WebDriverException:
        Logging(Red("Add Category Vehicle =>--------- FAIL"))
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_vehicle"]["fail"])



    Logging("--------------------- Add Category Normal   ---------------------")


    try:

        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus"])
        Logging("1.Click Icon Plus successfully")
        Commands.Wait10s_ClickElement(data["resource"]["select_type_normal"])
        Logging("2.Select Type Category successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_category_name"],data["resource"]["input_category_name_normal"])
        Logging("3. Input Category Name successfully" + " :  " + data["resource"]["input_category_name_normal"])
        Commands.Wait10s_ClickElement(data["resource"]["btn_save_resource_name"])
        Logging("A. Add Category Normal successfully")
        Commands.scroll_view(data["resource"]["pull_the_scroll_bar"])
        time.sleep(2)
        Logging(Green("Add Category Normal  =>--------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_normal"]["pass"])
    except WebDriverException:
        Logging(Red("Add Category Normal  =>--------- FAIL"))
        TestCase_LogResult(**data["testcase_result"]["resource"]["add_category_normal"]["fail"])





def resource_add_resource_category_room(domain_name):
    Logging("--------------------- Add  Reservation System Resource Meeting Room - GW-733 : Define resource in Reservation System  ---------------------")
    time.sleep(1)
    #click_click_list_collapsed = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["list_collapsed"])))
    #click_click_list_collapsed .click()
    #Logging("1.Click List Collapsed   successfully")
    #time.sleep(1)
    #click_list_icon_add_resource = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["add_resource"])))
    #click_list_icon_add_resource .click()
    #Logging("2.Click List Add Resource   successfully")
    #time.sleep(1)
    #select_add_resource = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["select_add_resource"])))
    #select_add_resource .click()
    
    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["pull_the_scroll_bar"])))
    #element.location_once_scrolled_into_view
    

    try:

        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(1)
        Logging("3.Click Add Resource   successfully")
        Commands.Wait10s_ClickElement(data["resource"]["select_category_add"])
        Logging("4.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus_meeting_room"])
        Logging("5.Click Icon Plus successfully")
        Logging("A. GW-733 : Define resource in Reservation System successfully")
        time.sleep(2)
        if 'Reservation System' in driver.page_source :
            Logging(Green("1. Define resource in Reservation System => --------PASS"))
        else:
            Logging(Red("1. Define resource in Reservation System => --------FAIL"))
            ValidateFailResultAndSystem("<div>[Resource]Define resource in Reservation System </div>")
            
        
        Logging("--------------------- Save Add Resource Meeting Room GW-737 : Add Person in Charge  ---------------------")
        Commands.Wait10s_InputElement(data["resource"]["txt_conference_room_name"],data["resource"]["conference_room_name"])
        Logging("=>  Input Resource Name successfully" + " :  " + data["resource"]["conference_room_name"])
        Logging("6.Input Conference Room Name successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_description_conference_room_name"],data["resource"]["description_conference_room_content"])
        Logging("=>  Input Description successfully" + " :  " + data["resource"]["description_conference_room_content"])
        Logging("7.Input Description Reservation System successfully")

        Logging("--------------------- Save Add Resource Meeting Room -GW-739 : Upload resource image   ---------------------")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["resource"]["txt_upload_image_file"])))
        get_file.send_keys(luu_function.file_img)
        time.sleep(1)
        Logging("A. GW-739 : Upload resource image successfully")
        time.sleep(2)
        if 'signature_mage' in driver.page_source :
            Logging(Green("1.Upload resource image=> ---------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["upload_resource_image"]["pass"])
        else:
            Logging(Red("1.Upload resource image=> ---------- FAIL"))
            ValidateFailResultAndSystem("<div>[Resource]Upload resource image</div>")
            TestCase_LogResult(**data["testcase_result"]["resource"]["upload_resource_image"]["fail"])



        Logging("--------------------- Save Add Resource Meeting Room -GW-740 : Select user with permission to reserve   ---------------------")
        try:
            Commands.Wait10s_ClickElement(data["resource"]["click_org_user_permisson"])
            Logging("11. Add Users with Permission to Reserve Conference Room successfully")
            Commands.Wait10s_InputElement_return(data["resource"]["txt_search_org_permisson"],data["resource"]["search_user_permission"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["resource"]["select_user_permisson_2"])
            Commands.Wait10s_ClickElement(data["resource"]["icon_add_user_per"])
            time.sleep(1)
            Logging("12.Add User  successfully")
            Commands.Wait10s_ClickElement(data["resource"]["click_button_save_per"])
            Logging("A. GW-740 : Select user with permission to reserve successfully")
        except WebDriverException:
            Logging(Red("Select user with permission to reserve => ---------- FAIL"))
            Commands.Wait10s_ClickElement(data["resource"]["home_resource"])



        Logging("--------------------- Save Add Resource Meeting Room  GW-730 : Add resource 'Meeting Room' ---------------------")

        try:
            Commands.Wait10s_ClickElement(data["resource"]["click_button_save_add_resource"])
            Logging("14.Click Button Save Add Resource Meeting Room successfully")
            Commands.scroll_view(data["resource"]["pull_the_scroll_bar"])
            time.sleep(1)
            driver.execute_script("window.scrollTo(100, 0)")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["resource"]["select_category_add"])
            time.sleep(1)
            if 'Room Reservation System' in driver.page_source :
                Logging(Green("1.Add resource 'Meeting Room Reservation System' => --------- PASS"))
                TestCase_LogResult(**data["testcase_result"]["resource"]["resource_reservation_system"]["pass"])
            else:
                Logging(Red("1.Add resource 'Meeting Room Reservation System' => --------- FAIL"))
                ValidateFailResultAndSystem("<div>[Resource]Add resource 'Meeting Room Reservation System'</div>")
                TestCase_LogResult(**data["testcase_result"]["resource"]["resource_reservation_system"]["fail"])


            Logging("--------------------- Add  Permission System Resource Meeting Room   ---------------------")
            driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["resource"]["icon_plus_meeting_room"])
            time.sleep(1)
            Logging("5.Click Icon Plus successfully")
            Commands.Wait10s_InputElement(data["resource"]["txt_conference_room_name"],data["resource"]["conference_room_name_sytem"])
            Logging("=>  Input Resource Name successfully" + " :  " + data["resource"]["conference_room_name_sytem"])
            Logging("1.Input Conference Room Name successfully")
            Commands.Wait10s_ClickElement(data["resource"]["permisson_system"])
            Logging("2.Check Permission System successfully")
            Commands.Wait10s_InputElement(data["resource"]["txt_description_conference_per_system"],data["resource"]["description_conference_room_sytem"])
            Logging("=>  Input Description successfully" + " :  " + data["resource"]["description_conference_room_sytem"])
            Logging("3.Input Description Reservation System successfully")
            Commands.Wait10s_ClickElement(data["resource"]["click_button_save_add_resource"])
            Logging("9.Click Button Save Add Resource  successfully")
            Logging("A. Add  Permission System Resource Meeting Room successfully")
            Commands.scroll_view(data["resource"]["pull_the_scroll_bar"])
            time.sleep(1)
            driver.execute_script("window.scrollTo(100, 0)")
            time.sleep(3)
            Commands.Wait10s_ClickElement(data["resource"]["select_category_add"])
            if 'Room Permission System' in driver.page_source :
                Logging(Green("1.Add resource 'Meeting Room Permission System' => --------- PASS"))
                TestCase_LogResult(**data["testcase_result"]["resource"]["resource_permission_system"]["pass"])
            else:
                Logging(Red("1.Add resource 'Meeting Room Permission System' => --------- FAIL"))
                ValidateFailResultAndSystem("<div>[Resource]Add resource 'Meeting Room Permission System'</div>")
                TestCase_LogResult(**data["testcase_result"]["resource"]["resource_permission_system"]["fail"])
        except WebDriverException:
            Logging(Red("Add  Permission System Resource Meeting Room  => --------- FAIL"))


    except WebDriverException:
        Logging(Red("1.Add resource 'Meeting Room Permission System' => --------- FAIL"))
        

    time.sleep(1)
def resource_add_resource_category_vehicle(domain_name):
    Logging("--------------------- Add  Reservation System Resource Vehicle  -  GW-735 : Define available time to reserve ---------------------")
    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_vehicle"])
        time.sleep(1)
        Logging("4.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus_vehicle"])
        Logging("5.Click Icon Plus successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_conference_room_name_reser_vehicle"],data["resource"]["vehicle_reser_room_name"])
        Logging("=>  Input Room Name successfully" + " :  " + data["resource"]["vehicle_reser_room_name"]) 
        Commands.Wait10s_InputElement(data["resource"]["txt_car_number"],data["resource"]["input_car_number"])
        Logging("=>  Input Car Number successfully" + " :  " + data["resource"]["input_car_number"])
        Commands.Wait10s_InputElement(data["resource"]["txt_vin"],data["resource"]["input_vin_number"])
        Logging("=>  Input VIN successfully" + " :  " + data["resource"]["input_vin_number"])
        Commands.Wait10s_InputElement(data["resource"]["txt_mileage"],data["resource"]["input_mileage_number"])
        Logging("=>  Input VIN successfully" + " :  " + data["resource"]["input_mileage_number"])
        driver.execute_script("window.scrollTo(0, 100)")
        Commands.Wait10s_ClickElement(data["resource"]["check_date_vihicle"])
        Logging("A. GW-735 : Define available time to reserve successfully")
        Logging(Green("=> Define available time to reserve => PASS"))

    except WebDriverException:
        Logging(Red("Define available time to reserve => --------- FAIL"))
        Logging(Red("=> Define available time to reserve => FAIL"))
        ValidateFailResultAndSystem("<div>[Resource]Define available time to reserve </div>")


    Logging("--------------------- Add  Reservation System Resource Vehicle  -  GW-736 : Define Reservation Type---------------------")
    try:
        Commands.Selectbox_ByVisibleText(data["resource"]["select_reservation_type"],data["resource"]["select_resource_hour"])
        #select_field_search = Select(driver.find_element_by_xpath(data["resource"]["select_reservation_type"]))
        #select_field_search.select_by_visible_text("2 hour interval, Available to Use Later")
        Logging("A. GW-736 : Define Reservation Type successfully")
        time.sleep(1)
        if '2 hour interval, Available to Use Later' in driver.page_source :
            Logging(Green("1. Define Reservation Type => ------------- PASS"))
        else:
            Logging(Red("1. Define Reservation Type => -------------FAIL"))
            ValidateFailResultAndSystem("<div>[Resource]Define Reservation Type</div>")

    except WebDriverException:
        Logging(" Define Reservation Type Fail")




    time.sleep(1)
    Logging("--------------------- Add  Reservation System Resource Vehicle  -  GW-738 : Select resource status---------------------")

    try:
        Commands.Wait10s_ClickElement(data["resource"]["select_status_malfunctioning"])
        time.sleep(1)
        Logging("A. GW-738 : Select resource status successfully")
        if 'Malfunctioning' in driver.page_source :
            Logging(Green("1. Select resource status => ------------- PASS"))
        else:
            Logging(Red("1. Select resource status => -------------FAIL"))
            ValidateFailResultAndSystem("<div>[Resource]Select resource status</div>")
    except WebDriverException:
        Logging(" Define Reservation Type Fail")


    

    Logging("--------------------- Save Add Resource Meeting Room  GW-730 : Add resource 'Vehicle' ---------------------")

    try:
        Commands.Wait10s_ClickElement(data["resource"]["click_button_save_add_resource"])
        Logging("14.Click Button Save Add Resource Meeting Room successfully")
        Logging("A. GW-731 : Add resource 'Vehicle' successfully")
        Commands.scroll_view(data["resource"]["pull_the_scroll_bar_vehicle"])
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_vehicle"])
        if 'Vehicle Reservation System' in driver.page_source :
            Logging(Green("1.Add resource 'Vehicle' => --------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["add_vehicle_system"]["pass"])
        else:
            Logging(Red("1.Add resource 'Vehicle' => --------- FAIL"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["add_vehicle_system"]["fail"])
    except WebDriverException:
        Logging(" Add resource 'Vehicle' Fail")




    
def resource_add_resource_category_normal(domain_name):
    Logging("--------------------- Save Add Resource Meeting Room  GW-730 : Add resource 'Normal' ---------------------")


    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_normal"])
        time.sleep(1)
        Logging("4.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["icon_plus_vehicle"])
        time.sleep(1)
        Logging("5.Click Icon Plus successfully")
        Commands.Wait10s_InputElement(data["resource"]["txt_conference_room_name_reser_vehicle"],data["resource"]["normal_reser_room_name"])
        Logging("=>  Input Room Name successfully" + " :  " + data["resource"]["normal_reser_room_name"])
        Commands.Wait10s_ClickElement(data["resource"]["click_button_save_add_resource"])
        Logging("14.Click Button Save Add Resource Normal successfully")
        Logging("A. GW-732 : Add resource 'Normal' successfully")
        Commands.scroll_view(data["resource"]["pull_the_scroll_bar_normal"])
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_normal"])
        time.sleep(2)
        if 'Normal Reservation System' in driver.page_source :
            Logging(Green("1.Add resource 'Normal' => --------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["add_normal_reservation_system"]["pass"])
        else:
            Logging(Red("1.Add resource 'Normal' => --------- FAIL"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["add_normal_reservation_system"]["fail"])
        time.sleep(2)
    except WebDriverException:
        Logging("  Add resource 'Normal' Fail")



def resource_delete_category(domain_name):    
    Logging("--------------------- Delete category ---------------------")

    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_room_delete"])
        time.sleep(1)
        Logging("1.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["delete_category"])
        Logging("2.Click Icon Delete successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["btn_ok_delete_category"])
        time.sleep(1)
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_normal_delete"])
        Logging("1.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["delete_category"])
        Logging("2.Click Icon Delete successfully")
        Commands.Wait10s_ClickElement(data["resource"]["btn_ok_delete_category"])
        time.sleep(1)
        Logging("14. Delete Category Normal successfully")
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["resource"]["select_category_vehicle_delete"])
        time.sleep(2)
        Logging("1.Select Category  successfully")
        Commands.Wait10s_ClickElement(data["resource"]["delete_category"])
        Logging("2.Click Icon Delete successfully")
        time.sleep(3)
        Commands.Wait10s_ClickElement(data["resource"]["btn_ok_delete_category"])
        Logging("14. Delete Category Normal successfully")
        Logging("A. Delete category successfully")
        if 'Hanbiro Room' in driver.page_source :
            Logging(Red("1.Delete category=> Fail"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["delete_category"]["fail"])
        else:
            Logging(Green("1.Delete category => --------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["resource"]["delete_category"]["pass"])
    except WebDriverException:
        Logging("Can not Delete category ")
    time.sleep(2)
    
    Logging("--------------------- Resource List ---------------------")
    try:
        Commands.Wait10s_ClickElement(data["resource"]["collapsible_icon_resource"])
        time.sleep(1)
        '''
        click_resource_list = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["resource"]["click_resource_list"])))
        if click_resource_list.is_displayed():
            Logging("=>Show Resource List")
        else:
            Logging("=> Not show Resource List")
            Commands.Wait10s_ClickElement(data["resource"]["collapsible_icon_add_resource"])   
        '''
        
        try:
            Commands.Wait10s_ClickElement(data["resource"]["click_resource_list"])
        except WebDriverException:
            Commands.Wait10s_ClickElement(data["resource"]["collapsible_icon_add_resource"])  
            Commands.Wait10s_ClickElement(data["resource"]["click_resource_list"])
        
        time.sleep(2)
        #Commands.Wait10s_ClickElement(data["resource"]["click_resource_list"])
        time.sleep(2)
        total=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
        Logging("---  Total Resource List before filtering : " + total)
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["click_resource_list_icon_filter_status"])
        Commands.Wait10s_ClickElement(data["resource"]["filter_status_malfunctioning"])
        time.sleep(6)
        total1=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
        Logging("---  Total Resource List after filtering : " + total1)
        time.sleep(1)
        total=so(total)
        total1=so(total1) 
        if total1 <= total:
            Logging("=> Search => Pass")
        else:
            Logging("=> Search => Fail")
    except WebDriverException:
        Logging("Resource List => Fail ")




def resource_add_resource_manager(domain_name):
    Logging("--------------------- Admin-Add Resource Manager ---------------------")
    try:
        time.sleep(1)

        try:
            Logging("=>Show Add Resource Manager")
            Commands.Wait10s_ClickElement(data["resource"]["click_add_reource_manager"])
        except WebDriverException:
            Logging("=> Not show Add Resource Manager")
            Commands.Wait10s_ClickElement(data["resource"]["admin_resource"])
            Commands.Wait10s_ClickElement(data["resource"]["click_add_reource_manager"])
        time.sleep(1)
        Logging("1.Click Folder Name successfully")
        Commands.Wait10s_ClickElement(data["resource"]["icon_folder_name_resource_manager"])
        Logging("2.Click Folder Name successfully")
        time.sleep(1)
        Commands.Wait10s_InputElement_return(data["resource"]["txt_search_user_resource_manager"],data["resource"]["user_search_org_manager"])
        time.sleep(1)
        Logging("3. Search user successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["resource"]["select_user_manager_resource"])
        Logging("4.Select user successfully")
        Commands.Wait10s_ClickElement(data["resource"]["btn_save_add_manager_resource"])
        Logging("5.Button Save successfully")
        Commands.Wait10s_ClickElement(data["resource"]["manager_list_resource"])
        Logging("6.Click Manager List successfully")
        Logging(Green("1.Admin-Add Resource Manager=> PASS"))

    except WebDriverException:
        Logging(Red("1.Admin-Add Resource Manager=> FAIL"))



    Logging("--------------------- Delete-Add Resource Manager ---------------------")

    try:

        Commands.Wait10s_InputElement_return(data["resource"]["txt_search_user_manager_list"],data["resource"]["user_search_org_manager"])
        time.sleep(1)
        Logging("7. Search Title Task successfully")
        Commands.Wait10s_ClickElement(data["resource"]["check_user_delete"])
        Logging("1. Select User Delete successfully")
        Commands.Wait10s_ClickElement(data["resource"]["btn_delete_manager_list_resource"])
        time.sleep(1)
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["resource"]["btn_ok_delete_manager_list"])
        time.sleep(1)
    except WebDriverException:
        Logging("Delete-Add Resource Manager => Fail ")

def access_menu_resource(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)


    '''
    if admin == True:
        try:
            resource_add_category(domain_name)
            Logging("create category successfully")
        except WebDriverException:
            Logging("fail to category ")
        
    else:
        Logging("1.Create category => Account is not admin")

    
    if admin == True:
        try:
            resource_add_resource_category_room(domain_name)
            Logging("create create Resource - Room successfully")
        except WebDriverException:
            Logging("fail to create Resource - Room ")
        
    else:
        Logging("2.create Resource - Room => Account is not admin")

    if admin == True:
        try:
            resource_add_resource_category_vehicle(domain_name)
            Logging("create Resource - Vehicle successfully")
        except WebDriverException:
            Logging("fail to create Resource - Vehicle ")
        
    else:
        Logging("3.create Resource - Vehicle => Account is not admin")


    if admin == True:
        try:
            resource_add_resource_category_normal(domain_name)
            Logging("create Resource - Normal successfully")
        except WebDriverException:
            Logging("fail to create Resource - Normal ")
        
    else:
        Logging("4.create Resource - Normal => Account is not admin")



    if admin == True:
        try:
            resource_delete_category(domain_name)
            Logging("Delete Category Resource successfully")
        except WebDriverException:
            Logging("fail to Delete Category Resource  ")
        
    else:
        Logging("5.Delete Category Resource  => Account is not admin")



    if admin == True:
        try:
            resource_add_resource_manager(domain_name)
            Logging("Add Resource Manager successfully")
        except WebDriverException:
            Logging("Add Resource Manager Fail")
        
    else:
        Logging("5.Delete Category Resource  => Account is not admin")

    '''


    if admin == True:
        try:
            result_folder_parent = True
            resource_add_category(domain_name)
            Logging("create category successfully")
        except WebDriverException:
            result_folder_parent = False
            Logging("fail to category ")
        
    else:
        Logging("1.Create category => Account is not admin")
        result_folder_parent = False

    if result_folder_parent == True :
        try:
            resource_add_resource_category_room(domain_name)
            Logging("create create Resource - Room successfully")
        except WebDriverException:
            Logging("fail to create Resource - Room ")
        time.sleep(1)
        try:
            resource_add_resource_category_vehicle(domain_name)
            Logging("create Resource - Vehicle successfully")
        except WebDriverException:
            Logging("fail to create Resource - Vehicle ")
        time.sleep(1)


        try:
            resource_add_resource_category_normal(domain_name)
            Logging("create Resource - Normal successfully")
        except WebDriverException:
            Logging("fail to create Resource - Normal ")


        try:
            resource_delete_category(domain_name)
            Logging("Delete Category Resource successfully")
        except WebDriverException:
            Logging("fail to Delete Category Resource  ")
        time.sleep(1)

    if admin == True:
        try:
            resource_add_resource_manager(domain_name)
            Logging("Add Resource Manager successfully")
        except WebDriverException:
            Logging("Add Resource Manager Fail")
        
    else:
        Logging("5.Delete Category Resource  => Account is not admin")
    


    time.sleep(2)
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(3)
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
with open(local+'\\'+'luu_resource.txt','w') as resource:
    domain="http://qa.hanbiro.net"
    access_menu_resource(domain,resource)



result=open(local+'\\result.txt','r')
file_result=result.read()
Logging(file_result)
'''
  