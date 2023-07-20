from selenium import webdriver
from webdriver_auto_update import check_driver
import os
import Exec
import configure
from Exec import *
from configure import *

try:
    cwd = os.path.abspath(os.getcwd()+"chromedriver.exe")
    Exec.execution(username=configure.username,password=configure.password,about=configure.about,address=cwd,
                   sleepTime=configure.cooldown, bg=configure.background)
except:
    # Pass in the folder used for storing/downloading chromedriver
    cwd = os.path.abspath(os.getcwd())
    check_driver(cwd)
    cwd = os.path.abspath(os.cwd() + "chromedriver.exe")
    Exec.execution(username=configure.username, password=configure.password, about=configure.about, address=cwd,
                   sleepTime=configure.cooldown, bg=configure.background)