from ast import Str
import  json,os,re
from pathlib import Path
from sys import platform
from vacation_set_up import driver,datetime

json_file = os.path.dirname(Path(__file__).absolute())+"\\vacation_data.json"
if platform == "linux" or platform == "linux2": 
    json_file =  json_file.replace("\\","/") 
with open(json_file) as json_file:
    data = json.load(json_file)

Pass   = "pass"
Fail   = "fail"
All    = "all"
Con    = "vc_con"
Am     = "am"
Pm     = "pm"
Hour   = "hour"
Des    = "description"

class pr_log():
    # login #
    menu      = data["testcase_result"]["admin"]["menu"]
    no_menu   = data["testcase_result"]["admin"]["no_menu"]
    ResultLog = data["testcase_result"]["log"]["login"]
    id        = data["login_msg"]["input_id"]
    pa        = data["login_msg"]["input_pass"]
    log       = data["login_msg"]["login"]
    
class pr_rq():
    rq_vc            = data["rq_vc"]
    msg              = data['re_msg']
    AccessSubmenuMy  = data["testcase_result"]["my_vc"]["submenu_my"]
    AccessTabInfor   = data["testcase_result"]["my_vc"]["tab_infor_my"]
    AccessTabStatus  = data["testcase_result"]["my_vc"]["tab_request_my"]
    AccessTabHistory = data["testcase_result"]["my_vc"]["tab_history_my"]
    AccessTabSchedule= data["testcase_result"]["my_vc"]["submenu_schedule"]
    AccessTabDepartment= data["testcase_result"]["my_vc"]["submenu_depart_vc"]
    AccessSubmenuCc    = data["testcase_result"]["my_vc"]["submenu_view"]
    AccessSubmenuSettlement      = data["testcase_result"]["my_vc"]["submenu_re_settle"]
    AccessTabSettlementHistory   = data["testcase_result"]["my_vc"]["tab_re_settlement"]
    AccessTabSettlementRequest   = data["testcase_result"]["my_vc"]["tab_hs_settlement"]
    AccessNoSubmenuSettlement    = data["testcase_result"]["my_vc"]["no_submenu_re_settle"]
    SelectApprover     = data["testcase_result"]["my_vc"]["re_select_approver"]
    AddApprover        = data["testcase_result"]["my_vc"]["re_add_approver"]
    SaveApprover       = data["testcase_result"]["my_vc"]["re_save_approver"]
    Approver           = data["testcase_result"]["my_vc"]["re_approver"]
    NoApprover         = data["testcase_result"]["my_vc"]["re_no_approver"]
    SelectCC           = data["testcase_result"]["my_vc"]["re_select_cc"]
    ClickCC            = data["testcase_result"]["my_vc"]["re_click_cc"]
    ResultNumber       = data["testcase_result"]["my_vc"]
    CCSaveSelect       = data["testcase_result"]["my_vc"]["re_save_select_cc"]
    CC                 = data["testcase_result"]["my_vc"]["re_cc"]
    Search             = data["testcase_result"]["my_vc"]["search"]
    CCClickUser        = data["re_msg"]["pass_cc_click_user"]
    CCClickAdd         = data["re_msg"]["pass_cc_add"]
    CCClickSave        = data["re_msg"]["pass_cc_save"]
    SelectDate         = data["re_msg"]["pass_select_date"]
    ApproverLine       = data["re_msg"]["pass_approver_line"]
    ApproverException  = data["re_msg"]["pass_approver_exception"]
    InputUser          = data["testcase_result"]["my_vc"]["in_user"]
    SelectUser         = data["testcase_result"]["my_vc"]["sl_org"]
    EnterReason        = data["testcase_result"]["my_vc"]["re_reason"]
    HourStart          = data["testcase_result"]["my_vc"]["hour_start"]
    HourSEnd           = data["testcase_result"]["my_vc"]["hour_end"]
    NoWorkPolicy       =  data["testcase_result"]["time_card"]["no_policy"]
    AccessTimeSheets   =  data["testcase_result"]["time_card"]["sub_calendar"]
    NoApproval         =  data["testcase_result"]["time_card"]["no_policy"]
    DisplayedVacation  =  data["testcase_result"]["time_card"]["tc_vacation"]
    SelectVacationName = data["re_msg"]["pass_ad_select_vacation"]
    NoVacationToRequest = data["testcase_result"]["my_vc"]["no_vc"]
    RequestVacationAll  = data["testcase_result"]["my_vc"]["request_all"]
    VacationConsecutive = data["testcase_result"]["my_vc"]["request_con"]
    RequestVacationAm = data["testcase_result"]["my_vc"]["request_am"]
    RequestVacationPm = data["testcase_result"]["my_vc"]["request_pm"]
    RequestVacationHour = data["testcase_result"]["my_vc"]["request_hour"]
    NoRequestToCancel   = data["testcase_result"]["my_vc"]["no_cancel"]
    ClickOnCancelIcon   = data["testcase_result"]["my_vc"]["icon_cancel"]
    CancelRequest       = data["testcase_result"]["my_vc"]["cancel_request"]
    StatusOfRequest     = data["testcase_result"]["my_vc"]["cancel_status"]
    StatusIsUserCancel  = data["testcase_result"]["my_vc"]["user_cancel"]
    NoUseAm             = data["testcase_result"]["my_vc"]["no_am"]
    NoUsePm             = data["testcase_result"]["my_vc"]["no_pm"]
    NotEnoughDayAm      = data["testcase_result"]["my_vc"]["not_enough_am"]
    NotEnoughDayPm      = data["testcase_result"]["my_vc"]["not_enough_pm"]
    NoUseHourUnit       = data["testcase_result"]["my_vc"]["no_use_hour"]
    NotEnoughDayPm      = data["testcase_result"]["my_vc"]["not_enough_hour"]
    NotEligibleRequest  = data["testcase_result"]["my_vc"]["can_re"]
    NoDisplayData       = data["testcase_result"]["my_vc"]["no_org"] 
    InputUserToSearch   = data["testcase_result"]["my_vc"]["ip_search"]
    SearchUser          = data["testcase_result"]["my_vc"]["search"]
    
    
    
