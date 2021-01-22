## -*- coding: utf-8 -*-
#"""
#Created on Thu Jan 14 09:09:16 2021
#
#@author: digitalisdiana
#"""

#Exercice 1 : Calculs

maliste = [3, 12, 16, 32, 54, 5, 23, 87, 98, 52, 99, 24]
##a. Créer le fonction somme() qui va additionner l’ensemble des éléments de la liste maliste

def addition(l):
    s = sum(l)
    return s
    
maliste_somme = addition(maliste)
print(maliste_somme)

#b. Créer la fonction moyenne() qui va retourner la moyenne de l’ensemble des éléments de maliste
def mean1(l):
    m = sum(l)/len(l)
    return m

#ALTERNATIVE 

def mean2(l):
    m = addition(l)/len(l)
    return m
    
maliste_mean1 = mean1(maliste)
print(maliste_mean1)

maliste_mean2 = mean2(maliste)
print(maliste_mean2)


#c. Créer la fonction nb_pair() qui va compter le nombre de nombres pairs de maliste

def even_numbers(l):
    n_count = 0
    for n in l:
        if n % 2 == 0:
            n_count += 1
    return n_count

maliste_even_count = even_numbers(maliste)
print(maliste_even_count)




#￼￼￼Exercice 2 : Dédoublonnage
maliste = [3, 12, 16, 3, 12, 8, 5, 12, 19, 3, 16, 19]
##Créer la fonction dedouble() qui va ressortir une liste contenant uniquement qu’une seule fois les éléments présents dans maliste

def remove_duplicate(l):
    listeunique = []    
    for n in l:
        if n not in listeunique:
            listeunique.append(n)
    return listeunique

malisteunique = remove_duplicate(maliste) 
print(malisteunique)
        


#Exercice 3 : Gestion des stock
#Soit un magasin de boisson qui a les stocks suivants :
stock = [["coca", 4], ["fanta", 25], ["volvic", 50], ["kirene", 29], ["perrier", 30]]

#a. écrire une fonction qui affiche l’état du stock

def inventory(l):
    etat_stock = {}
    for l_2 in l :
        etat_stock[l_2[0]] = l_2[1]
    print("Voici l'etat de stock :")
    return etat_stock

my_inventory = inventory(stock)
print(my_inventory)
            
""" La question est bizarre!!!      
def inventory(l):
    print(l) 
"""

    
#b. écrire une fonction vente() qui demande en entrée le nom du
#produit ainsi que la quantité vendue et qui vérifie si la
#quantité est disponible, si oui qui met à jour le stock

def inventory(l, alone=True):
    etat_stock = {}
    for l_2 in l :
        etat_stock[l_2[0]] = l_2[1]
    if alone :
        print("Voici l'etat de stock :")
    return etat_stock
#    
def sale(l):    
    product_name = input("Veuillez entrer le nom de produit : ")
    product_quantity = int(input("Veuillez entrer la quantite : "))
    if inventory(l, alone=False)[product_name] > product_quantity:
        quantity_left = inventory(l, alone=False)[product_name] - product_quantity
        print("Vous avez assez de {} en stock. Il vous en reste :".format(product_name))
        return quantity_left
    else :
        print("Vous n'avez pas assez de {} en stock; il vous en reste {}.".format(product_name, inventory(l, alone=False)[product_name]))        

quantity_left = sale(stock)
print(quantity_left)

    
#c. écrire une fonction achat() qui permet de renouveler le stock

def achat(l):
    product_name = input("Veuillez entrer le nom de produit : ")
    stock_update = inventory(l, alone=False)
    
    while True : 
        if stock_update[product_name] > 10:
            print ("Vous avez assez de {} en stock.".format(product_name))
            break
        else :
            print("Le stock de {} est insuffisant!".format(product_name))
            new_product_quantity = int(input("Veuillez entrer la quantite a commander : "))
            stock_update[product_name] += new_product_quantity

    return stock_update[product_name]

