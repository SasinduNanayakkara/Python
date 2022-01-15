from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.edupub.gov.lk/")  # get the source code of a web page
# print(response.text) # print the source code

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
print(soup.title)
print(soup.find(name="a",href="BooksDownload.php", class_="LeftNaviNormal").getText())
print(print(soup.find(name="a",href="BooksDownload.php", class_="LeftNaviNormal").get("href")))
