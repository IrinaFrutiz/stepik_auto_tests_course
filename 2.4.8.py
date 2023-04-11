from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

#задаём ожидание пока цена не станет 100
wait = WebDriverWait(driver, 12)
price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
#booking
button = driver.find_element(By.ID, "book")
button.click()

# find x on page and formula calculation(y)
x_element = driver.find_element(By.ID, "input_value")
driver.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
y = calc(x)

# add y to the answer field and scrolling
add_text = driver.find_element(By.ID, "answer")
add_text.send_keys(y)

# click Submit
button = driver.find_element(By.ID, "solve")
button.click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
driver.quit()
