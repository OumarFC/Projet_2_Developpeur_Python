"""
 Cette focntion doit extraire les liens  de chaque categories
 elle est appellée dans la fonction fonc_category_page pour lui transmettre les liens des
 categories
"""
import requests
from bs4 import BeautifulSoup

def fonc_category_link(urls) :
    links=[]
    response = requests.get(urls)
    if response.ok:
        soup=BeautifulSoup(response.content, 'html.parser')
        divs=soup.find('ul', class_='nav-list')
        for h in divs.findAll('li'):
            a = h.find('a')
            link= a['href']
            links.append('https://books.toscrape.com/' + link.strip('..'))
        return(links)

#recette
#urls="https://books.toscrape.com/"
#print(fonc_category_link(urls))
