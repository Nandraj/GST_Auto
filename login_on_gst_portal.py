from selenium import webdriver
import time


# login into gst portal and accessing required data
def login_on_GSTPortal(login_id, pwd):
    # change download setting
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {"download.prompt_for_download": True, "download.dictionery_upgrade": True})

    browser = webdriver.Chrome(chrome_options=options)
    # open gst login page
    browser.get('https://services.gst.gov.in/services/login')

    # maximise screen and wait for some seconds to loan
    browser.maximize_window()
    browser.implicitly_wait(30)

    # go to login id input
    id_box = browser.find_element_by_id("username")
    id_box.clear()

    # enter ID
    id_box.send_keys(login_id)

    # go to password input
    pswd_box = browser.find_element_by_id("user_pass")
    pswd_box.clear()

    # enter password
    pswd_box.send_keys(pwd)

    # go to capcha input
    capcha_box = browser.find_element_by_id("captcha")
    capcha_box.clear()

    capcha_box.send_keys(" ")
