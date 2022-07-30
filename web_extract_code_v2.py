import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#1- ===========================Extraire les informations d'un produits d'une categorie ================
links=[]
fileout="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category1_prod1.csv"
urls="http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
with open(fileout, 'w', encoding="utf-8") as out:
    out.write('product_page_url;universal_product_code;titre;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url \n')
    urls=urls.strip()
    reqs = requests.get(urls)
    if reqs.ok:
        soup = BeautifulSoup(reqs.text, 'html.parser')
        img = soup.find('img', {'src': re.compile('.jpg')})
        categ = soup.find('ul', class_='breadcrumb')
        image_url ='https://books.toscrape.com/'+img['src'].strip('../').strip('\n')
        titre = soup.find('h1').text
        info = soup.find_all('td')
        infop = [infop.text for infop in info]
        catego = [h.text.strip('\n') for h in categ.findAll('li')]
        pageurl = [h for h in categ.findAll('a')]
        universal_product_code=infop[0]
        price_including_tax=infop[2].strip('Â')
        price_excluding_tax=infop[3].strip('Â')
        number_available=infop[5]
        review_rating=infop[6]
        category=catego[2]
        #titre=catego[3]
        product_page_url='https://books.toscrape.com/catalogue' + pageurl[2]['href'].strip('..')
        product_description = soup.find("div", class_="sub-header").find_next_sibling().get_text()
        out.write(product_page_url+ ';'+ universal_product_code+ ';' + titre + ';' + price_including_tax + ';'+price_excluding_tax+ ';'+ number_available+ ';'+ product_description+ ';'+ category + ';'+ review_rating+';'+ image_url+ '\n')
        #print(product_page_url + ' ;'+ universal_product_code+ ';' + titre + ';' + price_including_tax + ';'+price_excluding_tax+ ';'+ number_available+ ';'+ product_description+ ';'+ category + ';'+ review_rating+';'+ image_url+ '\n')
        #print(price_excluding_tax)
