
# coding: utf-8

# Web Scraping Exercice 1 :
# Récupérer tous les articles à cette adresse:
# https://www.metrodakar.net/
# en recuperant specifiquement:
# - Le titre de l’article
# - Le type de l’article (ACTUALITE?, POLITIQUE?, ...)
# - Le nom de l’auteur
# - La date de publication
# - Le contenu

# In[33]:


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs #BeautifulSoup


# In[36]:


print("requests version :", requests.__version__)
print("pandas version :", pandas.__version__)
print("numpy version :", numpy.__version__)
print("bs4 version :", bs4.__version__)


# In[4]:


my_request = requests.get("https://www.metrodakar.net/")
my_page = my_request.text
my_page


# In[5]:


soup_object = bs(my_page, "html.parser")
soup_object


# In[6]:


# pretty_soup = soup_object.prettify() #Truly optional
# pretty_soup


# In[7]:


#Le titre du Site
title = soup_object.title.text
title


# In[8]:


my_articles = soup_object.findAll("div", class_="td-module-container td-category-pos-")
my_articles


# In[9]:


the_article = my_articles[0]
the_article.prettify()


# In[10]:


the_article.a(title)


# In[11]:


#Le titre de l'article 
the_title = the_article.a["title"]
the_title


# In[12]:


#Le type de l’article (ACTUALITE?, POLITIQUE?, ...)
the_category = the_article.find("a", class_="td-post-category")
the_category.text


# In[13]:


#Le nom de l’auteur
the_author = the_article.find("span", class_="td-post-author-name")
the_author.text


# In[25]:


#La date de publication
publishing_date = the_article.time["datetime"][:10]
publishing_date
publishing_time = the_article.time["datetime"][11:]
publishing_time


# In[15]:


#lLe contenu
the_body = the_article.find("div", class_="td-excerpt")
the_body.text


# # Let's do this the badass way

# In[30]:


all_articles = soup_object.findAll("div", class_="td-module-container td-category-pos-")
all_data = {
    "Title" : [],
    "Category" : [],
    "Author" : [],
    "Pub_date" : [],
    "Pub_time" : [],
    "Exerpt" : []
}

for article in all_articles:
    title = article.a["title"]
    category = article.find("a", class_="td-post-category")
    author = article.find("span", class_="td-post-author-name")
    pub_date = article.time["datetime"][:10]
    pub_time = article.time["datetime"][11:]
    exerpt = article.find("div", class_="td-excerpt")
    
    all_data["Title"].append(title)
    all_data["Category"].append(category.text)
    all_data["Author"].append(author.text)
    all_data["Pub_date"].append(pub_date)
    all_data["Pub_time"].append(pub_time)
    all_data["Exerpt"].append(exerpt.text)


print(all_data)    


# In[40]:


#Turning it into a Data Frame

my_tabled_data = pd.DataFrame(all_data)
my_tabled_data


# In[32]:


my_tabled_data.to_csv("/Users/digitalisdiana/Documents/DSInt Scripts/the_metrodakar_HW.csv")


# In[35]:


#For the columns

my_tabled_data[["Author", "Category"]].head()


# In[41]:


#For the lines
my_tabled_data.loc[[1, 2]]


# In[42]:


my_tabled_data[["Title", "Pub_date"]].loc[[21]]


# In[43]:


#Types de donnees 
my_tabled_data.dtypes


# In[47]:


#Rendre les data dependant du type de donnees
my_tabled_data.select_dtypes(include=np.number).head()


# In[46]:


#Passer de Data Frame a un Numpy array
my_tabled_data.values


# In[48]:


#Specific Access
my_tabled_data.at[18, "Category"]


# In[56]:


#Filtre par Condition
my_tabled_data[my_tabled_data["Category"] == "Politique"]


# In[57]:


my_tabled_data[(my_tabled_data["Category"] == "Politique") & (my_tabled_data["Pub_date"] == "2021-01-18")]


# In[58]:


#Binary operators on Data Frames {& : and, | : or, ".between" operator }


# In[63]:


my_tabled_data[my_tabled_data["Author"].str.startswith("Sira")]


# # THE PANDAS HOMEWORK SERIE 2

# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Importer les libraries necessaires

# In[1]:


import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup # Only for the webscraping(if it already looks like a table just read it directly)


# ### Step 2. Importer le dataset a partir de cette [addresse](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Lire les donnees dans une variable chipo.

# In[74]:


in_table = pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
print(in_table)
type(in_table)


# In[107]:


my_df = pd.DataFrame(in_table)
my_df.head(1)


# ### Step 4. Combien de produits coutent plus de $10.00?

# In[102]:


#Turning Item Price into Integer
#my_df[my_df.columns[-1]] = my_df[my_df.columns[-1]].replace('[\$,]', '', regex=True).astype(float)
#my_df.head(1)


# In[108]:


#ALTERNATIVE FOR TRANSFOMATION

my_df.head() #To check

def transfloat(price):
    return float(price[1:])


# In[110]:


my_df["item_price"].apply(transfloat)


# In[72]:


# Bring back everything superior to 10 
ten_plus = my_df[my_df["item_price"] > 10.]
ten_plus.tail()


# ### Step 5. Quel est le prix de chaque produit? 
# ###### print a data frame with only two columns item_name and item_price

# In[53]:


two_columns = my_df[["item_name", "item_price"]]
two_columns.tail(9)


# ### Step 6. Sort by the name of the item

# In[63]:


sorted_by_name = two_columns.sort_values(["item_name"])
sorted_by_name.tail(1)


# ### Step 7. Quelle est la quantite du produit le puls cher vendu?

# In[70]:


the_expensivest = max(my_df["item_price"])
the_expensivest


# ### Step 8. Combien de fois le produit Veggie Salad Bowl a ete achete?

# In[91]:


veggie_bowls = my_df[my_df["item_name"] == "Veggie Salad Bowl"]["item_name"].count()
veggie_bowls


# ### Step 9. Combien de fois quelqu'un a t-il achete plus d'une Canned Soda?

# In[92]:


canned_soda = my_df[(my_df["item_name"] == "Canned Soda") & (my_df["quantity"] > 1)]["item_name"].count()
canned_soda


# In[93]:


len(my_df)


# In[94]:


my_df.count()


# ## Statistiques

# In[95]:


my_df["quantity"].sum()


# In[96]:


my_df["quantity"].mean()


# In[97]:


my_df["quantity"].median()


# In[98]:


my_df["quantity"].max()


# In[99]:


my_df["quantity"].min()


# In[100]:


#Descriptive STATS
my_df.describe()


# In[101]:


my_df.dtypes


# In[117]:


my_df["cmy_df["choice_description"].isna()]


# In[128]:


my_df[pd.isnull(my_df).any(axis=1)]


# In[132]:


set(df["item_name"])


# In[133]:


len(set(df["item_name"]))


# # Coder la transformation en categorie

# In[134]:


df[["item_name"]].head()


# In[142]:


df["item_name"] = pd.Categorical(df["item_name"])


# In[143]:


df.dtypes


# In[144]:


df["item_name_code"] = df["item_name"].cat.codes


# In[145]:


df


# In[151]:


df.groupby("item_name_code").count()


# In[152]:


df.groupby("item_name").count()


# In[154]:


the_first_code = df[df["item_name_code"] == 0]
the_first_code


# # Remplacer par valeur la plus frequente/ Always remember the "set" when looking for unique values
