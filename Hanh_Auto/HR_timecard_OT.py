#from NQ_HR_timecard import clock_in
from ast import Pass
import re, sys, json#, testlink
import time, random
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from random import choice
from pathlib import Path
from datetime import datetime
import os.path
import time
import select
from H_functions import driver, data,TesCase_LogResult, Logging#, TestlinkResult_Fail, TestlinkResult_Pass
from framework_sample import *

now = datetime.now()
date_time = now.strftime("%Y/%m/%d, %H:%M:%S")

date_id = date_time.replace("/", "").replace(":", "").replace(", ", "")
n = random.randint(1,1000)

now = datetime.now()
date = now.strftime("%m/%d/%y %H:%M:%S")

print_date = now.strftime("%H:%M")


def clock_in():
    Commands.ClickElement(data["TIMECARD"]["timesheet_page"])
    Waits.WaitElementLoaded(10, data["TIMECARD"]["timesheet_wait"])
    time.sleep(3)
    output_clockin = Functions.GetElementText(data["TIMECARD"]["out_put_clockin"])
    time.sleep(2)
    Logging("Clock-in: " + output_clockin)
    if output_clockin == "-":
        output_clockin = None
    else:
        return output_clockin

def Napproval_OT(time_clock_in):
    if bool(time_clock_in) == True:
        Logging("Run pre OT function")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["check_true"]["pass"])
        text_format_hour = output(data["TIMECARD"]["timesheet_wait"])
        clock_in_default_hour = text_format_hour.split(" ")[0]
        #Logging(clock_in_default_hour)

        #Calculate to find out valid time 
        text_OT_since = output(data["TIMECARD"]["text_OT_since"])
        Logging("OT since: " + text_OT_since)
        OT_since_hour_decimal = int(text_OT_since.split(":")[0])
        OT_since_minute_decimal = int(text_OT_since.split(":")[1])

        OT_since_decimal = ((OT_since_minute_decimal) / 60) + (OT_since_hour_decimal)
        Logging("OT time after change to decimal: " + str(OT_since_decimal))

        work_shift = driver.find_element_by_xpath(data["TIMECARD"]["work_shift"])
        work_shift.location_once_scrolled_into_view
        Commands.ClickElement(data["TIMECARD"]["work_shift"])
        time.sleep(3)
        Commands.ClickElement(data["TIMECARD"]["work_shift_search"])
        time.sleep(3)
        wss_search2 =  Commands.InputElement(data["TIMECARD"]["ws_search"], "automationtest1")
        wss_search2.send_keys(Keys.ENTER)
        time.sleep(3)
        Commands.ClickElement(data["TIMECARD"]["click_first_choice"])
        Commands.ClickElement(data["TIMECARD"]["work_shift_search"])
        time.sleep(3)
        text_work_method_name = output(data["TIMECARD"]["text_work_method_name"])
        Logging("Work method name: " + text_work_method_name)
        x9 = text_work_method_name

        basic = driver.find_element_by_xpath(data["TIMECARD"]["basic"])
        basic.location_once_scrolled_into_view
        basic.click()
        Waits.WaitElementLoaded(10, data["TIMECARD"]["setting_wait"])
        time.sleep(2)
        Commands.ClickElement(data["TIMECARD"]["work_policy"])
        time.sleep(3)
        work_policy = driver.find_element_by_xpath(data["TIMECARD"]["work_policy"])
        Commands.ClickElement(data["TIMECARD"]["click_work_policy"] % x9)

        #Check OT data
        OT_data = driver.find_element_by_xpath(data["TIMECARD"]["OT_data"])
        OT_data.location_once_scrolled_into_view
        time.sleep(2)
        OT_data_time = driver.find_element_by_xpath(data["TIMECARD"]["OT_data_time"])
        OT_data_time_value = OT_data_time.get_attribute("value")
        #Logging("Total of OT time: " + OT_data_time_value)
        OT_data_time_hour = OT_data_time_value
        OT_data_time_decimal = int(OT_data_time_hour)
        Logging("Total of OT time: " + str(OT_data_time_decimal) + "hrs")

        #Print available application time
        Commands.ClickElement(data["TIMECARD"]["over_time_work"]).click()
        available_application_time = driver.find_element_by_xpath(data["TIMECARD"]["available_application_time"])
        available_application_time_value = available_application_time.get_attribute("value")
        #Logging(available_application_time_value)
        Logging("Available application time: " + available_application_time_value + " hours")
        available_application_time_hour = available_application_time_value
        available_application_time_decimal = int(available_application_time_hour)

        '''Calculate to find out valid time'''
        # Logging(OT_since_decimal)
        # Logging(available_application_time_decimal)
        result = OT_since_decimal - available_application_time_decimal
        #Logging("Valid time to apply pre-ot: " + result + "hr")
        Logging("Valid time to apply pre-ot(decimal): " + str(result))

        Logging("Current time: " + print_date)
        print_date_hour_decimal = int(print_date.split(":")[0])

        print_date_minute_decimal = int(print_date.split(":")[1])

        print_date_decimal = ((print_date_minute_decimal) / 60) + (print_date_hour_decimal)
        Logging("Current time after change to decimal: " + str(print_date_decimal))

        try:
            # Logging(print_date)
            # Logging(result)
            if int(print_date_decimal) < int(result):
                Logging("=> Able to apply pre-OT")
                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_check"]["pass"])
                driver.refresh()
                Commands.ClickElement(data["TIMECARD"]["setting_approval"])
                # Logging("- Setting: Basic_Approval")
                time.sleep(3)
                OT = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["OT_scroll"])))
                OT.location_once_scrolled_into_view
                time.sleep(2)
                OT_list = Functions.GetListLength(data["TIMECARD"]["OT_list"])

                approval_OT_list = []
                i = 0
                for i in range(OT_list):
                    i += 1
                    approvalOT = driver.find_element_by_xpath(data["TIMECARD"]["approvalOT"] + data["TIMECARD"]["approval_OT"] % str(i))
                    approval_OT_list.append(approvalOT.text)
                
                Logging("Total of type Approval OT: " + str(len(approval_OT_list)))
                #Logging(approval_OT_list)

                x = random.choice(approval_OT_list)
                time.sleep(1)
                select_approval_OT = driver.find_element_by_xpath(data["TIMECARD"]["OT_list"] + data["TIMECARD"]["select_approval_OT"] % str(x))
                select_approval_OT.click()
                Logging("Select Approval OT type")
                time.sleep(2)
                Logging("Approval type: " + str(x))

                if str(x) == "Approval Line":
                    try:
                        approver = driver.find_element_by_xpath(data["TIMECARD"]["approver"])
                        if approver.text == "No data was found.":
                            Logging("- Don't have approval line")
                            Commands.ClickElement(data["TIMECARD"]["add_approver"])
                            Waits.WaitElementLoaded(10, data["TIMECARD"]["wait_OT"])
                            time.sleep(2)
                            approval_line = Commands.InputElement(data["TIMECARD"]["approval_line"], data["name_keyword"][1])
                            approval_line.send_keys(Keys.ENTER)
                            time.sleep(3)
                            Commands.ClickElement(data["TIMECARD"]["select_user"])
                            Commands.ClickElement(data["TIMECARD"]["plus_button"])
                            Commands.ClickElement(data["TIMECARD"]["save_approver"])
                            Logging("- Save approval line")
                            approver_list = Waits.WaitElementLoaded(10,  data["TIMECARD"]["approver_list"] + data["name_keyword"][1] + "')]")
                            if approver_list.is_displayed():
                                Logging("- Save approvers list Successfully")
                            else:
                                Logging("- Save approvers list Fail")
                        else:
                            Logging("- Approval line has already")
                    except:
                        Logging()

                driver.refresh()
                time.sleep(3)
                Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
                time.sleep(1)
                Commands.ClickElement(data["TIMECARD"]["calendar"])
                Waits.WaitElementLoaded(10, data["TIMECARD"]["wait_calendar"])
                time.sleep(3)
                Commands.ClickElement(data["TIMECARD"]["add_event"])
                time.sleep(1)
                Commands.ClickElement(data["TIMECARD"]["add_OT"])
                time.sleep(3)
                #Check max application time
                text_max_application_time = output(data["TIMECARD"]["text_max_application_time"])
                #Logging("Max application time: " + text_max_application_time)
                max_application_hour = text_max_application_time.split("H")[0]
                Logging("Max application time: " + max_application_hour)

                text_remaining_OT_time = output(data["TIMECARD"]["text_remaining_OT_time"])
                #Logging("Remaining OT time: " + text_remaining_OT_time)
                remaining_OT_number = text_remaining_OT_time.split("/")[0].split("H")[0]
                Logging("Remaining OT time: " + remaining_OT_number)

                #Calculation to check pre OT data
                # Logging(max_application_hour)
                # Logging(remaining_OT_number)
                # Logging(OT_data_time_decimal)
                if int(max_application_hour) + int(remaining_OT_number) == OT_data_time_decimal:
                    Logging("Max application time is correct")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["pass"])
                else:
                    Logging("Max application time is false")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["fail"])

                #Estimate working hours
                text_estimate_default = output(data["TIMECARD"]["text_estimate_default"])
                Logging("Estimate time before select filter: " + text_estimate_default)
                estimate_time_decimal = int(text_estimate_default.split("~")[1].split(":")[0])
                #Logging(estimate_time_decimal)


                driver.find_element_by_xpath(data["TIMECARD"]["filter"]).click()
                filters_OT_list = Functions.GetListLength(data["TIMECARD"]["filters_OT_list"])

                list_filters_OT = []
                y = 0
                for y in range(filters_OT_list):
                    y += 1
                    filters = driver.find_element_by_xpath(data["TIMECARD"]["filters"] % str(y))
                    list_filters_OT.append(filters.text)

                m = random.choice(list_filters_OT)
                filter_time = driver.find_element_by_xpath(data["TIMECARD"]["filter_time"] % str(m))
                filter_time.click()
                Logging("Select filters time OT")
                time.sleep(3)

                filter_number = driver.find_element_by_xpath(data["TIMECARD"]["filter_number"])
                m1 = filter_number.text
                #Logging(m1)
                filter_number_decimal = int(m1.split(" ")[0])
                #Logging(filter_number_decimal)

                #Check estimate time
                text_estimate_after_select_OT = output(data["TIMECARD"]["text_estimate_after_select_OT"])
                Logging("Estimate time after select filter: " + text_estimate_after_select_OT)
                estimate_after_select_OT_decimal = int(text_estimate_after_select_OT.split("~")[1].split(":")[0])
                #Logging(estimate_after_select_OT_decimal)

                try:
                    if estimate_time_decimal + filter_number_decimal == estimate_after_select_OT_decimal:
                        Logging("Estimate working hours is correct")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_estimate"]["pass"])
                    else:
                        Logging("Estimate working hours is false")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_estimate"]["fail"])
                except:
                    Logging(" ")


                memo_approval_line = Commands.InputElement(data["TIMECARD"]["memo_approval_line"], "I would like to OT " + str(m) + " after work. Date: " + date)
                time.sleep(3)
                #Check details data
                try:  
                    # date_data = driver.find_element_by_xpath(data["TIMECARD"]["date_data"])
                    # date_data_value = date_data.get_attribute("value")
                    date_data = Functions.GetInputValue(data["TIMECARD"]["date_data"])
                    #Logging("Date: " + str(date_data_value))
                except:
                    Logging(" ")
                
                try:
                    #memo_data = driver.find_element_by_xpath(data["TIMECARD"]["memo_approval_line"]).text
                    memo_data = Functions.GetElementText(data["TIMECARD"]["memo_approval_line"])
                    #Logging("Memo: " + memo_data)
                except:
                    Logging(" ")
                try:
                    #approver_data = driver.find_element_by_xpath(data["TIMECARD"]["route_add_event"]).text
                    approver_data = Functions.GetElementText(data["TIMECARD"]["route_add_event"])
                    #Logging ("Approver: " + approver_data)
                except:
                    Logging(" ")

                Commands.ClickElement(data["TIMECARD"]["save_approval_line"])
                Logging("- Apply Pre OT")

                try:
                    noty_success = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["pre_OT_noty"])))
                    time.sleep(3)
                    noty_list = [data["TIMECARD"]["pre_OT_noty_success"][0], data["TIMECARD"]["pre_OT_noty_success"][1]]
                    if noty_success.text in noty_list:
                        Logging("- Apply Pre OT Successfully")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["pass"])
                    elif noty_success.text == data["TIMECARD"]["pre_OT_noty_error"]:
                        Logging("- Apply Pre OT has already")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["pass"])
                        time.sleep(3)
                        Commands.ClickElement(data["TIMECARD"]["exit_button"])
                        time.sleep(2)
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["exit"]))).click()
                    else:
                        Logging("- Apply Pre OT Fail")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["fail"])

                except:
                    Logging("- Apply Pre OT Fail")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["fail"])


                time.sleep(5)
                Commands.ClickElement(data["TIMECARD"]["approval"])
                #Logging("- My Timecard: Approval")
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["approval_list"])))
                time.sleep(3)
                pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["pre_OT"])
                try:
                    if pre_OT.text == "Over Time (Pre)":
                        Logging("- Approval list: Pre OT")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_displayed"]["pass"])
                        #Scroll to detail
                        slider = driver.find_element_by_xpath("//div[@ref='eBodyHorizontalScrollViewport']")
                        horizontal_bar = driver.find_element_by_xpath("//div[@ref='eHorizontalRightSpacer']")
                        webdriver.ActionChains(driver).click_and_hold(slider).move_to_element(horizontal_bar).perform()
                        webdriver.ActionChains(driver).release().perform()
                        time.sleep(5)
                        Commands.ClickElement(data["TIMECARD"]["detail"])
                        Logging("- View detail approval")
                        time.sleep(2) 
                        if str(x) == "Automatic approval":
                            status_pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["status_pre_OT"])
                            if status_pre_OT.text == "Approved":
                                Logging("- Pre OT has been approved automatically")
                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT_auto"]["pass"])
                                #Details data
                                date_data_check = driver.find_element_by_xpath(data["TIMECARD"]["date_data_check"])
                                Logging("Date: " + date_data_check.text)
                                memo_data_check = driver.find_element_by_xpath(data["TIMECARD"]["memo_data_check"])
                                Logging("Memo: " + memo_data_check)
                                time_data_check = driver.find_element_by_xpath(data["TIMECARD"]["time_data_check"])
                                Logging("Duration: " + time_data_check)
                                time_data_check_decimal = int(time_data_check.text.split(" ")[0].split("H")[0])

                                try:
                                    if time_data_check.is_displayed:
                                        Logging("Duration is displayed")
                                        try:
                                            if time_data_check_decimal == filter_number_decimal:
                                                Logging("Duration is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["pass"])
                                        except: 
                                                Logging("Duration is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["fail"])
                                    else:
                                        Logging("Duration is empty")
                                except:
                                    Logging("Duration is empty")

                                try:
                                    if date_data_check.is_displayed:
                                        Logging("Date is displayed")
                                        try:
                                            if date_data_check.text == str(date_data):
                                                Logging("Data is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["pass"])
                                        except: 
                                                Logging("Data is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["fail"])
                                    else:
                                        Logging("Date is empty")
                                except:
                                    Logging("Date is empty")
                                
                                try:
                                    if memo_data_check.is_displayed:
                                        Logging("Memo is displayed")
                                        try:
                                            if memo_data_check.text == memo_data.text:
                                                Logging("Memo is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["pass"])
                                        except: 
                                                Logging("Memo is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["fail"])
                                    else:
                                        Logging("Memo is empty")
                                except:
                                    Logging("Memo is empty")

                                Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                time.sleep(2)
                            else:
                                Logging("- Pre OT hasn't been approved automatically")
                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT_auto"]["fail"])
                                Logging("=> Fail")
                                Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                time.sleep(2)
                        else:
                            status_pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["status_pre_OT"])
                            time.sleep(2)
                            if status_pre_OT.text == "Approved":
                                Logging("- Pre OT has been Approved")
                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approve_pre_OT"]["pass"])
                                #Details data
                                date_data_check = driver.find_element_by_xpath(data["TIMECARD"]["date_data_check"])
                                Logging("Date: " + date_data_check.text)
                                memo_data_check = driver.find_element_by_xpath(data["TIMECARD"]["memo_data_check"])
                                Logging("Memo: " + memo_data_check.text)
                                time_data_check = driver.find_element_by_xpath(data["TIMECARD"]["time_data_check"])
                                Logging("Duration: " + time_data_check.text)
                                time_data_check_decimal = int(time_data_check.text.split(" ")[0].split("H")[0])
                                try:
                                    if time_data_check.is_displayed:
                                        Logging("Duration is displayed")
                                        try:
                                            if time_data_check_decimal == filter_number_decimal:
                                                Logging("Duration is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["pass"])
                                        except: 
                                                Logging("Duration is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["fail"])
                                    else:
                                        Logging("Duration is empty")
                                except:
                                    Logging("Duration is empty")

                                try:
                                    if date_data_check.is_displayed:
                                        Logging("Date is displayed")
                                        try:
                                            if date_data_check.text == str(date_data):
                                                Logging("Data is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["pass"])
                                        except: 
                                                Logging("Data is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["fail"])
                                    else:
                                        Logging("Date is empty")
                                except:
                                    Logging("Date is empty")
                                
                                try:
                                    if memo_data_check.is_displayed:
                                        Logging("Memo is displayed")
                                        try:
                                            if memo_data_check.text == memo_data:
                                                Logging("Memo is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["pass"])
                                        except: 
                                                Logging("Memo is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["fail"])
                                    else:
                                        Logging("Memo is empty")
                                except:
                                    Logging("Memo is empty")


                                Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                time.sleep(2)
                            elif status_pre_OT == "Cancelled":
                                Logging("- Pre OT has been Cancelled")
                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT"]["pass"])
                                Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                time.sleep(2)
                            elif status_pre_OT == "Progressing":
                                Logging("- Pre OT is in progressing")
                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["progress_pre_OT"]["pass"])
                                #Details data
                                date_data_check = driver.find_element_by_xpath(data["TIMECARD"]["date_data_check"])
                                Logging("Date: " + date_data_check.text)
                                memo_data_check = driver.find_element_by_xpath(data["TIMECARD"]["memo_data_check"])
                                Logging("Memo: " + memo_data_check.text)

                                try:
                                    approver_data_check = driver.find_element_by_xpath(data["TIMECARD"]["route_add_event"])
                                    Logging ("Approver: " + approver_data_check.text)
                                    try:
                                        if approver_data_check.is_displayed:
                                            Logging("Approver is displayed")
                                            try:
                                                if approver_data_check.text == approver_data:
                                                    Logging("Approver is saved successfully")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["pass"])
                                            except: 
                                                    Logging("Approver is saved failed")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["fail"])
                                        else:
                                            Logging("Approver is empty")
                                    except:
                                        Logging("Approver is empty")
                                except:
                                    Logging ("Approver is empty")

                                time_data_check = driver.find_element_by_xpath(data["TIMECARD"]["time_data_check"])
                                Logging("Duration: " + time_data_check.text)
                                time_data_check_decimal = int(time_data_check.text.split(" ")[0].split("H")[0])

                                try:
                                    if time_data_check.is_displayed:
                                        Logging("Duration is displayed")
                                        try:
                                            if time_data_check_decimal == filter_number_decimal:
                                                Logging("Duration is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["pass"])
                                        except: 
                                                Logging("Duration is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["fail"])
                                    else:
                                        Logging("Duration is empty")
                                except:
                                    Logging("Duration is empty")

                                try:
                                    if date_data_check.is_displayed:
                                        Logging("Date is displayed")
                                        try:
                                            if date_data_check.text == str(date_data):
                                                Logging("Data is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["pass"])
                                        except: 
                                                Logging("Data is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["fail"])
                                    else:
                                        Logging("Date is empty")
                                except:
                                    Logging("Date is empty")
                                
                                try:
                                    if memo_data_check.is_displayed:
                                        Logging("Memo is displayed")
                                        try:
                                            if memo_data_check.text == memo_data:
                                                Logging("Memo is saved successfully")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["pass"])
                                        except: 
                                                Logging("Memo is saved failed")
                                                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["fail"])
                                    else:
                                        Logging("Memo is empty")
                                except:
                                    Logging("Memo is empty")


                                Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                time.sleep(2)
                            else:
                                status_pre_OT.click()
                                Logging("- Cancel Pre OT")
                                time.sleep(2)
                                Commands.ClickElement(data["TIMECARD"]["yes_but"][1])
                                time.sleep(5)
                                Commands.ClickElement(data["TIMECARD"]["reload"])
                                status_update = Waits.WaitElementLoaded(10, data["TIMECARD"]["status_update"])
                                time.sleep(5)
                                if status_update.text == "Cancelled":
                                    Logging("- Cancel Pre OT successfully")
                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["click_cancel_pre_OT"]["pass"])
                                    #Details data
                                    open_detail = Commands.ClickElement(data["TIMECARD"]["detail"])
                                    time.sleep(3)
                                    #Details data
                                    date_data_check = driver.find_element_by_xpath(data["TIMECARD"]["date_data_check"])
                                    Logging("Date: " + date_data_check.text)
                                    memo_data_check = driver.find_element_by_xpath(data["TIMECARD"]["memo_data_check"])
                                    Logging("Memo: " + memo_data_check.text)
                                    
                                    try:
                                        approver_data_check = driver.find_element_by_xpath(data["TIMECARD"]["route_add_event"])
                                        Logging ("Approver: " + approver_data_check.text)
                                        try:
                                            if approver_data_check.is_displayed:
                                                Logging("Approver is displayed")
                                                try:
                                                    if approver_data_check.text == approver_data:
                                                        Logging("Approver is saved successfully")
                                                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["pass"])
                                                except: 
                                                        Logging("Approver is saved failed")
                                                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["fail"])
                                            else:
                                                Logging("Approver is empty")
                                        except:
                                            Logging("Approver is empty")
                                    except:
                                        Logging ("Approver is empty")

                                    time_data_check = driver.find_element_by_xpath("//div[contains(@data-lang-id, 'tc_title_time')]/following-sibling::div")
                                    Logging("Duration: " + time_data_check.text)
                                    time_data_check_decimal = int(time_data_check.text.split(" ")[0].split("H")[0])

                                    try:
                                        if time_data_check.is_displayed:
                                            Logging("Duration is displayed")
                                            try:
                                                if time_data_check_decimal == filter_number_decimal:
                                                    Logging("Duration is saved successfully")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["pass"])
                                            except: 
                                                    Logging("Duration is saved failed")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["fail"])
                                        else:
                                            Logging("Duration is empty")
                                    except:
                                        Logging("Duration is empty")

                                    try:
                                        if date_data_check.is_displayed:
                                            Logging("Date is displayed")
                                            try:
                                                if date_data_check.text == str(date_data):
                                                    Logging("Data is saved successfully")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["pass"])
                                            except: 
                                                    Logging("Data is saved failed")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["fail"])
                                        else:
                                            Logging("Date is empty")
                                    except:
                                        Logging("Date is empty")
                                    
                                    try:
                                        if memo_data_check.is_displayed:
                                            Logging("Memo is displayed")
                                            try:
                                                if memo_data_check.text == memo_data:
                                                    Logging("Memo is saved successfully")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["pass"])
                                            except: 
                                                    Logging("Memo is saved failed")
                                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["fail"])
                                        else:
                                            Logging("Memo is empty")
                                    except:
                                        Logging("Memo is empty")

                                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                                    time.sleep(2)
                                else:
                                    Logging("- Cancel Pre OT fail")
                                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["click_cancel_pre_OT"]["pass"])
                    else:
                        Logging("Request is not displayed in approval list")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_displayed"]["fail"])
                except:
                    Logging("Request is not displayed in approval list")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_displayed"]["fail"])
            else:
                Logging("Can't apply pre-OT")
                TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_check"]["fail"])
        except:
            Logging("Pass")
    else: 
        Logging("Can't run pre OT function")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["check_true"]["fail"])


    Commands.ClickElement(data["TIMECARD"]["menu_report"])
    Waits.WaitElementLoaded(10, data["TIMECARD"]["report_wait"])
    time.sleep(2)   
    Commands.ClickElement(data["TIMECARD"]["report_weekly_page"])
    time.sleep(5)

    weekly_average = driver.find_element_by_xpath(data["TIMECARD"]["weekly_average"])
    weekly_average.location_once_scrolled_into_view
    time.sleep(2)

    text_working_time = output(data["TIMECARD"]["text_working_time"])
    #Logging(working_time.text)
    working_time_hour_decimal = int(text_working_time.split(" ")[0].split("H")[0])
    #Logging(working_time_hour_decimal)

    text_break_time = output(data["TIMECARD"]["text_break_time"])
    #Logging(break_time.text)
    break_time_hour_decimal = int(text_break_time.split(" ")[0].split("H")[0])
    #Logging(break_time_hour_decimal)

    text_OT_time = output(data["TIMECARD"]["text_OT_time"])
    #Logging(OT_time.text)
    OT_time_hour_decimal = int(text_OT_time.split(" ")[0].split("H")[0])
    #Logging(OT_time_hour_decimal)

    text_total_working_hour = output(data["TIMECARD"]["text_total_working_hour"])
    #Logging(total_working_hour.text)
    total_working_time_hour_decimal = int(text_total_working_hour.split(" ")[0].split("H")[0])
    #Logging(total_working_time_hour_decimal)

    #Clear clock-out
    Commands.ClickElement(data["TIMECARD"]["timesheet_page"])
    Waits.WaitElementLoaded(30, data["TIMECARD"]["timesheet_wait"])

    clockout_scroll = driver.find_element_by_xpath(data["TIMECARD"]["clockout_scroll"])
    clockout_scroll.location_once_scrolled_into_view
    time.sleep(2)

    clear_clock_out = Commands.ClickElement(data["TIMECARD"]["clockout_scroll"])
    clear_clock_out_yes = Commands.ClickElement(data["TIMECARD"]["clear_clock_out_yes"])
    time.sleep(5)


    # time.sleep(5)
    Commands.ClickElement(data["TIMECARD"]["report_page"])
    Waits.WaitElementLoaded(30, data["TIMECARD"]["report_wait"])
    time.sleep(2)   
    Commands.ClickElement(data["TIMECARD"]["report_weekly_page"])
    time.sleep(5)

    Logging(" ")
    weekly_average = driver.find_element_by_xpath(data["TIMECARD"]["weekly_average"])
    weekly_average.location_once_scrolled_into_view
    time.sleep(2)

    text_after_working_time = output(data["TIMECARD"]["text_working_time"])
    #Logging(after_working_time.text)
    after_working_time_hour_decimal = int(text_after_working_time.split(" ")[0].split("H")[0])
    #Logging(after_working_time_hour_decimal)

    text_after_break_time = output(data["TIMECARD"]["text_break_time"])
    #Logging(after_break_time.text)
    after_break_time_hour_decimal = int(text_after_break_time.split(" ")[0].split("H")[0])
    #Logging(after_break_time_hour_decimal)

    text_after_OT_time = output(data["TIMECARD"]["text_OT_time"])
    #Logging(after_OT_time.text)
    after_OT_time_hour_decimal = int(text_after_OT_time.split(" ")[0].split("H")[0])
    #Logging(after_OT_time_hour_decimal)

    text_after_total_working_hour = output(data["TIMECARD"]["text_total_working_hour"])
    #Logging(after_total_working_hour.text)
    after_total_working_time_hour_decimal = int(text_after_total_working_hour.split(" ")[0].split("H")[0])
    #Logging(after_total_working_time_hour_decimal)

    #Calculate to find out if data has been updated or not
    try:
        if working_time_hour_decimal != after_working_time_hour_decimal:
            Logging("Working time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_workingtime"]["pass"])
        else:
            Logging("Working time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_workingtime"]["fail"])

        if break_time_hour_decimal != after_break_time_hour_decimal:
            Logging("Break time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_breaktime"]["pass"])
        else:
            Logging("Break time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_breaktime"]["fail"])

        if OT_time_hour_decimal == after_OT_time_hour_decimal:
            Logging("OT time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_OTtime"]["pass"])
        else:
            Logging("OT time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_OTtime"]["fail"])

        if total_working_time_hour_decimal != after_total_working_time_hour_decimal:
            Logging("Total working time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_totaltime"]["pass"])
        else:
            Logging("Working time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_totaltime"]["fail"])
    except:
        Logging("Can't check data")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data"]["fail"])



    #Clock-out
    try:
        #pop up clock-in display
        pop_up = driver.find_element_by_xpath(data["TIMECARD"]["pop_up"])
        time.sleep(1)
        if pop_up.is_displayed():
            try:
                clock_out_but = driver.find_element_by_xpath(data["TIMECARD"]["clock_out_but"])
                clock_out_but.click()
                Logging("Clock-out")
                time.sleep(5)
                Commands.InputElement(data["TIMECARD"]["input_reason_leave_early"], data["TIMECARD"]["reason_leave_early"])
                Logging("- Input reason")
                time.sleep(2)
                Commands.ClickElement(data["TIMECARD"]["save"])
                Logging("- Save reason")
                time.sleep(3)
            except:
                Logging("Clock-out already")
                Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
                Logging("Select My timecard: Timesheets")
        else:
            Logging("Clock-out already")
            
    except:
        #pop up clock-in don't display
        pop_up_hid = driver.find_element_by_xpath(data["TIMECARD"]["pop_up_hid"])
        pop_up_hid.click()
        Logging("Click show pop up")
        time.sleep(5)
        try:
            Waits.WaitElementLoaded(10, data["TIMECARD"]["OT_popup"])
            Commands.ClickElement(data["TIMECARD"]["OT_clockout"])
            Logging("Clock-out")
            time.sleep(2)
            Commands.ClickElement(data["TIMECARD"]["yes_but"][0])
        except:
            pop_up = driver.find_element_by_xpath(data["TIMECARD"]["pop_up"])
            if pop_up.is_displayed():
                try:
                    clock_out_but = driver.find_element_by_xpath(data["TIMECARD"]["clock_out_but"])
                    clock_out_but.click()
                    Logging("Clock-out")
                    time.sleep(5)
                    Commands.InputElement(data["TIMECARD"]["input_reason_leave_early"], data["TIMECARD"]["reason_leave_early"])
                    Logging("- Input reason")
                    time.sleep(2)
                    Commands.ClickElement(data["TIMECARD"]["save"])
                    Logging("- Save reason")
                    time.sleep(3)
                except:
                    Logging("Clock-out already")
                    Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
                    Logging("Select My timecard: Timesheets")
            else:
                Logging("Clock-out already")

