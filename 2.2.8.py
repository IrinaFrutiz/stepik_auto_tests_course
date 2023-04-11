from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys("First")

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Last")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("Email")

    #add file
    directory = "d:\Ira\Work\img/" #путь к папке, где лежит файл
    current_dir = os.path.abspath(os.path.dirname(__file__)) #если файл лежит в томже месте откуда запускаем
    file_name = "PDF_Test.pdf"
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    file_path = os.path.join(directory, file_name) #путь для конкретного файла
    file_created = os.path.join(current_dir, "test.txt") #путь для созданного питоном файла
    element = driver.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_created) #добавление файла

    # click Submit
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
