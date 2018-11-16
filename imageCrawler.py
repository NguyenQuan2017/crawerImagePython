import requests
import urllib.request
import os
import uuid
from bs4 import BeautifulSoup

def spider(max_pages):
   page = 1
   while page <= max_pages:
        url = 'https://truyenqq.com/truyen-tranh/dao-hai-tac-128-chap-3.html'
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
    forderName = '/home/quan/Pictures/Crawler/1'
    pathFileName = os.path.join(forderName)
    if not os.path.exists(pathFileName):
        os.makedirs(pathFileName)
    file_suffix = os.path.splitext(url)[1]
    filename = '{}{}{}{}'.format(pathFileName, os.sep, file_name, file_suffix)
    print( urllib.request.urlretrieve(url, filename=filename))

spider(1)