def Napproval_OT(output_clockin):
    if bool(output_clockin) == True:
        Logging("Run pre OT function")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["check_true"]["pass"])
        define_valid_time()
        
    else: 
        Logging("Can't run pre OT function")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["check_true"]["fail"])
    
def define_valid_time():
    text_format_hour = Functions.GetElementText(data["TIMECARD"]["text_format_hour"])
    clock_in_default_hour = text_format_hour.split(" ")[0]
    Logging(clock_in_default_hour)

    #Calculate to find out valid time 
    text_OT_since = Functions.GetElementText(data["TIMECARD"]["text_OT_since"])
    Logging("OT since: " + text_OT_since)
    OT_since_hour_decimal = int(text_OT_since.split(":")[0])
    OT_since_minute_decimal = int(text_OT_since.split(":")[1])

    OT_since_decimal = ((OT_since_minute_decimal) / 60) + (OT_since_hour_decimal)
    Logging("OT time after change to decimal: " + str(OT_since_decimal))

    work_shift = driver.find_element_by_xpath(data["TIMECARD"]["work_shift"])
    work_shift.location_once_scrolled_into_view
    Commands.ClickElement(data["TIMECARD"]["work_shift"])
    time.sleep(3)
    Commands.ClickElement(data["TIMECARD"]["work_shift_search"])
    time.sleep(3)
    wss_search2 =  Commands.InputElement(data["TIMECARD"]["ws_search"], "automationtest1")
    wss_search2.send_keys(Keys.ENTER)
    time.sleep(3)
    Commands.ClickElement(data["TIMECARD"]["click_first_choice"])
    Commands.ClickElement(data["TIMECARD"]["work_shift_search"])
    time.sleep(3)
    text_work_method_name = Functions.GetElementText(data["TIMECARD"]["text_work_method_name"])
    Logging("Work method name: " + text_work_method_name)
    x9 = text_work_method_name

    basic = driver.find_element_by_xpath(data["TIMECARD"]["basic"])
    basic.location_once_scrolled_into_view
    basic.click()
    Waits.WaitElementLoaded(10, data["TIMECARD"]["setting_wait"])
    time.sleep(2)
    Commands.ClickElement(data["TIMECARD"]["work_policy"])
    time.sleep(3)
    work_policy = driver.find_element_by_xpath(data["TIMECARD"]["work_policy"])
    Commands.ClickElement(data["TIMECARD"]["click_work_policy"] % x9)

    #Check OT data
    OT_data = driver.find_element_by_xpath(data["TIMECARD"]["OT_data"])
    OT_data.location_once_scrolled_into_view
    time.sleep(2)
    OT_data_time = driver.find_element_by_xpath(data["TIMECARD"]["OT_data_time"])
    OT_data_time_value = OT_data_time.get_attribute("value")
    #Logging("Total of OT time: " + OT_data_time_value)
    OT_data_time_hour = OT_data_time_value
    OT_data_time_decimal = int(OT_data_time_hour)
    Logging("Total of OT time: " + str(OT_data_time_decimal) + "hrs")

    #Print available application time
    Commands.ClickElement(data["TIMECARD"]["over_time_work"]).click()
    available_application_time = driver.find_element_by_xpath(data["TIMECARD"]["available_application_time"])
    available_application_time_value = available_application_time.get_attribute("value")
    #Logging(available_application_time_value)
    Logging("Available application time: " + available_application_time_value + " hours")
    available_application_time_hour = available_application_time_value
    available_application_time_decimal = int(available_application_time_hour)

    '''Calculate to find out valid time'''
    # Logging(OT_since_decimal)
    # Logging(available_application_time_decimal)
    result = OT_since_decimal - available_application_time_decimal
    #Logging("Valid time to apply pre-ot: " + result + "hr")
    Logging("Valid time to apply pre-ot(decimal): " + str(result))

    Logging("Current time: " + print_date)
    print_date_hour_decimal = int(print_date.split(":")[0])
    print_date_minute_decimal = int(print_date.split(":")[1])
    print_date_decimal = ((print_date_minute_decimal) / 60) + (print_date_hour_decimal)
    Logging("Current time after change to decimal: " + str(print_date_decimal))
    
    if int(print_date_decimal) < int(result):
        Logging("=> Able to apply pre-OT")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_check"]["pass"])
        driver.refresh()
        try:
            x = approval_setting()
        except:
            x = None

        if bool(x) == True:
            Logging("Apply OT")
            apply_OT(OT_data_time_decimal, x)
        else:
            Logging("Can't apply OT")
            pass

    else:
        Logging("Can't apply pre-OT")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_check"]["fail"])
        pass
    
    return OT_data_time_decimal
    

