from vacation_set_up import driver,data,Keys,EC,By,WebDriverWait,json
from vacation_functions import commons
from vacation_param import pr_log,Pass,Fail

def login(domain,id,pw):
    
   
    commons.Title("LOGIN")
    driver.get(commons.Url(domain))

    # Input Id 
    commons.FindElementById("log-userid").send_keys(id)
    commons.Content(pr_log.id)

    # Input Pass 
    commons.SwitchToFrame("iframeLoginPassword" , "p" , pw)
    commons.SwitchToDefaultContent()
    commons.Content(pr_log.pa)
    
    # Login
    commons.FindElementById("btn-log").send_keys(Keys.RETURN)
    commons.Content(pr_log.log)

    # Check Login #
    ResultLogin = True
    if commons.IsDisplayedById("menubar") == True :
        commons.WriteOnExcel(pr_log.ResultLog[Pass])
        Info_User = commons.ChangeLanguage()
    else :
        ResultLogin = False
        commons.WriteOnExcel(pr_log.ResultLog[Fail])

    # Check Access menu HR #
    AccessMenuVacation = False
    if  ResultLogin == True :
        driver.get(commons.Menu(domain))
        FindIframe = commons.IsDisplayedByXpath(data["iframe_vc"])
        if FindIframe == True :
            driver.switch_to.frame(driver.find_element_by_xpath(data["iframe_vc"]))
            if commons.IsDisplayedByXpath(data["menu_vc"]) == True :
                driver.find_element_by_xpath(data["menu_vc"]).click()
            
                if commons.IsDisplayedByXpath(data["sm_my_vc_sta"]) == True :
                    AccessMenuVacation = True
                    commons.Title("ACCESS VACATION")
                    commons.WriteOnExcel(pr_log.menu[Pass])
                    commons.PopupTimeCard()
                else:
                    commons.WriteOnExcel(pr_log.menu[Fail])
            else :
                commons.WriteOnExcel(pr_log.no_menu[Fail])
        else:
            AccessMenuVacation = False
    return AccessMenuVacation , Info_User 


