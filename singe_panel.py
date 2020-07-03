import translator
import nlp
import composit_image
import getimage
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import os
import datetime
import firebase
import getimage_bing


def single_panel(prime_sent,return_list):


    noun_list = nlp.nlp(prime_sent)

    trans_list = translator.trans(noun_list)

    print(trans_list)

    image_path_list = []
    for word in trans_list:
        if word == "up" or word == "down" or word == "left" or word == "right" or word == "plus":
            path = firebase.get_arrow(word)
        else:
            path = firebase.get_icon(word)

            if(path == None):
                path = getimage_bing.crawler_bing(word)
                firebase.post_address(path, word)

        path=str(path).replace('C:\\Users\\a1235\\Desktop\\P\\', "./")
        path=str(path).replace('\\', "/")
        image_path_list.append(path)

    print(image_path_list)

    # composite_image_path = composit_image.composit_icon(image_path_list)

    # step_panel = Image.new('RGB', (394, 493), (255, 255, 255))
    
    # step_image = Image.open(composite_image_path)

    # step_border = ImageDraw.Draw(step_panel)
    # step_border.line([(0, 101), (389, 101)], fill=(117, 0, 0), width=5)


    # # set border

    # # x-top
    # step_border.line([(0, 2.5), (394, 2.5)], fill=(117, 0, 0), width=5)

    # # x-bottom
    # step_border.line([(0, 490.5), (394, 490.5)], fill=(117, 0, 0), width=5)

    # # y-left
    # step_border.line([(2.5, 0), (2.5, 493)], fill=(117, 0, 0), width=5)

    # # y-right
    # step_border.line([(391.5, 0), (391.5, 493)], fill=(117, 0, 0), width=5)



    # font = ImageFont.truetype("microblack.ttf", 35)
    # step_text = ImageDraw.Draw(step_panel)
    # step_text.text((5, 5), prime_sent, font=font, fill=(0, 0, 0), align="center")

    # step_panel.paste(step_image, (5, 104))


    # theTime = datetime.datetime.now()
    # str_time = str(theTime).replace(".", "_")
    # str_time = str_time.replace(":", "_")

    # folder_path = "./panel_image/"+str_time

    # if(os.path.exists(folder_path) == False):
    #     os.makedirs(folder_path)

    # image_path = folder_path+"/merge.jpg"
    # step_panel.save(image_path)

    return_list.append(image_path_list)
    
