from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
time.sleep(10)
