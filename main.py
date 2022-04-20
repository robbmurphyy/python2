#Author: Robert Murphy
#Class: Python 307
#Assignment 7 webscraping
#date 4/20/22

import bs4
import requests
import re
import os

res = requests.get("https://www.blackhat.com/html/bh-media-archives/bh-archives-2000.html")
res.raise_for_status()
blackhat = bs4.BeautifulSoup(res.text, 'html.parser')
pres = blackhat.select('b')
pres2 = str(pres)
list_of_presenters = re.findall(r'(?m)^.*\">(.*)<', pres2)
list_of_presenters2 = str(list_of_presenters)
#list_of_presenters3 = re.findall(r'(.*)[</a>]|[</a>\\xa0]|[</a></b>]', list_of_presenters2)
print(list_of_presenters2)
os.system('cmd /c "echo" main.list_of_majors')




