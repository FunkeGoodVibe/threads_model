####
#
####
###
from bs4 import BeautifulSoup
import requests
import random

word_list = {

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

    my_dict = list(word_list.keys())

    for word in my_dict:
        if word in sentence: 
            print("found",word)


    