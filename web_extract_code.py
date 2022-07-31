import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# recuperer l'url des pages categories
# recuperer l'url de toutes les pages produits  de chaque categorie
# recuperer les informations ci-dessous à partir de l'url des pages produits
#
#product_page_url
#universal_ product_code (upc)
#title
#price_including_tax
#price_excluding_tax
#number_available
#product_description
#category
#review_rating
#image_url

# Créer un dataframe qui a ces informations comme nom de colonne
# exporter dans un fichier csv.
"""
urls="https://books.toscrape.com/"
reqs = requests.get(urls)
soup = BeautifulSoup(reqs.text, 'html.parser')
# opening a file in write mode
f = open("C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category_link.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = "https://books.toscrape.com/" + link.get('href')
    if data.find("category") != -1:
       f.write(data)
       f.write("\n")
f.close()
"""

"""
filename = "C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category_link.txt"

with open(filename) as file:
    for line in file:
        line=line.strip('\n')
        response = requests.get(line)
        soup = BeautifulSoup(response.text, 'html.parser')
        #links = [ link['href'] for link in soup.find_all('a', href=True)]
        #linka = ["https://books.toscrape.com/catalogue/" + lin1.strip('../..') for lin1 in links]
        print(soup)
"""

"""
linka = ["https://books.toscrape.com/catalogue/" + lin1.strip('../..') for lin1 in links]
linka1 = [lin1 for lin1 in linka if requests.get(lin1).status_code == 200 ]
print(linka1)
"""
       # response = requests.get(data)
       # soup = BeautifulSoup(response.text, 'html.parser')
       # links = [link['href'] for link in soup.find_all('a', href=True)]
       # linka = [lin1.strip('../..') for lin1 in links]
       # linka2 = ["https://books.toscrape.com/catalogue/" + lino for lino in linka]
       # for i in linka2:
       #     response = requests.get(i)
       #     if response.status_code == 200:
       #         sublik.append(i)
        #sublik1.extend(sublik)
       # print(sublik)

       # f.write(data)
       # f.write("\n")
#f.close()


"""
SubLink = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(SubLink)
soup = BeautifulSoup(response.text, 'html.parser')
links = [ link['href'] for link in soup.find_all('a', href=True)]
linka = [lin1.strip('../..') for lin1 in links]
linka2=["https://books.toscrape.com/catalogue/" + lino for lino in linka]

sublik=[]
for i in linka2:
    response = requests.get(i)
    if response.status_code == 200:
        sublik.append(i)
print(sublik)
"""


    #if response.status_code == 200:
     #   print('Web site exists')
    #else:
     #   print('Web site does not exist')


# root = 'https://books.toscrape.com'
# reqs = requests.get(root)

# soup = BeautifulSoup(reqs.text, 'html.parser')
# links = ['https://books.toscrape.com' + link['href'] for link in soup.find_all('a', href=True)]
# print(links)

# linka = [lin1.strip('../..') for lin1 in links]

# linka2=["https://books.toscrape.com/catalogue/" + lino for lino in linka]

# print(linka2)

#    box = soup.find('article', class_='main-article')
#    title = box.find('h1').get_text()
#    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

#    with open(f'{title}.txt', 'w') as file:
#        file.write(transcript)


#response = requests.get("http://books.toscrape.com/catalogue/reasons-to-stay-alive_959/index.html")
#webpage=response.content
#soup=BeautifulSoup(webpage,"html.parser")

#table = soup.find_all('table', class_="table table-striped")[0]
#article = soup.find_all('article', class_="product_page")[0]
#print(article)

#for row in table.find_all('tr'):
    #print(row)


#for row in table.find_all('tr'):
#    #print(row)
#    columns = row.find_all('th')
#    zone = columns[0].text.strip()
#    print(zone)