class pr_ap():
    vc_ap = data["vc_ap"]
    AccessSubmenuAp            = data["testcase_result"]["manager"]["menu_vc_approve"]
    NoSubMenuApprove           = data["testcase_result"]["manager"]["no_menu_approve"]
    NoVcToApproval             = data["testcase_result"]["manager"]["no_ap"]
    ApproveRequest             = data["testcase_result"]["manager"]["approve"]
    ClickOnApproveIcon         = data["testcase_result"]["manager"]["icon_approve"]
    StatusChangedToApproved    = data["testcase_result"]["manager"]["status_after_approve"]
    NoVacationToReject         = data["testcase_result"]["manager"]["no_reject"]
    NoVacationToCancelApprove  = data["testcase_result"]["manager"]["no_cancel_approve"]
    ClickOnRejectIcon          = data["testcase_result"]["manager"]["ic_reject"]
    RejectRequest              = data["testcase_result"]["manager"]["vc_reject"]
    RequestAfterReject         = data["testcase_result"]["manager"]["remove_re"]
    ClickOnCancelApproveIcon   = data["testcase_result"]["manager"]["ic_cancel_approve"]
    CancelApprove              = data["testcase_result"]["manager"]["vc_cancel_approve"]
    RequestAfterCancelApprove  = data["testcase_result"]["manager"]["remove_cancel"]
    NoVacationToDelete         = data["testcase_result"]["manager"]["no_delete"]
    ClickOnDeleteIcon          = data["testcase_result"]["manager"]["ic_delete"]
    DeleteVacation             = data["testcase_result"]["manager"]["delete"]
    VacationRemoved            = data["testcase_result"]["manager"]["delete_removed"]

class pr_mn():
    mn_pro = data["mn_pro"]    
    AccessSubmenuAdjust        = data["testcase_result"]["manager_pro"]["sub_menu_vc_adjust"]
    NoSubMenuAdjust            = data["testcase_result"]["manager_pro"]["no_menu_adjust"]
    ClickRadioAdjust           = data["testcase_result"]["manager_pro"]["radio_adjust"]
    NoVacationToAdjust         = data["testcase_result"]["manager_pro"]["no_condition"]
    ClickOnButtonAdjust        = data["testcase_result"]["manager_pro"]["adjust_one"]
    AdjustVacation             = data["testcase_result"]["manager_pro"]["adjust"]
    NumberAdjust               = data["testcase_result"]["manager_pro"]["re_adjust"]
    ClickRadioGrant            = data["testcase_result"]["manager_pro"]["radio_grant"]
    NoVcToGrant                = data["testcase_result"]["manager_pro"]["no_vc_grant"]
    InputDays                  = data["testcase_result"]["manager_pro"]["days_grant"]
    ClickOnButtonGrant         = data["testcase_result"]["manager_pro"]["grant_one"]
    GrantVacation              = data["testcase_result"]["manager_pro"]["grant"]

