# login first
# then add item to cart and verify cart count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(4)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

assert cart_count == "1"
driver.quit()
