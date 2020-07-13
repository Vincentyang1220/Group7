import translator
import nlp
import composit_image
#import getimage
import getimage_bing

prime_sent=input("input a sentence: ")

nlp_list=nlp.nlp(prime_sent)

print(nlp_list)

noun_list=[]

for key,value in nlp_list[0].items():
 
    if "Na" in value:
        noun_list.append(key)
    
    elif "Nb" in value:
        noun_list.append(key)
    
    elif "Nc" in value:
        noun_list.append(key)
    

print(noun_list)


trans_list=translator.trans(noun_list)

print(trans_list)

image_path_list=[]
for word in trans_list:
    path_dict=getimage_bing.crawler_bing(word)

    for key,value in path_dict[0].items():
        for path in value:
            print(path)
            image_path_list.append(path)
    
print(image_path_list)

composite_image_path=composit_image.composit(image_path_list)

