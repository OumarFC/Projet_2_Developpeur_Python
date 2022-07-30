"""
 Cette focntion extrait les informations des produits de la page produit
 elle appelle la fonction fonc_category_page pour lui transmettre les liens des
 produits par categorie

"""
import re
import requests
from bs4 import BeautifulSoup

def infos_produits(table, fileOut):
    siteUrl='https://books.toscrape.com/'
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
                print(product_desc)
                product_description = str(product_desc)
                csv_file.write(
                    urls + '|' + universal_product_code + '|' + titre + '|' + price_including_tax +
                    '|' + price_excluding_tax + '|' + number_available +
                    '|' + product_description +
                    '|' + category + '|' + review_rating + '|' + image_url + '\n')

#Recette