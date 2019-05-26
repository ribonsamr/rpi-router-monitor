from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("http://192.168.1.1/rpSys.html")

username = driver.find_element_by_name("Login_Name")
password = driver.find_element_by_name("Login_Pwd")
username.send_keys("")
password.send_keys("")

driver.find_element_by_name("texttpLoginBtn").click()

tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')

tutorial_code_soup = tutorial_soup.find("b", text="Downstream:").find_next_sibling("font")