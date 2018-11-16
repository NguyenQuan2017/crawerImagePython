import requests
import urllib.request
import os
import uuid
from bs4 import BeautifulSoup

def spider(url):
   page = 1
   while page <= 1:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.findAll('img',):
            href = link.get('src')
            if href == None:
                print('find nothing')
                break
            else:
                save_image(href)
        page += 1

def save_image(url):
    file_name = 'one-piece-' + str(uuid.uuid1())
    forderName = '/home/quan/Pictures/manga/onepice/1'
    pathFileName = os.path.join(forderName)
    if not os.path.exists(pathFileName):
        os.makedirs(pathFileName)
    file_suffix = os.path.splitext(url)[1]
    originalImage = file_suffix.split("?")[0]
    filename = '{}{}{}{}'.format(pathFileName, os.sep, file_name, originalImage)
    print( urllib.request.urlretrieve(url, filename=filename))


spider('https://truyenqq.com/truyen-tranh/dao-hai-tac-128-chap-1.html')