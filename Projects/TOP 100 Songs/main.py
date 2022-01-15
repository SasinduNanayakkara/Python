from bs4 import BeautifulSoup
import requests
import datetime

date = input("Witch year songs do you want ? type the date in this format YYYY-MM-DD : ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

webPage = response.text
soup = BeautifulSoup(webPage, "html.parser")
song_title = soup.find_all(name="h3", id="title-of-a-story", class_="c-title  a-no-trucate a-font-primary-bold-s "
                                                                    "u-letter-spacing-0021 lrv-u-font-size-18@tablet "
                                                                    "lrv-u-font-size-16 u-line-height-125 "
                                                                    "u-line-height-normal@mobile-max "
                                                                    "a-truncate-ellipsis u-max-width-330 "
                                                                    "u-max-width-230@tablet-only")


print(song_title)

