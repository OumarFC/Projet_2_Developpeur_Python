# Projet 2 : Utilisez les bases de Python pour l'analyse de marché

![logo.png](logo.png)

**Installation en ligne de commande pour l'execution du projet**
  
1- Telecharger et installer la dernière version de Python.
		 Pour ma part j'ai installé la version python 3.10.6
		 
2 - Depuis votre terminal sous windows ( cmd )  

          verifier que vous avez pip installer sur la machine
          pour cela lancer la commande pip --help 
		 
		 vous devez avoir les information ci-dessous ( L'information est plus longue )

			  Usage:
		  pip <command> [options]

		Commands:
		  install                     Install packages.
		  download                    Download packages.
		  uninstall                   Uninstall packages.
		  freeze                      Output installed packages in requirements format.
		  inspect                     Inspect the python environment.
		  list                        List installed packages.
		  show                        Show information about installed packages.
		  check                       Verify installed packages have compatible dependencies.
		  config                      Manage local and global configuration.
		  search                      Search PyPI for packages.
		  cache                       Inspect and manage pip's wheel cache.
		  index                       Inspect information available from package indexes.
		  wheel                       Build wheels from your requirements.
		  hash                        Compute hashes of package archives.
		  completion                  A helper command used for command completion.
		  debug                       Show information useful for debugging.
		  help                        Show help for commands.

3- Créer votre dossier projet sous windows
	     
		mkdir < monProjet2 > où monProjet2 est le nom de votre projet
		cd < monProjet2 > 
		
	
4- Créer votre environnement virtuel
	  
	    pip -m venv < NonEnv > où NonEnv est le nom pour votre environnemet virtuel
		
5- Activer votre environnement virtuel
	    
		Sous windows avec la commande :  envproj2\Scripts\activate.bat
		
6 - Installer les package depuis le fichier requirements.txt
	 
		 sous windows avec la commande : pip install -r requirements.txt

		 
7 - Verifier l'installation des packages 
	 
		 sous windows avec la commande : pip freeze
		 
		 vous avez la liste ci-dessous affichées
		 
            beautifulsoup4==4.11.1
            bs4==0.0.1
            certifi==2022.6.15
            charset-normalizer==2.1.0
            idna==3.3
            numpy==1.23.1
            pandas==1.4.3
            python-dateutil==2.8.2
            pytz==2022.1
            requests==2.28.1
            six==1.16.0
            soupsieve==2.3.2.post1
            urllib3==1.26.11
	
8 - Exclure l'environnement virtuel des commit sur le serveur distant 
	
		sous windows, editer le fichier  .git\info\exclude 
		ajouter a la ligne suivante le nom de l'envrionnement virtuel ici : monProjet2
		comme ci-dessous :
		
		# git ls-files --others --exclude-from=.git/info/exclude
		# Lines that start with '#' are comments.
		# For a project mostly in C, the following would be a good set of
		# exclude patterns (uncomment them if you want to use them):
		# *.[oa]
		# *~
		envproj2
		

9 - Ajouter dans votre projet, les codes du projet 2 que vous avez recuperer dans Github :
		
		fonc_category_link.py
		fonc_category_page.py
		fonc_imageExtract.py
		fonc_InfosProduit.py
		fonc_nextpage_link.py
		lanc_TraitementParCategorie.py
		lanc_TraitementTouteCategorie.py
		Lanc_TraitementToutEnUneFois.py
	     
	
10 -  Modification à faire 

		  Dans les programmes de lancement ( lanc_*.py ), modifier le parametre racine 
		  racine est le chemin où doit être stocké les données.
		  n'oubliez pas le double antislash après le dernier repertoire
              exemple : 
		  racine = "C:\\Users\\Itec Global Services\\OneDrive\\dev_app_python\\OpenclassroomsProject\\projet_2\\data\\"
		  
11 - Lancement 
	
		 1- lanc_TraitementParCategorie.py : pour chaque categorie, un sous repertoire est créé contenant toutes les informations de cette categorie
		 2- lanc_TraitementTouteCategorie.py : pour toutes les catégories de tout le site, un sous repertoire contenant toutes les informations
		 3- Lanc_TraitementToutEnUneFois.py : tout le traitement en un seul lancement, la fusion des points 1 et 2 