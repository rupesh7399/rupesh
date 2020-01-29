import requests
import re
count = 0
word = input("Enter a search:")
with open('wiki', 'rt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search( word , line):
            print(line.replace(word, '\033[44;33m{}\033[m'.format(word)))
            count +=1
            continue
    print(count)
    print('wiki')