import os
import os.path
import requests
import collections
from collections import Counter
import re
from html.parser import HTMLParser
number_of_starttags = 0
number_of_endtags = 0
Urls = []
resent = []


class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global number_of_starttags
        number_of_starttags += 1

    def handle_endtag(self, tag):
        global number_of_endtags
        number_of_endtags += 1

class searchw(object):

    def storeF(self, file, data):

        self.file = file
        filename = self.file
        self.data = data
        data = self.data
        for root, dirs, files in os.walk('./'):
            if filename in files:
                print("Save")
            else :
                with open(filename, 'wb') as fobj:
                    fobj.write(data)
                f = str(filename)
                Urls.append(f)
                
    def EnterUrl(self):
        path = input("Enter a URL / or 'Exit' Command:") 
        page = requests.get(path)
        data = page.content
        name = path.split('/')[-2]
        store.storeF(name,data)
        print(Urls)

    def Search(self,word):
        self.word = word
        word = self.word
        count = 0
        resent.append(word)
        print("Entery")
        for filename in Urls:
            with open(filename, 'rt') as f:
                lines = f.readlines()
                for line in lines:
                    if re.search( word , line):
                        print(line.replace(word, '\033[44;33m{}\033[m'.format(word)))
                        count +=1
                        continue
            print("Avelebal words:",count)
            print("NAme of file",filename)
            continue
        print("Name of Text file",Urls)
        print("Resent Search:",list(dict.fromkeys(resent)))
        print("Top Search:",max(set(resent), key = resent.count))
    
    def rem(self):
        for i in Urls:
            os.remove(i)
      
    def Counthatml(self):
        for filename in Urls:
            with open(filename, 'rt') as f:
                for line in f:
                    parser = MyHTMLParser()
                    parser.feed(str(line))
            print("File Of",filename,"Starting Tag = ",number_of_starttags,",Ending Tag = ",number_of_endtags)

while True:
    try:
        
        print('/' * 100)
        print("1:Enter a Url \n2:Search \n3:Count Tage \n4:Exit")
        task = input("Enter a Task No:")
        store = searchw()
        parc = MyHTMLParser()
        
        if task == '1':
            store.EnterUrl()
            
            
        elif task == '2':
            store.Search(input("Enter a Search Word:"))
            
            
        elif task == '3':
            store.Counthatml()
            
        elif task == '4':
            store.rem()
            break
    except:
        store.rem()
        break
