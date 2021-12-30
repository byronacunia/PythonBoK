# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

position = 18
times = 7
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Khajusta.html'
list_nomes = re.findall("[a-zA-Z]+", url)
nome = list_nomes[-2]
for i in range(times):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    count = 1
    tags = soup('a')
    for tag in tags:
        if count == position:
            list_nomes = re.findall("[a-zA-Z]+", tag.get('href', None))
            nome = nome +" "+ list_nomes[-2]
            count += 1
            url = tag.get('href', None)
        else:
            count += 1
print(nome)
