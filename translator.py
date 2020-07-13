from googletrans import Translator


def trans(word_list):
    translator=Translator();
    after_tran_list=[]
    for word in word_list:
        after_tran_word=translator.translate(word).text
        after_tran_list.append(after_tran_word)

    return after_tran_list