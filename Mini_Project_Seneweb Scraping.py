
# coding: utf-8

# # Web Scraping avec beautiful soup

# In[1]:


import requests
from bs4 import BeautifulSoup


# ## Recuperation des articles dans la page d'acceuil seneweb

# In[2]:


# Recuperer une page web sur seneweb
req = requests.get('https://seneweb.com/news/societe/')
page = req.text
page


# In[3]:


# Initialisation d'un objet de type BeautifulSoup pour pouvoir manipuler la page
soup = BeautifulSoup(page)
print(soup.prettify())


# In[4]:


# Recuperer le titre
titre = soup.title.text
titre


# In[5]:


# Recuperer tous les articles dans la page
articles = soup.find_all('div', class_='module_news_item_content')
articles


# In[6]:


# Recuperons le premier article pour le scraper (individuellement)
article = articles[0]
print(article.prettify())


# In[7]:


# Recuperons le titre de l'article
titre = article.a.text
titre


# In[8]:


# contenu de l'article
contenu = article.find_all('a')[1].text
contenu


# In[9]:


# date de publication 
date_pub = article.find_all('span', class_='meta_item meta_date')[0].text
date_pub


# In[10]:


# nombre de vues de l'article
nombre_vues = article.find_all('span', class_='meta_item meta_views')[0].text
nombre_vues


# In[68]:


nombre_commentaires = article.find_all('span', class_='meta_item meta_comments')[0].text
nombre_commentaires


# In[11]:


# Ici nous condensons tout le code precedent pour l'executer
articles = soup.find_all('div', class_='module_news_item_content')
data = {
    "titre": [],
    "contenu": [],
    "date_pub": [],
    "nombre_vues": [],
    "nombre_commentaires": []
}
for article in articles:
    titre = article.a.text
    contenu = article.find_all('a')[1].text
    date_pub = article.find_all('span', class_='meta_item meta_date')[0].text
    nombre_vues = article.find_all('span', class_='meta_item meta_views')[0].text
    nombre_commentaires = article.find_all('span', class_='meta_item meta_comments')[0].text
    
    data['titre'].append(titre)
    data['contenu'].append(contenu)
    data['date_pub'].append(date_pub)
    data['nombre_vues'].append(nombre_vues)
    data['nombre_commentaires'].append(nombre_commentaires)

    article_d = {
        "titre": titre,
        "contenu": contenu,
        "date_pub": date_pub,
        "nombre_vues": nombre_vues,
        "nombre_commentaires": nombre_commentaires
    }

print(data)


# ## Enregistrer les donnees recuper dans un fichier csv

# In[12]:


import pandas as pd


# In[13]:


df = pd.DataFrame(data)
df.head()


# In[14]:


df.to_csv('articles_seneweb.csv')


# Les donnees sont enregistrees dans le fichier article_seneweb.csv
