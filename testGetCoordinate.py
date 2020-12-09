from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://tai-anh.herokuapp.com/getAutoMove"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

lng = soup.find_all("h1", {"id":"lng"})
lat = soup.find_all("h1", {"id":"lat"})
print("lng: " +str(lng)[14:-6])
print("lat: " +str(lat)[14:-6])