new_quantity = achat(stock)
print(new_quantity)


#Exercice 4 : Facturation
#mes_achats = [[désignation, quantité, prix ht]]
#mes_achats = [["coca", 2, 250], ["volvic", 5, 600], ["kirene", 1, 350]]
#Ecrire une fonction qui à partir de liste mes_achats() 
#va afficher les éléments de la facture : liste de produits vendus ligne à ligne, total HT, montant de la TVA (18%), montant TTC
mes_achats = [["coca", 2, 250], ["volvic", 5, 600], ["kirene", 1, 350]]


def facturation(l):
    facture = {}
    for l_2 in l:
        facture["Produit"] = l_2[0]
        facture["Prix Unique HT"] = l_2[2]
        facture["Prix Total HT"] = l_2[2] * l_2[1]
        facture["Montant TVA"] = (l_2[2] * l_2[1]) * 0.18
        facture["Montant TTC"] = (l_2[2] * l_2[1]) - (l_2[2] * l_2[1]) * 0.18
    print("Voici votre facture :")
    return facture
    
mafacture = facturation(mes_achats)
print(mafacture)
    

#Exercice 5 : Tour du Faso
#Ecrire un ensemble de fonctions qui vont permettre de gérer la liste des concurrents du tour du Faso. 
#Pour chaque joueur on va stocker le prénom, le nom, la nationalité, l'âge, le numéro ainsi que le nombre de points du concurrent.

concurrents =[["Sadio", "Mane", "Senegalaise", 36, 27, 321],["Mahfouz", "Sani", "Niger", 29, 76, 234],["Brad", "Pitt", "Americaine", 62, 12, 143]]

def dict_concurrent(l):
    concurrents_tournoi = {}
    for concurrent in l:
        concurrents_tournoi["Prenom"] = concurrent[0]
        concurrents_tournoi["Nom"] = concurrent[1]
        concurrents_tournoi["Nationalite"] = concurrent[2]
        concurrents_tournoi["Age"] = concurrent[3]
        concurrents_tournoi["Numero"] = concurrent[4]
        concurrents_tournoi["Nombre de points"] = concurrent[5]        
    return concurrents_tournoi

les_concurrents = dict_concurrent(concurrents)
print(les_concurrents)

    
#￼￼a. Ecrire la fonction ajout() qui permet d’ajouter un concurrent


newly_signed_in = [["Abass", "Ndao", "Senegalaise", 87, 23, 1],["Abubakar", "Ally", "Togo", 18, 18, 87],["Malik", "Whitefield", "Americaine", 62, 64, 843]]

def ajout_concurrent(l):
    renewed_dict = dict_concurrent(l)
    
    for concurrent in l:
        if concurrent[4] != dict_concurrent(l)["Numero"]:
            dict_concurrent(l) += concurrent
            
    return renewed_dict

updated_list = ajout_concurrent(newly_signed_in)
print(updated_list)


    
#b. Ecrire la fonction abandon() qui permet d’enlever un
#concurrent de la liste
    
#c. Ecrire la fonction liste(tri) qui permet de lister les
#concurrents. La paramètre tri permet de trier par prénom,
#nom, âge, nationalité, numéro, nombre de points
    
#d. Ecrire la fonction podium() qui donne la liste des 3 premiers
#concurrents


#
#Exercice 7 : Multiples de 3 et 7
#Ecrire un programme qui affiche tous les nombres divisibles ​(nombre % 3 == 0)​ par 3 ou par 7 compris entre 100 et 850.

def exercice_7_problem():# Can I have multiple return statements ?
    number = 0
    multiples_of_three = []
    multiples_of_seven = []
    
    for number in range (100, 850):
        if number % 3 == 0:
            multiples_of_three.append(number)
        elif number % 7 == 0:
            multiples_of_seven.append(number)
    print("Below are, respectively, the multiples of three and seven.")
    return multiples_of_three, multiples_of_seven

