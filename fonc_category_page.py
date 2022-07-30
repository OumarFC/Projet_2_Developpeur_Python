import requests
from bs4 import BeautifulSoup

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
            links.append('https://books.toscrape.com/catalogue/' + link.strip('../') )
    return links

#recette
#url='http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#print(category_page(url))