class pr_ad():
    dt_ad = data["admin"]
    UserNoAdmin                = data["testcase_result"]["admin"]["permiss"]
    ClickNextButton            = data["testcase_result"]["admin"]["vacation_next"]
    InputVacationName          = data["testcase_result"]["admin"]["ip_vc_name"]
    InputVacationNumber        = data["testcase_result"]["admin"]["ip_vc_number"]
    AccessSubMenuVc            = data["testcase_result"]["admin"]["sub_menu_vc"]  
    DisplayVacation            = data["testcase_result"]["admin"]["display_vc"]
    NoVacationToDelete         = data["testcase_result"]["admin"]["no_vc_delete"]
    ClickOnIconDelete          = data["testcase_result"]["admin"]["icon_vc_delete"]
    ClickOnButtonDelete        = data["testcase_result"]["admin"]["bt_vc_delete"]
    DeleteVacation             = data["testcase_result"]["admin"]["delete_vc"]
    AccessSubMenuMn            = data["testcase_result"]["admin"]["sub_menu_mn"]
    ClickOnManagerButton       = data["testcase_result"]["admin"]["bt_manager"]
    ClickSelectUser            = data["testcase_result"]["admin"]["mn_select_user"]
    ClickToAddUser             = data["testcase_result"]["admin"]["mn_add_user"]
    AddManager                 = data["testcase_result"]["admin"]["manager"]
    DisplayManager             = data["testcase_result"]["admin"]["display_manager"]
    NoManagerToDelete          = data["testcase_result"]["admin"]["no_mn_delete"]
    ClickOnIconDelete          = data["testcase_result"]["admin"]["icon_delete"]
    DeleteManager              = data["testcase_result"]["admin"]["delete_manager"]
    RemovedManager             = data["testcase_result"]["admin"]["removed_manager"]
    AccessTabAP                = data["testcase_result"]["admin"]["tab_ap_setting"]
    ClickOnButtonApprover      = data["testcase_result"]["admin"]["ad_click_approver"]
    ClickSelectUserAd          = data["testcase_result"]["admin"]["ad_sl_user"] 
    ClickToAddUserAd           = data["testcase_result"]["admin"]["ad_add_user"] 
    ArbitraryDecision          = data["testcase_result"]["admin"]["arbitrary_decision"] 
    DisplayArbitraryDecision   = data["testcase_result"]["admin"]["ad_display"] 
    AccessSubMenuBs            = data["testcase_result"]["admin"]["sub_menu_bc"]
    ClickOnButtonAdd           = data["testcase_result"]["admin"]["ae_add_bt"]
    ClickToAddUserAe           = data["testcase_result"]["admin"]["ae_add_user"] 
    ApprovalException          = data["testcase_result"]["admin"]["approval_exception"] 
    DisplayApprovalException   = data["testcase_result"]["admin"]["ae_display"] 
    
    
