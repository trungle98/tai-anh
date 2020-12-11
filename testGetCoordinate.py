from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil
import time
from serial import Serial

port = '/dev/ttyUSB1'
for i in range(4):
    try:
        arduino = Serial(port,19200,timeout=5)
    except:
        print("error")

url = "https://tai-anh.herokuapp.com/getAutoMove"
urlDefault = "https://tai-anh.herokuapp.com/setAutoMove?x=0&y=0"
#url = "http://127.0.0.1:5000/getAutoMove"
preLng = 0
preLat = 0
def sendData(data):
    arduino.flush()
    temp = str(data)
    arduino.write(temp.encode("utf-8"))
    response = requests.get(urlDefault)
    print(data)
while True:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    lng = soup.find_all("h1", {"id":"lng"})
    lat = soup.find_all("h1", {"id":"lat"})
    lng = str(lng)[14:-6]
    lat = str(lat)[14:-6]
    if (lng != str(preLng) and lat != str(preLat)) or (int(lng) != 0 and int(lat) != 0):
        sendData(lat+","+lng+"\n")
        print((lng != preLng and lat != preLat))
        preLat = lat
        preLng = lng
    time.sleep(3)
