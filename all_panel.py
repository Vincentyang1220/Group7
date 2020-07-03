import singe_panel
import threading
import time
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import composit_image

data=["把鍋子放在桌上","將水倒入鍋子中","用刀將雞肉切成丁","將雞肉倒入鍋中","用火煮至湯沸騰"]
title_text="我是測試食譜"
return_list=[]
thread_list=[]

for step_sent in data:
    step_thread=threading.Thread(target=singe_panel.single_panel,args=(step_sent,return_list))
    thread_list.append(step_thread)

for step_thread in thread_list:
    step_thread.start()

    step_thread.join()
    

print(return_list)

# composite_image_path = composit_image.composit_step(return_list)

# step_panel = Image.new('RGB', (1185,1123), (255, 255, 255))
# step_image = Image.open(composite_image_path)

# step_border = ImageDraw.Draw(step_panel)

# step_border.line([(0,135.5), (1185,135.5)], fill=(117, 0, 0), width=5)

# # x-top
# step_border.line([(0, 2.5), (1185, 2.5)], fill=(117, 0, 0), width=5)

# # x-bottom
# step_border.line([(0,1120.5), (1185,1120.5)], fill=(117, 0, 0), width=5)

# # y-left
# step_border.line([(2.5, 0), (2.5,1123)], fill=(117, 0, 0), width=5)

# # y-right
# step_border.line([(1182.5, 0), (1182.5,1123)], fill=(117, 0, 0), width=5)

# font = ImageFont.truetype("microblack.ttf",72)
# step_text = ImageDraw.Draw(step_panel)
# step_text.text((420,5),title_text, font=font, fill=(0, 0, 0), align="center")


# step_panel.paste(step_image, (2, 138))
# step_panel.show()
# step_panel.save("./finished_image/merge.jpg")