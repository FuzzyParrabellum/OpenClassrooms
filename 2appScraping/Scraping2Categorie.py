import requests 
from bs4 import BeautifulSoup
import re
import csv
import sys

try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit("Veuillez indiquer un lien valide d'une catégorie du site books.toscrape.com après Scraping2Livre.py")

def book_scraper(url, category_name=0):
    # La fonction book_scraper prends en argument un url, et va ensuite scraper le titre du livre,
    # la page web du livre, la table des prix, le code_upc du livre, les prix avec et sans taxe, 
    # le nombre d'exemplaires disponibles, la description, la catégorie, la note et l'url de l'image
    # représentant le livre.
    

    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    #titre du livre
    book_title = soup.select("div h1")
    book_title = book_title[0].string
    #page web du livre
    product_page_url = url
    #scraping de la table des prix
    table_scraping = soup.select("td")
    #code_upc
    universal_product_code = table_scraping[0].string
    #les prix
    price_excluding_tax = table_scraping[2].string
    price_including_tax = table_scraping[3].string
    #le nombre d'exemplaires disponibles
    number_available = table_scraping[5].string
    number_available = re.findall('\d+', number_available)[0]
    #scraping de la description du livre
    paragraph_scraper = soup.select("p")
    paragraph_printer = []
    for p in paragraph_scraper:
        paragraph_printer.append(p.string)
    product_description = paragraph_printer[3]
    #la catégorie
    category = soup.select("ul li a")
    a_list = []
    for a in category:
        a_list.append(a.string)
    category = a_list[2]
    # la note du livre
    review_rating = soup.select("div p")
    review_printer = []
    dictionnary_printer = []
    list_printer = []
    for text in review_rating:
        review_printer.append(text.attrs)
    for dictionnary in review_printer:
        dictionnary_printer.append(list(dictionnary.values()))
    for element in dictionnary_printer:
        for kelement in element:
            list_printer.append(kelement)
    review_rating = list_printer[2][1]
    # l'url de l'image
    url_img = soup.find("img")
    url_img = url_img["src"] 
    image_url = "http://books.toscrape.com/" + re.sub('^\W{6}', '', url_img)
    

    if category_name == 0:
        with open('book.csv', 'w', encoding='utf-8') as out:
            csv_writing = csv.writer(out, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
            list_of_entete = ['product_page_url', 'universal_product_code(upc)',' title', 'price_including_tax', 'price_excluding_tax', \
    'number_available', 'product_description', 'category', 'review_rating', 'image_url']
            list_of_rowvalues = [product_page_url, universal_product_code, book_title, price_including_tax, price_excluding_tax, \
    number_available, product_description, category, review_rating, image_url]
            csv_writing.writerow(list_of_entete)
            csv_writing.writerow(list_of_rowvalues)
            

    else:
        list_of_rowvalues = [product_page_url, universal_product_code, book_title, price_including_tax, price_excluding_tax, \
    number_available, product_description, category, review_rating, image_url]
        return list_of_rowvalues

            
        

    

def category_scraper(category_url):
    # La fonction category_scraper prends en argument l'url de l'index d'une catégorie du site books.toscrape.com,
    # et écrit ensuite un fichier .csv comprenant toutes les informations scrapées par la fonction book_scraper,
    # appliquée à tous les livres présents dans la catégorie.

    category_webpage = requests.get(category_url)
    soup_category = BeautifulSoup(category_webpage.content, "html.parser")

    next_page_button = soup_category.find(attrs={'class':'next'})
    
    # met la premiere page parsée par BeautifulSoup dans une liste
    soups = [soup_category]

    # tant qu'il y a un bouton next en bas de la page, on rajoute un nouvel élément soup dans la liste et on passe à la prochaine page
    while next_page_button:
        for text in next_page_button:
            # va trouver l'url de la prochaine page si il y en a une
            category_url = re.sub('[indexpage-]*\d*\.html$', '', category_url)
            next_page_button_url = category_url + text.attrs['href']   
        new_category_webpage = requests.get(next_page_button_url)
        new_soup = BeautifulSoup(new_category_webpage.content, "html.parser")
        soups.append(new_soup) 
        next_page_button = new_soup.find(attrs={'class':'next'})
    
    links = []
    
    #Scrapage de tous les liens présents sur la page
    for soup_parsing in soups:
        lis = soup_parsing.select("li h3 a")
        for a in lis:
            links.append(a.attrs["href"])

    #Chaque lien se voit attribuer le bon début pour accéder à une page au lieu de ../..
    for index in range(len(links)):
        links[index] = "http://books.toscrape.com/catalogue/" + re.sub('^\W{9}', '', links[index])
    
    # on trouve le nom de la categorie pour pouvoir nommer le fichier csv
    category_name = re.sub('.+category\/books\/', '', category_url)
    category_name = category_name[0:-1]

    # on écrit un fichier .csv comportant les informations de tous les livres de la catégorie choisie
    with open('{}.csv'.format(category_name), 'w', encoding='utf-8') as out:
        csv_writing = csv.writer(out, delimiter = ';', quoting = csv.QUOTE_ALL)
        list_of_entete = ['product_page_url', 'universal_product_code(upc)',' title', 'price_including_tax', 'price_excluding_tax', \
'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        csv_writing.writerow(list_of_entete)
        for book in links:
            new_row = book_scraper(book, category_name)
            csv_writing.writerow(new_row)
        
    
# On appelle la fonction category_scraper avec l'argument passé avec le fichier Scraping2Categorie.py 
category_scraper(arg)
    
    
    

    


