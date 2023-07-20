from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from warnings import filterwarnings
filterwarnings('ignore')


def execution(username,password,about,address,sleepTime,bg):

    ## time

    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    print("Naukri Code Excecution Started", date_time)

    ## Add your chrome browser address

    print("Code Started At : ", date_time)
    user = username
    while True:

        ## Update Time
        time_now = datetime.datetime.now()
        time_now = time_now.strftime("%m/%d/%Y, %H:%M:%S")

        print("Naukri Code Excecution Started", time_now)

        ## Add your chrome browser address
        address = address

        browser = webdriver.Chrome()
        if bg:
            browser.set_window_position(10000,100000)
        browser.get("https://www.naukri.com/nlogin/login")
        browser.implicitly_wait(60)

        print("Naukri Accessed At : ", time_now)

        ## Username & Pass
        password = password

        # get username and password
        emailElem = browser.find_element(By.ID,'usernameField')
        emailElem.clear()
        emailElem.send_keys(user)
        passwordElem = browser.find_element(By.ID,'passwordField')
        passwordElem.clear()
        passwordElem.send_keys(password)
        passwordElem.submit()
        time.sleep(5)

        print(f"Naukri Login Successfull for {user}: ", time_now)

        browser.get("https://www.naukri.com/mnjuser/profile?id=&altresid")
        #########################################################################
        resumeHeadlineSpans = browser.find_element(By.CLASS_NAME,"resumeHeadline").find_elements(By.TAG_NAME,"span")

        for span in resumeHeadlineSpans:
            if span.text == "editOneTheme":
                span.click()
                break

        # Here updating Naukri Profile Resume Headline.
        headline = about

        resumeHeadlineTextArea = browser.find_element(By.CLASS_NAME,"resumeHeadlineTxt")
        resumeHeadlineTextArea.clear()
        resumeHeadlineTextArea.send_keys(headline)

        btnList = browser.find_elements(By.TAG_NAME,"button")

        for item in btnList:
            if item.text == "Save" or item.text =='SAVE':
                item.click()
                break

        print("Naukri Resume Headline Updated : ", time_now)

        browser.close()
        print("Naukri Job Success::", time_now)
        time.sleep(sleepTime)
        print("Re Execution Started::", time_now)