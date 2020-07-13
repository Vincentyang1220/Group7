from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
def composit_icon(path_list):
    image_count=len(path_list)

    if(image_count<=2):
        merge_width=128*image_count
    else:
        merge_width=128*3
    
    merge_height=128*(int(image_count/3)+1)

    toImage = Image.new('RGB', (merge_width,merge_height),(255,255,255))

    img_dict={}
    for path in path_list:

        if ".svg" in path:
            after_path=os.path.dirname(path)+"\\after.png"

            if os.path.exists(after_path)==False:       
                drawing = svg2rlg(path)
                renderPM.drawToFile(drawing,after_path,fmt='PNG')
            path_index=path_list.index(path)
            path_list[path_index]=after_path
            path=after_path

        img=Image.open(path)

        img = img.convert("RGBA")   

        ##if img.mode in ('RGBA', 'LA'):
        background = Image.new("RGBA", img.size,(255,255,255))
        background.paste(img,mask=img.convert('RGBA').getchannel('A')) 
        background.convert('RGB')
        img = background

        ##new_img=img.resize((128, 128),Image.BILINEAR)

        path_index=path_list.index(path)
        img_dict[path_index]=img
    
    for key,value in img_dict.items():

        
        index=int(key)

        if index==0:
            x=0
            y=0
        elif index%3==0 and index!=0:
            x=0
            y=128*(int(index/3))
        else:
            x=128*(index%3)
            y=128*(int(index/3))
        if "FB"  in path_list[index]: 
            new_img=value.resize((128,128),Image.BILINEAR)
        else:
            new_img=value.resize((128, 128),Image.BILINEAR)

        toImage.paste(new_img,(x,y))

    
    #函式描述：toImage:背景圖片,paste()函式四個變數分別為：起始橫軸座標，起始縱軸座標，橫軸結束座標，縱軸結束座標；
    

    theTime = datetime.datetime.now()
    str_time=str(theTime).replace(".","_")
    str_time=str_time.replace(":","_")

    
    folder_path="./composite_image/"+str_time

    if(os.path.exists(folder_path)== False):
        os.makedirs(folder_path)

    image_path=folder_path+"/merge.jpg"
    toImage.save(image_path)
    return image_path

def composit_step(path_list):
    image_count=len(path_list)

    if(image_count<=2):
        merge_width=395*image_count
    else:
        merge_width=395*3
    
    merge_height=495*(int(image_count/3)+1)

    toImage = Image.new('RGB',(merge_width,merge_height),(255,255,255))

    img_dict={}
    
    for path in path_list:
        img=Image.open(path)

        path_index=path_list.index(path)
        img_dict[path_index]=img
    
    for key,value in img_dict.items():

        
        index=int(key)

        if index==0:
            x=0
            y=0
        elif index%3==0 and index!=0:
            x=0
            y=495*(int(index/3))
        else:
            x=395*(index%3)
            y=495*(int(index/3))

        toImage.paste(value,(x,y))
    
    
    #函式描述：toImage:背景圖片,paste()函式四個變數分別為：起始橫軸座標，起始縱軸座標，橫軸結束座標，縱軸結束座標；
    

    theTime = datetime.datetime.now()
    str_time=str(theTime).replace(".","_")
    str_time=str_time.replace(":","_")

    
    folder_path="./composite_image/"+str_time

    if(os.path.exists(folder_path)== False):
        os.makedirs(folder_path)

    image_path=folder_path+"/merge.jpg"
    toImage.save(image_path)

    return image_path
