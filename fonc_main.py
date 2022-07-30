# fonction principale

import os
import fonc_category_page
import fonc_category_link
import fonc_nextpage_link
import fonc_InfosProduit
import fonc_imageExtract

# 1- ===========================Extraire les informations d'un produits d'une categorie ================

siteUrl = 'https://books.toscrape.com/'
racine = "C:\\Users\\Itec Global Services\\OneDrive\\dev_app_python\\OpenclassroomsProject\\projet_2\\data\\"

#lancement des traitements

tab_category = fonc_category_link.fonc_category_link(siteUrl)

tab = []
for k in tab_category[1:]:
    base = fonc_nextpage_link.next_page(k)
    tab.append(base)
print(tab)

for i in tab:
    if not os.path.exists(racine + "Category" + "_" + str(tab.index(i)) ):
        os.makedirs(racine + "Category" + "_" + str(tab.index(i)))
    base = [element for list in [fonc_category_page.category_page(j) for j in i] for element in list]
    fonc_InfosProduit.infos_produits(base, racine + "Category" + "_" + str(tab.index(i)) + "\\" + "infos_produits.csv")
   # fonc_imageExtract.extract_image(base, racine + "Category" + "_" + str(tab.index(i)))

