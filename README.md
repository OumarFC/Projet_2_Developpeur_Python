# Projet_2_Developpeur_Python

**Installation en ligne de commande**
  
1- Telecharger et installer la dernière version de Python.
		 Pour ma part j'ai installé la version python 3.10.6
		 
2 - Depuis votre terminal   

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

3- Créer votre dossier projet 
	     
		mkdir < monProjet2 > où monProjet2 est le nom de votre projet
		cd < monProjet2 > 
		
	
4- Créer votre environnement virtuel
	  
	    pip -m venv < NonEnv > où NonEnv est le nom pour votre environnemet virtuel
		
5- Activer votre environnement virtuel
	    
		Sous windows avec la commande :  envproj2\Scripts\activate.bat
		
6 - Installer les package depuis le fichier requirements.txt
	 
		 sous windows avec la commande : pip install -r requirements.txt
		 
		 après execution vous avez un resumé comme ci-dessous

            Collecting beautifulsoup4==4.11.1
              Using cached beautifulsoup4-4.11.1-py3-none-any.whl (128 kB)
            Collecting bs4==0.0.1
              Using cached bs4-0.0.1.tar.gz (1.1 kB)
              Preparing metadata (setup.py) ... done
            Collecting certifi==2022.6.15
              Using cached certifi-2022.6.15-py3-none-any.whl (160 kB)
            Collecting charset-normalizer==2.1.0
              Using cached charset_normalizer-2.1.0-py3-none-any.whl (39 kB)
            Collecting idna==3.3
              Using cached idna-3.3-py3-none-any.whl (61 kB)
            Collecting numpy==1.23.1
              Downloading numpy-1.23.1-cp310-cp310-win_amd64.whl (14.6 MB)
                 ---------------------------------------- 14.6/14.6 MB 4.2 MB/s eta 0:00:00
            Collecting pandas==1.4.3
              Downloading pandas-1.4.3-cp310-cp310-win_amd64.whl (10.5 MB)
                 ---------------------------------------- 10.5/10.5 MB 4.1 MB/s eta 0:00:00
            Collecting python-dateutil==2.8.2
              Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
            Collecting pytz==2022.1
              Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
            Collecting requests==2.28.1
              Using cached requests-2.28.1-py3-none-any.whl (62 kB)
            Collecting six==1.16.0
              Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
            Collecting soupsieve==2.3.2.post1
	    
		 
7 - Verifier l'installation des packages 
	 
		 sous windows avec la commande : pip freeze
		 
		 vous avez la liste ci-dessous affichées
		 
		  ( capture écran )
	
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
		

9 - Ajouter dans votre projet, les codes projet 2 que vous avez recuprer dans Github :
		
		fonc_category_link.py
		fonc_category_page.py
		fonc_imageExtract.py
		fonc_InfosProduit.py
		fonc_nextpage_link.py
		lanc_TraitementParCategorie.py
		lanc_TraitementTouteCategorie.py
		Lanc_TraitementToutEnUneFois.py
	     
	
10 -  Modification à faire 

		  Dans les programmes de lancement ( lanc_*.py ), le parametre racine 
		  racine est le repertoire où doit être stocké les données.
		  n'oubliez pas le double antislash après le dernier repertoire
          exemple : 
		  racine = "C:\\Users\\Itec Global Services\\OneDrive\\dev_app_python\\OpenclassroomsProject\\projet_2\\data\\"
		  
11 - Lancement 
	
		 1- lanc_TraitementParCategorie.py : pour chaque categorie, un sous repertoire est créé contenant toute les informations de cette categorie
		 2- lanc_TraitementTouteCategorie.py : pour toutes les catégories de tout le site, un sous repertoire contenant toutes les informations
		 3- Lanc_TraitementToutEnUneFois.py : tout le traitement en un lancement, la fusion des points 1 et 2 