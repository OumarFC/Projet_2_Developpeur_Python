"""
Fonction d'extraction des images de chaque categorie de pages

"""
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib
import re
import os

def extract_image(table, repOut):
    siteUrl = 'https://books.toscrape.com/'
    for urls in table:
        urls = urls.strip()
        reqs = requests.get(urls)
        if reqs.ok:
            soup = BeautifulSoup(reqs.content, 'html.parser')
            img = soup.find('img', {'src': re.compile('.jpg')})
            image_url = siteUrl + img['src'].strip('../')
            a = urlparse(image_url)
            ImgName = os.path.basename(a.path)
            urllib.request.urlretrieve(image_url, repOut + "\\" + ImgName)

#recette
         