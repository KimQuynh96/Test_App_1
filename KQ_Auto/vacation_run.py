from vacation_login import login
from vacation_my_vacation import MyVacation
from vacation_manager_processing import ManagerProcessing
from vacation_admin_settings import AdminSettings

def run(domain,id,pw) :
    ResultLogin , Info_User = login(domain,id,pw)
    if ResultLogin == True :
        MyVacation(Info_User)
        ManagerProcessing()
        AdminSettings()
        
def RunSubMyVacation():
    MyVacation(Info_User)

def RunSubManagerProcessing():
    ManagerProcessing()
    
def RunSubAdminSettings():
    AdminSettings()

#run("tg01.hanbiro.net","automationtest","automationtest1!")
















