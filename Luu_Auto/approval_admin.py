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
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Green,Yellow,Red,Commands
from luu_function import driver

# Page



def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Approval------------------------------------------------------")
    driver.get(domain_name + "/approval/list/progress/ireq/")
    time.sleep(2)
    Logging("1. Access Menu Approval successfully")
    Commands.Wait10s_ClickElement(data["approval"]["click_list_in_progress_approval"])
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin



def approval_write_all_form(domain_name):
    Logging("------------------------------------------------------Menu Approval------------------------------------------------------")
    time.sleep(2)
    #access_menu_approval = driver.find_element_by_xpath("//span[contains(.,'Approval')]")
    #access_menu_approval.click()
    #driver.get(domain_name + "/approval/list/progress/ireq/")
    #Logging("1. Access Menu Approval successfully")
    
    '''
    list_in_progress = driver.find_element_by_xpath(data["approval"]["list_data_in_progress_approval"])
    click_list_in_progress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_list_in_progress_approval"])))
    if  list_in_progress.is_displayed():
        click_list_in_progress.click()
        Logging("2. Click list In Progress successfully")
    else:
        Logging("2. Click list In Progress Fail")
    Logging("1. Click List Hide In Progress successfully")
    '''
    
    
    Logging("---------------- Write All Form ------------------")

    try:
        Commands.Wait10s_ClickElement(data["approval"]["admin_approval"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_all_form"])
        time.sleep(5)
        Logging("3. Click All Forms successfully")
        total=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
        Logging("---  Total All Form before create new : " + total)
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["icon_create_all_form"])
        Commands.Wait10s_ClickElement(data["approval"]["form_selection"])
        Commands.Wait10s_ClickElement(data["approval"]["folder_approval"])
        Logging("5. Click folder approval successfully")
        Commands.Wait10s_ClickElement(data["approval"]["agreement_route"])
        #click_agreement_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["agreement_route"])))
        #click_agreement_route.click()
        Logging("6. Click Agreement Route successfully")
        Commands.Wait10s_ClickElement(data["approval"]["click_common"])
        Logging("7. Click Common successfully") 
        try:
            Commands.Wait10s_ClickElement(data["approval"]["button_confirm"])
            Logging("8. Click button confirm successfully")
            form_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_form_name"])))
            form_name.send_keys(data["approval"]["form_name"])
            title_form_name=form_name.get_attribute("value")
            if(title_form_name==data["approval"]["form_name"]):
                Logging("7. Add Form Name =>pass")
            else:
                Logging("7. Add Form Name =>fail")
            Logging("8. Input Add Form Name successfully" + " :  " + data["approval"]["form_name"] )
            Commands.Wait10s_ClickElement(data["approval"]["icon_button_doc_no"])
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["button_save_doc_no"]) 
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 100)")
            time.sleep(3) 
            #editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
            #driver.switch_to.frame(editor_frame)
            #content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
            #content_input.send_keys(data["approval"]["content_form_name"])
            #driver.switch_to.default_content()
            
        except WebDriverException:
            Logging(" Create Form => ---- FAIL ")
            Commands.Wait10s_ClickElement(data["approval"]["btn_home_write_form"]) 
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_back_write_form"]) 
        time.sleep(1)

        Commands.Wait10s_ClickElement(data["approval"]["click_button_save_all_form"]) 
        time.sleep(2)
        Logging("9. Input Content All Form successfully")
        Logging("10. Save All Form successfully")
        time.sleep(3)
        total1=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
        time.sleep(2)
        total=so(total)
        total1=so(total1)    
        Logging("---  Total all form after create : ")
        time.sleep(2)
        Logging(total1)
        time.sleep(2)
        if total1== total +1 :
            Logging(" ***  Total All Form displayed correctly")
            Logging(Green("Write All Form => ---------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["pass"])
        else:
            Logging(Red(" Write All Form => ---- FAIL "))
            ValidateFailResultAndSystem("<div>[Approval]2. Write All Form </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["fail"])
        
        Logging("----------------Search Form by Type ------------------")
        try:
            time.sleep(2)
            total1=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
            total1=so(total1)
            time.sleep(2)
            Logging("---  Total all form before search : ")
            time.sleep(1)
            Logging(total1)
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["click_deatail_search_all_form"]) 
            Logging("1. Click Details successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["select_agreement_search_all_form"]) 
            Logging("2. Click Agreement Route successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["btn_search_all_form"]) 
            Logging("3. Click Button Search by Type successfully")
            Commands.Wait10s_ClickElement(data["approval"]["click_deatail_search_all_form"]) 
            time.sleep(2)
            total1=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
            total1=so(total1)
            time.sleep(2)
            total2=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
            total2=so(total2)
            Logging("---  Total all form after search : ")
            time.sleep(1)
            Logging(total2)
            time.sleep(3)
            if total2 <= total1 :
                Logging("Search Form by Type => ---------PASS")
                TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["pass"])
            else:
                Logging(" Search Form by Type => ---- FAIL ")
        except WebDriverException:
            Logging(" Search Form by Type => ---- FAIL ")

        Logging("----------------Delete All Form ------------------")
        try:
            Commands.Wait10s_InputElement_return(data["approval"]["txt_search_approval_form"],data["approval"]["search_form_delete"])
            time.sleep(5)
            Logging("1. Show form name Search successfully")
            Commands.Wait10s_ClickElement(data["approval"]["checkbox_all_form"])
            Logging("2. Click checkbox all Form successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["btn_delete_all_form"])
            Logging("3. Click button Delete successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_ok_delete_form"])
            Logging("5.Search and Delete  All Form successfully")
        except WebDriverException:
            Logging("=> Delete All Form Fail")
        time.sleep(1)

        try:
            Logging("----------------Create Form Section------------------")
            Commands.Wait10s_ClickElement(data["approval"]["btn_more"])
            Logging("1. Click button More successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["form_section"])
            Logging("2. Click Form Section successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["list_parent_folder"])
            Logging("3. Click Parent Folder successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["parent_folder_click_approval"])
            Logging("4. Click Approval in Parent folder successfully")
            Commands.Wait10s_ClickElement(data["approval"]["select_agreement_route"])
            Logging("5. Click Agreement Route successfully")
            Commands.Wait10s_InputElement(data["approval"]["txt_folder_name_section"],data["approval"]["folder_name_section"])
            Logging("6. Input Folder name Form Section successfully")
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_folder_name_section"])
            Logging("7. Click butotn Save successfully")
        except WebDriverException:
            Logging("=> Create Form Section Fail")

        time.sleep(1)


        
        Logging("----------------Check Create Form Section and Delete Form Section------------------")

        try:
            Commands.Wait10s_ClickElement(data["approval"]["btn_more"])
            Logging("1. Click button More successfully")
            Commands.Wait10s_ClickElement(data["approval"]["form_section"])
            Logging("2. Click Form Section successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["form_section_check_data"])
            Logging("3. Click Approval check data successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["form_section_select_agreement_route_check_data"])
            Logging("4. Click Agreement Route  check data successfully")
            Commands.scroll_view(data["approval"]["view_section_form_check_data"])
            Logging("5.Create Form Section successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["view_section_form_check_data"])
            Logging("6.Click Form Section successfully")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["delete_section_form"])
            Logging("7.Click button Delete Form Section successfully")
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_ok_delete_section_form"])
            Logging("8.Click button OK - Delete Form Section successfully")
        except WebDriverException:
            Logging("=> Create Form Section Fail")
        

    except WebDriverException:
        Logging("6.Create Form Fail")


def approval_write_all_official_form(domain_name):
    time.sleep(2)
    Logging("-------------- Write All Official Forms ------------------")  
    try:
        #Commands.Wait10s_ClickElement(data["approval"]["admin_approval"])
        time.sleep(1)
        Logging("2. Click Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["all_official_form"])
        Logging("1. Click All Official Forms successfully")
        Commands.Wait10s_ClickElement(data["approval"]["create_a_new_approval_route"])
        Logging("2. Click Create a new Approval Route successfully")
        now = datetime.now()
        name_all_official_approval = "Generated by selenium at" +" " +str(now)
        input_name_all_official_approval = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_textbox_name_official_forms"])))
        input_name_all_official_approval.send_keys(name_all_official_approval)
        time.sleep(1)
        Commands.SwitchToFrame_no(data["approval"]["input_editor"])
        Commands.Wait10s_InputElement_return(data["approval"]["input_editor_tynmce"],data["approval"]["content_form_name_official_forms"])
        driver.switch_to.default_content()
        time.sleep(2)
        Logging("5. Input Content All Form successfully")
        Commands.Wait10s_ClickElement(data["approval"]["button_save_all_offcial_form"])
        Logging("6. Save All Official Forms successfully")
        time.sleep(2)
        if 'Generated by' in driver.page_source :
            Logging(Green("=>  1. Write All Official Forms  PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["pass"])
        else:
            Logging(Red("=>  1. Write All Official Forms  FAIL"))
            ValidateFailResultAndSystem("<div>[Approval] Write All Official Forms  </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["fail"])
        Logging("-------------Delete All Official Forms - Admin---------------")
        Commands.scroll_view(data["approval"]["select_official_forms_delete"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["select_official_forms_delete"])
        Logging("1. Click checkbox Delete All Official Forms Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_delete_official_forms"])
        time.sleep(1)
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_approval_routes_admin"])
        Logging("3. Click button confirm successfully")
        Logging("=> Delete Default Approval Routes - Admin successfully")
    except WebDriverException:
        Logging("6.Write All Official Forms Fail")


def approval_view_all_approvals(domain_name):
   
    Logging("----------------- View All Approvals ------------------")
    try:
        Commands.scroll_view(data["approval"]["all_approvals"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["all_approvals"])
        Logging("1. Click All Approvals successfully")
        '''
        click_comprehensive_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["comprehensive_search"])))
        click_comprehensive_search.send_keys(data["approval"]["title_approvals"])
        click_comprehensive_search.send_keys(Keys.RETURN)
        '''
        Commands.Wait10s_ClickElement(data["approval"]["click_a_approval"])
        try:
            Commands.Wait10s_InputElement(data["approval"]["txt_input_secrutity_pw"],data["approval"]["secrutity_pw"])
            time.sleep(1)
            Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_secrutity_pw"])
            Logging(" Input Password successfully") 
        except WebDriverException:
            Logging("NOT SHOW Security Pasword ")
        Logging("3. View All Approvals successfully")
        time.sleep(1)
        if 'Date Created' in driver.page_source :
            Logging(Green("=> 1.View All Approvals=> ---------- PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["pass"])
        else:
            Logging(Red("=> 1.View All Approvals =>---------- FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]2. View All Approvals </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["fail"])
    except WebDriverException:
        Logging("View All Approvals  Fail ")

    
def approval_view_official_documentation(domain_name):
    Logging("--------------- View Official Documentation ------------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["official_documentation"])
        Logging("1. Click Official Documentation successfully")
        '''
        time.sleep(3)
        click_official_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["textbox_input_search"])))
        click_official_search.send_keys(data["approval"]["search_title_official_documentation"])
        click_official_search.send_keys(Keys.RETURN)
        time.sleep(3)
        Logging("2. Search Official Documentation successfully")
        '''
        Commands.Wait10s_ClickElement(data["approval"]["click_official_documenttation"])
        Logging("3. View Official Documentation successfully")
        time.sleep(2)
        if 'Print' in driver.page_source :
            Logging(Green(" => 1.View Official Documentation =>  PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["pass"])
        else:
            Logging(Red("=>1.View Official Documentation => FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]View Official Documentation </div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["fail"])
    except WebDriverException:
        Logging("View Official Documentation Fail ")


def approval_arbitrary_decision(domain_name):
    Logging("-------------- Arbitrary Decision Settings -----------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["click_arbitrary_decision"])
        Logging("1. Click Arbitrary Decision successfully")
        Commands.Wait10s_InputElement_return(data["approval"]["search_user_arbitrary_decision"],data["approval"]["search_user"])
        time.sleep(1)
        Logging("6. Search user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_arbitrary_decision"])
        Logging("3. Select user successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["button_click_save_arbitrary_decision"])
        Logging("3. Arbitrary Decision Settings successfully")
        Commands.scroll_view(data["approval"]["show_arbitrary_decision"])
        time.sleep(1)
        Logging(Green("=> Arbitrary Decision Settings =>--------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["pass"])
    except WebDriverException:
        Logging(Red("=> Arbitrary Decision Settings=>---------- FAIL"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["fail"])
    time.sleep(1)
    try:
        Logging("-------------Delete User Arbitrary Decision Settings ---------------")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_delete_arbitrary_decision"])
        Logging("1. Click User Delete Change Approval Route successfully")
        Commands.Wait10s_ClickElement(data["approval"]["button_click_save_arbitrary_decision"])
        Logging("2. Delete Change Approval Route successfully")
    except WebDriverException:
        Logging("Delete User Arbitrary Decision Settings Fail ")



'''
def approval_change_approval_route(domain_name):
    Logging("------------- Change Approval Route ---------------")
    click_change_approval_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["change_approval_route"])))
    click_change_approval_route.click()
    Logging("1. Click Change Approval Route successfully")
    time.sleep(1)
    click_folder_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["dept_user_change_approval"]))).click()
    select_user_change_approval_route = driver.find_element_by_xpath(data["approval"]["select_user_change_approval_route"])
    select_user_change_approval_route.click()
    Logging("3. Select user Change Approval Route successfully")
    time.sleep(1)
    click_save_change_approval_route = driver.find_element_by_xpath(data["approval"]["button_click_save_change_approval_route"])
    click_save_change_approval_route.click()
    time.sleep(1)
    Logging("3. Add User Change Approval Route successfully")
    time.sleep(2)
'''



    
def approval_default_approval_route(domain_name):
    Logging("------------- Default Approval Routes - Admin---------------")

    try:
        Commands.Wait10s_ClickElement(data["approval"]["select_default_approval_routes_admin"])
        time.sleep(1)
        Logging("1. Click Default Approval Route Admin successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_create_a_new_approval_route_admin"])
        Logging("2. Click Create a new approval Route successfully")
        now = datetime.now()
        name_default_approval_routes = "Generated by selenium at" +" " +str(now)
        input_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_approval_route_name_admin"])))
        input_default_approval_routes.send_keys(name_default_approval_routes)
        Commands.Wait10s_ClickElement(data["approval"]["icon_org_default_approval_name_admin"])
        Logging("5. Click Org successfully")

        '''
        search_org_default_approval_routes_admin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_org_default_admin"])))
        search_org_default_approval_routes_admin.send_keys(data["approval"]["user_search_org_approval"])
        search_org_default_approval_routes_admin.send_keys(Keys.RETURN)
        time.sleep(1)
        Logging("6. Search user successfully")
        time.sleep(3)
        '''

        try:
            Commands.Wait10s_ClickElement(data["approval"]["dept_defaul_approval_admin"])
            Commands.Wait10s_ClickElement(data["approval"]["select_user_default_approval_admin"])
            time.sleep(5)
            Logging("7. Select user successfully")
            try:
                check_add_user_share = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_user_org_default_approval_admin"])))
                Logging("8. Add User successfully")
                time.sleep(2)
                Commands.scroll_view(data["approval"]["btn_save_org_app_default_admin"])
                Commands.Wait10s_ClickElement(data["approval"]["btn_save_org_app_default_admin"])
                Logging("9. Save user successfully")
            except WebDriverException:
                Logging("Add User Share => Fail")
        except WebDriverException:
            Logging("9. Save user Fail")
            Commands.Wait10s_ClickElement(data["approval"]["home_org_default_approval_admin"])
        try:
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_defaul_approval_routes"])
            Logging("10. Save Default Approval Routes successfully")
        except WebDriverException:
            Logging("Add User Share => Fail")
            Commands.Wait10s_ClickElement(data["approval"]["btn_close_warning_defaul_approval_routes"])

        Logging("-------------Delete Default Approval Routes - Admin---------------")
        try:
            driver.execute_script("window.scrollTo(0, 100)")
            time.sleep(2)
            Commands.Wait10s_ClickElement(data["approval"]["check_approval_routes_type_admin"])
            Logging("1. Click checkbox Delete Default Approval Routes Admin successfully")
            driver.execute_script("window.scrollTo(100, 0)")
            time.sleep(1)
            try:
                Commands.Wait10s_ClickElement(data["approval"]["btn_delete_approval_routes_admin"])
                Logging("2. Click button Delete successfully")
                Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_approval_routes_admin"])
                Logging("3. Click button confirm successfully")
                Logging("=> Delete Default Approval Routes - Admin successfully")
            except WebDriverException:
                Logging("Not show data delete")
            time.sleep(1)
        except WebDriverException:
            Logging("Delete Default Approval Routes - Admin => Fail")
        time.sleep(1)
        Logging("------------- Set Official Seal - Admin ---------------")
        try:
            Commands.Wait10s_ClickElement(data["approval"]["select_value_set_official_seal"])
            Logging("1. Click Set Official Seal successfully")
            time.sleep(1)
            get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["file_set_official_seal"])))
            get_file.send_keys(luu_function.file_img)
            Logging("2. Attch Signature Image successfully")
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_set_official_seal"])
            Logging("3. Click button Save Set Official Seal successfully")
            time.sleep(1)
        except WebDriverException:
            Logging("Set Official Seal - Admin => Fail")
        time.sleep(1)
        try:
            Logging("------------- Delete Set Official Seal - Admin ---------------")
            Commands.Wait10s_ClickElement(data["approval"]["check_data_save_set_official_seal"])
            Commands.Wait10s_ClickElement(data["approval"]["btn_save_set_official_seal"])
        except WebDriverException:
            Logging("=> Delete Set Official Seal - Admin=>---------- FAIL")
        

        '''
        Logging("------------- Search Discarded Documents - Admin ---------------")
        time.sleep(1)
        click_discarded_documents = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_discarded_documents"]))).click()
        time.sleep(2)
        click_discarded_documents_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_discarded_document"])))
        click_discarded_documents_search.send_keys(data["approval"]["comprehensive_search_documet"])
        click_discarded_documents_search.send_keys(Keys.RETURN)
        time.sleep(5)
        time.sleep(2)
        if 'Luu' in driver.page_source :
            Logging(" => 1.View Official Documentation =>  PASS")
        else:
            Logging("=>1.View Official Documentation => FAIL")
        time.sleep(2)
        Logging("1. Search Discarded Documents successfully")
        '''
    except WebDriverException:
        Logging("Default Approval Routes - Admin Fail ")




def approval_default_approval_route_setting(domain_name):

    Logging("------------- Default Approval Routes-Setting---------------")
    try:
        Commands.scroll_view(data["approval"]["click_sttings_approval"])
        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_sttings_approval"])))
        #element.location_once_scrolled_into_view
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["click_sttings_approval"])
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Logging("1. Click Settings successfully")
        Commands.Wait10s_ClickElement(data["approval"]["select_default_approval_routes"])
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Logging("2. Click Default Approval Route successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["create_default_approval_routes"])
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
        Commands.Wait10s_ClickElement(data["approval"]["create_default_approval_routes"])
        time.sleep(1)
        Logging("3. Click button Create a new Approval Route successfully")
        now = datetime.now()
        name_default_approval_routes_setting = "Generated by selenium at" +" " +str(now)
        input_default_approval_routes_setting = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["input_appproval_route_name"])))
        input_default_approval_routes_setting.send_keys(name_default_approval_routes_setting)
        Commands.Wait10s_ClickElement(data["approval"]["click_org_default_approval_routes"])
        Logging("4. Click Org successfully")
        Commands.Wait10s_InputElement_return(data["approval"]["search_user_approval_in_org"],data["approval"]["user_search_org_approval"])
        time.sleep(2)
        Logging("5. Search user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["select_user_defaul_setting"])
        

        '''
        time.sleep(1)
        #select_dept_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_dept_defaul_setting"]))).click()
        time.sleep(1)
        select_user_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["user_reviewer_01"])))
        select_user_org_default_approval_routes.click()
        time.sleep(1)
        add_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_add_user"])))
        add_user_org_default_approval_routes.click()
        Logging("8. Add user successfully")
        time.sleep(2)
        try:
            check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
            if check_show_sub_dept.is_displayed():
                click_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_ok_select_sub_dept"]))).click()
                Logging("=> Select Sub Dept => --------PASS")
            else:
                Logging("=> Sub Dept not show  ")
                
        except WebDriverException:
            Logging("Not Show sub Dept ")
        '''

        time.sleep(1)
        Logging("6. Select user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["icon_add_user"])
        Logging("7. Add user successfully")
        try:
            check_add_user_share = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_user_org_default_approval_setting"])))
            Logging("8. Add User successfully")
            Commands.Wait10s_ClickElement(data["approval"]["button_save_reviewers_approval"])
            Logging("9. Save user successfully")
        except WebDriverException:
            Logging("Add User Share => Fail")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_default_approval_route"])
        Logging("10. Save Default Approval Routes successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_default_approval_route"])
        Logging("11. Close successfully")
        time.sleep(2)
        if 'Generated by' in driver.page_source :
            Logging(Green("=> 1. Default Approval Routes => ------------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["pass"])
        else:
            Logging(Red("=> 1. Default Approval Routes => ------------ FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]Default Approval Routes</div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["fail"])
    except WebDriverException:
        Logging("Default Approval Routes-Setting Fail ")

    try:
        Logging("-------------Delete Default Approval Routes-Setting---------------")
        Commands.Wait10s_ClickElement(data["approval"]["btn_check_all_approval_routes"])
        Logging("1. Click checkbox Delete Default Approval Routes successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_delete_approval_routes"])
        Logging("2. Click button Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm"])
        Logging("3.Delete  Delete Default Approval Routes successfully")
    except WebDriverException:
        Logging("Delete Default Approval Routes-Setting => Fail")



def approval_manage_my_folder_setting(domain_name):
    Logging("------------- Manage My Folder---------------")
    try:
        Commands.Wait10s_ClickElement(data["approval"]["setting_manager_my_folder"])
        Logging("1. Click Manage My Folder successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["select_my_folder"])
        Logging("2. Click My Folder successfully")
        time.sleep(1)
        #Commands.Wait10s_InputElement(data["approval"]["txt_folder_name_approval"],data["approval"]["folder_name_approval"])
        now = datetime.now()
        name_manage_my_folder_setting = "Generated by selenium at" +" " +str(now)
        input_name_manage_my_folder_setting = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_folder_name_approval"])))
        input_name_manage_my_folder_setting.send_keys(name_manage_my_folder_setting)
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_folder_approval"])
        Logging("4. Click Button Save Folder successfully")
        time.sleep(3)
        if 'Generated by' in driver.page_source :
            Logging(Green("=> 1. Add Manage My Folder => ------------PASS"))
            TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["pass"])
        else:
            Logging(Red("=> 1. Add Manage My Folder => ------------ FAIL"))
            ValidateFailResultAndSystem("<div>[Approvals]Manage My Folder</div>")
            TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["fail"])
        Logging("-------------Delete Manage My Folder---------------")
        Commands.Wait10s_ClickElement(data["approval"]["select_my_folder_delete"])
        Logging("1. Click My Folder Delete successfully")
        Commands.Wait10s_ClickElement(data["approval"]["icon_delete_my_folder"])
        Logging("2. Click icon Delete My Folder successfully")
        Logging("=> Delete My Folder successfully")
    except WebDriverException:
        Logging("Manage My Folder Fail ")



def approval_display_setting(domain_name):
    
    Logging("-------------Display Settings ---------------")
    try:
        Commands.scroll_view(data["approval"]["click_display_settings"])
        time.sleep(2)
        Commands.Wait10s_ClickElement(data["approval"]["click_display_settings"])
        Logging("1. Click Display Settings successfully")
        
        '''
        click_org_elect_deputy_user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_org_select_deputy_user"]))).click()
        Logging("2. Click Select Deputy User successfully")
        search_org_user_deputy = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_deputy"])))
        search_org_user_deputy.send_keys(data["approval"]["user_search_org_approval"])
        search_org_user_deputy.send_keys(Keys.RETURN)
        time.sleep(1)
        Logging("3. Search user successfully")
        time.sleep(3)
        select_user_deputy = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_deputy"])))
        select_user_deputy.click()
        time.sleep(3)
        time.sleep(1)
        Logging("4. Select user Deputy successfully")
        '''

        Commands.Wait10s_ClickElement(data["approval"]["click_org_user_with_per_to_read"])
        Logging("2. Click Select Deputy User successfully")

        '''
        search_user_per_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_user_per_to_read"])))
        search_user_per_to_read.send_keys(data["approval"]["user_search_org_approval"])
        search_user_per_to_read.send_keys(Keys.RETURN)
        time.sleep(1)
        Logging("6. Search user Permission to read successfully")
        '''

        Commands.Wait10s_ClickElement(data["approval"]["select_dept_per_to_read"])
        Commands.Wait10s_ClickElement(data["approval"]["select_user_to_read"])
        Commands.Wait10s_ClickElement(data["approval"]["icon_add_user_per_to_read"])
        time.sleep(1)
        try:
            check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
            Commands.Wait10s_ClickElement(data["approval"]["click_ok_select_sub_dept"])
            Logging("=> Select Sub Dept => --------PASS") 
        except WebDriverException:
            Logging("Not Show sub Dept ")
        Logging("3. Add user successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_add_user_to_read"])
        Logging("4. Save user successfully")
        get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_attach_signature_image"])))
        get_file.send_keys(luu_function.file_img)
        Logging("5. Attch Signature Image successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_signature_image"])
        Logging("6. Click Button save successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_signature"])
        Logging("7. Click Button Close successfully")
        time.sleep(1)
        Logging(Green("=> Change Signature Image  => --------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["pass"])
    except WebDriverException:
        Logging(Red("=> Change Signature Image  => --------FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]Change Signature Image</div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["fail"])


    try:
        Logging("-------------Delete Display Settings ----------------")
        Commands.Wait10s_ClickElement(data["approval"]["click_org_user_with_per_to_read"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["click_icon_delete_user_per"])
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_add_user_to_read"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["delete_signature_image"])
        Logging("1. Click Icon Delete successfully")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_confirm_delete_signature"])
        Logging("2. Click Button Confirm successfully")
        Logging("=> Delete Signature Image  => --------PASS")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["approval"]["btn_save_signature_image"])
        time.sleep(1)
        Logging("3. Click Button save successfully")
        Commands.Wait10s_ClickElement(data["approval"]["btn_close_signature"])
        Logging("4. Click Button Close successfully")
        Logging("=> Delete Display Settings  => --------PASS")
    except WebDriverException:
        Logging("Delete Display Settings Fail ")




def access_menu_approval(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)

    
    if admin == True:
        try:
            approval_write_all_form(domain_name)
            Logging("Create all Form successfully")
        except WebDriverException:
            Logging("Fail to Create all Form")
        
    else:
        Logging("1.Write All Form => Account is not admin")
    

    if admin == True:
        try:
            approval_write_all_official_form(domain_name)
            Logging("Create All Official Form successfully")
        except WebDriverException:
            Logging("Fail to Create All Official Form")
        
    else:
        Logging("2.Write All Official Forms => Account is not admin")

    if admin == True:
        try:
            approval_view_all_approvals(domain_name)
            Logging("View All Approval  successfully")
        except WebDriverException:
            Logging("Fail to View All Approval ")
        
    else:
        Logging("3.View All Approvals => Account is not admin")

    if admin == True:
        try:
            approval_view_official_documentation(domain_name)
            Logging("View Official Documentation  successfully")
        except WebDriverException:
            Logging("Fail to Official Documentation ")
        
    else:
        Logging("4.View Official Documentation in Admin => Account is not admin")

    
    if admin == True:
        try:
            approval_arbitrary_decision(domain_name)
            Logging("Create Arbitrary Decision successfully")
        except WebDriverException:
            Logging("Fail to Arbitrary Decision ")
        
    else:
        Logging("5.Create Arbitrary Decision => Account is not admin")
    
    '''
    if admin == True:
        try:
            approval_change_approval_route(domain_name)
            Logging("Change Approval Route Admin successfully")
        except WebDriverException:
            Logging("Fail to Change Approval Route Admin ")
        
    else:
        Logging("6.Change Approval Route => Account is not admin")


    '''


    if admin == True:
        try:
            approval_default_approval_route(domain_name)
            Logging("Change Default Approval Routes Admin successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Admin ")
        
    else:
        Logging("7.Default Approval Routes in Admin => Account is not admin")


    if admin == True:
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")
        
    else:
        Logging("User Change Default Approval Routes")
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")



    if admin == True:
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")
        
    else:
        Logging("User create Manage My Folder")
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")


    if admin == True:
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")
        
    else:
        Logging("User create Display Settings ")
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")





    time.sleep(2)
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)
    
time.sleep(3)

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
with open(os.path.dirname(Path(__file__).absolute())+'\\'+'luu_approval.txt','w') as approval:
    domain="http://qa.hanbiro.net"
    access_menu_approval(domain,approval)



result=open(os.path.dirname(Path(__file__).absolute())+'\\result.txt','r')
file_result=result.read()
Logging(file_result)
'''
  