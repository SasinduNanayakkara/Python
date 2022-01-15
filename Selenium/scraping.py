from selenium import webdriver

chrome_driver_path = "C:\\Users\\Sasindu\\Downloads\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time") # get the times
event_names = driver.find_elements_by_css_selector(".event-widget li a") # get the names
event = {}

for n in range (len(event_times)): # create a dictionary with data
    event[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }


for name in event_names:
    print(name.text)

driver.close()