from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\\Users\\Sasindu\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_css_selector(".top")
fname.send_keys("Sasindu") # fill the input

lname = driver.find_element_by_css_selector(".middle")
lname.send_keys("Nanayakkara") # fill the input

email = driver.find_element_by_css_selector(".bottom")
email.send_keys("sas@gmail.com") # fill the input

submit = driver.find_element_by_css_selector(".btn")
submit.click() # click the submit button
