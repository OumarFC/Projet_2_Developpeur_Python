# fonction principale

import os
import fonc_category_page
import fonc_category_link
import fonc_nextpage_link
import fonc_InfosProduit
import fonc_imageExtract

siteUrl = 'https://books.toscrape.com/'
racine = "C:\\Users\\Itec Global Services\\OneDrive\\dev_app_python\\OpenclassroomsProject\\projet_2\\data\\"
tab=[]
tabA=[]
# 4- Traitement pour l'ensemble des categories

print (" - DEBUT - ")

print (" -Extraction des liens de chaque Categorie de produit -")

tab_category = fonc_category_link.fonc_category_link(siteUrl)


print ("- Extraction des pages et les pages suivantes pour chaque Categorie de proudit -")

for k in tab_category:
    base = fonc_nextpage_link.next_page(k)
    tab.append(base)
print(tab)


print("- Creation de la table de lien pour tous les produits du site --")

base = fonc_nextpage_link.next_page(tab_category[0])
for i in base:
    baseA = fonc_category_page.category_page(i)
    tabA.extend(baseA)

print("- Creation du fichiers csv et télechargement des photos  pour toutes les categories du site --")

if not os.path.exists(racine + "GlobalExtract"):
    os.makedirs(racine + "GlobalExtract")
fonc_InfosProduit.infos_produits(tabA, racine + "GlobalExtract" + "\\" + "infos_AllproduitsExtract.csv")
fonc_imageExtract.extract_image(tabA, racine + "GlobalExtract")

print (" - FIN - ")