class type_vc():
    def check_type(type_request , text):
        if type_request  == "all" :
            text_request = "All day : "
        elif type_request == "hour" :
            text_request  = "Hour Unit : "
        elif type_request == "vc_con" :
            text_request  = "Vacation consecutive : "
        elif type_request == "half_day" :
            text_request  = "Half day : "
        return text_request + text

    def MsgViewDetailApprover(type_request):
        text_request = {}
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["total_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["total_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["total_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["total_half"]
        
        return text_request 

    def MsgDisplayedRequest(type_request):
        text_request = {}
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["re_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["re_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["re_con"]
        else :
            text_request  = pr_rq.ResultNumber["re_half"]
        return text_request 

    def MsgRequest(type_request):
        text_request = {}
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["request_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["request_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["request_con"]
        else :
            text_request  = pr_rq.ResultNumber["request_half"]
        return text_request 

    def MsgViewDetail(type_request):
        text_request = {}
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["detail_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["detail_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["detail_con"]
        else :
            text_request  = pr_rq.ResultNumber["detail_half"]
        return text_request 

    def MsgRequestTotal(type_request):
        text_request = {}
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["total_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["total_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["total_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["total_half"]
        return text_request 
    
    def MsgRequestUsed(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["used_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["used_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["used_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["used_half"]
        return text_request 

    def MsgRequestRemain(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["remain_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["remain_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["remain_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["remain_half"]
        return text_request 
    
    def MsgCancelTotal(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["cancel_all_total"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["cancel_hour_total"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["cancel_consecutive_total"]
        else :
            text_request  = pr_rq.ResultNumber["cancel_half_total"]
        return text_request 
    
    def MsgCancelUsed(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["cancel_all_used"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["cancel_hour_used"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["cancel_consecutive_used"]
        else :
            text_request  = pr_rq.ResultNumber["cancel_half_used"]
        return text_request 
    
    def MsgCancelRemain(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["cancel_all_remain"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["cancel_hour_remain"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["cancel_consecutive_remain"]
        else :
            text_request  = pr_rq.ResultNumber["cancel_half_remain"]
        return text_request 

    def MsgBeforeRequest(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["before_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["before_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["before_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["before_half"]
        return text_request 

    def MsgBeforeCancel(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["before_cancel_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["before_cancel_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["before_cancel_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["before_cancel_half"]
        return text_request 
    
    def MsgAfterRequest(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["after_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["after_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["after_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["after_half"]
        return text_request 
    
    def MsgAfterCancel(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["cancel_all"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["cancel_hour"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["cancel_consecutive"]
        else :
            text_request  = pr_rq.ResultNumber["cancel_half"]
        return text_request 

    def MsgDetailApproverException(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_approver_exception"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_approver_exception"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_approver_exception"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_approver_exception"]
        return text_request 

    def MsgDetailApprover(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_aprover"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_aprover"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_aprover"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_detail_aprover"]
        return text_request 
    
    def MsgDetailApproverLine(type_request):
        print("hoa")
        text_request=""
        print("type_request :",type_request)
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_aprover"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_aprover"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_aprover"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_aprover"]
        print("text_request :",text_request)
        return text_request 
    
    def MsgDetailVacationDate(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_vc_date"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_vc_date"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_vc_date"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_vc_date"]
        return text_request 
    
    def MsgDetailUsed(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_used"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_used"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_used"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_used"]
        return text_request

    def MsgDetailRequestDate(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_detail_request_date"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_detail_request_date"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_detail_request_date"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_request_date"]
        return text_request 

    def MsgDetailReason(type_request):
        if type_request  == "all" :
            text_request = pr_rq.ResultNumber["all_reason"]
        elif type_request == "hour" :
            text_request  = pr_rq.ResultNumber["hour_reason"]
        elif type_request == "vc_con" :
            text_request  = pr_rq.ResultNumber["consecutive_reason"]
        else :
            text_request  = pr_rq.ResultNumber["half_detail_reason"]
        return text_request

    def hour_use(type_request):
        if type_request == "all" :
            hour_use = "1D"
        elif type_request == "vc_con" :
            hour_use = "2D"
        elif type_request == "hour" :
            hour_use = "2H"
        else :
            hour_use = "4H"
        return hour_use

class xpath():
    def TimeComparison(infor_request,today):
        vacation   = {
            "request_date" :infor_request["vacation_time"],
            "today"        :today
            
            }
        return vacation
        
    def HourToDaysUsed(vc_bf_use,oneday,hour_use,use_hour_unit,type_request):
        vacation   = {
            "tp1"          :vc_bf_use["used"],
            "tp2"          :vc_bf_use["remain"],
            "oneday"       :oneday,
            "plus"         :"plus",
            "hour_use"     :hour_use,
            "use_hour_unit":use_hour_unit,
            "type_request" :type_request
            }
        return vacation

    def UHourToDaysNone(vc_bf_use,oneday,hour_use,use_hour_unit,type_request):
        vacation   = {
            "tp1"          :vc_bf_use["used"],
            "tp2"          :None,
            "oneday"       :oneday,
            "plus"         :"plus",
            "hour_use"     :hour_use,
            "use_hour_unit":use_hour_unit,
            "type_request" :type_request
            }
        return vacation
    
    def RHourToDaysNone(vc_bf_use,oneday,hour_use,use_hour_unit,type_request):
        vacation   = {
            "tp1"          :vc_bf_use["remain"],
            "tp2"          :None,
            "oneday"       :oneday,
            "plus"         :"minus",
            "hour_use"     :hour_use,
            "use_hour_unit":use_hour_unit,
            "type_request" :type_request
            }
        return vacation
    
    def UCHourToDaysNone(vc_bf_use,oneday,hour_use,use_hour_unit,type_request):
        vacation   = {
            "tp1"          :vc_bf_use["used"],
            "tp2"          :None,
            "oneday"       :oneday,
            "plus"         :"minus",
            "hour_use"     :hour_use,
            "use_hour_unit":use_hour_unit,
            "type_request" :type_request
            }
        return vacation

    def RCHourToDaysNone(vc_bf_use,oneday,hour_use,use_hour_unit,type_request):
        vacation   = {
            "tp1"          :vc_bf_use["remain"],
            "tp2"          :None,
            "oneday"       :oneday,
            "plus"         :"plus",
            "hour_use"     :hour_use,
            "use_hour_unit":use_hour_unit,
            "type_request" :type_request
            }
        return vacation

    def ResultBefore(vc_bf_use,days,msg):
        vacation   = {
            "number_before" :vc_bf_use["total"],
            "number_after"  :days,
            "msg"           :msg
            
            }
        return vacation

    def ResultBeforeOther(vc_bf_use,msg):
        vacation   = {
            "number_before" :vc_bf_use["total"],
            "number_after"  :"-",
            "msg"           :msg
            
            }
        return vacation
    

    def ParVacation():
        vacation   = {
            "total"        :"",
            "used"         :"",
            "remain"       :"",
            "start"        :"",
            "expiration"   :"",
            "vacation_name":""
            }
        return vacation
    
    def ParVacationUse():
        vacation   = {
            "vacation_name"  : "",
            "number_of_days" : "",
            "number_of_hours": ""
                
            }
        return vacation
    
    def ParResultApprover():
        vacation   = {
            "user_name"   : "",
            "is_selected" : ""
                
        }
        return vacation
    
    def ParSelectApprover():
        select_approver = {
            "result_approver"   : False ,
            "approver_name"     : True  ,
            "approval_line"     : False ,
            "approval_exception": False 
            }
        return select_approver
    
    def ParUsageSettings():
        usage_settings = {
            "vacation_name"  : "",
            "number_of_days" : "",
            "number_of_hours": "",
            "use_hour_unit"  : "",
            "use_half_day"   : "",
            "hour_use"       : ""
            }
        return usage_settings
    
    def ParInfo():
        info = {
            "vc_date"      : "",
            "used"         : "",
            "request_date" : "",
            "approver"     : "",
            "reason"       : ""
            }
        return info
    
    def ParVacationRequest():
        vc_rq = {
            "vc_name"     : "",
            "vc_date"     : "",
            "request_date": "",
            "status"      : "Request"
            }
        return vc_rq
    
    def ParInforRequest():
        infor_request = {
            "no"           :"",
            "vacation_name":"",
            "vacation_date":"",
            "use"          :"",
            "request_date" :"",
            "status"       :"",
            "icon_cancel"  :"",
            "vacation_time":""
            }
        return infor_request
    
    
    
    def ParInforVacation():
        infor_request = {
            "no"           :"",
            "request_by"   :"",
            "vacation_name":"",
            "vacation_date":"",
            "use"          :"",
            "request_date" :"",
            "status"       :"",
            "icon_cancel"  :""
            }
        return infor_request
    
    def ParApproverResult():
        result = { 
            "rs_resaon"  :False ,
            "rs_approver":False ,
            "info_after" :""    ,
            "info_before":""    }
        return result
    
    def par_vacation_request(request_date):
        vacation_request = {
            "vc_name"     : ""           ,
            "vc_date"     : ""           ,
            "request_date": request_date ,
            "status"      : "Request"
            }
        return vacation_request

    

    def ParChooseDate(rs_date,vc_date,vc_rq):
        result = {
        "result_date"         :rs_date,
        "vc_date"             :vc_date,
        "vacation_request"    :vc_rq,
        }
        return result
    
    def ParTimeCard(Approver,Date):
        result = {
        "Date_Request"         :Date["vc_date"],
        "Approver"             :Approver
        
        }
        return result
       
    def par_all_day():
        result = {
        "result_date"          :"",
        "vc_date"              :"",
        "oneday"               :"",
        "number_before_request":"",
        "result_select_vc"     :"",
        "use_hour_unit"        :"",
        "hour_use"             :"",
        "vc_name"              :""
        }
        return result

    def ParNumberOfDaysTest(NumberBeforeRequest,NumberAfterRequest,type,SelectVacation,Oneday):
        result = {
            "before"       : NumberBeforeRequest ,
            "after"        : NumberAfterRequest,
            "hour_use"     : SelectVacation["hour_use"] ,
            "vc_name"      : SelectVacation["vc_name"],
            "oneday"       : Oneday,
            "use_hour_unit": SelectVacation["use_hour_unit"],
            "type_request" : type
        }
        return result
    
    def ParNumberOfDays(NumberBeforeRequest,type,SelectVacation):
        if type == Am or type == Pm : 
            type = "half_day"
        result = {
            "before"       : NumberBeforeRequest ,
            "hour_use"     : SelectVacation["hour_use"] ,
            "vc_name"      : SelectVacation["vc_name"],
            "oneday"       : 8,
            "use_hour_unit": SelectVacation["use_hour_unit"],
            "type_request" : type
        }
        return result

    def ParCancelRequest(SelectVacation):
        result = {
            "oneday"            : 8 ,
            "use_hour_unit"     : SelectVacation["use_hour_unit"] 
        }
        return result
    
    def ParamCreateRequest(VacationRequest,SelectVacation,Approver,type):
        result = {
            "Info_Vc"       : VacationRequest,
            "Type"  : type,
            "Use_Hour_Unit" : SelectVacation["use_hour_unit"],
            "Approver"      : Approver
        }
        return result
    
    def ParChooseVacation(Hour_Use,Result_Select_Vc,Use_Hour_Unit,Vacation_Request,Vc_Name):
        result = {
        "hour_use"         :Hour_Use,
        "result_select_vc" :Result_Select_Vc,
        "use_hour_unit"    :Use_Hour_Unit,
        "vacation_request" :Vacation_Request,
        "vc_name"          :Vc_Name
        }
        return result

    def ParamRequestAll(Approver,ResultApprover):
        result = {
            "Approver"        : Approver,
            "ResultApprover"  : ResultApprover,
            "Type"            : "all",
            "Msg"             : pr_rq.RequestVacationAll,
            "Condition"       : pr_rq.NotEligibleRequest
        }
        return result

    def ParamRequestConsecutive(Approver,ResultApprover):
        result = {
            "Approver"        : Approver,
            "ResultApprover"  : ResultApprover,
            "Type"            : "vc_con",
            "Msg"             : pr_rq.VacationConsecutive,
            "Condition"       : pr_rq.NotEligibleRequest
        }
        return result

    def ParamRequestAm(Approver,ResultApprover):
        result = {
            "Approver"        : Approver,
            "ResultApprover"  : ResultApprover,
            "Type"            : "am",
            "Msg"             : pr_rq.RequestVacationAm,
            "Condition"       : pr_rq.NotEligibleRequest
        }
        return result
    def ParamRequestPm(Approver,ResultApprover):
        result = {
            "Approver"        : Approver,
            "ResultApprover"  : ResultApprover,
            "Type"            : "pm",
            "Msg"             : pr_rq.RequestVacationPm,
            "Condition"       : pr_rq.NotEligibleRequest
        }
        return result
    
    def ParamRequestHour(Approver,ResultApprover):
        result = {
            "Approver"        : Approver,
            "ResultApprover"  : ResultApprover,
            "Type"            : "hour",
            "Msg"             : pr_rq.RequestVacationHour,
            "Condition"       : pr_rq.NotEligibleRequest
        }
        return result
    
    def par_request(list_status_before):
        result = {
            "sta_name_to_filter" : "Request" ,
            "select_status"      : "select_st_request",
            "submenu"            : "myvacation" ,
            "list_status_before" : list_status_before 
            
        }
        return result
    
    def par_progress(list_status_before):
        result = {
            "sta_name_to_filter" : "Progressing" ,
            "select_status"      : "select_st_progressing",
            "submenu"            : "myvacation" ,
            "list_status_before" : list_status_before 
            
        }
        return result
    
    def par_completed(list_status_before):
        result = {
            "sta_name_to_filter" : "Completed" ,
            "select_status"      : "select_st_completed",
            "submenu"            : "myvacation" ,
            "list_status_before" : list_status_before 
            
        }
        return result

    def ParDateAndStatus(vc_date,vc_stat):
        result = {
            "vc_date" : vc_date ,
            "status"  : vc_stat ,
        }
        return result

    def ParAddUserAD():
        result = {
            "Button"     :  pr_ad.dt_ad["bt_add_arbitrary"],
            "Msg"        :  pr_ad.ClickOnButtonApprover
        }
        return result
    
    def ParAddUserAE():
        result = {
            "Button"     :  pr_ad.dt_ad["bt_add_user"],
            "Msg"        :  pr_ad.ClickOnButtonAdd
        }
        return result

    def ParSaveUser(Add , Apporver_Total , Total_Apporver):
        result = {
            "Add"               :  Add,
            "Apporver_Total"    :  Apporver_Total,
            "Total_Apporver"    :  Total_Apporver
        }
        return result
    
    def ParAddAD():
        result = {
            "Button"    :  pr_ad.dt_ad["bt_select_approver"],
            "Msg"       :  pr_ad.ArbitraryDecision
        }
        return result
    
    def ParAddAE():
        result = {
            "Button"    :  pr_ad.dt_ad["bt_add_approval_exception"],
            "Msg"       :  pr_ad.ApprovalException
        }
        return result


    def ParFindVacationApprove():
        result = {
            "Approval_Type" : "approve" ,
            "Icon"          : "ic_approve" ,
            "Button"        : "bt_approve" ,
            "Status_Name"   : "Request",
            "Msg1"          : pr_ap.ClickOnApproveIcon,
            "Msg2"          : pr_ap.ApproveRequest
          
        }
        return result
    
    def ParFindVacationReject():
        result = {
            "Approval_Type" : "reject" ,
            "Icon"          : "ic_reject" ,
            "Button"        : "bt_reject" ,
            "Status_Name"   : "Request",
            "Msg1"          : pr_ap.ClickOnRejectIcon,
            "Msg2"          : pr_ap.RejectRequest
          
        }
        return result
    
    def ParFindVacationCancelApprove():
        result = {
            "Approval_Type" : "cancel_approve" ,
            "Icon"          : "ic_cancel_approve" ,
            "Button"        : "bt_cancel_approve" ,
            "Status_Name"   : "Approved",
            "Msg1"          : pr_ap.ClickOnCancelApproveIcon,
            "Msg2"          : pr_ap.CancelApprove
          
        }
        return result


    def ParCheckResultApprove(Icon_Approve,Result_Approve ,Request_Use_To_Approval,Total_Request,Approval_Type):
        result = {
            "Approval_Type"           : Approval_Type ,
            "Icon_Approve"            : Icon_Approve   ,
            "Result_Approve"          : Result_Approve ,
            "Request_Use_To_Approval" : Request_Use_To_Approval ,
            "Total_Request"           : Total_Request,
            "Msg1"                    : pr_ap.StatusChangedToApproved,
            "Msg2"                    : pr_ap.NoVcToApproval
          
        }
        return result
    
    def ParCheckResultReject(Icon_Approve,Result_Approve ,Request_Use_To_Approval,Total_Request,Approval_Type):
        result = {
            "Approval_Type"           : Approval_Type ,
            "Icon_Approve"            : Icon_Approve   ,
            "Result_Approve"          : Result_Approve ,
            "Request_Use_To_Approval" : Request_Use_To_Approval ,
            "Total_Request"           : Total_Request,
            "Msg1"                    : pr_ap.RequestAfterReject,
            "Msg2"                    : pr_ap.NoVacationToReject
          
        }
        return result
    def ParCheckResultCancelApprove(Icon_Approve,Result_Approve ,Request_Use_To_Approval,Total_Request,Approval_Type):
        result = {
            "Approval_Type"           : Approval_Type ,
            "Icon_Approve"            : Icon_Approve   ,
            "Result_Approve"          : Result_Approve ,
            "Request_Use_To_Approval" : Request_Use_To_Approval ,
            "Total_Request"           : Total_Request,
            "Msg1"                    : pr_ap.RequestAfterCancelApprove,
            "Msg2"                    : pr_ap.NoVacationToCancelApprove
          
        }
        return result

    def cc_request(list_status_before):
        result = {
            "sta_name_to_filter" : "Request" ,
            "select_status"      : "select_st_request",
            "submenu"            : "viewcc" ,
            "list_status_before" : list_status_before 
            
        }
        return result

    def cc_progress(list_status_before):
        result = {
            "sta_name_to_filter" : "Progressing" ,
            "select_status"      : "select_st_progressing",
            "submenu"            : "viewcc" ,
            "list_status_before" : list_status_before 
            
        }
        return result

    def cc_completed(list_status_before):
        result = {
            "sta_name_to_filter" : "Completed" ,
            "select_status"      : "select_st_completed",
            "submenu"            : "viewcc" ,
            "list_status_before" : list_status_before 
            
        }
        return result

    def LiVacation(i,possiton): 
        if possiton == True :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_name_one"] % str(i)).text
        else :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_name"] % str(i)).text

        return text
    def LiRequest(i,type): 
       
        if type == "na" :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_date_mo"] % str(i)).text
           
        elif type == "da":
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_date"] % str(i)).text

        elif type == "us" :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_use"] % str(i)).text
            
        elif type == "rd" :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_vc_date"] % str(i)).text
           
        elif type == "st" :
            text = driver.find_element_by_xpath(pr_rq.rq_vc["request_status"] % str(i)).text

        return text

    def InDetail(info_vc,type):
        text = ""
        if   type == "if" :
            text = info_vc["vc_date"].rfind(data["detail"]["all"])
            
        elif type == "re" :
            #date  = info_vc["vc_date"].replace(data["detail"]["all"], "")
            date  = info_vc["vc_date"]
            text  =  data["detail"]["date"] % date

        elif type == "no" :
            text  =  data["detail"]["date"] % info_vc["vc_date"]
    
        elif type == "dt" :
            text  =  data["detail"]["request"] % info_vc["request_date"]

        elif type == "us" :
            text  =  data["detail"]["used"] % info_vc["used"]

        else :
            text  =  data["detail"]["reason"] % info_vc["reason"]
        return text

    def MnInforRequest(i):
        Infor_Request = xpath.ParInforVacation()
        Infor_Request["request_by"]    = driver.find_element_by_xpath(pr_ap.vc_ap["request_by"] % str(i)).text
        Infor_Request["vacation_name"] = driver.find_element_by_xpath(pr_ap.vc_ap["vc_name"] % str(i)).text
        Infor_Request["vacation_date"] = driver.find_element_by_xpath(pr_ap.vc_ap["vc_date"] % str(i)).text
        Infor_Request["use"]           = driver.find_element_by_xpath(pr_ap.vc_ap["use"] % str(i)).text
        Infor_Request["request_date"]  = driver.find_element_by_xpath(pr_ap.vc_ap["request_date"] % str(i)).text
        Infor_Request["status"]        = driver.find_element_by_xpath(pr_ap.vc_ap["status"] % str(i)).text
        return Infor_Request

    def ComparePequest(request1, request2):
        if  request1["vacation_date"].strip() == request2["vacation_date"].strip() and \
            request1["request_date"].strip()  == request2["request_date"].strip()  and \
            request1["request_by"]            == request2["request_by"]            and \
            request1["use"]                   == request2["use"]                       :
            return True
        else:
            return False
    
    def two_requests_are_the_same(request1,request2):
        if  request1["vacation_name"] == request2["vacation_name"] and \
            request1["vacation_date"] == request2["vacation_date"] and \
            request1["use"]           == request2["use"]           and \
            request1["request_date"]  == request2["request_date"]:
            return True
        else: 
            return False

    def VcAvailable(i,type):
        if type   == "to":
            xpath = data["available"]["to"] % str(i)
            text  = driver.find_element_by_xpath(xpath).text
            
        elif type == "na" :
            xpath = data["available"]["na"] % str(i)
            text  = driver.find_element_by_xpath(xpath).text
            
        elif type == "us":
            xpath = data["available"]["us"] % str(i)
            text  = driver.find_element_by_xpath(xpath).text
           
        elif type == "re" :
            xpath = data["available"]["re"] % str(i)
            text  = driver.find_element_by_xpath(xpath).text
           
        elif type == "ex" :
            xpath = data["available"]["ex"] % str(i)
            text  = driver.find_element_by_xpath(xpath).text 
        
        return text

    def VacationCarry(Vacation):
        Name = Vacation.rfind("[Carry-over]") 
        if Name > 0 :
            Vacation = Vacation.replace("[Carry-over]", "")
        return Vacation

    def ResultCondition(Info_Vc,Vc_Re):
        Info_Vc["vc_date"] = Info_Vc["vc_date"].replace(" ", "")
        Vc_Re["vc_date"]   = Vc_Re["vc_date"].replace(" ", "")
        Info_Vc["vc_name"] = xpath.VacationCarry(Info_Vc["vc_name"])
        if  Info_Vc["vc_name"] == Vc_Re["vc_name"]           and \
            Info_Vc["vc_date"] == Vc_Re["vc_date"]           and \
            Info_Vc["status"]  == Vc_Re["status"]            and \
            Info_Vc["request_date"] == Vc_Re["request_date"]     :
            return True
        else :
            return False

    def ConditionRequest(SelectVacation,ResultApprover,ChooseDate):
        if  bool(SelectVacation["result_select_vc"])  == True and \
            bool(ResultApprover)                      == True and \
            bool(ChooseDate["result_date"])           == True     :
            return True
        else :
            return False

    def User(Name):
        User_Name = Name.rfind("(")
        if User_Name > 0 :
            Name = Name.replace("(", "").replace(")", "")
        Name = Name.replace(" ", "")
        return Name

    def VcReplace(vacation,type):
        if type == "da" :
            return vacation["vc_date"].replace("\n", " ")
        else :
            return vacation["vc_name"].replace("\n", "").replace(" ", "")
            
    def SelectDate(selected_date,type):
        if type == "y" :
            return selected_date[None: int(selected_date.rfind("["))].replace(" ", "")
        else :
            return selected_date.replace(" ", "")
 
    def DataColumn(data_column,type):
        if type == "d" :
            return data_column[None : int(data_column.rfind("D"))]
        else :
            return data_column[int(data_column.rfind("H")) -1: int(data_column.rfind("H"))]

    def TcHourUse(hour_use,type):
        if type == "d" :
            return hour_use[int(hour_use.rfind("Use:")): int(hour_use.rfind("] ["))]
        else :
            return hour_use[int(hour_use.rfind("Real Used:") + 10) : int(hour_use.rfind("H )"))]

    def VcStart(vacation_name):
        return vacation_name[vacation_name.rfind("\n") + 1 : int(vacation_name.rfind("\n")) + 11]

    def VcChange(vacation, vacation_name):
        return vacation_name[0:int(vacation_name.rfind("\n"))] + "["+vacation["start"] + " ~ " + vacation["expiration"] + "]"

    def TcHour(hour_use):
        return int(re.search(r'\d+',hour_use).group(0)) 
    
    def VacationName(vacation_name):
        return vacation_name[None:int(vacation_name.rfind("("))-1] + vacation_name[int(vacation_name.rfind(")"))+2: None]

    def VacationNumberDay(vacation_name, type):
        if type == "d" :
            return vacation_name[int(vacation_name.rfind("(")) + 1: int(vacation_name.rfind("D"))]
        else :
            return vacation_name[int(vacation_name.rfind("(")) + 1: int(vacation_name.rfind("H"))]
            
    def VacationNumberHours(vacation_name):
        return vacation_name[int(vacation_name.rfind("D")) + 1 : int(vacation_name.rfind("H"))]

    def VacationDate(type,vc_date):
        if type == "d" :
            return vc_date.replace("(", "").replace(")", "")
        else :
            return vc_date[None: int(vc_date.rfind("H"))-1] + vc_date[int(vc_date.rfind("H")): len(vc_date)-1] 

    def TotalHour(tp1,tp2,oneday):
        return int(tp1["hour"]) + int(tp2["hour"]) + int(tp1["day"]*oneday) + int(tp2["day"]*oneday)

    def DaysUse(vacation_name):
        return vacation_name[int(vacation_name.rfind("(") + 2) : int(vacation_name.rfind(")"))]

    def UsChange(vacation_name):
        return vacation_name[None:int(vacation_name.rfind("("))-1] + vacation_name[int(vacation_name.rfind(")"))+2: None]

    def VcName(vc_name):
        name = vc_name[None: int(vc_name.rfind("~"))] + " ~ " + vc_name[ int(vc_name.rfind("~"))+ 1 : None]
        return name

    def Year(today,request_date):
        ToDay        = datetime.date.today() 
        year         = ToDay.strftime("%Y")
        ShortYear    = year[2:None]
        request_date = request_date.replace("-", "/").replace(year, ShortYear)
        today        = today.replace("-", "/").replace(year, ShortYear)
        return request_date , today
       


   
            
    