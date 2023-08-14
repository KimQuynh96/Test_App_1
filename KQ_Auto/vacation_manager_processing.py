from lib2to3.pgen2.token import RPAR
from msilib.schema import ComboBox
from vacation_login import driver
from vacation_functions import commons,data,datetime,time,Keys
from vacation_param import pr_ap,Pass,Fail,xpath,pr_mn,Des

def InfoRequestInVacationApprove(j,Approval_Type):
    if  Approval_Type  == "approve":
        icon_approval  =  commons.IsDisplayedByXpath(pr_ap.vc_ap["ic_approve"] % str(j))
    elif Approval_Type == "cancel_approve":
        icon_approval  =  commons.IsDisplayedByXpath(pr_ap.vc_ap["ic_cancel_approve"] % str(j))
    else:
        icon_approval  =  commons.IsDisplayedByXpath(pr_ap.vc_ap["ic_reject"] % str(j))

    if  icon_approval  == True :
        InforRequest   =  xpath.MnInforRequest(j)
        return InforRequest 
    else :
        return False

def CountAllVacationRequest():
    # Count all vacation from all page #
    time.sleep(3)
    i             = 1
    Total_Request = 0
    if commons.IsDisplayedByXpath(pr_ap.vc_ap["check_list"]) == False :
        driver.find_element_by_xpath(pr_ap.vc_ap["end_page"]).click()
        End_Page_Text = driver.find_element_by_xpath(pr_ap.vc_ap["page_current"]).text
        End_Page      = int(End_Page_Text)
        driver.find_element_by_xpath(pr_ap.vc_ap["to_first_page"]).click()
        while  i <= End_Page:
            if i == End_Page :
                driver.find_element_by_xpath(pr_ap.vc_ap["end_page"]).click()
                time.sleep(3)
                List_Request  = driver.find_elements_by_xpath(pr_ap.vc_ap["list_cancel"])
                Total         = commons.TotalData(List_Request)
                Total_Request = Total_Request + Total
            else:
                Total_Request = Total_Request + 20
            i = i + 1
    return Total_Request

def FindStatusOfVacation(Total_Request,Approval_Type,Icon,Button,Status_Name,Msg1,Msg2):
    j                       = 0
    Result_Approve          = False
    Icon_Approve            = False
    Request_Use_To_Approval = False

    while j <= Total_Request :
        time.sleep(1)
        if j == 0 :
            status_name = commons.GetText(pr_ap.vc_ap["ap_status"])
        else :
            status_name = commons.GetTextWithI(pr_ap.vc_ap["on_status"],j)

        # Find request has status is request  #
        if  status_name == Status_Name :
            Request_Use_To_Approval = InfoRequestInVacationApprove(j,Approval_Type)
            if  Request_Use_To_Approval != False :
                Icon_Approve = True
                if j == 0 :
                    driver.find_element_by_xpath(pr_ap.vc_ap[Icon] % str(0)).click()
                else :
                    driver.find_element_by_xpath(pr_ap.vc_ap[Icon] % str(j)).click()
                
                # If have permission approve for this request => Click on approve icon to approve #
                if commons.IsDisplayedByXpath(pr_ap.vc_ap[Button]) == True :
                    commons.CasePass(Msg1[Pass][Des])
                    driver.find_element_by_xpath(pr_ap.vc_ap[Button]).click()
                    time.sleep(6)
                    if commons.IsDisplayedByXpath(pr_ap.vc_ap["bt_close"]) == True :
                        commons.WriteOnExcel(Msg2[Fail])
                    else:
                        commons.WriteOnExcel(Msg2[Pass])
                        Result_Approve = True
                    break
                else :
                    commons.WriteOnExcel(Msg1[Fail])
                break  
        j = j + 1
    if  Approval_Type == "approve" :
        ParCheckResultApprove = xpath.ParCheckResultApprove(Icon_Approve,Result_Approve,Request_Use_To_Approval,Total_Request,Approval_Type)
    else :
        ParCheckResultApprove = xpath.ParCheckResultReject(Icon_Approve,Result_Approve,Request_Use_To_Approval,Total_Request,Approval_Type)
    return ParCheckResultApprove

