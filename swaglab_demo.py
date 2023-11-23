from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.saucedemo.com/v1/')

#Login Page
Username = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
Password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')
Btn_Login = driver.find_element(By.ID, 'login-button').click()

#Home page 
Product = driver.find_element(By.XPATH,'//div[@class="inventory_item_name"]').click()

#Product Page
Btn_AddCart = driver.find_element(By.XPATH,'//button[@class="btn_primary btn_inventory"]').click()
Btn_Cart = driver.find_element(By.CSS_SELECTOR,'.fa-layers').click()

#Cart Page
Btn_Checkout = driver.find_element(By.XPATH,'//a[@class="btn_action checkout_button"]').click()

#Checkout: Your Information Page
InputFirstName = driver.find_element(By.XPATH,'//input[@id="first-name"]').send_keys('John Doe')
InputLastName = driver.find_element(By.XPATH,'//input[@id="last-name"]').send_keys('Doe')
InputZip = driver.find_element(By.XPATH,'//input[@id="postal-code"]').send_keys('13510')
Btn_Continue = driver.find_element(By.XPATH,'//input[@type="submit"]').click()

#Checkout: Overview Page
Btn_Finish = driver.find_element(By.XPATH,'//a[@class="btn_action cart_button"]').click()

#Transaction Success Page
Btn_Hamburger = driver.find_element(By.XPATH,'//button[@style="position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; margin: 0px; padding: 0px; border: none; opacity: 0; font-size: 8px; cursor: pointer;"]').click()
Btn_Logout = driver.find_element(By.XPATH,'//div/div/div/div/div/nav/a[@id="logout_sidebar_link"]').click()