# ===================================Debut extraction code ALL Page =======================================
"""
links = []

for i in range(51):
    urls="http://books.toscrape.com/catalogue/category/books_1/page-" + str(i) + ".html"
    response = requests.get(urls)
    if response.ok:
        #print('page:' + str(i))
        soup=BeautifulSoup(response.text, 'html.parser')
        divs=soup.findAll('h3')
        for li in divs:
            a=li.find('a')
            link=a['href']
            links.append('https://books.toscrape.com/catalogue/' + link.strip('../..'))
        print(len(links))
"""

"""
fileLink="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\all_category_link.txt"
with open(fileLink,'w') as file:
    for link in links:
        link=link.strip('../..')
        file.write(link + '\n')        
"""
"""
fileLink="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\all_category_link.txt"
fileout="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\all_category_link.csv"
data=[]
with open(fileLink,'r') as file:
    with open(fileout, 'w') as out:
        out.write('product_code,category,price_including_tax,price_excluding_tax \n')
        for row in file:
            url=row.strip()
            reqs = requests.get(url)
            if reqs.ok:
                soup = BeautifulSoup(reqs.text, 'html.parser')
                price = soup.find_all('td')
                tit=[]
                tit = [k.text for k in price ]
                product_code=tit[0]
                print(product_code)
                category=tit[1]
                print(category)
                price_including_tax=tit[2]
                price_excluding_tax=tit[3]
                out.write(product_code + ',' + category + ',' + price_including_tax + ',' + price_excluding_tax + '\n')
                print(product_code + ',' + category + ',' + price_including_tax + ',' + price_excluding_tax + '\n')

#product_page_url
#universal_ product_code (upc)
#title
#price_including_tax
#price_excluding_tax
#number_available
#product_description
#category
#review_rating
#image_url

"""
# ========================== FIN EXTRACTION ALL PAGE ==============================================================

# ========================== DEBUT EXTRACTION CATEGORY==============================================================
"""
links=[]
urls="https://books.toscrape.com/catalogue/category/books_1/index.html"
response = requests.get(urls)
if response.ok:
    #print('page:' + str(i))
    soup=BeautifulSoup(response.content, 'html.parser')
    divs=soup.find('ul', class_='nav-list')
    for h in divs.findAll('li'):
        a = h.find('a')
        link= a['href']
        links.append('https://books.toscrape.com/catalogue/category' + link.strip('..'))
        print(links)

    fileLink = "C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category_link.txt"
    with open(fileLink, 'w') as file:
        for link in links:
            file.write(link + '\n')
"""
#=========== FIN EXTRACTION CATHEGORIE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#fileLink="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category_link.txt"
fileout="C:\\Users\\fodex\\OneDrive\\dev_app_python\\OpenclassroomsProject\\category_link3.txt"
url="https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
links = []
#with open(fileLink,'r') as file:
with open(fileout, 'w') as out:
    #out.write('category,Lien' '\n')
    #for row in file:
    url=url.strip()
    reqs = requests.get(url)
    if reqs.ok:
        soup = BeautifulSoup(reqs.content, 'html.parser')
        divs = soup.find_all('div',class_='image_container')
        #head = soup.find_all('div', class_='page-header action')
        #images = soup.find('img', {'src': re.compile('.jpg')})
        #img = images['src']
        category= soup.find('h1').text
        #Titre= soup.find('h3').text
        for h in divs:
            a = h.find('a')
            link = a['href']
            links.append(category + ',' + 'https://books.toscrape.com/catalogue/' + link.strip('../') )
            print(links)
            with open(fileout, 'w') as file:
                for link1 in links:
                    file.write(link1 + '\n')

               # divs = soup.find_all('article', class_='product_pod').find('h3').find('a')
               # divs = soup.find_all('article', class_='product_pod')
                # category = soup.find('div', class_='page-header action').find('h1').text
                #category = soup.find('div', class_='page-header action').find('h1').text
                #images = soup.find('img', {'src': re.compile('.jpg')})
                #lien=divs['href']
                #titre=divs['title']
                #img=images['src']
                #print('category= ' + category + ' '+ 'lien= ' + lien + ' ' + 'titre= ' + titre + ' ' + 'image= ' + img )

               # out.write(product_code + ',' + category + ',' + price_including_tax + ',' + price_excluding_tax + '\n')