def approval_setting():
    Commands.ClickElement(data["TIMECARD"]["setting_approval"])
    # Logging("- Setting: Basic_Approval")
    time.sleep(3)
    OT = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["OT_scroll"])))
    OT.location_once_scrolled_into_view
    time.sleep(2)
    OT_list = Functions.GetListLength(data["TIMECARD"]["OT_list"])

    approval_OT_list = []
    i = 0
    for i in range(OT_list):
        i += 1
        approvalOT = driver.find_element_by_xpath(data["TIMECARD"]["approvalOT"] + "[" + str(i) + "]/label")
        approval_OT_list.append(approvalOT.text)
    
    Logging("Total of type Approval OT: " + str(len(approval_OT_list)))
    #Logging(approval_OT_list)

    x = random.choice(approval_OT_list)
    time.sleep(1)
    select_approval_OT = driver.find_element_by_xpath(data["TIMECARD"]["OT_list"] + "[contains(.,'" + str(x) + "')]")
    select_approval_OT.click()
    Logging("Select Approval OT type")
    time.sleep(2)
    Logging("Approval type: " + str(x))
    
    if str(x) == "Approval Line":
        try:
            approver = driver.find_element_by_xpath(data["TIMECARD"]["approver"])
            if approver.text == "No data was found.":
                Logging("- Don't have approval line")
                Commands.ClickElement(data["TIMECARD"]["add_approver"])
                Waits.WaitElementLoaded(10, data["TIMECARD"]["wait_OT"])
                time.sleep(2)
                approval_line = Commands.InputElement(data["TIMECARD"]["approval_line"], data["name_keyword"][1])
                approval_line.send_keys(Keys.ENTER)
                time.sleep(3)
                Commands.ClickElement(data["TIMECARD"]["select_user"])
                Commands.ClickElement(data["TIMECARD"]["plus_button"])
                Commands.ClickElement(data["TIMECARD"]["save_approver"])
                Logging("- Save approval line")
                approver_list = Waits.WaitElementLoaded(10,  data["TIMECARD"]["approver_list"] + data["name_keyword"][1] + "')]")
                if approver_list.is_displayed():
                    Logging("- Save approvers list Successfully")
                else:
                    Logging("- Save approvers list Fail")
            else:
                Logging("- Approval line has already")
        except:
            Logging()

    driver.refresh()
    return x

