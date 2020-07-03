import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import json
import datetime

def getimage(key):

    url="https://www.flaticon.com/search?word="+key
    photo_limit=3


    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36","upgrade-insecure-requests":"1"}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content,"html.parser")


    items = soup.find_all("img",attrs={"class":"lzy"})

    theTime = datetime.datetime.now()
    str_time=str(theTime).replace(".","_")
    str_time=str_time.replace(":","_")

    print(str_time)

    folder_path="./image/"+str_time+"/"+key+"/"

    if(os.path.exists(folder_path)== False):
        os.makedirs(folder_path)

    img_arr=[]

    for index , item in enumerate(items):
        if(item and index < photo_limit):
            html = requests.get(item.get("data-src"))
            img_name = folder_path + str(index+1)+".png"
            img_arr.append(img_name)

            print("finish",index+1)
        else:
            break

        with open(img_name,"wb") as file:
            file.write(html.content)
            file.flush()
        file.close()

    return  img_arr[0]