resultat_exercice_7 = exercice_7_problem()
print(resultat_exercice_7)
            


#Exercice 8 : Cotation service expédition
#Binta est responsable d’une société de transport.
#Les tarifs d’expédition dépendent du poids des colis et sont définis comme suit :
#De 0 à 2kg : 2000 FCFA/kg
#de 2 à 5kg : 1500 FCFA/kg
#de 5 à 10kg : 1350 FCFA/kg
#de 10 à 50kg : 1000 FCFA/kg
#>50kg : 850 FCFA/kg
#Ecrire un programme qui va donner le tarif en fonction du poids du colis
#
#
#Exercice 9
#consider the following lists : list1 = ["M", "na", "i", "Ago"] list2 = ["y", "me", "s", "suma"]
#￼￼￼￼
#￼￼a. Can you obtain the following output? Then save the output list. The zip function is your friend
#['My', 'name', 'is', 'Agosuma']
#b. from the list above, replace 'name' by 'full name' and 'Agosuma' by ‘Foo Bar’ ;
#c. propose another solution for question b ;
#d. Can you tell the difference between the methods append and extend?
#
#
#
#Exercice 10 : Pyramide
#Ecrire un programme qui affiche la figure suivante : *
#**
#***
#**** 
#***** 
#**** 
#*** 
#**
#*
#
#
#
#Exercice 11
#a. Create a tuple containing one element ;
#b. Consider the following tuple, can you unpack them? In 2
#variables? In 3 variables? In 4 variables?
#aTuple = (10, 20, 30, 40)
#c. Consider the following tuples, can you swap them?
#￼￼
#￼￼tuple1 = (11, 22) tuple2 = (99, 88)
#d. Consider the following variables, can you print their respective types:
#sampleSet = {"Yellow", "Orange", "Black"} sampleList = ["Blue", "Green", "Red"]
#e. Can you update sampleSet, by adding the content of sampleList. The dir function is your friend ;
#f. Consider the following sets, can you find the intersection? set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#g. Can you tell how to merge those 2 sets?
#
#
#
#Exercice 12
#a. Soit la variable suivante, transformez la en liste de caractères:
#sentence = "In her entire life, Habiba has never seen such a big rain" .
#b. À partir de la liste de caractères, retirez tous les doublons.
#
#
#
#Exercice 13 : Palindrome
#Faire un programme qui vérifie si un mot est un Palindrome.
#
#
#
#Exercice 14 : Code MORSE
#￼￼￼￼
#Ecrire un encodeur et décodeur de code morse. Aller sur ​cette page pour trouver l'équivalent en Morse de l'alphabet Francais.
#
#
#
#Exercice 15 : Bataille Navale
#Créer la variable bateau qui comprend la position de l’ensemble des bateau de l’utilisateur A.
#Soit 2 bateaux sur 2 cases, 2 bateaux de 3 cases, 1 bateau de 4 cases.
#Demander à l’utilisateur B de tirer sur une position (exemple B3). avec un input.
#Le programme doit répondre “Touché” ou “Dans l’eau”.
#
#
#
#Exercice 16 : Place de Cinéma
#Ecrire un programme qui calcule le prix d’une place de cinéma selon les conditions suivantes :
#a. La place coûte 2700f du Lundi au Vendredi ;
#b. Une augmentation de 1450f est effectuée le Samedi ;
#c. Une augmentation de 1200f est effectuée le Dimanche ;
#d. Le Samedi et le Dimanche, une réduction de 975f est effectuée
#pour les personnes de moins de 14 ans et celles de plus de 65
#ans;
#e. Le Mercredi, une réduction de 1150f est effectuée pour les
#personnes de moins de 22 ans ;
#f. Si un jour est férié, le prix de la place d’une personne est
#augmenté de 800f après le calcul avec les conditions précédentes.