def CheckResult(Icon_Approve,Result_Approve,Request_Use_To_Approval,Total_Request,Approval_Type,Msg1,Msg2):
    if  Result_Approve == True :
        m = 0
        driver.find_element_by_xpath(pr_ap.vc_ap["bt_refresh"]).click()
        Total = Total_Request -1

        if  Approval_Type == "approve" :
            while m <= Total:
                re_af_ap = xpath.MnInforRequest(m)
                check_request_approved = xpath.ComparePequest(re_af_ap,Request_Use_To_Approval)
                if check_request_approved == True:
                    status_after_approved = driver.find_element_by_xpath(pr_ap.vc_ap["status"] % str(m)).text
                    if status_after_approved == "Approved" :
                        commons.WriteOnExcel(Msg1[Pass])
                        break
                    else :
                        commons.WriteOnExcel(Msg1[Fail])
                m = m + 1

        else :
            find_request = False
            while m <= Total:
                re_af_ap = xpath.MnInforRequest(m)
                check_request_reject    = xpath.ComparePequest(re_af_ap,Request_Use_To_Approval)
                if check_request_reject == True :
                    find_request        =  True
                    break
                m = m + 1
            if  find_request == False :
                commons.WriteOnExcel(Msg1[Pass])
            else :
                commons.WriteOnExcel(Msg1[Fail])


    if  Icon_Approve == False:
        commons.WriteOnExcel(Msg2[Pass])

    time.sleep(5)
    driver.find_element_by_xpath(pr_ap.vc_ap["bt_refresh"]).click()

def ApproveForRequest(Total_Request):
    try :
        commons.Title("Approve Request")
        if  Total_Request == 0 :
            commons.WriteOnExcel(pr_ap.NoVcToApproval[Pass])
        else:
            ParFindVacationApprove = xpath.ParFindVacationApprove()
            commons.AddTotal(ParFindVacationApprove,Total_Request)
            ParCheckResultApprove         = FindStatusOfVacation(**ParFindVacationApprove)
            CheckResult(**ParCheckResultApprove)
    except:
        commons.ClickElementWithText("Vacation Approve")

def RejectForRequest(Total_Request):
    try :
        time.sleep(10)
        commons.Title("Reject Request")
        if  Total_Request == 0 :
            commons.WriteOnExcel(pr_ap.NoVacationToReject[Pass])
        else:
            ParFindVacationReject = xpath.ParFindVacationReject()
            commons.AddTotal(ParFindVacationReject,Total_Request)
            ParCheckResultReject         = FindStatusOfVacation(**ParFindVacationReject)
            CheckResult(**ParCheckResultReject)
    except:
        commons.ClickElementWithText("Vacation Approve")

def CancelApproveForRequest(Total_Request):
    try :
        time.sleep(10)
        commons.Title("Cancel Approve")
        if  Total_Request == 0 :
            commons.WriteOnExcel(pr_ap.NoVacationToCancelApprove[Pass])
        else:
            ParFindVacationCancelApprove = xpath.ParFindVacationCancelApprove()
            commons.AddTotal(ParFindVacationCancelApprove,Total_Request)
            ParCheckResultCancelApprove         = FindStatusOfVacation(**ParFindVacationCancelApprove)
            CheckResult(**ParCheckResultCancelApprove)
    except:
        commons.ClickElementWithText("Vacation Approve")