def apply_OT(x, OT_data_time_decimal, **details_data):
    # details_data = {}
    # try:
    Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
    Commands.ClickElement(data["TIMECARD"]["calendar"])
    Waits.WaitElementLoaded(10, data["TIMECARD"]["wait_calendar"])
    Commands.ClickElement(data["TIMECARD"]["add_event"])
    Commands.ClickElement(data["TIMECARD"]["add_OT"])
    time.sleep(5)
    #Check max application time
    text_max_application_time = Functions.GetElementText(data["TIMECARD"]["text_max_application_time"])
    # Logging(text_max_application_time)
    # Logging("Max application time: " + text_max_application_time)
    max_application_hour = text_max_application_time.split("H")[0]
    Logging("Max application time: " + max_application_hour)

    text_remaining_OT_time = Functions.GetElementText(data["TIMECARD"]["text_remaining_OT_time"])
    # Logging(text_remaining_OT_time)
    # Logging("Remaining OT time: " + text_remaining_OT_time)
    remaining_OT_number = text_remaining_OT_time.split("/")[0].split("H")[0]
    Logging("Remaining OT time: " + remaining_OT_number)

    #Calculation to check pre OT data
    # Logging(max_application_hour)
    # Logging(remaining_OT_number)
    # Logging(OT_data_time_decimal)
    if int(max_application_hour) + int(remaining_OT_number) == OT_data_time_decimal:
        Logging("Max application time is correct")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["pass"])
    else:
        Logging("Max application time is false")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["fail"])

    #Estimate working hours
    text_estimate_default = Functions.GetElementText(data["TIMECARD"]["text_estimate_default"])
    Logging("Estimate time before select filter: " + text_estimate_default)
    estimate_time_decimal = text_estimate_default.split("~")[1].split(":")[0]
    #Logging(estimate_time_decimal)


    Commands.ClickElement(data["TIMECARD"]["filter"])
    filters_OT_list = Functions.GetListLength(data["TIMECARD"]["filters_OT_list"])

    list_filters_OT = []
    y = 0
    for y in range(filters_OT_list):
        y += 1
        filters = driver.find_element_by_xpath(data["TIMECARD"]["filters"] % str(y))
        list_filters_OT.append(filters.text)

    m = random.choice(list_filters_OT)
    filter_time = driver.find_element_by_xpath(data["TIMECARD"]["filter_time"] % str(m))
    filter_time.click()
    Logging("Select filters time OT")
    time.sleep(3)

    filter_number = driver.find_element_by_xpath(data["TIMECARD"]["filter_number"])
    m1 = filter_number.text
    #Logging(m1)
    filter_number_decimal = int(m1.split(" ")[0])
    # details_data["filter_number_decimal"] = filter_number_decimal
    #Logging(filter_number_decimal)

    #Check max application time
    text_max_application_time = Functions.GetElementText(data["TIMECARD"]["text_max_application_time"])
    #Logging("Max application time: " + text_max_application_time)
    max_application_hour = text_max_application_time.split("H")[0]
    Logging("Max application time: " + max_application_hour)

    text_remaining_OT_time = Functions.GetElementText(data["TIMECARD"]["text_remaining_OT_time"])
    #Logging("Remaining OT time: " + text_remaining_OT_time)
    remaining_OT_number = text_remaining_OT_time.split("/")[0].split("H")[0]
    Logging("Remaining OT time: " + remaining_OT_number)

    #Calculation to check pre OT data
    # Logging(max_application_hour)
    # Logging(remaining_OT_number)
    # Logging(OT_data_time_decimal)
    if int(max_application_hour) + int(remaining_OT_number) == OT_data_time_decimal:
        Logging("Max application time is correct")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["pass"])
    else:
        Logging("Max application time is false")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["data_check_OT_max"]["fail"])

    #Estimate working hours
    text_estimate_default = Functions.GetElementText(data["TIMECARD"]["text_estimate_default"])
    Logging("Estimate time before select filter: " + text_estimate_default)
    estimate_time_decimal = int(text_estimate_default.split("~")[1].split(":")[0])
    #Logging(estimate_time_decimal)


    memo_approval_line = Commands.InputElement(data["TIMECARD"]["memo_approval_line"], "I would like to OT " + str(m) + " after work. Date: " + date)
    time.sleep(3)

    datas()

    Commands.ClickElement(data["TIMECARD"]["save_approval_line"])
    Logging("- Apply Pre OT")

    try:
        noty_success = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["pre_OT_noty"])))
        time.sleep(3)
        noty_list = [data["TIMECARD"]["pre_OT_noty_success"][0], data["TIMECARD"]["pre_OT_noty_success"][1]]
        if noty_success.text in noty_list:
            Logging("- Apply Pre OT Successfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["pass"])
            check_details_data(x) 
        elif noty_success.text == data["TIMECARD"]["pre_OT_noty_error"]:
            Logging("- Apply Pre OT has already")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["pass"])
            time.sleep(3)
            Commands.ClickElement(data["TIMECARD"]["exit_button"])
            time.sleep(2)
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["exit"]))).click()
    except:
        Logging("- Apply Pre OT Fail")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT"]["fail"])

    check_popup_OT(x, **details_data)   
    # except: 
    #     Logging("Can't run pre OT function")
    #     TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["check_true"]["fail"])

