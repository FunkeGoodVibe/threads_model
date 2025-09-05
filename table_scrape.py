###
from bs4 import BeautifulSoup
import requests
"""
This script scrapes the concordence word count table, from the artbible website
article: https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_get_text_method.htm
"""

url_list = []

def get_url(): 

    url = r"https://www.artbible.info/concordance/{0}.html"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #create the urls for every letter in the alphabet
    for item in alphabet: 
        url_list.append(url.format(item))


def scrape():

    r = requests.get(url_list[0])
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    #raw_strip = soup.find("div", {"id": "contentkol"})
    raw_strip = soup.find(attrs={'class':'concorde'})
    print(raw_strip)

    #get all the word url numeric reference links (for the word mapping dictionary)
    num_map_ref = []
    for link in soup.find_all('a'):
        num_map_ref.append(link.get('href'))


    #get the index of the last html element 
    #get the url for each populated url reference, referenced below 
    num_map_urls = []  
    end_val = len(num_map_ref) - 10 
    for i in range(27, end_val): 
        num_map_urls.append(num_map_ref[i]) #i.e. 110-1.html


    #get the table contents (i.e. OT, NT, .. total word count)
    word_map_table = []
    for row in soup.find_all('tr'):
        word_map_table.append(row.get_text()) #returns i.e. [azrikam 6 0 0 6]

    print(len(word_map_table))
    word_table = []
    for i in range(2,len(word_map_table)):  #for the first leible word in the table, to the last element
        word_table.append(word_ma
    p_table[i].split("\n"))  #i.e. returns ['', 'azrikam', '6', '0', '0', '6', ''] ... 

    

    

if __name__ == "__main__":

    get_url()
    scrape()