def DeleteVacation(Total_Request):
    try :
        commons.Title("Delete Vacation")
        m             = 0
        Result_Delete = False
        Find_Delete   = False

        if Total_Request == 0 :
            commons.WriteOnExcel(pr_ap.NoVacationToDelete[Pass])

        else:
            Total_Before = CountAllVacationRequest()
            time.sleep(3)
            while m <= Total_Request: 
                i = m + 1
                # Find request has status is Rejected or Canceled #
                status = commons.GetTextWithI(pr_ap.vc_ap["mc_status"],i)
                status = commons.ReplaceSpace(status)
                if status == "Rejected" or  status== "Cancelled":

                    # Determine if this request has completed the cancellation process #
                    if commons.IsDisplayedByXpath(pr_ap.vc_ap["ic_delete"] % str(m)) == True :
                        Find_Delete = True
                    # If find request can delete => Delete request #
                    if  Find_Delete == True:
                        driver.find_element_by_xpath(pr_ap.vc_ap["ic_delete"] % str(m)).click()
                        if  commons.IsDisplayedByXpath(pr_ap.vc_ap["bt_close"]) == True :
                            commons.CasePass(pr_ap.ClickOnDeleteIcon[Pass][Des])
                            driver.find_element_by_xpath(pr_ap.vc_ap["bt_delete"]).click()
                            if  commons.IsDisplayedByXpath(pr_ap.vc_ap["bt_close"]) == True : 
                                commons.WriteOnExcel(pr_ap.DeleteVacation[Fail])
                            else:
                                commons.WriteOnExcel(pr_ap.DeleteVacation[Pass])
                                Result_Delete = True
                            break
                        else :
                            commons.WriteOnExcel(pr_ap.ClickOnDeleteIcon[Fail])
                            break
                m = m + 1   

            # Check deleted request removed from the request list #
            driver.find_element_by_xpath(pr_ap.vc_ap["refresh"]).click()
            time.sleep(2)
            if  Result_Delete == True:
                Total_After   = CountAllVacationRequest()
                if  Total_After + 1 == Total_Before :
                    commons.WriteOnExcel(pr_ap.VacationRemoved[Pass])
                else:
                    commons.WriteOnExcel(pr_ap.VacationRemoved[Fail])
            if Find_Delete == False :
                commons.WriteOnExcel(pr_ap.NoVacationToDelete[Pass])
    except:
        commons.ClickLinkText("Vacation Approve")


def SelectUserFromDepart():
    #Select user from org 
    time.sleep(3)
    List_Depart  = driver.find_elements_by_xpath(pr_mn.mn_pro["list_depart"])
    Total_Depart = commons.TotalData(List_Depart) + 1
    for i in range(1 , Total_Depart):
        time.sleep(1)
        Depart_Has_User = commons.IsDisplayedByXpath(pr_mn.mn_pro["depart_name"] % str(i)) 
        if  Depart_Has_User == True :
            driver.find_element_by_xpath(pr_mn.mn_pro["depart_name"] % str(i)).click()
            time.sleep(1)
            List_User  = driver.find_elements_by_xpath(pr_mn.mn_pro["list_user"])
            Total_user = commons.TotalData(List_User) + 1
            for i in range(1 , Total_user):
                Is_User = commons.IsDisplayedByXpath(pr_mn.mn_pro["sl_user"] % str(i)) 
                if  Is_User == True:
                    user_name = driver.find_element_by_xpath(pr_mn.mn_pro["sl_user"] % str(i))
                    user_name.click()
                    return True  
    return False 

def GetColumnData():
    Colum_Total = driver.find_element_by_xpath(pr_mn.mn_pro["ip_hour_adjust"])
    Total_Days  = int(Colum_Total.get_attribute('value'))

    Remain = commons.GetText(pr_mn.mn_pro["remain_adjust"])
    if  Remain.rfind("D") >0 :
        Remain  = int(Remain[None: int(Remain.rfind("D"))])
    else:
        Remain  = 0
    
    Hour_Used   = commons.GetText(pr_mn.mn_pro["used_adjust"])
    if  Hour_Used.rfind("D") >0 :
        Hour_Used  = int(Hour_Used[None: int(Hour_Used.rfind("D"))])
    else:
        Hour_Used  = 0
    
    return Total_Days , Remain , Hour_Used

