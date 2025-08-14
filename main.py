####
#
####
###
from bs4 import BeautifulSoup
import requests
import random

dict_word_list = {

    "amaze": 1240,
    "amazement":3333

}

#0=first character; 1=index; 2=nt/ot
#"https://www.artbible.info/concordance/a/1240-2.html"
url_base_ot = r"https://www.artbible.info/concordance/{0}/{1}-1.html"
url_base_nt = r"https://www.artbible.info/concordance/{0}/{1}-2.html"
url_base_all = r"https://www.artbible.info/concordance/{0}/{1}-{2}.html"

while True: 

    sentence = input("Say something: ")

    my_dict = list(dict_word_list.keys())

    for word in my_dict:
        if word in sentence: 

            #temp: print the word if found
            print("found", word)
            
            #get the index of the 
            index = dict_word_list[word]

            #generate a random number 1/2 for old and new testament
            random_int = random.randint(1,2)

            #construct the concordence urls 
            url_base_ot = url_base_ot.format(word[0], index)
            url_base_nt = url_base_nt.format(word[0], index)
            url_base_all = url_base_all.format(word[0], index, random_int)



    