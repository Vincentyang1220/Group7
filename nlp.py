from ckiptagger import data_utils, construct_dictionary, WS, POS, NER


def nlp(sent):

    ws = WS("./data")
    pos = POS("./data")
    ner = NER("./data")


    sentence_list=[]
    sentence_list.append(sent)

    word_list = ws(sentence_list)

    pos_list = pos(word_list)

    entity_list = ner(word_list,pos_list)

    return_list=[]



    flat_list=[]
    for word_sent in word_list:
        for word in word_sent:           
            flat_list.append(word)      
    word_list=[]
    word_list=flat_list

    flat_list=[]
    for pos_sent in pos_list:
        for pos in pos_sent:           
            flat_list.append(pos)             
            
    pos_list=flat_list

    words_and_pos=dict(zip(word_list,pos_list))

    noun_list=[]


    for key,value in words_and_pos.items():
        arrow_indicate=""

        if "Na" in value:
            noun_list.append(key)
    
        elif "Nb" in value:
            noun_list.append(key)
    
        elif "Ncd" in value:

            arrow_indicate="plus"    

            if "上"  in key:
            
                arrow_indicate="plus"
            elif "下" in key:
                arrow_indicate="down"

            elif "前" in key:
                arrow_indicate="left"

            elif "後" or "中" or "內" or "裡" or "外" or "邊" in key:
                arrow_indicate="right"

            print(arrow_indicate+" "+str(len(noun_list)))

            noun_list.append(arrow_indicate)
            if len(noun_list)>=2:
                temp=""
                temp=noun_list[len(noun_list)-2]
                noun_list[len(noun_list)-2]=noun_list[len(noun_list)-1]
                noun_list[len(noun_list)-1]=temp
        
        elif "Nc" in value:
            noun_list.append(key)

        elif "VC" in value:
            if "起" in key:
                arrow_indicate="up"
                noun_list.append(arrow_indicate)       
            elif "下" in value:
                arrow_indicate="down"
                noun_list.append(arrow_indicate)

    return noun_list