def Adjust():
    # Choose user from Org 
    Choose_User = SelectUserFromDepart()

    # Check have vacation to adjust 
    Select_Vc    = False 
    Check_Adjust = False
    increase     = False
    if Choose_User == True :
        Vacation_Name = commons.GetText(pr_mn.mn_pro["vc_name_adjust"])
        if  Vacation_Name != "-":
            Select_Vc = True
            
        if  Select_Vc == True :
            
            Total_Days , Remain , Hour_Used = GetColumnData()

            Colum_Total = driver.find_element_by_xpath(pr_mn.mn_pro["ip_hour_adjust"])
            Colum_Total.clear()

            if  Remain == 0 or Remain == Total_Days :
                # adjusted holiday increase 
                increase = True
                Colum_Total.send_keys(Total_Days + 1)
            else :
                # adjusted holiday reduced
                Colum_Total.send_keys(Total_Days - 1)

            driver.find_element_by_xpath(pr_mn.mn_pro["bt_adjust"]).click()
            if  commons.IsDisplayedByXpath(pr_mn.mn_pro["adjust"]) == True :
                commons.CasePass(pr_mn.ClickOnButtonAdjust[Pass][Des])
                driver.find_element_by_xpath(pr_mn.mn_pro["adjust"]).click()
                if  commons.IsDisplayedByXpath(pr_mn.mn_pro["bt_close"]) == True :
                    commons.WriteOnExcel(pr_mn.AdjustVacation[Fail])
                else :
                    Check_Adjust = True
                    commons.WriteOnExcel(pr_mn.AdjustVacation[Pass])
            else :
                commons.WriteOnExcel(pr_mn.ClickOnButtonAdjust[Fail])

    if  Check_Adjust == True :
        commons.ClickLinkText("Request Vacation")
        commons.ClickLinkText("Vacation Adjust")
        driver.find_element_by_xpath(pr_mn.mn_pro["ra_adjust"]).click()
        Choose_User = SelectUserFromDepart()
        if  Choose_User == True :
            Vacation = commons.GetText(pr_mn.mn_pro["vc_name_adjust"])
            if Vacation == Vacation_Name :
                Total_Days_One , Remain_One , Hour_Used_One = GetColumnData()
                if  increase == True :
                    if  Total_Days_One == Total_Days + 1 and \
                        Remain_One     == Remain     + 1 and \
                        Hour_Used_One  == Hour_Used          :
                        commons.WriteOnExcel(pr_mn.NumberAdjust[Pass])
                    else :     
                        commons.WriteOnExcel(pr_mn.NumberAdjust[Fail])
                else :
                    if  Total_Days_One == Total_Days - 1 and \
                        Remain_One     == Remain     - 1 and \
                        Hour_Used_One  == Hour_Used          :
                        commons.WriteOnExcel(pr_mn.NumberAdjust[Pass])
                        commons.WriteOnExcel(pr_mn.NumberAdjust[Fail])
    else :
        commons.WriteOnExcel(pr_mn.NoVacationToAdjust[Pass])

