import os
import sys
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def msg(contacts, message):
    driver_path = 'C:\\Users\\HP\\Downloads\\chromedriver.exe'  # Update this with your ChromeDriver path
    wtapp_profile = "user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\wah"
    
    options = Options()
    options.add_argument(wtapp_profile)
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    
    # Suppress Selenium logs
    options.add_argument('--log-level=3')
    
    # Suppress DevTools logs by redirecting stderr
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        
        driver.get('https://web.whatsapp.com/')
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))

        for contact in contacts:
            try:
                search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                search_box = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath)))
                search_box.clear()
                search_box.send_keys(contact)
                search_box.send_keys(Keys.ENTER)
                
                time.sleep(5)
                
                message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                message_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
                message_box.send_keys("Use OTP "+str(message)+" to reset your password.")
                message_box.send_keys(Keys.ENTER)

                time.sleep(5)
                print("message sent")
            except Exception as e:
                print(f"Failed to send message to {contact}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Reset standard output and error to original state
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        driver.quit()

