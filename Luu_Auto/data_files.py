import platform, json, time
from datetime import datetime
from selenium import webdriver


class objects:
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time1 = now.strftime("%H:%M:%S")
    date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
    date_id = date_time.replace("/", "").replace(", ", "").replace(":", "")[2:]

system_name = str(platform.system())
if system_name == "Windows":
    local_path = "D:\\PhuongDofu\\groupware-auto-test-2"
    local_luu = "D:\\File_Du_Lieu\\Selenium\\Edit_Link\\luungo_automationtest"
    json_file = local_path + "\\config.json"
    with open(json_file) as json_data_file:
        data = json.load(json_data_file)
    # start web browser
    driver = webdriver.Chrome(data["chromedriver_path"])
    log_folder = "\\Log\\"
    execution_log = local_path + log_folder + "execution_log_" + str(objects.date_id) + ".txt"
    fail_log = execution_log.replace("execution_log_", "fail_log_")
    error_log = execution_log.replace("execution_log_", "error_log_")
    recipients = "phuong@hanbiro.vn"
    clouddisk_folder = "\\Attachment\\CloudDisk\\"
    image = "\\Attachment\\download.jpg"
    asset_import = "\\Attachment\\Asset-SeleniumPython.xls"
    expense_import = "\\Attachment\\Expense-SeleniumPython.xls"
    contact_import = "\\Attachment\\Contact-SeleniumPython.xls"
    calendar_import = "\\Attachment\\Calendar-SeleniumPython.xls"
    organization_import = "\\Attachment\\Organization-SeleniumPython.xls"


if system_name == "Linux":
    local_path = "/home/oem/groupware-auto-test"
    json_file = local_path + "/config.json"
    with open(json_file) as json_data_file:
        data = json.load(json_data_file)
    # start web browser
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    log_folder = "/Log/"
    execution_log = local_path + log_folder + "execution_log_" + str(objects.date_id) + ".txt"
    fail_log = execution_log.replace("execution_log_", "fail_log_")
    error_log = execution_log.replace("execution_log_", "error_log_")
    recipients = "qavn@hanbiro.vn, linux@hanbiro.com, phong@hanbiro.vn"
    clouddisk_folder = "/Attachment/CloudDisk/"
    image = "/Attachment/download.jpg"
    asset_import = "/Attachment/Asset-SeleniumPython.xls"
    expense_import = "/Attachment/Expense-SeleniumPython.xls"
    contact_import = "/Attachment/Contact-SeleniumPython.xls"
    calendar_import = "/Attachment/Calendar-SeleniumPython.xls"
    organization_import = "/Attachment/Organization-SeleniumPython.xls"

# create log file of fail test case
open(execution_log, "x").close()

# create log file of fail test case
open(fail_log, "x").close()

# create log file of fail test case
open(error_log, "x").close()

def Logging(msg):
    print(msg)
    log_msg = open(execution_log, "a")
    log_msg.write(str(msg) + "\n")
    log_msg.close()

def ValidateFailResultAndSystem(fail_msg):
    print(fail_msg)
    append_fail_result = open(fail_log, "a")
    append_fail_result.write("[FAILED TEST CASE] " + str(fail_msg) + "\n")
    append_fail_result.close()


