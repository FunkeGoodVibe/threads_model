####
#
####
#check out fast-api
from bs4 import BeautifulSoup
import requests
import random
import re

dict_word_list = {

    "amaze": 1240,
    "amazement":3590
    
}

#0=first character; 1=index; 2=nt/ot
#"https://www.artbible.info/concordance/a/1240-2.html"

def speak(): 

    """
    0) stores the concordence url for new/old testament (and randomiser)
    1) takes input from the user
    2) construct the concordence url, for either the new/old testament using randomiser
    """

    url_base_ot = r"https://www.artbible.info/concordance/{0}/{1}-1.html"
    url_base_nt = r"https://www.artbible.info/concordance/{0}/{1}-2.html"
    url_base_all = r"https://www.artbible.info/concordance/{0}/{1}-{2}.html"

    sentence = input("Say something: ")
    sentence = sentence.lower()
    sentence_list = sentence.split(" ") #split each word 

    my_dict = list(dict_word_list.keys()) #.values , #.items()- tuple

    print(sentence_list)
    if len(sentence_list) >= 0:

        for word in sentence_list: 

            print(word)
            
            if word not in my_dict: 
                pass

            else: 
            
                print("found", word)
                    
                #get the index of the 
                index = dict_word_list[word]

                #generate a random number 1/2 for old and new testament
                random_int = random.randint(1,2)

                #construct the concordence urls 
                url_base_ot = url_base_ot.format(word[0], index)
                url_base_nt = url_base_nt.format(word[0], index)
                url_base_all = url_base_all.format(word[0], index, random_int)

                #determine which url to use 
                #url = url_base_all 
                url = url_base_nt 

                return url
    

def get_verse(url):

    """
    1) 
    2) 
    3) 
    """

    related_verses = []
    r = requests.get(url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    #raw_strip = soup.find("div", {"id": "contentkol"})
    raw_strip = soup.find(attrs={'id':'contentkol'})
    #print(raw_strip)

    p_el = soup.find_all('p')
    # print(p_el)

    el_list = []
    for element in p_el:
        element = element.get_text() #remove all the tags
        el_list.append(element)

    #print(el_list[1])
    num_verse_full_string = str(el_list[1])
    x = re.search(r"\d+", num_verse_full_string)
    verse_count = int(x.group())


    for i in range(2,(2+verse_count)):
        related_verses.append(el_list[i])
        print(el_list[i], "\n\n")

    for verse in related_verses:
        #strip_book_chapter = re.search(r".+:\d+$", verse)
        strip_book_chapter = re.search(r".*:\d*", verse)
        print(strip_book_chapter)
        #current_reading = verse.replace(strip_book_chapter,"")

        #print(current_reading)
        #print("\n\n")
    

if __name__ == "__main__":

    while True: 
        url = speak()
        
        if url != None: 
            scrape_verses = get_verse(url)
            #select_random_verse(scrape_verses)