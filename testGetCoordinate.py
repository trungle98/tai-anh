from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://rubikscode.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a", class_='entry-featured-image-url')