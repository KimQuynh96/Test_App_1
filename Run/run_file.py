import os
from os import pipe ,path
from pathlib import Path
import sys


Domain        = "tg01.hanbiro.net"
ID            = "automationtest"
Pass          = "automationtest1!"
Domain_GW     = "http://%s/ngw/app/#" % Domain
Folder_List   = {
    # "LUU"           : "Luu_Auto",
    # "NGOC GW"       : "Ngoc_Auto\\Ngoc_GW",
    # "NGOC COMANAGE" : "Ngoc_Auto\\Ngoc_Comanage",
    # "NHU QUYNH"     : "NQ_Auto",
    "KIM QUYNH"     : "KQ_Auto",
    "HANH"          : "Hanh_Auto"
    }

for Tester, Folder in Folder_List.items() :
    local      = os.path.dirname(Path(__file__).absolute())
    local      = local.replace("Run",Folder)
    sys.path.insert(0, local)
    match Tester:
        case "LUU":
            from luu_run_file import Luu_My_Execution
            Luu_My_Execution(Domain_GW)
        case "NGOC GW":
            from MN_run_file  import My_Execution
            My_Execution(Domain_GW)
        case "NGOC COMANAGE":
            from new_comanage import access_hr , comanage
        case "NHU QUYNH":
            from NQ_run_file  import My_Execution
            My_Execution(Domain_GW)
        case "KIM QUYNH":
            from vacation_run import run
            run(Domain,ID,Pass)
        case "HANH":
            from H_run_file   import My_Execution
            My_Execution(Domain,ID,Pass)

                
    



















