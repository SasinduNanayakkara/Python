from selenium import webdriver # import package
from selenium.webdriver.common.keys import Keys # import key package
chrome_driver_path = "C:\\Users\\Sasindu\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path) # set up chrome driver

# driver.get("https://www.amazon.com/Geforce-GDDR6X-Express-Graphics-Titanium/dp/B096L83WV8/ref=sr_1_1?crid"
#         "=3RGIGLROA9L8T&keywords=rtx+3080+ti&qid=1642276393&sprefix=rtx%2Caps%2C587&sr=8-1")  # redirect to the
# relevant URL automatic browser

# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

# driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder")) # print the placeholder name

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text) # print the text

driver.get("https://en.wikipedia.org/wiki/Main_Page")
all_portals = driver.find_element_by_link_text("All portals") # select the link
# all_portals.click() # click the link

search = driver.find_element_by_name("search") # select the search bar
search.send_keys("python") # type the text
search.send_keys(Keys.ENTER) # pass the enter key value

# driver.close()  # close the tab
# driver.quit()  # close down the entire program