def datas():
    #Check details data
    try:  
        # date_data = driver.find_element_by_xpath(data["TIMECARD"]["date_data"])
        # date_data_value = date_data.get_attribute("value")
        date_data = Functions.GetInputValue(data["TIMECARD"]["date_data"])
        #Logging("Date: " + str(date_data_value))
    except:
        Logging(" ")
    
    try:
        #memo_data = driver.find_element_by_xpath(data["TIMECARD"]["memo_approval_line"]).text
        memo_data = Functions.GetElementText(data["TIMECARD"]["memo_approval_line"])
        #Logging("Memo: " + memo_data)
    except:
        Logging(" ")
    try:
        #approver_data = driver.find_element_by_xpath(data["TIMECARD"]["route_add_event"]).text
        approver_data = Functions.GetElementText(data["TIMECARD"]["route_add_event"])
        #Logging ("Approver: " + approver_data)
    except:
        Logging(" ")

    details_data = {
        "date_data": date_data,
        "memo_data": memo_data,
        "approver_data": approver_data, 
    }

    return details_data

def check_popup_OT(x, **details_data):
    try:
        Waits.WaitElementLoaded(10, data["TIMECARD"]["pop_up_OT"])
        Commands.ClickElement(data["TIMECARD"]["cancel_OT"])
        Commands.ClickElement(data["TIMECARD"]["cancel_OT_yes"])
        Logging("Close pop-up OT")
        check_details_data(x, **details_data)
    except:
        Logging("Pop-up was already closed")

    
    

