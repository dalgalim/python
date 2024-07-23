# -*- coding: utf-8 -*-

import os
import subprocess
import datetime
import time
import shutil

#******************************************
# Written by : xian.luo@cj.net
# Date : 2021.01.13
# Script Name : mchk.py
# Purpose : It will download the MCHK
#******************************************

# ***** Start global variable declaration *****
# scp Env
path_scp = os.path.abspath("D:\__일일점검\mchk\scp")
os.chdir(path_scp)

# Calculation date
today1 = datetime.date.today()
today = today1.strftime("%Y%m%d")
threeday1 = today1 - datetime.timedelta(3)
threeday = threeday1.strftime("%Y%m%d")

# Copy file path
copy_path = ":/home/tibero/YSS/PB_TRACE_LIST/"
### _copy_path = ":/home/cgvadmin/sys_check/log/" + today
### copy_path1 = copy_path + "*" + ".log"
### copy_path2 = _copy_path + "*" + ".log"

copy_path1 = copy_path + "PB_TRACE_list_final*.log"


# ***** End of global variable declaration *****

# Copy pscp file and path location
def scp(pw, server_path, file_path):
    subprocess.Popen(["pscp.exe", "-pw", pw, server_path, file_path])
    return subprocess.Popen

# SSH 2016 port
def scp_2016(pw, server_path, file_path):
    subprocess.Popen(["pscp.exe", "-P", "2016", "-pw", pw, server_path, file_path])
    return subprocess.Popen

# Create file storage location
### create_folder_path = "D:\\_01. CGV운영\\_____Infra관리(IDC)\\mchk\\scp" + today
create_folder_path = "D:\\__일일점검\\mchk\\logs\\tibero_DB\\" + today

def create_folder_today(create_folder_path):
    if not os.path.exists(create_folder_path):
        os.mkdir(create_folder_path)
        print("************************************************")
        return print("Create File: ", create_folder_path)
    else:
        print("************************************************")
        return print(create_folder_path, ": File exists")

# Delete data 3 days ago
### remove_folder_path = "C:\\mchk\\" + threeday
### remove_folder_path = "\\\\10.130.59.24\\sm\\SM-Infra\\96. 系统检查(시스템점검)\001. IDC(TA)\IDC_MCHK\_Server\\" + threeday
def remove_data(filepath):
    if os.path.exists(filepath):
        shutil.rmtree(filepath)
        print("")
        print("************************************************")
        print("Delete Directory")
        return print("Remove All File:", remove_folder_path)
    else:
        print("************************************************")
        print("")
        print("Delete Directory")
        return print("Directory Not Found:", remove_folder_path)

# Server Information

# ESB Server Information
def esb():
    print("************************************************")
    print("")
    print("ESB Downloading...")
    # Today ESB folder
    save_path = create_folder_path + "\\ESBDB(tibero1)"
    create_folder_today(save_path)
    print("************************************************")
    print("")
    # ESB IF #1
    pifesb1_ip = "tibero@10.131.25.54" + copy_path1
    pesbdb1_pw = "#EDCvfr4"
    scp(pesbdb1_pw, pifesb1_ip, save_path)
    time.sleep(0.5)

# Other Notice
def notice():
    os.system("cls")
    print("")
    print("")
    print("************************************************")
    print("*               Warning Notice!                *")
    print("*  MCHK Download Script.                       *")
    print("*  You have download CJ CGV(China)'s           *")
    print("*  server information.                         *")
    print("************************************************")
    print("")
    print("")
    input("Press Enter to Continue...")
    print("")
    os.system("cls")

if __name__ == '__main__':
    # Information Print
    notice()
    # Create Today Folder
    create_folder_today(create_folder_path)
    # ESB Execute
    esb()


    # Delete data 3 days ago
    ### remove_data(remove_folder_path)
    print("")
    print("************************************************")
    print("The download has been completed.")
    input("Press and key to exit...")
