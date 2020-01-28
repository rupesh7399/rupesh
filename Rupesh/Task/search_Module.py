import os
import os.path
import requests
import collections
from collections import Counter
import re
from html.parser import HTMLParser
number_of_starttags = 0
number_of_endtags = 0

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global number_of_starttags
        number_of_starttags += 1

    def handle_endtag(self, tag):
        global number_of_endtags
        number_of_endtags += 1



    
    