def check_details_data(x, **details_data):
    time.sleep(5)
    Commands.ClickElement(data["TIMECARD"]["ap_proval_page"])
    Logging("- My Timecard: Approval")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, data["TIMECARD"]["approval_list"])))
    time.sleep(3)
    pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["pre_OT"])
    try:
        if pre_OT.text == "Over Time (Pre)":
            Logging("- Approval list: Pre OT")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["pre_OT_displayed"]["pass"])
            # #Scroll to detail
            # slider = driver.find_element_by_xpath("//div[@ref='eBodyHorizontalScrollViewport']")
            # horizontal_bar = driver.find_element_by_xpath("//div[@ref='eHorizontalRightSpacer']")
            # webdriver.ActionChains(driver).click_and_hold(slider).move_to_element(horizontal_bar).perform()
            # webdriver.ActionChains(driver).release().perform()
            time.sleep(5)
            Commands.ClickElement(data["TIMECARD"]["approval_detail"])
            Logging("- View detail approval")
            if str(x) == "Automatic approval":
                status_pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["status_pre_OT"])
                if status_pre_OT.text == "Approved":
                    Logging("- Pre OT has been approved automatically")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT_auto"]["pass"])
                    detail_data(details_data)
                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                    time.sleep(2)
                else:
                    Logging("- Pre OT hasn't been approved automatically")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT_auto"]["fail"])
                    Logging("=> Fail")
                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                    time.sleep(2)
            else:
                Logging("Not auto approval")
                status_pre_OT = driver.find_element_by_xpath(data["TIMECARD"]["status_pre_OT"])
                time.sleep(2)
                if status_pre_OT.text == "Approved":
                    Logging("- Pre OT has been Approved")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approve_pre_OT"]["pass"])
                    detail_data(**details_data)
                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                    time.sleep(2)
                elif status_pre_OT == "Cancelled":
                    Logging("- Pre OT has been Cancelled")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["cancel_pre_OT"]["pass"])
                    detail_data(**details_data)
                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                    time.sleep(2)
                
                elif status_pre_OT == "Pending":
                    Logging("- Pre OT is pending")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["progress_pre_OT"]["pass"])
                    detail_data(**details_data)
                    Commands.ClickElement(data["TIMECARD"]["turn_off_view"])
                    time.sleep(2)
                # else:
                #     status_pre_OT.click()
                #     Logging("- Cancel Pre OT")
                #     time.sleep(2)
                #     Commands.ClickElement(data["TIMECARD"]["yes_but"][1])
                #     time.sleep(5)
                #     Commands.ClickElement(data["TIMECARD"]["reload"])
                #     status_update = Waits.WaitElementLoaded(10, data["TIMECARD"]["status_update"])
                #     time.sleep(5)
                #     if status_update.text == "Cancelled":
                #         Logging("- Cancel Pre OT successfully")
                #         TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["click_cancel_pre_OT"]["pass"])
                #     else:
                #         Logging("- Cancel Pre OT fail")
                #         TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["click_cancel_pre_OT"]["pass"])
    except:
        Logging(" ")   

