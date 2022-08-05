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

print ("--------------Extraction des liens de chaque Categorie de produit -------------")
tab_category = fonc_category_link.fonc_category_link(siteUrl)
print ("-------------Fin d'extraction de lien --------------------------------------")

print ("--------Extraction des pages et les pages suivantes pour chaque Categorie de proudit -------")
tab = []
for k in tab_category:
    base = fonc_nextpage_link.next_page(k)
    tab.append(base)
print(tab)
print("---------------- Fin d'extractions des pages de chaque Categorie ----------------------------")

tabAll=[]
print ("----------------Creation des fichiers csv et télechargement des photos de chaque categorie ---")
for i in tab[0]:
    if not os.path.exists(racine + "GlobalExtract" ):
        os.makedirs(racine + "GlobalExtract" )
    base=fonc_category_page.category_page(i)
    tabAll.extend(base)
print(tabAll)
print ("------------FIN Creation des fichiers csv------------------------------------------------------")

print ("----------------Creation des fichiers csv et télechargement des photos  pour tout le site ------")

fonc_InfosProduit.infos_produits(tabAll, racine + "GlobalExtract" + "\\" + "infos_AllproduitsExtract.csv")
#fonc_imageExtract.extract_image(tabAll, racine + "Category" + "_" + str(tab.index(i)))
#print ("---------------------------Fin des traitement ! ------------------------------------------------")
