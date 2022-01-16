from selenium import webdriver
import time

chrome_driver_path = "C:\\Users\\Sasindu\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

# cookie = driver.find_element_by_id("cookie")
# timeMachine = driver.find_element_by_id("buyTime machine")
# portal = driver.find_element_by_id("buyPortal")
# alchemyLab = driver.find_element_by_id("buyAlchemy lab")
# shipment = driver.find_element_by_id("buyShipment")
# mine = driver.find_element_by_id("buyMine")
# factory = driver.find_element_by_id("buyFactory")
# grandMa = driver.find_element_by_id("buyGrandma")
# cursor = driver.find_element_by_id("buyCursor")
#
# fiveSec = time.time() + 5
# timeout = time.time() + 60*5
#
# all_prices = driver.find_elements_by_css_selector("#store b")
# item_price = []
#
# for price in all_prices:
#     element_text = price.text
#     if element_text != "":
#         cost = int(element_text.split("-")[1].strip().replace(",", ""))
#         item_price.append(cost)
#
# money_element = driver.find_element_by_id("money").text
# if "," in money_element:
#     money_element = money_element.replace(",", "")
# cookie_count = int(money_element)
#
# while True:
#     if time.time() > timeout:
#         break
#     if time.time() > fiveSec:
#         if cookie_count > item_price[-1]:
#             timeMachine.click()
#         elif cookie_count > item_price[-2]:
#             portal.click()
#         elif cookie_count > item_price[-3]:
#             alchemyLab.click()
#         elif cookie_count > item_price[-4]:
#             shipment.click()
#         elif cookie_count > item_price[-5]:
#             mine.click()
#         elif cookie_count > item_price[-6]:
#             factory.click()
#         elif cookie_count > item_price[-7]:
#             grandMa.click()
#         else:
#             cursor.click()
#
#     cookie.click()

# catch the cookie element
cookie = driver.find_element_by_id("cookie")

#catch the other elements
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

fiveSec = time.time() + 5
timeout = time.time() + 60*5

while True:
    cookie.click()

    # every 5 seconds
    if time.time() > fiveSec:

        # get price tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # get price integers
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #get cookie count integer
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

        # store prices items prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find currently affordable items
        affordable_items = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_items[cost] = id

        # purchase the most expensive item
        height_affordable_items = max(affordable_items)
        print(height_affordable_items)
        purchase_item = affordable_items[height_affordable_items]

        driver.find_element_by_id(purchase_item).click()

        # after another 5 seconds
        fiveSec = time.time() + 5

    # after 5 minutes stop the bot and check cookies per second count
    if time.time() > timeout:
        cookies_p_seconds = driver.find_element_by_id("cps").text
        print(cookies_p_seconds)
        break