def detail_data(**details_data):
    filter_number_decimal = details_data["filter_number_decimal"]
    date_data = details_data["date_data"]
    memo_data = details_data["memo_data"]
    approver_data = details_data["approver_data"]

    Logging(filter_number_decimal)
    Logging(date_data)
    Logging(memo_data)
    Logging(approver_data)
    #Details data
    date_data_check = driver.find_element_by_xpath(data["TIMECARD"]["date_data_check"])
    Logging("Date: " + date_data_check.text)
    memo_data_check = driver.find_element_by_xpath(data["TIMECARD"]["memo_data_check"])
    Logging("Memo: " + memo_data_check)
    time_data_check = driver.find_element_by_xpath(data["TIMECARD"]["time_data_check"])
    Logging("Duration: " + time_data_check)
    time_data_check_decimal = int(time_data_check.text.split(" ")[0].split("H")[0])

    try:
        if time_data_check.is_displayed:
            Logging("Duration is displayed")
            try:
                if time_data_check_decimal == filter_number_decimal:
                    Logging("Duration is saved successfully")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["pass"])
            except: 
                    Logging("Duration is saved failed")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_duration"]["fail"])
        else:
            Logging("Duration is empty")
    except:
        Logging("Duration is empty")

    try:
        if date_data_check.is_displayed:
            Logging("Date is displayed")
            try:
                if date_data_check.text == str(date_data):
                    Logging("Data is saved successfully")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["pass"])
            except: 
                    Logging("Data is saved failed")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_data"]["fail"])
        else:
            Logging("Date is empty")
    except:
        Logging("Date is empty")

    try:
        if memo_data_check.is_displayed:
            Logging("Memo is displayed")
            try:
                if memo_data_check.text == memo_data.text:
                    Logging("Memo is saved successfully")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["pass"])
            except: 
                    Logging("Memo is saved failed")
                    TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_memo"]["fail"])
        else:
            Logging("Memo is empty")
    except:
        Logging("Memo is empty")

    try:
        approver_data_check = driver.find_element_by_xpath(data["TIMECARD"]["route_add_event"])
        Logging ("Approver: " + approver_data_check.text)
        try:
            if approver_data_check.is_displayed:
                Logging("Approver is displayed")
                try:
                    if approver_data_check.text == approver_data:
                        Logging("Approver is saved successfully")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["pass"])
                except: 
                        Logging("Approver is saved failed")
                        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["approval_details_approver"]["fail"])
            else:
                Logging("Approver is empty")
        except:
            Logging("Approver is empty")
    except:
        Logging ("Approver is empty")

    









