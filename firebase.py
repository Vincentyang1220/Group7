# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from PIL import Image
import matplotlib.pyplot as plt
import os
import requests

def get_arrow(word):
    
    if (not len(firebase_admin._apps)):     
        cred = credentials.Certificate('./serviceAccount.json')
        firebase_admin.initialize_app(cred)
    # 初始化firestore
    db = firestore.client()

    #---------------------------讀取資料---------------------------------
    #第一種 取得單一物件
    #取得集合內的單一物件

    ########################
    path = "箭頭圖庫/"+word####  主要更動位置
    ########################

    #建立文件的參考
    doc_ref = db.document(path)

    # 直接get取得資料，一旦路徑錯誤，將使得程式拋出錯誤
    try:
        doc = doc_ref.get()

        # to_dict()將文件轉為dictionary
        content = doc.to_dict()
        print("文件內容為：\n{}".format(content['Path']))

        # 下載圖片
        os.makedirs('./FB_image/', exist_ok=True)
        IMAGE_URL = content['Path']
        def request_download():
            r = requests.get(IMAGE_URL)
            with open('./FB_image/'+content['name']+'.png', 'wb') as f:
                f.write(r.content)
        request_download()

        arrow_path='./FB_image/'+content['name']+'.png'
       
        return arrow_path
    except:
        print("指定文件的路徑: {} 不存在\n請檢查路徑是否正確".format(path))

def get_icon(word):
    if (not len(firebase_admin._apps)):     
        cred = credentials.Certificate('./serviceAccount.json')
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    ########################
    try:
        path = "icon_collect/"+word####  主要更動位置
    except:
        icon_path=""
        return icon_path
    ########################

    #建立文件的參考
    doc_ref = db.document(path)

    # 直接get取得資料，一旦路徑錯誤，將使得程式拋出錯誤
    try:
        doc = doc_ref.get()

        # to_dict()將文件轉為dictionary
        content = doc.to_dict()
        print("文件內容為：\n{}".format(content['path']))

        icon_path=content['path']
    
        return icon_path
    except:
        print("指定文件的路徑: {} 不存在\n請檢查路徑是否正確".format(path))

def post_address(address,icon_name):
    if (not len(firebase_admin._apps)):     
        cred = credentials.Certificate('./serviceAccount.json')
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    ########################
    try:
        path = "icon_collect"####  主要更動位置
    except:
        icon_path=""
        print("has no db")
        return icon_path
    ########################
    doc_ref = db.collection(path).document(icon_name)
    doc = {
    'name': icon_name,
    'path': address
    }
    doc_ref.set(doc)





    # #第二種 取得複數物件
    # #建立集合的參考
    # path = "pyradise_students"
    # collection_ref = db.collection(path)

    # # 1.透過迴圈取出集合內的所有文件
    # docs = collection_ref.stream()
    # for doc in docs:
    #     print("文件內容：{}".format(doc.to_dict()))
    # print("↑迴圈取得所有文件")

    # # 2.或是可以透過限制式取得集合內的特定文件
    # docs = collection_ref.where('number','>', '1').stream()
    # for doc in docs:
    #     print("文件內容：{}".format(doc.to_dict()))
    # print("↑透過限制式取得特定文件")