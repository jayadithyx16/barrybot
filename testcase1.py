import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
























try:
    #the code for shorten login starts here.....
    #headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36","Referer":"https://tnshort.net/"}
    login_url= "https://tnshort.net/auth/signin"
    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    referer = "https://tnshort.net/"
    chrome_options.add_argument(f"referer={referer}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(login_url)
    time.sleep(4)
    username = 'barryallen16'
    password = 'Suriya@1616'
    usernam_field = driver.find_element(By.ID,'username')
    pass_field= driver.find_element(By.ID,'password')
    usernam_field.send_keys(username)
    pass_field.send_keys(password)
    remember_field=driver.find_element(By.ID,'remember-me')
    remember_field.click()
    pass_field.send_keys(Keys.RETURN)
    print("logged in successfully...")
    driver.implicitly_wait(16)
    driver.get("https://tnshort.net/member/links")
    time.sleep(2)
    new_sl = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-block.btn-social.btn-github.btn-lg.shorten-button")
    new_sl.click()
    url_field = driver.find_element(By.ID,'url')
    url_field.send_keys("https://www.zenrows.com/blog/bypass-cloudflare")
    time.sleep(1.5)
    shorten_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-submit.btn-primary.btn-xs")
    shorten_button.click()
    try:
        div_element = driver.find_element(By.CSS_SELECTOR,"div.input-group-addon.copy-it")
        scopy = div_element.get_attribute("data-clipboard-text")
        print(scopy)
    except:
        print(" this doesnt work")
except:
    print("the shortner login or process failed")