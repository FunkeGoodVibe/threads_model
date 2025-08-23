####
#
####
#check out fast-api
from bs4 import BeautifulSoup
import requests
import random

dict_word_list = {

    "amaze": 1240,
    "amazement":3333
    
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

    my_dict = list(dict_word_list.keys())

    for word in my_dict:

        # word=r"\s{0}\s".format(word) #word separated by spaces
        # x = re.search(word, sentence)
        #if x.group() in sentence: 
        
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

            #determine which url to use 
            url = url_base_all 

        return url


def get_verse(url):

    """
    1) 
    2) 
    3) 
    """

    r = requests.get(url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    #raw_strip = soup.find("div", {"id": "contentkol"})
    raw_strip = soup.find(attrs={'id':'contentkol'})
    #print(raw_strip)

    p_el = soup.find_all('p')
    el_list = []
    for element in p_el:
        el_list.append(element)

    print(el_list[1])



if __name__ == "__main__":

    while True: 
        url = speak()
        get_verse(url)
    

