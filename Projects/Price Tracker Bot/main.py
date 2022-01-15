from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.com/Geforce-GDDR6X-Express-Graphics-Titanium/dp/B096L83WV8/ref=sr_1_1"
                        "?crid=I2985V13NMNB&keywords=rtx+3080+ti&qid=1642255151&sprefix=rt%2Caps%2C413&sr=8-1")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = soup.find(name="span", class_="a-price-whole")
print(soup.prettify())