def Grant():
    # Choose user from Org 
    Choose_User = SelectUserFromDepart()
    driver.find_element_by_css_selector(pr_mn.mn_pro["select_vc"]).click()
    time.sleep(2)
    if Choose_User == True :
        Vacation_Name = driver.find_element_by_xpath(pr_mn.mn_pro["choose_vc"])
        if Vacation_Name.text == "No options" :
            commons.WriteOnExcel(pr_mn.NoVcToGrant[Pass])

        else:
            Vacation_Name.click()
             
            # Enter days to grant #
            time.sleep(1)
            Days = driver.find_element_by_xpath(pr_mn.mn_pro["ip_day"])
            Days.clear()
            Days.send_keys(5)
            Days.send_keys(Keys.RETURN)
        
            if  int(Days.get_attribute('value')) == 5 :
                commons.CasePass(pr_mn.InputDays[Pass][Des])
                driver.find_element_by_xpath(pr_mn.mn_pro["bt_grant"]).click()
                if commons.IsDisplayedByXpath(pr_mn.mn_pro["grant"]) == True :
                    commons.CasePass(pr_mn.ClickOnButtonGrant[Pass][Des])
                    driver.find_element_by_xpath(pr_mn.mn_pro["grant"]).click()
                    if  commons.IsDisplayedByXpath(pr_mn.mn_pro["bt_close"]) == True :
                        commons.WriteOnExcel(pr_mn.GrantVacation[Fail])
                    else :
                        commons.WriteOnExcel(pr_mn.GrantVacation[Pass])
                else :
                    commons.WriteOnExcel(pr_mn.ClickOnButtonGrant[Fail])
            
            else:
                commons.WriteOnExcel(pr_mn.InputDays[Fail])
   
           
def VacationAdjust():
    if  commons.IsDisplayedByTextLink("Vacation Adjust") == True :
        commons.ClickLinkText("Vacation Adjust")
        if  commons.IsDisplayedByXpath(pr_mn.mn_pro["radio_adjust"]) == True:
            commons.WriteOnExcel(pr_mn.AccessSubmenuAdjust[Pass])
            driver.find_element_by_xpath(pr_mn.mn_pro["ra_adjust"]).click()
            if  commons.IsDisplayedByXpath(pr_mn.mn_pro["bt_adjust"]) == True :
                commons.CasePass(pr_mn.ClickRadioAdjust[Pass][Des])
                Adjust()
            else :
                commons.WriteOnExcel(pr_mn.ClickRadioAdjust[Fail])
            driver.find_element_by_xpath(pr_mn.mn_pro["ra_grant"]).click()
            if  commons.IsDisplayedByXpath(pr_mn.mn_pro["bt_grant"]) == True :
                commons.CasePass(pr_mn.ClickRadioGrant[Pass][Des])
                Grant()
            else :
                commons.WriteOnExcel(pr_mn.ClickRadioGrant[Fail])


        else :
            commons.WriteOnExcel(pr_mn.AccessSubmenuAdjust[Fail])
    else :
        commons.WriteOnExcel(pr_mn.NoSubMenuAdjust[Pass])

def VacationApprove():
    if  commons.IsDisplayedByTextLink("Vacation Approve") == True :
        commons.ClickLinkText("Vacation Approve")
        if  commons.IsDisplayedByXpath(pr_ap.vc_ap["sub_cancel_request"]) :
            commons.WriteOnExcel(pr_ap.AccessSubmenuAp[Pass])
            time.sleep(5)  
            
            List_Request  = driver.find_elements_by_xpath(pr_ap.vc_ap["list_request"])
            Total_Request = commons.TotalData(List_Request)
            if Total_Request == 1 :
                if  commons.IsDisplayedByXpath(pr_ap.vc_ap["check_list"]) == True :
                    Total_Request = 0

            ApproveForRequest(Total_Request)
            RejectForRequest(Total_Request)
            CancelApproveForRequest(Total_Request)

            commons.ClickElementWithXpath(pr_ap.vc_ap["sub_cancel_request"])
            if commons.IsDisplayedByXpath(pr_ap.vc_ap["all_status"]) == True :
                List_Request  = driver.find_elements_by_xpath(pr_ap.vc_ap["list_request"])
                Total_Request = commons.TotalData(List_Request)
                DeleteVacation(Total_Request)
        else :
            commons.WriteOnExcel(pr_ap.AccessSubmenuAp[Fail])
    else :
        commons.WriteOnExcel(pr_ap.NoSubMenuApprove[Pass])


def ManagerProcessing():
    try :
        VacationApprove()
    except:
        commons.Content("Error Code")
    try :
        VacationAdjust()
    except:
        commons.Content("Error Code")
   
    

        

