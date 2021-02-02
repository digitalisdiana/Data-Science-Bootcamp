
# coding: utf-8

# # Clustering
# ## Les données

# Pour ce exercice, nous tenterons d'utiliser le clustering **K-Means** pour regrouper les universités en deux groupes, privés et publics. Nous utiliserons une base de données avec 777 observations sur les 18 variables suivantes.

# * Private Un facteur avec les niveaux Non et Oui indiquant une université privée ou publique
# * Apps Nombre de candidatures reçues
# * Accept Nombre d'applications acceptées
# * Enroll Nombre de nouveaux étudiants inscrits
# * Top10perc PCT. nouveaux étudiants parmi les 10% supérieurs de H.S. classe
# * Top25perc PCT. nouveaux étudiants parmi les 25% supérieurs de H.S. classe
# * F.Undergrad Nombre d'étudiants à temps plein
# * P.Undergrad Nombre d'étudiants de premier cycle à temps partiel
# * Outstate Frais de scolarité hors de l'État
# * Room.Board Frais de chambre et de pension
# * Livres Coûts estimés des livres
# * Dépenses personnelles estimées personnelles
# * PhD Pct. des professeurs titulaires d'un doctorat
# * Terminal PCT. du corps professoral avec diplôme terminal
# * Ratio S.F. Ratio étudiants / professeurs
# * perc.alumni PCT. anciens qui font un don
# * Dépense. les dépenses d'enseignement par élève
# * Grad.Rate Taux de diplomation

# ## Q1: Chargement des données

# **a. Lisez le fichier College_Data à l'aide de read_csv. Découvrez comment définir la première colonne comme index.**

# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')
import sys
import sklearn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


data = pd.read_csv("data/College_Data.csv", index_col = 0)


# **b.Vérifiez les premier lignes avec la finction head()**

# In[54]:


univ = pd.DataFrame(data)
univ.head(100)


# **c.  Vérifiez les informations sur les données avec la méthodes info().**

# In[19]:


univ.info(verbose = True)


# **d. faites une description des données avec la methode describe ().**

# In[90]:


univ.describe()


# In[91]:


univ.columns


# ## Q2: Analyse exploratoire

# **a. Créez un nuage de points (scatterplot) de Grad.Rate versus Room.Board (et leur ajustement linéaire) où les points sont colorés par la colonne Private.**

# In[105]:


sns.lmplot("Grad.Rate", "Room.Board", univ, hue = "Private")


# In[84]:


help(sns.lmplot)


# In[96]:


#Color establishment for private column
def denumerisation(df):
    for x in range(len(df["Private"])):
        if df["Private"][x] == 1:
            df["Private"][x] = "Yes"
        elif df["Private"][x] == 0:
            df["Private"][x] = "No"
    return df


# In[98]:


univ = denumerisation(univ)
univ.head()


# **b. Créez un nuage de points de F.Undergrad versus Outstate où les points sont colorés par la colonne Private.**
# 

# In[99]:


sns.lmplot("F.Undergrad", "Outstate", univ, hue = "Private")


# **c. Que pouvez-vous dire a partir du graphique ci-dessus?**

# Private schools have less undergrads and cost more for out of state students while it is the opposite for public schools

# **d. Créer une boîte à moustaches (boxplot) du ratio étudiants-professeurs en fonction du type d'université**

# In[165]:


sns.boxplot(x = univ["Private"], y = univ["S.F.Ratio"])


# **e.Créez une boîte à moustaches du pourcentage d'anciens (perc.alumni) qui font un don en fonction du type d'université**

# In[166]:


sns.boxplot( x = univ["Private"], y = univ["perc.alumni"])


# **f. Créez un histogramme empilé montrant les frais de scolarité hors État en fonction de la colonne Private.**

# In[157]:


sns.set_style("darkgrid")
graph = sns.FacetGrid(univ, hue ="Private", aspect = 2, palette = "coolwarm", size =9) 
graph = graph.map(plt.hist, 'Outstate', histtype = "barstacked", alpha = 0.8, bins = 20) 
plt.show() 


# **d. Créez un histogramme similaire pour la colonne Grad.Rate.**

# In[161]:


sns.set_style("darkgrid")
graph = sns.FacetGrid(univ, hue ="Private", aspect = 2, palette = "husl", size =9) 
graph = graph.map(plt.hist, "Grad.Rate", histtype = "barstacked", alpha = 0.8, bins = 20) 
plt.show()


# **e. Quelle anomalie pouvez vous detetecter sur ce graphique?**

# **Réponse**
# 
# 

# One university has more than 100% success rate.

