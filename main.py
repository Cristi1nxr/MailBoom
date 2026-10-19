from selenium import webdriver  
from selenium.webdriver.common.by import By
import random
import string

website = input("Enter the website you want(full-name with https): ")
driver = webdriver.Chrome()
driver.get(website)
lastName = input("Enter a random Last-Name: ") 
firstName = input("Enter a random First-Name: ")
emails = input("Enter your email MUST BE A GMAIL + ENTER IT WITHOUT THE @: " ) 
random_str = "".join(random.choices(string.ascii_lowercase, k=5))
last_name = driver.find_element(By.ID, "account-last-name")
last_name.send_keys(lastName)
first_name = driver.find_element(By.ID, "account-first-name")
first_name.send_keys(firstName)
email = driver.find_element(By.ID, "account-email")
email.send_keys(f"{emails}+{random_str}@gmail.com")
div_element = driver.find_element(By.CSS_SELECTOR, "div.mt-8.space-y-3")
div_element.click()
input("If you received the code on email , press ENTER to exit")
driver.quit()