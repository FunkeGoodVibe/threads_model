###
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
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


def scrape(i):

    r = requests.get(url_list[i])
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    #raw_strip = soup.find("div", {"id": "contentkol"})
    # raw_strip = soup.find(attrs={'class':'concorde'})
    # print(raw_strip)

    #1. get all the word url numeric reference links (for the word mapping dictionary)
    num_map_ref = []
    for link in soup.find_all('a'):
        num_map_ref.append(link.get('href'))

    #regex = re.compile(r'^http[s]?:\/?\/?([^:\/\s]+)/')
    regex = re.compile(r'.*-[12].html$')
    urls_wanted_list = [i for i in num_map_ref if regex.match(i)]

    #2. get the index of the last html element 
    #get the url for each populated url reference, referenced below 
    num_map_urls = []  
    end_val = len(urls_wanted_list) - 10 
    for i in range(0, end_val): 
        num_map_urls.append(num_map_ref[i]) #i.e. 110-1.html 

    #3. get the table contents (i.e. OT, NT, .. total word count)
    word_map_table = []
    for row in soup.find_all('tr'):
        word_map_table.append(row.get_text()) #returns i.e. [azrikam 6 0 0 6]

    word_table = []
    for i in range(1,len(word_map_table)):  #for the first leible word in the table, to the last element
        word_table.append(word_map_table[i].split("\n"))  #i.e. returns ['', 'azrikam', '6', '0', '0', '6', ''] ... 
    

    #4. list comprehension strip/clean table, taking index 1:5 [azrikam', '6', '0']
    word_table_clean = [row[1:-3] for row in word_table]
    number_table_clean = [row[2:-3] for row in word_table]
   
    df = pd.DataFrame(word_table_clean, columns=['word', 'ot_count', 'nt_count'])

    # df_ot = df["ot_count"][df["ot_count"]!="0"]
    # df_nt = df["nt_count"][df["nt_count"]!="0"]

    # print("{0} + {1} + {2} = {3}".format(len(df_ot), len(df_nt), len(df_ap), len(df_ot)+len(df_nt)+len(df_ap)))
    # print(len(num_map_urls))

    #5. get ot,nt numbers only for url referencing ['6', '0']
    flatten_num_table_test = [x for list in number_table_clean for x in list] 
    non_zero_num_table_test = [x for x in flatten_num_table_test if x != "0"]

    # print(len(non_zero_num_table_test))
    # print(len(urls_wanted_list))

    for i in range(0,len(non_zero_num_table_test)):
        print("{0}:{1}".format(non_zero_num_table_test[i],urls_wanted_list[i]))
    

if __name__ == "__main__":

    get_url()
    for i in range(len(url_list)):
        print(url_list[i])
        scrape(i)
        print("\n")
    #scrape(22)