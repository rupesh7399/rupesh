import os
import os.path
import requests
import collections
from collections import Counter
import re
from html.parser import HTMLParser
number_of_starttags = 0
number_of_endtags = 0

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global number_of_starttags
        number_of_starttags += 1

    def handle_endtag(self, tag):
        global number_of_endtags
        number_of_endtags += 1
    
    def count_char(self):
        str1 = str(page.content)
        char = len(str1) - str1.count(' ')
        print("Total No of Char are:",char)
    
    def searchw(self, word):
        self.word =  word
        key = self.word
        str1 = str(page.content)
        try:
            print(str1.find(key))
        except:
            print("Not Avelebal")
        
        
         

    def count_repeat(self, file):
        self.file = file
        filename = self.file
        words = re.findall('\w+', open(filename).read().lower())
        print(Counter(words).most_common())

URL = input("Enter a URL:")
search = input("Enter a Searching word:")
page = requests.get(URL)

filename = URL.split('/')[-2]



def printT():
    parser = MyHTMLParser()
    parser.feed(str(page.content))
    parser.count_repeat(filename)
    parser.count_char()
    
    print("Total html Tag is ",number_of_starttags+number_of_endtags)
    print("Startin html tage:" , number_of_starttags )
    print("Ending Html Tag is:" ,  number_of_endtags)
    


def count_line(name):
    count = 0
    num_words = 0
    
    with open(name , 'rt') as fobj:
        
        for line in fobj:
            count += 1
            words = line.split()
            num_words += len(words)
    
    
    print("Total number of lines is:", count)
    print("Total number of words is:" , num_words)



for root, dirs, files in os.walk('./'):
        if filename in files:
    
           printT()
           count_line(filename)
           
        else:
            req = requests.get(URL)
            with open(filename, 'wb') as fobj:
                fobj.write(req.content)
            printT()
            count_line(filename)
parc = MyHTMLParser()
parc.searchw(search)