-----------
2appScraping
------------

Cette application permet d'obtenir, en webscrapant, des données issues des livres présents sur le site books.toscrape.com.
À partir d'un url, on scrape ensuite le site pour écrire un fichier .csv comportant le titre du livre, la page web du livre, la table des prix, le code_upc du livre, les prix avec et sans taxe, le nombre d'exemplaires disponibles, la description, la catégorie, la note et l'url de l'image représentant le livre.

Suivant que l'on veut scraper les informations d'un seul livre, de toute une catégorie de livres, du site entier, ou du site entier en téléchargeant également les photos de tous les livres présents sur celui-ci, on utilisera 4 fichiers .py différents.
 
----------
Fonctionnement des fichiers et du code contenu à l'intérieur :
----------
A. Scraping1Livre.py correspond au code nécessaire pour scraper un seul livre, en utilisant la fonction book_scraper qui prend en paramètre l'url de la page du livre.
Un fichier .csv sera crée, appellé book, qui comprendra toutes les informations présentées ci-dessus.
On peut l'utiliser de cette manière :

python Scraping1Livre.py http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
-



B. Scraping2Categorie.py correspond au code nécessaire pour scraper toute une catégorie, en utilisant book_scraper à l'intérieur de la fonction category_scraper,
qui prend en paramètre l'url de la page de la catégorie souhaitée. Un fichier .csv du nom de la catégorie sera crée avec les informations des livres qui y sont contenus.
On peut l'utiliser de cette manière :

python Scraping2Categorie.py http://books.toscrape.com/catalogue/category/books/travel_2/index.html
-



C. Scraping3SiteBooks.py correspond au code nécessaire pour scraper tout le site de book.toscrape, en utilisant les fonctions book_scraper et category_scraper à l'intérieur
de la fonction book_site_scraper. Cette dernière fonction prend en paramètre l'url de la page d'acceuil du site.
Par défaut, tous les fichiers .csv seront enregistrés dans un dossier Csv_and_Images. 
On peut l'utiliser de cette manière :

python Scraping3SiteBooks.py
-



D. Scraping4DownloadImg.py correspond au code nécessaire pour scraper les informations du site de books.toscrape ET enregistrer toutes les images des livres
du site dans le même dossier Csv_and_Images. La même fonction book_site_scraper est utilisée, avec un argument supplémentaire, download_img = True, qui permet de télécharger les images en plus de la création des fichiers .csv.
On peut l'utiliser de cette manière :

python Scraping4DownloadImg.py
-

Il est possible d'ouvrir uniquement le fichier Scraping4DownloadImg  pour pouvoir voir toutes les fonctions crées, book_scraper, category_scraper et
book_site_scraper.



----------
Instructions temporaires pour faire fonctionner l'algorithme :
----------

- Installer Python

- utiliser la commande dans un éditeur de commande à l'endroit où on veut installer l'application :

python -m venv myapp
-
où myapp est le nom que vous voulez donner à votre environnement virtuel.

- Télécharger à partir de github les fichiers requirements.txt, README.md, Scraping1Livre, Scraping2Categorie, Scraping3SiteBooks, Scraping4DownloadImg dans le dossier
de votre environnement virtuel.

- Utiliser la commande dans un éditeur de commande
 
 pip install -r /path/to/requirements.txt 
 -
 où /path/to/requirements.txt est le chemin d'accès vers votre fichiers requirements.txt
 
 - Exécuter le fichier correspondant selon le souhait de scraper les informations d'un livre, d'une catégorie de livres, du site entier books.toscrape, ou les images de
 tous les livres contenues sur le site.

