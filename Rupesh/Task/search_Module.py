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

class Searchm(object):

    def add_url(self, url):
        self.url = url
        URL = self.url
        Urls.append(URL)
        return Urls

    def store(self):

        return
    
    def add_resent(self, res):
        self.res = res
        res = self.res
        resent.append(res)
        return resent

    def search(self, key):
        return
    
    def check_Made(self, Key):
        
        return