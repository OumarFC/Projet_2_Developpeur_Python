
# 0 - Import des packages indispensable pour le traitement

import re
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request


# 1- Intialisation des variables

tab = []
tabAll=[]
siteUrl = 'https://books.toscrape.com/'
racine = "C:\\Users\\Itec Global Services\\OneDrive\\dev_app_python\\OpenclassroomsProject\\projet_2\\data2\\"

# 2- Definition des fonctions

def category_page(url):
    links = []
    url=url.strip()
    reqs = requests.get(url)
    if reqs.ok:
        soup = BeautifulSoup(reqs.content, 'html.parser')
        divs = soup.find_all('div',class_='image_container')
        for h in divs:
            a = h.find('a')
            link = a['href']
            links.append(siteUrl + 'catalogue' + '/' + link.strip('../') )
    return links


def category_link(urls) :
    links=[]
    response = requests.get(urls)
    if response.ok:
        soup=BeautifulSoup(response.content, 'html.parser')
        divs=soup.find('ul', class_='nav-list')
        for h in divs.findAll('li'):
            a = h.find('a')
            link= a['href']
            links.append(siteUrl + link.strip('..'))
        return(links)


def next_page(link):
    nexpage = []
    nexpage.insert(0, link)
    response = requests.get(link)
    if response.ok:
        try:
            soup=BeautifulSoup(response.content, 'html.parser')
            last_page = soup.find('ul', class_='pager').find('li', {'class': 'current'}).text.strip().split()[3]
            for i in  range(2,int(last_page)+1):
                base_link = link.split('index')[0]
                nexpage.append(base_link + 'page-' + str(i) + '.html')

        except:

            print("Next page is don't exist for this page")

        return nexpage


def infos_produits(table, fileOut):
    with open(fileOut, mode='w', encoding='utf-8-sig') as csv_file:
        csv_file.write(
            "product_page_url | universal_product_code | titre | price_including_tax | price_excluding_tax | "
            "number_available | product_description | category | review_rating | image_url" + '\n')
        for urls in table:
            urls = urls.strip()
            reqs = requests.get(urls)
            if reqs.ok:
                soup = BeautifulSoup(reqs.content, 'html.parser')
                img = soup.find('img', {'src': re.compile('.jpg')})
                categ = soup.find('ul', class_='breadcrumb')
                rating = soup.find('div', class_='col-sm-6 product_main').find('p', {'class': 'star-rating'})
                review_rating = rating['class'][1]
                image_url = siteUrl + img['src'].strip('../')
                titre = soup.find('h1').text
                info = soup.find_all('td')
                infop = [infop.text for infop in info]
                catego = [h.text.strip('\n') for h in categ.findAll('li')]
                universal_product_code = infop[0]
                price_including_tax = str(infop[2])
                price_excluding_tax = str(infop[3])
                number_available = infop[5].split('(')[1].split()[0]
                category = catego[2]
                if soup.find("div", {"id": "product_description"}):
                    product_desc = soup.find("div", class_="sub-header").find_next_sibling().text.replace(";", ",")
                else:
                    product_desc = " Not found Description for this Product"
                product_description = str(product_desc)
                csv_file.write(
                    urls + '|' + universal_product_code + '|' + titre + '|' + price_including_tax +
                    '|' + price_excluding_tax + '|' + number_available +
                    '|' + product_description +
                    '|' + category + '|' + review_rating + '|' + image_url + '\n')


def extract_image(table, repOut):
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

# 3- Traitement par categorie de prodduit


print("- Extraction des liens de chaque Categorie de produit --")

tab_category = category_link(siteUrl)

print ("- Extraction des pages et les pages suivantes pour chaque Categorie de prouduit --")


for k in tab_category[1:]:
    base = next_page(k)
    tab.append(base)

print("- Creation des fichiers csv et télechargement des photos de chaque categorie -")

for i in tab:
    if not os.path.exists(racine + "Category" + "_" + str(tab.index(i)) ):
        os.makedirs(racine + "Category" + "_" + str(tab.index(i)))
    base = [element for list in [category_page(j) for j in i] for element in list]
    infos_produits(base, racine + "Category" + "_" + str(tab.index(i)) + "\\" + "infos_produits.csv")
    extract_image(base, racine + "Category" + "_" + str(tab.index(i)))

# 4- Traitement pour l'ensemble des categories

print("- Creation de la table de lien pour tous les produits du site---")

tabA=[]
base = next_page(tab_category[0])
for i in base:
    baseA = category_page(i)
    tabA.extend(baseA)

print("- Creation du fichiers csv et télechargement des photos  pour toutes les categories du site --")

if not os.path.exists(racine + "GlobalExtract"):
    os.makedirs(racine + "GlobalExtract")
infos_produits(tabA, racine + "GlobalExtract" + "\\" + "infos_AllproduitsExtract.csv")
extract_image(tabA, racine + "GlobalExtract")

print ("-Fin des traitement ! --")

