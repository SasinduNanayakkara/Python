from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")  # parsing object
# print(soup.title.name)  # display tag name
# print(soup)  # display whole html file
# print(soup.prettify()) # display with proper indentation
# print(soup.a)  # display the first anchor tag
# all_abchor_tags = soup.find_all(name="a")

# for tag in all_abchor_tags:
#     print(tag.getText())  # get the all link names in the html file
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")  # find a specific tag with mentioning tag name and id
section_heading = soup.find(name="h3", class_="heading")  # find a specific tag with mentioning tag name and class name
print(section_heading.getText())  # getText() - get the content of the tag