# **f. Réglez le taux de diplomation de cette école à 100 pour que cela soit logique. Vous pouvez recevoir un avertissement et non une erreur) lors de cette opération, utilisez donc des opérations de trame de données ou refaites simplement la visualisation de l'histogramme pour vous assurer qu'elle a bien été effectuée.**

# In[163]:


univ.head()


# In[167]:


def grad_normalizer(df):
    for x in range(len(df["Grad.Rate"])):
        if df["Grad.Rate"][x] > 100:
            df["Grad.Rate"][x] = 100
    return df


# In[170]:


univ = grad_normalizer(univ)


# **g. Vérifier que le problème est réglé**

# In[171]:


sns.set_style("darkgrid")
graph = sns.FacetGrid(univ, hue ="Private", aspect = 2, palette = "husl", size =9) 
graph = graph.map(plt.hist, "Grad.Rate", histtype = "barstacked", alpha = 0.8, bins = 20) 
plt.show()


# ## Q3: K Means Cluster Creation
# 
# 

# **a. Créez une instance d'un modèle K Means avec 2 clusters.**

# In[386]:


def numerisation(df):
    for x in range(len(df["Private"])):
        if df["Private"][x] == "Yes":
            df["Private"][x] = 1
        elif df["Private"][x] == "No":
            df["Private"][x] = 0
    return df


# In[398]:


univ_n = univ.drop("Cluster", axis=1)


# In[399]:


from sklearn.cluster import KMeans
km = KMeans(n_clusters = 2, n_init = 20, max_iter = 600)
km.fit(univ_n.drop(["Private"], axis = 1))


# **b. Entrainer le modèle sur toutes les données à l'exception de l'étiquette Private. avec la fonction _fit_**

# In[400]:


y_pred = km.predict(univ_n.drop(["Private"], axis = 1))
y_pred


# **c. Quels sont les vecteurs de centre de cluster?**

# In[401]:


km.cluster_centers_


# **d. Maintenant, comparez ces centres de cluster (pour toutes les dimensions / caractéristiques) aux moyennes connues des données étiquetées**

# In[403]:


univ_n[univ_n['Private'] == 1].describe()


# In[404]:


univ_n[univ_n['Private'] == 0].describe()


# **e. Créer un bloc de données avec des centres de cluster et avec des noms de colonnes empruntés au bloc de données d'origine**
# 
# **Cette base de données indique-t-elle quelle étiquette correspond au collège privé (0 ou 1)?**

# In[405]:


center_frame = pd.DataFrame(km.cluster_centers_)
center_frame.columns = ['Apps', 'Accept', 'Enroll', 'Top10perc', 'Top25perc',
       'F.Undergrad', 'P.Undergrad', 'Outstate', 'Room.Board', 'Books',
       'Personal', 'PhD', 'Terminal', 'S.F.Ratio', 'perc.alumni', 'Expend',
       'Grad.Rate']
center_frame


# **f. Quelles sont les étiquettes de cluster?**

# In[406]:


my_labels = km.labels_
my_labels


# ## Q4. Evaluation

# Il n'y a pas de moyen parfait d'évaluer le clustering si vous n'avez pas les étiquettes, mais comme il ne s'agit que d'un exercice, nous avons les étiquettes, nous en profitons donc pour évaluer nos clusters, gardez à l'esprit que vous avez généralement gagné '' J'ai ce luxe dans le monde réel.

# **a. Créez une nouvelle colonne pour df appelée «Cluster», qui est un 1 pour une école privée et un 0 pour une école publique.**

# In[407]:


univ_n["Cluster"] = my_labels
univ_n.head()


# **b. Créez une matrice de confusion et un rapport de classification pour voir dans quelle mesure le clustering K Means a fonctionné sans recevoir d'étiquettes.**

# In[409]:


confusion = pd.DataFrame(univ_n["Private"].copy())
confusion["Predicted"] = univ_n["Cluster"]
confusion.head()


# In[377]:


from sklearn.metrics import confusion_matrix
x = confusion_matrix(list(confusion["Private"]), list(confusion["Predicted"]))
x


# In[378]:


help(sns.heatmap)


# In[410]:


sns.heatmap(x/np.sum(x), annot = True, fmt = ".2%")


# ## Q5: Performances de clustering (par exemple, distance entre les centres de gravité)

# **a. Créez deux blocs de données constitués uniquement de données universitaires privées ou publiques**

# In[365]:


public = confusion[confusion["Private"] == 0]
private = confusion[confusion["Private"] == 1]


# In[342]:


public.head()


# In[1]:


private.head()