def report_weekly_before():
    Commands.ClickElement(data["TIMECARD"]["report_page"])
    Waits.WaitElementLoaded(30, data["TIMECARD"]["report_wait"])
    time.sleep(2)   
    Commands.ClickElement(data["TIMECARD"]["report_weekly_page"])
    time.sleep(5)

    weekly_average = driver.find_element_by_xpath(data["TIMECARD"]["weekly_average"])
    weekly_average.location_once_scrolled_into_view
    time.sleep(2)

    text_working_time = driver.find_element_by_xpath(data["TIMECARD"]["text_working_time"])
    #Logging(working_time.text)
    working_time_hour_decimal = int(text_working_time.split(" ")[0].split("H")[0])
    #Logging(working_time_hour_decimal)

    text_break_time = output(data["TIMECARD"]["text_break_time"])
    #Logging(break_time.text)
    break_time_hour_decimal = int(text_break_time.split(" ")[0].split("H")[0])
    #Logging(break_time_hour_decimal)

    text_OT_time = driver.find_element_by_xpath(data["TIMECARD"]["text_OT_time"])
    #Logging(OT_time.text)
    OT_time_hour_decimal = int(text_OT_time.split(" ")[0].split("H")[0])
    #Logging(OT_time_hour_decimal)

    text_total_working_hour = driver.find_element_by_xpath(data["TIMECARD"]["text_total_working_hour"])
    #Logging(total_working_hour.text)
    total_working_time_hour_decimal = int(text_total_working_hour.split(" ")[0].split("H")[0])
    #Logging(total_working_time_hour_decimal)

    #Clear clock-out
    Commands.ClickElement(data["TIMECARD"]["timesheet_page"])
    Waits.WaitElementLoaded(30, data["TIMECARD"]["timesheet_wait"])

    clockout_scroll = driver.find_element_by_xpath(data["TIMECARD"]["clockout_scroll"])
    clockout_scroll.location_once_scrolled_into_view
    time.sleep(2)

    clear_clock_out = Commands.ClickElement(data["TIMECARD"]["clockout_scroll"])
    clear_clock_out_yes = Commands.ClickElement(data["TIMECARD"]["confirm_yes"])
    time.sleep(5)

    work1 = working_time_hour_decimal
    break1 = break_time_hour_decimal
    OT1 = OT_time_hour_decimal
    total1 = total_working_time_hour_decimal

    elements = {
        "work" : work1,
        "break" : break1,
        "OT" : OT1,
        "total" : total1
    }

    return elements
    
def report_weekly_after(elements):
    workingtime = elements["work"]
    breaktime = elements["break"]
    OTtime = elements["OT"]
    totalworkingtime = elements["total"]

    # time.sleep(5)
    Commands.ClickElement(data["TIMECARD"]["report_page"])
    Waits.WaitElementLoaded(30, data["TIMECARD"]["report_wait"])
    time.sleep(2)   
    Commands.ClickElement(data["TIMECARD"]["report_weekly_page"])
    time.sleep(5)

    Logging(" ")
    weekly_average = driver.find_element_by_xpath(data["TIMECARD"]["weekly_average"])
    weekly_average.location_once_scrolled_into_view
    time.sleep(2)

    text_after_working_time = driver.find_element_by_xpath(data["TIMECARD"]["text_working_time"])
    #Logging(after_working_time.text)
    after_working_time_hour_decimal = int(text_after_working_time.split(" ")[0].split("H")[0])
    #Logging(after_working_time_hour_decimal)

    text_after_break_time = driver.find_element_by_xpath(data["TIMECARD"]["text_break_time"])
    #Logging(after_break_time.text)
    after_break_time_hour_decimal = int(text_after_break_time.split(" ")[0].split("H")[0])
    #Logging(after_break_time_hour_decimal)

    text_after_OT_time = driver.find_element_by_xpath(data["TIMECARD"]["text_OT_time"])
    #Logging(after_OT_time.text)
    after_OT_time_hour_decimal = int(text_after_OT_time.split(" ")[0].split("H")[0])
    #Logging(after_OT_time_hour_decimal)

    text_after_total_working_hour = driver.find_element_by_xpath(data["TIMECARD"]["text_total_working_hour"])
    #Logging(after_total_working_hour.text)
    after_total_working_time_hour_decimal = int(text_after_total_working_hour.split(" ")[0].split("H")[0])
    #Logging(after_total_working_time_hour_decimal)

    #Calculate to find out if data has been updated or not
    try:
        if workingtime != after_working_time_hour_decimal:
            Logging("Working time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_workingtime"]["pass"])
        else:
            Logging("Working time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_workingtime"]["fail"])

        if breaktime != after_break_time_hour_decimal:
            Logging("Break time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_breaktime"]["pass"])
        else:
            Logging("Break time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_breaktime"]["fail"])

        if OTtime == after_OT_time_hour_decimal:
            Logging("OT time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_OTtime"]["pass"])
        else:
            Logging("OT time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_OTtime"]["fail"])

        if totalworkingtime != after_total_working_time_hour_decimal:
            Logging("Total working time is updated succesfully")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_totaltime"]["pass"])
        else:
            Logging("Working time is updated failed")
            TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data_totaltime"]["fail"])
    except:
        Logging("Can't check data")
        TesCase_LogResult(**data["testcase_result"]["HR-Timecard"]["report_weekly_check_data"]["fail"])



    #Clock-out
    try:
        #pop up clock-in display
        pop_up = driver.find_element_by_xpath(data["TIMECARD"]["pop_up"])
        time.sleep(1)
        if pop_up.is_displayed():
            try:
                clock_out_but = driver.find_element_by_xpath(data["TIMECARD"]["clock_out_but"])
                clock_out_but.click()
                Logging("Clock-out")
                time.sleep(5)
                Commands.InputElement(data["TIMECARD"]["input_reason_leave_early"], data["TIMECARD"]["reason_leave_early"])
                Logging("- Input reason")
                time.sleep(2)
                Commands.ClickElement(data["TIMECARD"]["save"])
                Logging("- Save reason")
                time.sleep(3)
            except:
                Logging("Clock-out already")
                Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
                Logging("Select My timecard: Timesheets")
        else:
            Logging("Clock-out already")
            
    except:
        #pop up clock-in don't display
        pop_up_hid = driver.find_element_by_xpath(data["TIMECARD"]["pop_up_hid"])
        pop_up_hid.click()
        #Logging("Click show pop up")
        time.sleep(5)
        try:
            Waits.WaitElementLoaded(10, data["TIMECARD"]["OT_popup"])
            Commands.ClickElement(data["TIMECARD"]["OT_clockout"])
            Logging("Clock-out")
            time.sleep(2)
            Commands.ClickElement(data["TIMECARD"]["yes_but"][0])
        except:
            pop_up = driver.find_element_by_xpath(data["TIMECARD"]["pop_up"])
            if pop_up.is_displayed():
                try:
                    clock_out_but = driver.find_element_by_xpath(data["TIMECARD"]["clock_out_but"])
                    clock_out_but.click()
                    Logging("Clock-out")
                    time.sleep(5)
                    Commands.InputElement(data["TIMECARD"]["input_reason_leave_early"], data["TIMECARD"]["reason_leave_early"])
                    Logging("- Input reason")
                    time.sleep(2)
                    Commands.ClickElement(data["TIMECARD"]["save"])
                    Logging("- Save reason")
                    time.sleep(3)
                except:
                    Logging("Clock-out already")
                    Commands.ClickElement(data["TIMECARD"]["my_timesheets"])
                    Logging("Select My timecard: Timesheets")
            else:
                Logging("Clock-out already")

def timecard_OT():
    output_clockin = clock_in()
    #Napproval_OT(time_clock_in)
    #print(time_clock_in)
    #OT_data_time_decimal = define_valid_time()
    Napproval_OT(output_clockin)#, OT_data_time_decimal)
    details_data = datas()
    filter_number_decimal = apply_OT(**details_data)
    x = approval_setting(**details_data)
    #OT_data_time_decimal = define_valid_time()
    #Napproval_OT()

#def timecard_report():
    # elements = report_weekly_before()
    # report_weekly_after(elements)


