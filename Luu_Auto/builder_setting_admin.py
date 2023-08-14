from importlib.resources import path
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
import os,pathlib,glob
from sys import platform
import luu_function
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Red,Yellow,Green,Commands
from luu_function import driver

time.sleep(1)


def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Menu Builder------------------------------------------------------")
    driver.get(domain_name + "/custom_menu")
    #time.sleep(2)
    #driver.refresh()
    time.sleep(8)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["icon_create_menu"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin


def admin_write_menubuilder(domain_name):
    
    time.sleep(2)  
    Logging("------------------------------------------------------D. Menu Builder------------------------------------------------------")
    #driver.get(domain_name + "/custom_menu/write/")
    #access_menu_menu_builder = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["menu_builder"])))
    #access_menu_menu_builder.click()
    Logging("1. Access Menu Builder successfully")
    Logging("--------------------- Write Menu   ---------------------")

    try:
        Commands.Wait10s_ClickElement(data["menubuilder"]["icon_create_menu"])
    except WebDriverException:
        Logging("Not show Clock In")
        Commands.ClickElement(data["menubuilder"]["btn_close_clock_in"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["icon_create_menu"])

    time.sleep(1)
    Logging("1.Click button Create  successfully")
    time.sleep(8)

    try:
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_cancel_menu"])
        time.sleep(2)
        Logging("2.Click button Cancel  successfully")
        Commands.SwitchToFrame("//div[contains(@class, 'popup-formbuilder')]/div/iframe")
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["menubuilder"]["name_menu_builder"])

        time.sleep(2)
        txtname_clear_builder = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_name_builder"])))
        txtname_clear_builder.clear()
        time.sleep(2)

        txtname_clear_builder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_name_builder"]))) # có sửa nhưng chạy ko dk
        txtname_clear_builder.send_keys(data["menubuilder"]["name_menu_builder_update"])
        Logging("3. Input Name Menu Builder  successfully")

        Commands.Wait10s_ClickElement(data["menubuilder"]["click_menu_icon"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_icon"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_icon"])
        Logging("4. Select icon Menu Builder  successfully")
        Commands.Wait10s_InputElement(data["menubuilder"]["btn_sub_menu_name"],data["menubuilder"]["name_sub_menu"])
        Logging("5. Input Sub Menu Name Builder  successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["click_icon_sub_menu"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_icon_sub_menu"])
        Logging("6. Select icon Sub Menu Name Builder  successfully")
        time.sleep(1)
        Logging("---   Drag Layout Single Line   --- ")

        Commands.drag_drop_Element(data["menubuilder"]["single_line_from"],data["menubuilder"]["editor_to_drag"])
        Logging("7.Drag Layout Single Line  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["email_from"],data["menubuilder"]["editor_to_drag_2"])
        Logging("8.Drag Layout Email  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["url_from_builder"],data["menubuilder"]["editor_to_drag"])
        Logging("9.Drag Layout URL  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["date_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        Logging("10.Drag Layout Date  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["datetime_from_builder"],data["menubuilder"]["editor_to_drag"])
        Logging("11.Drag Layout Date/Time  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["daterange_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        Logging("11.Drag Date Range  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["phone_from_builder"],data["menubuilder"]["editor_to_drag"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["input_mask"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_input_mask"])
        time.sleep(1)
        Logging("12.Turn On Input Mask successfully")
        Logging("13.Drag Phone  successfully")
        Commands.drag_drop_Element(data["menubuilder"]["multi_line_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        Logging("14.Drag Layout Multi-Line  successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["multiple_choice_from_builder"],data["menubuilder"]["editor_to_drag"])
        time.sleep(1)

        Commands.Wait10s_clearElement(data["menubuilder"]["txt_options_1"])
      

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_options_1"],data["menubuilder"]["name_option1_choice"])

        Logging("15a.Input Option 1  successfully")
        time.sleep(1)
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_options_2"],data["menubuilder"]["name_option2_choice"])
        time.sleep(1)
        Logging("15b.Input Option 2  successfully")
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_options_3"],data["menubuilder"]["name_option3_choice"])
        time.sleep(1)
        Logging("15c.Input Option 3  successfully")


        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_choice"])
        Logging("15.Drag Layout Multiple Choice successfully")
        time.sleep(1)

        Commands.drag_drop_Element(data["menubuilder"]["single_choice_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        time.sleep(1)
        Commands.Wait10s_clearElement(data["menubuilder"]["txt_single_choice_options_1"])
        #txt_option1_single_choice = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_single_choice_options_1"])))
        #txt_option1_single_choice.clear()

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_single_choice_options_1"],data["menubuilder"]["name_option1_single_choice"])
        Logging("16a.Input Option 1 Single Choice successfully")
        time.sleep(1)

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_single_choice_options_2"],data["menubuilder"]["name_option2_single_choice"])
        time.sleep(1)
        Logging("16b.Input Option 2 Single Choice successfully")

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_single_choice_options_3"],data["menubuilder"]["name_option3_single_choice"])
        Logging("16c.Input Option 3 Single Choice successfully")

        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_single_choice"])
        time.sleep(1)
        Logging("16.Drag Layout Single Choice successfully")



        Commands.drag_drop_Element(data["menubuilder"]["address_from_builder"],data["menubuilder"]["editor_to_drag"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["address_city_from_builder"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["address_state_from_builder"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["address_postal_from_builder"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["address_country_from_builder"])
        Logging("16a.Check City-State-Postal/Zip Code - Country successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_address"])
        time.sleep(1)
        Logging("16.Drag Layout Address successfully")
        time.sleep(3)
        Commands.drag_drop_Element(data["menubuilder"]["editor_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        time.sleep(2)
        Commands.drag_drop_Element(data["menubuilder"]["currency_from_builder"],data["menubuilder"]["editor_to_drag"])
        time.sleep(2)

        select_currency_value_builder = Select(driver.find_element_by_xpath(data["menubuilder"]["list_currency_value"]))
        select_currency_value_builder.select_by_visible_text("VND (₫)")
        Logging("17a.Select Currency value successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_currency"])
        time.sleep(1)
        Logging("17.Drag Layout Currency successfully")
        Commands.drag_drop_Element(data["menubuilder"]["number_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        Logging("18.Drag Layout Number successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["percent_from_builder"],data["menubuilder"]["editor_to_drag"])
        Logging("19.Drag Layout Percent successfully")
        time.sleep(1)

        Commands.drag_drop_Element(data["menubuilder"]["multi_select_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        time.sleep(1)
        txt_option1_multi_select = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_multi_select_options_1"])))
        txt_option1_multi_select.clear()
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_multi_select_options_1"],data["menubuilder"]["name_option1_multi_select"])
        Logging("20a.Input Option 1 Multi-Select successfully")
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_multi_select_select_2"],data["menubuilder"]["name_option2_multi_select"])
        time.sleep(1)
        Logging("20b.Input Option 2 Multi-Select successfully")

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_multi_select_select_3"],data["menubuilder"]["name_option3_multi_select"])
        Logging("20c.Input Option 3 Multi-Select successfully")

        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_multi_select"])
        Logging("20.Drag Layout Multi-Select successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["pick_list_from_builder"],data["menubuilder"]["editor_to_drag"])
        time.sleep(1)
        txt_option1_pick_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_pick_list_options_1"])))
        txt_option1_pick_list.clear()
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_pick_list_options_1"],data["menubuilder"]["name_option1_pick_list"])
        Logging("21a.Input Option 1 Pick List successfully")

        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_pick_list_select_2"],data["menubuilder"]["name_option2_pick_list"])
        Logging("21b.Input Option 2 Pick List successfully")
        time.sleep(1)
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_pick_list_select_3"],data["menubuilder"]["name_option3_pick_list"])
        Logging("21c.Input Option 3 Pick List successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_done_option_pick_list"])
        time.sleep(1)
        Logging("21.Drag Layout Pick List successfully")
        Commands.scroll_view(data["menubuilder"]["org_from_builder"])
        time.sleep(2)

        Commands.drag_drop_Element(data["menubuilder"]["org_from_builder"],data["menubuilder"]["editor_to_drag_2"])
        Logging("22.Drag Layout Organization successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["attachfile_from_builder"],data["menubuilder"]["editor_to_drag"])
        Logging("23.Drag Layout Attach files successfully")
        time.sleep(1)
        Commands.drag_drop_Element(data["menubuilder"]["comment_from_builder"],data["menubuilder"]["editor_to_drag"])
        Logging("24.Drag Layout Comments successfully")
        time.sleep(1)

        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_and_close"])
        time.sleep(6)
        Logging("A. Create Menu successfully")
    
    except WebDriverException:
        Logging("A. Create Menu Fail")
    time.sleep(1)  
    driver.refresh()
    time.sleep(4)
    driver.get(domain_name + "/custom_menu")
    time.sleep(2)
    Logging("1. Access Menu Builder successfully")


    try:
        Logging("-------------- Search Menu Name ------------------")
        Commands.Wait10s_InputElement_return(data["menubuilder"]["textbox_search_menu_builder"],data["menubuilder"]["search_menu_name_menu_builder"])
        Logging("1. Search Menu Name successfully")
        time.sleep(5)
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_menu_luuluu"])
        Logging("2. Click menu QA Hanbiro successfully")
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        time.sleep(1)
        if 'Sub QA' in driver.page_source :
            Logging(Green("1.Create Menu => ----------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["write_menu"]["pass"])
        else:
            Logging(Red("1.Create Menu => ----------- PASS"))
            ValidateFailResultAndSystem("<div>[Menu Builder]1.Write Menu </div>")
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["write_menu"]["fail"])
    except WebDriverException:
        Logging("A. Search Menu Name Fail")



    '''
    #menu_builder_create = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["show_menu_builder_create"])))
    if 'Sub QA' in driver.page_source :
        Logging("1.Create Menu => ----------- PASS")
    else:
        Logging("1.Create Menu => ----------- FAIL")
        ValidateFailResultAndSystem("<div>[Menu Builder]1.Write Menu </div>")
    '''
    time.sleep(1)
    try:
        Logging("-----------------------------Tab Who Can See - Permission------------------------------")
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Commands.Wait10s_ClickElement(data["menubuilder"]["setting_builder"])
        Logging("1.Click Settings successfully")
   


        Logging("-----------------------------Tab Manage Modules - Edit Menu------------------------------")
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_tab_manage_modules"])
        Logging("1.Click Tab Manage Modules successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["icon_edit_layout"])
        time.sleep(1)
        Logging("2.Click Icon Edit Layout successfully")
        driver.switch_to.frame(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["click_icon_sub_menu"])
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_icon_sub_menu_edit"])
        Logging("3.Edit Icon Sub Menu successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_and_close"])
        time.sleep(3)
        Logging("A. Edit Menu successfully")
        if 'Sub QA' in driver.page_source :
            Logging(Green("1.Edit Menu => ----------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["edit_menu"]["pass"])
        else:
            Logging(Red("1.Edit Menu => ----------- FAIL"))
            ValidateFailResultAndSystem("<div>[Menu Builder]1.Edit Menu </div>")
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["edit_menu"]["fail"])
        
        Logging("-----------------------------Clone Layout------------------------------")
        driver.refresh()
        time.sleep(4)

        Commands.Wait10s_ClickElement(data["menubuilder"]["click_icon_clone_layout"])
        Logging("1.Click icon Clone Layout successfully")
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_layout_name"],data["menubuilder"]["name_clone_layout"])
        Logging("2.Input Clone Layout successfully")
        time.sleep(1)

        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_clone_layout"])
        Logging("A. Clone Layout successfully")
        time.sleep(3)
        if 'Sub QA 2' in driver.page_source :
            Logging(Green("1.Clone Layout => -------------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["clone_layout"]["pass"])
        else:
            Logging(Red("1.Clone Layout => -------------- FAIL"))
            ValidateFailResultAndSystem("<div>[Menu Builder]1.Clone Layout</div>")
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["clone_layout"]["fail"])



        try:    
            Logging("-----------------------------Add Folder------------------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_add_folder"])
            Logging("1.Click button Add Folder successfully")
            Commands.Wait10s_InputElement(data["menubuilder"]["txt_folder_name"],data["menubuilder"]["folder_name"])
            Logging("2.Input Folder Name successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_add_folder"])
            Logging("3.Click button Save successfully")
            Logging("A. Add Folder successfully")
            time.sleep(2)
            if 'Folder QA' in driver.page_source :
                Logging(Green("1.Add Folder => ------------ PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["add_folder"]["pass"])
            else:
                Logging(Red("1.Add Folder => ------------ FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Add Folder</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["add_folder"]["fail"])

            Logging("-----------------------------Edit Folder------------------------------")

            Commands.Wait10s_ClickElement(data["menubuilder"]["edit_name_folder"])
            Logging("1.Click Folder successfully")
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_edit_name_folder"],data["menubuilder"]["name_folder_edit"])
            Logging("2.Edit Folder Name successfully")
            Logging("A. Edit Name Folder successfully")
            time.sleep(3)
            if 'Folder Builder' in driver.page_source :
                Logging("1.Edit Folder => --------- PASS")
            else:
                Logging("1.Edit Folder => ---------  FAIL")

            Logging("-----------------------------Delete  Folder------------------------------")
            driver.refresh()
            time.sleep(4)
            #WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
            #access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
            #access_menu_home.click()
            #driver.get(domain_name + "/custom_menu")
            #select_a_menu_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["select_menu_luuluu"])))
            #select_a_menu_name.click()
            #time.sleep(2)
            #Logging("1. Click menu QA Hanbiro successfully")
            #click_setting_builder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["setting_builder"])))
            #click_setting_builder.click()

            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_delete_folder_bd"])
            time.sleep(1)
            Logging("1.Click icon Delete successfully")

            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_ok_delete"])
            Logging("A. Delete Folder successfully")
            time.sleep(2)
            if 'Folder Builder' in driver.page_source :
                Logging(Red("1.Delete  Folder => ---------FAIL"))
            else:
                Logging(Green("1.Delete  Folder => ---------PASS"))
        except WebDriverException:
            Logging(" Add Folder Fail")
        
        '''
        try:
            Logging("-----------------------------Export Layout------------------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_export_layout"])
            if 'json' in driver.page_source :
                Logging(Green("Export Layout successfully =>------ PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["export_layout"]["pass"])
            else:
                Logging(Red("Export Layout fail =>------- FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Export Layout fail</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["export_layout"]["fail"])
        except WebDriverException:
            Logging(" Export Layout Fail")
        time.sleep(2)  
        '''

        try:
            Logging("-----------------------------Mode View------------------------------")
            driver.refresh()
            time.sleep(4)    
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_mode_view"])
            time.sleep(1)
            Logging("1.Click icon Mode View successfully")
            show_calendar_view_on = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["show_date_turn_on_calenda_view"])))
            if show_calendar_view_on.is_displayed():
                Logging("=> Calendar View ON")
            else:
                Commands.Wait10s_ClickElement(data["menubuilder"]["turn_on_calenda_view"])
                time.sleep(1)  
                Logging("2.Turn On/Off Calendar View successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_calendar_view"])
            driver.refresh()
            time.sleep(2) 
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_mode_view"])
            time.sleep(3)
            Logging("A. Mode View Calendar View successfully")
            if 'Calendar View' in driver.page_source :
                Logging(Green(" Mode View =>--------- PASS"))
            else:
                Logging(Red("Mode View =>---------- FAIL"))
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_calendar_view"])
            time.sleep(1)
        except WebDriverException:
            Logging("Mode View Fail")


        
        Logging("-----------------------------Alert/Warning Settings------------------------------")
        driver.refresh()
        time.sleep(4)      
        click_icon_alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["icon_alert"])))
        click_icon_alert.click()
        Logging("1.Click Icon Alert/Warning Settings successfully")
        select_value_do_not_use = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["select_disable"])))
        select_value_do_not_use.click()
        Logging("2.Select Value Do Not Use successfully")

        '''
        if 'Alert/Warning Settings' in driver.page_source :
            Logging(" Alert/Warning Settings =>--------- PASS")
        else:
            Logging("Alert/Warning Settings =>---------- FAIL")
            ValidateFailResultAndSystem("<div>[Menu Builder]Alert/Warning Settings</div>")
        '''
    
        click_btn_save_alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["btn_save_alert"])))
        click_btn_save_alert.click()
        Logging("A. Select Alert/Warning Settings successfully")
        




        try:
            Logging("-----------------------------Import Layout------------------------------")
            driver.refresh()
            time.sleep(4)  
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_add_module_layout"])
            time.sleep(1)
            driver.switch_to.frame(1)
            Logging("2.Click button Add Module successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_import_layout"])
            Logging("3. Click button IMPORT LAYOUT successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_layout_import"])
            Logging("4. Select Layout successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_ok_import_layout"])
            Logging("5.Click button OK successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement(data["menubuilder"]["btn_sub_menu_name"],data["menubuilder"]["menu_sub_import"])
            Logging("5. Input Sub Menu Name Builder  successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_and_close"])
            time.sleep(2)
            driver.refresh()
            time.sleep(4)
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
            Logging("A. Import Layout Menu Builder successfully")
            time.sleep(3)
            if 'Import Layout' in driver.page_source :
                Logging(Green(" Import Layout =>----------- PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["import_layout"]["pass"])
            else:
                Logging(Red("Import Layout =>------------ FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Import Layout</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["import_layout"]["fail"])

            Logging("-----------------------------Delete Layout------------------------------")
            driver.refresh()
            time.sleep(4)  
            Commands.Wait10s_ClickElement(data["menubuilder"]["setting_builder"])
            Logging("1.Click Settings successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_delete_layout"])
            Logging("1.Click icon Delete successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_ok_delete"])
            Logging("A. Delete Layout successfully")
            time.sleep(3)
            if 'Import Layout' in driver.page_source :
                Logging(Red(" Delete Layout => --------------- FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Delete Layout</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["delete_layout"]["fail"])
            else:
                Logging(Green("Delete Layout => --------------- PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["delete_layout"]["pass"])
        except WebDriverException:
            Logging("Create Layout successfully")


    except WebDriverException:
        Logging("1.Click Settings successfully")
time.sleep(1)    




def write_layout_menubuilder(domain_name):
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    time.sleep(2)
    driver.get(domain_name + "/custom_menu/list/")
    time.sleep(4)
    Logging("1. Access Menu Builder successfully")

    try:
        Logging("-------------- Search Menu Name ------------------")
        Commands.Wait10s_InputElement_return(data["menubuilder"]["textbox_search_menu_builder"],data["menubuilder"]["search_menu_name_menu_builder"])
        Logging("1. Search Menu Name successfully")
        time.sleep(6)
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_menu_luuluu"])
        time.sleep(5)
        Logging("2. Click menu QA Hanbiro successfully")
        if 'Sub QA' in driver.page_source :
            Logging(Green("1.Acess Menu => ----------- PASS"))
        else:
            Logging(Red("1.Acess Menu => ----------- FAIL"))
    
        Logging("--------------------- Create Layout  ---------------------")
        try:
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_sub_2"])
        except WebDriverException:
            Logging("Not show Clock In")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_close_clock_in"])
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_sub_2"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["button_create_title"])
        Logging("1. Click Create successfully")
        
        time.sleep(1)
        now = datetime.now()
        name_layout_builder = "Generated by selenium at" +" " + str(now)
        input_description_board = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["textbox_name_builder"])))
        input_description_board.send_keys(name_layout_builder)
        time.sleep(2)



        '''
        title_layout_name=click_textbox_name_menu_builder.get_attribute("value")
        if(title_layout_name==data["menubuilder"]["name_layout"]):
            Logging("=> Input Name Layout =>pass")
        else:
            Logging("=> Input Name Layout =>fail")
        Logging("2. Input Name Layout successfully" + " :  " + data["menubuilder"]["name_layout"])
        '''

        Commands.Wait10s_ClickElement(data["menubuilder"]["multiple_choice"])
        Logging("6. Select Multiple successfully")
        time.sleep(1)
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_currency"],data["menubuilder"]["input_currency"])
        Logging("8. Input Currency successfully" + " :  " + data["menubuilder"]["input_currency"])
        time.sleep(1)

        Commands.Wait10s_InputElement_return(data["menubuilder"]["click_pick_list"],data["menubuilder"]["name_search_pick_list"])
        Logging("10. Select Pick List successfully")
        time.sleep(1)
        Commands.Wait10s_InputElement(data["menubuilder"]["textbox_url"],data["menubuilder"]["name_url"])
        Logging("4. Input URL successfully" + " :  " + data["menubuilder"]["name_url"])
        Commands.Wait10s_InputElement(data["menubuilder"]["textbox_single_line"],data["menubuilder"]["name_single_line"])
        Logging("3. Input Name Single Line successfully"  + " :  " + data["menubuilder"]["name_single_line"])
        Commands.Wait10s_InputElement(data["menubuilder"]["textbox_phone"],data["menubuilder"]["number_phone"])
        Logging("5. Input Phone successfully" + " :  " + data["menubuilder"]["number_phone"])
        time.sleep(1)
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_address"],data["menubuilder"]["name_address"])
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_address_2"],data["menubuilder"]["name_address_2"])
        Logging("7. Input Address successfully" + " :  " + data["menubuilder"]["name_address"]+ data["menubuilder"]["name_address_2"])
        time.sleep(1)
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_percent"],data["menubuilder"]["input_percent"])
        Logging("9. Input Phone successfully" + " :  " + data["menubuilder"]["input_percent"])
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        time.sleep(1)
        click_txt_multi_line = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["txt_multi_line"])))
        click_txt_multi_line.click()
        click_txt_multi_line.send_keys(data["menubuilder"]["content_multi_line"])
        Logging("13. Input Multi-Line successfully")
        time.sleep(1)
        editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
        driver.switch_to.frame(editor_frame)
        input_editor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["input_editor"])))
        input_editor.send_keys(data["menubuilder"]["editor_content"])
        Logging("17. Input Editor successfully")
        time.sleep(1)
        driver.switch_to.default_content()
        Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_multi_select"],data["menubuilder"]["search_multi_select"])
        time.sleep(1)
        Logging("19. Select Multi-Select successfully")


        Commands.Wait10s_InputElement(data["menubuilder"]["txt_email"],data["menubuilder"]["input_email"])
        Logging("11. Input Mail successfully" + " :  " + data["menubuilder"]["input_email"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["click_date_range_from"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_date_range_from"])
        time.sleep(1)
        Logging("14. Select Date Range From successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["click_date_range_to"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["menubuilder"]["select_date_range_to"])
        Logging("15. Select Date Range To successfully")
        time.sleep(1)
        driver.execute_script("window.scrollTo(100, 0)")
        get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["click_add_file"])))
        get_file.send_keys(luu_function.file_img)
        time.sleep(2)
        Logging("21. Attach file successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_menu_builder"])
        time.sleep(10)
        Logging("22.Save Layout successfully")
        Logging("A. Create Layout successfully")
        time.sleep(10)
        '''
        if 'Generated by' in driver.page_source :   # check data
            Logging(Green("1.Create Layout => -------------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["create_data"]["pass"])
        else:
            Logging(Red("1.Create Layout => -------------- FAIL"))
            ValidateFailResultAndSystem("<div>[Menu Builder]1.Create Layout</div>")
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["create_data"]["fail"])
        '''
        time.sleep(2)
        Logging("--------------------- View and Comment  ---------------------")

        try:
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_back_builder"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_title"])    # Title
            time.sleep(3)
            Commands.Wait10s_ClickElement(data["menubuilder"]["txt_comment_builder"])
            time.sleep(3)
            Commands.Wait10s_InputElement(data["menubuilder"]["input_coment"],data["menubuilder"]["content_comment"])
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_comment"])
            time.sleep(1)
            Logging("A. Save comment successfully")
            driver.execute_script("window.scrollTo(0, 100)")
            time.sleep(5)
            Logging(Green("1.View and Comment => ---------  PASS"))
            time.sleep(1)
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["view_and_comment"]["pass"])
        except WebDriverException:
            Logging(Red("1.View and Comment => --------- FAIL"))
            ValidateFailResultAndSystem("<div>[Menu Builder]View and Comment</div>")
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["view_and_comment"]["fail"])



        Logging("--------------------- Import Menu Builder  ---------------------")
        try:

            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_back_builder"])
            driver.refresh()
            time.sleep(3)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_more"])
            Commands.Wait10s_ClickElement(data["menubuilder"]["import_file"])
            select_file = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["add_file"])))
            select_file.send_keys(luu_function.file_buildr)
            Logging("1.Select File successfully")
            time.sleep(2)

            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_upload"])
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_select_name"],data["menubuilder"]["name_search"])
            time.sleep(2)
            Logging("2.Select Name successfully")
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_create_date"],data["menubuilder"]["create_date_search"])
            Logging("3.Select Created Date successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_single_line"],data["menubuilder"]["single_line_search"])
            Logging("4.Select Single Line successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_email"],data["menubuilder"]["email_search"])
            Logging("5.Select Value Email successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_url"],data["menubuilder"]["url_search"])
            Logging("6.Select Value URL successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_date"],data["menubuilder"]["date_search"])
            Logging("7.Select Date successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_date_time"],data["menubuilder"]["date_time_search"])
            Logging("8.Select Date Time successfully")
            time.sleep(1)

            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_date_range"],data["menubuilder"]["date_range_search"])
            Logging("9.Select Date Range successfully")
            time.sleep(1)

            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_phone"],data["menubuilder"]["phone_search"])
            Logging("10.Select Phone successfully")
            time.sleep(1)

            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_multi_line"],data["menubuilder"]["multi_line_search"])
            Logging("11.Select Multi Line  successfully")
            time.sleep(1)

            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_multiple_choice"],data["menubuilder"]["multiple_choice_search"])
            Logging("12.Select Multiple Choice successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_single_choice"],data["menubuilder"]["single_choice_search"])
            Logging("13.Select Single Choice successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_address"],data["menubuilder"]["address_search"])
            Logging("14.Select Address successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_currency"],data["menubuilder"]["currency_search"])
            Logging("15.Select Currency successfully")


            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_number"],data["menubuilder"]["number_search"])
            Logging("16.Select Number successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_percent"],data["menubuilder"]["percent_search"])
            Logging("17.Select Percent successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_multi_select"],data["menubuilder"]["multi_select_search"])
            Logging("18.Select Multi Select successfully")
            time.sleep(1)
            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_value_pick_list"],data["menubuilder"]["pick_list_search"])
            Logging("19.Select Pick List successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_import"])
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_back_import"])
            time.sleep(4)
            Logging("A. Import successfully")
            if 'Luu Luu 03' in driver.page_source :
                Logging(Green("1. Import Menu Builder =>--------  PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["import_data"]["pass"])
            else:
                Logging(Red("1.Import Menu Builder =>---------  FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Import Menu Builder</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["import_data"]["fail"])
        except WebDriverException:
            Logging("Import Menu Builder => Fail")
        time.sleep(1)



        try:
            Logging("--------------------- Search Menu Builder  ---------------------")
            driver.refresh()
            time.sleep(9)
            Logging("--------- a. Search All --------- ")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["click_list_search_field"])
            Logging("1.Click List Search Field successfully")
            time.sleep(2)

            Commands.Wait10s_InputElement_return(data["menubuilder"]["txt_search_keyword_all"],data["menubuilder"]["name_search_all"])  # search title
            Logging("2.Input value successfully")
            time.sleep(2)   
            if 'Total 1' in driver.page_source :
                Logging(Green("Search Menu Builder =>----- PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["search_data"]["pass"])
            else:
                Logging(Red("Search Menu Builder =>----- FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]SEARCH</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["search_data"]["fail"])
        except WebDriverException:
            Logging("Search Menu Builder => Fail")
        

        try:
            Logging("--------------------- Export Menu Builder  ---------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_more"])
            Logging("1.Click button More  successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_export"])
            Logging("2.Click Export successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["click_select_all"])
            Logging("3.Select All successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_export"])
            Logging("A. Export successfully")
            time.sleep(1)
            Logging(Green("1. EXPORT =>----------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["export_data"]["pass"])
        except WebDriverException:
            Logging(Red("1. EXPORT =>----------- FAIL"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["export_data"]["fail"])
        

        try:
            Logging("--------------------- Mark as Read  ---------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_mark_as_read"])
            time.sleep(2)
            Logging("1.Click icon Mark as Read  successfully")
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
            Logging("A. Mark as Read successfully")
            time.sleep(6)
            if 'Total 2' in driver.page_source :
                Logging("Mark as Read =>----- PASS")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["mark_as_read"]["pass"])
            else:
                Logging("Mark as Read =>----- FAIL")
                ValidateFailResultAndSystem("<div>[Menu Builder]Mark as Read</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["mark_as_read"]["fail"])
        except WebDriverException:
            Logging(" Mark as Read Fail")


        Logging("--------------------- Download All Attachments  ---------------------")
        try:
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_download_all_file"])
            Logging("1.Click icon Download All Attachments  successfully")
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
            time.sleep(2)
            if 'custom' in driver.page_source :
                Logging(Green("Download All Attachments =>----- PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["download_all_attachment"]["pass"])
            else:
                Logging(Red("Download All Attachments =>----- FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Download All Attachments Fail</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["download_all_attachment"]["fail"])
            Logging("--------------------- Download File  ---------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["select_title_download"])  # select title donwload
            Logging("1.Select Title successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_download_file_layout"])
            Logging("2.Click icon Download file  successfully")
            time.sleep(2)
            if 'signature_mage' in driver.page_source :
                Logging(Green("Download File => ---------- PASS"))
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["download_file"]["pass"])
            else:
                Logging(Red("Download File => ---------- FAIL"))
                ValidateFailResultAndSystem("<div>[Menu Builder]Download File</div>")
                TestCase_LogResult(**data["testcase_result"]["menubuilder"]["download_file"]["fail"])
        except WebDriverException:
            Logging("Download All Attachments Fail")

        time.sleep(1)
        Logging("--------------------- Copy-Past  ---------------------")
        try:
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_more_copy"])
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["value_copy_data"])
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_close_copy_data"])
            time.sleep(2)
            try:
                Commands.Wait10s_ClickElement(data["menubuilder"]["button_create_title"])
            except WebDriverException:
                Logging("Not show Clock In")
                Commands.Wait10s_ClickElement(data["menubuilder"]["btn_close_clock_in"])
                Commands.Wait10s_ClickElement(data["menubuilder"]["button_create_title"])
            time.sleep(1)
            Logging("1. Click Create successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_paste_copy_data"])
            time.sleep(1)
            driver.refresh()
            time.sleep(8)
            '''
            try:
                click_btn_close_clock_in = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["btn_close_clock_in"])))
                click_btn_close_clock_in.click()
            except WebDriverException:
                Logging("Not show Clock In")
            '''
            Logging("2. Click button Past successfully")
            click_textbox_name_menu_builder = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["textbox_name_builder"])))
            click_textbox_name_menu_builder.clear()
            click_textbox_name_menu_builder.send_keys(data["menubuilder"]["title_copy"])
            Logging("3. Input Name Menu Builder  successfully")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_save_menu_builder"])
            time.sleep(5)
            Logging("SAVE SAVE SAVE => ---------- PASS")
        except WebDriverException:
            Logging("Can not copy/paste")
        time.sleep(1)

        try:
            Logging("--------------------- View Timeline  ---------------------")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_timeline"])
            Logging(Green("=> View Timeline  =>--------- PASS"))
        except WebDriverException:
            Logging("View Timeline Fail")
            Logging(Red("=> View Timeline =>---------- FAIL"))


        time.sleep(1)
        Logging("--------------------- Delete layout Name ---------------------")
        driver.refresh()
        time.sleep(15)
        try:
            #Commands.Wait10s_ClickElement(data["menubuilder"]["btn_back_builder"])
            time.sleep(4)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_more_copy"])
            time.sleep(5)
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_delete_layout_user"])
        except WebDriverException:
            Logging("Not show Clock In")
            Commands.Wait10s_ClickElement(data["menubuilder"]["btn_close_clock_in"])
            time.sleep(4)
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_back_builder"])

        time.sleep(2)
        Logging("Delete User => Pass")




        Logging("--------------------- Calendar View  ---------------------")
        try:
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_calendar_view"])  
            time.sleep(8)
            if 'Lunar' in driver.page_source :
                Logging(Green("Calendar View => ---------- PASS"))
            else:
                Logging(Red("Calendar View => ---------- FAIL"))
            Commands.Wait10s_ClickElement(data["menubuilder"]["icon_list_view"])
            time.sleep(3)
        except WebDriverException:
            Logging("Not show Calendar View")
        
        time.sleep(2)
    except WebDriverException:
        Logging("Search Fail")

        
def delete_menubuilder(domain_name):
    time.sleep(2)
    Logging("------------------------------------------------------D. Delete Menu ------------------------------------------------------")
    Commands.Wait10s_ClickElement(data["menubuilder"]["screen_home_gw"])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    driver.get(domain_name + "/custom_menu")
    time.sleep(2)
    Logging("1. Access Menu Builder successfully")
    Commands.Wait10s_InputElement_return(data["menubuilder"]["textbox_search_menu_builder"],data["menubuilder"]["search_menu_name_menu_builder"])
    Logging("1. Search Menu Name successfully")
    time.sleep(1)
    try:
        Commands.Wait10s_ClickElement(data["menubuilder"]["click_btn_delete_menu"])
        time.sleep(1)
        Logging("8. Click icon Delete successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["check_force_delete"])
        Logging("9. Check Force Delete successfully")
        Commands.Wait10s_InputElement(data["menubuilder"]["txt_input_pw_delete"],data["menubuilder"]["name_pw_delete"])
        Logging("10. Input Password successfully")
        Commands.Wait10s_ClickElement(data["menubuilder"]["btn_ok_delete_menubd"])
        Logging("A. Delete Menu Builder successfully")
        time.sleep(6)
        if 'Total 0' in driver.page_source :
            Logging(Green("DELETE MENU => ------ PASS"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["delete_menu"]["pass"])
        else:
            Logging(Red("DELETE MENU => ------- FAIL"))
            TestCase_LogResult(**data["testcase_result"]["menubuilder"]["delete_menu"]["fail"])
    except WebDriverException:
            Logging("Not show Menu builder")
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    
   

    
    jpg = glob.glob(os.path.join("Downloads\\signature_mage.jpg"))
    for image in jpg:
        os.remove(image)



    '''
    json = glob.glob(os.path.join("Downloads\\Sub QA 2.json"))
    for item in json:
        os.remove(item)
    files = glob.glob(os.path.join("Downloads\\*.xls"))
    for file in files:
        os.remove(file)
    filezip = glob.glob(os.path.join("Downloads\\*.zip"))
    for zipbd in filezip:
        os.remove(zipbd)
    
    '''


    
def admin_menu_menubuilder(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)
    if admin == True:
        admin_write_menubuilder(domain_name)
        '''
        try:
            admin_write_menubuilder(domain_name)
            Logging("create Menu Builder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        '''
    else:
        Logging("1.Create Menu Builder => Account is not admin")


def write_menu_menubuilder(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)
    if admin == True:
        try:
            write_layout_menubuilder(domain_name)
            Logging("create Menu Builder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        
    else:
        Logging("2.Create Menu Builder => Account is not admin")

    if admin == True:
        try:
            delete_menubuilder(domain_name)
            Logging("Delete Menu Builder successfully")
        except WebDriverException:
            Logging("Delete Menu Builder Fail")
        
    else:
        Logging("Delete => Account is not admin")
    




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
with open(local+'\\'+'luu_builder.txt','w') as builder:
    domain="http://qa.hanbiro.net"
    admin_menu_menubuilder(domain,builder)       
    write_menu_menubuilder(domain,builder)   


result=open(local+'\\result.txt','r')
file_result=result.read()
Logging(file_result)
'''






