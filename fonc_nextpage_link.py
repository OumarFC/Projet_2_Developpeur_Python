"""
Cette fonction recoit en parametre l'url de la page d'acceuil d'une category d'article
puis retourne une liste contenant toutes les pages suivantes de la même cartegorie.

"""
from bs4 import BeautifulSoup
import requests

def next_page(link):
    NexPage = []
    NexPage.insert(0, link)
    response = requests.get(link)
    if response.ok:
        try:
            soup=BeautifulSoup(response.content, 'html.parser')
            last_page = soup.find('ul', class_='pager').find('li', {'class': 'current'}).text.strip().split()[3]
            for i in  range(2,int(last_page)+1):
                base_link = link.split('index')[0]
                NexPage.append(base_link + 'page-' + str(i) + '.html')
        except:
            print("Next page is don't exist")
        return NexPage

#recette
#url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
#base=next_page(url)
#print(base)


