import cv2
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
cascadePath = "haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(cascadePath)

def downloadimage(url):
    path = "dataset/"
    for ig in os.listdir(path):
        os.remove(os.path.join(path, ig))
        
    response =requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    image = soup.find_all("img")
    
    for index ,img in enumerate(image):
        image_url = img["src"]
        nameimg = image_url.split("/")[-1]
        name , ext = nameimg.split(".")
        print(name)
        print(ext)
        picture = Image.open(requests.get(url+image_url,stream = True).raw).convert("RGB")
        cv_img = np.array(picture)
        namesave = name +"-"+ str(index) + "." + ext
        cv_img = cv_img[:,:,::-1].copy()
        
        faces = facecascade.detectMultiScale(cv_img, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.imwrite("dataset/" + namesave, cv_img[y:y+h,x:x+w])
            
    print("update complete")

import numpy as np
url = "https://tai-anh.herokuapp.com/"
downloadimage(url)
