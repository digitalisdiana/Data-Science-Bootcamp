##Exercice 1 : Multiples de 3 et 7
##Ecrire un programme qui affiche tous les nombres divisibles ​(nombre % 3 == 0)​ par 3 ou par 7 compris entre 100 et 850.

number = 0
list_number = []

for number in range (100,850):
    if number % 3 == 0 or number % 7 == 0:
        list_number.append(number)
    print(list_number)

#Exercice 2 : Cotation service expédition
#Binta est responsable d’une société de transport.
#Les tarifs d’expédition dépendent du poids des colis et sont définis comme suit :
#De 0 à 2kg : 2000 FCFA/kg
#￼￼￼￼￼de 2 à 5kg : 1500 FCFA/kg 
#de 5 à 10kg : 1350 FCFA/kg 
#de 10 à 50kg : 1000 FCFA/kg 
#>50kg : 850 FCFA/kg
#Ecrire un programme qui va donner le tarif en fonction du poids du colis 
"""
Scenario 1 : Calcul en entreprise. Par exemple, si on faisais payer le client apres traitement de la requete.
"""
#
#poids_du_colis = 64.5
#prix_total = 0
#
#if 0 < poids_du_colis <= 2 :
#    prix_total = poids_du_colis * 2000
#    print("L'expedition de votre colis vous coutera {}".format(prix_total))
#elif 2 < poids_du_colis <= 5 :
#    prix_total = poids_du_colis * 1500
#    print("L'expedition de votre colis vous coutera {}".format(prix_total))
#elif 5 < poids_du_colis <= 10 :
#    prix_total = poids_du_colis * 1350
#    print("L'expedition de votre colis vous coutera {}".format(prix_total))
#elif 10 < poids_du_colis <= 50 :
#    prix_total = poids_du_colis * 1000
#    print("L'expedition de votre colis vous coutera {}".format(prix_total))
#elif poids_du_colis > 50:
#    prix_total = poids_du_colis * 850
#    print("L'expedition de votre colis vous coutera {}".format(prix_total))
#else :
#    print("Au moins mettez quelque chose sur la balance :D") #Pas necessaire mais fun

"""
Scenario 2 : Calcul clientele. Par exemple, si le client paie au pesage et qu'il pese lui meme. Honor system. EXAMPLE DE PROGRAMME PAS DEMANDE :D
"""
prix_total = 0

while True :
    
    poids_du_colis = float(input("Veuillez entrer le poids de votre colis : "))
    prix_total = 0


    if 0 < poids_du_colis <= 2 :
        prix_total = poids_du_colis * 2000
        print("L'expedition de votre colis vous coutera {}".format(prix_total))
    elif 2 < poids_du_colis <= 5 :
        prix_total = poids_du_colis * 1500
        print("L'expedition de votre colis vous coutera {}".format(prix_total))
    elif 5 < poids_du_colis <= 10 :
        prix_total = poids_du_colis * 1350
        print("L'expedition de votre colis vous coutera {}".format(prix_total))
    elif 10 < poids_du_colis <= 50 :
        prix_total = poids_du_colis * 1000
        print("L'expedition de votre colis vous coutera {}".format(prix_total))
    elif poids_du_colis > 50:
        prix_total = poids_du_colis * 850
        print("L'expedition de votre colis vous coutera {}".format(prix_total))
    else :
        print("Au moins mettez quelque chose sur la balance :D") #Pas necessaire mais fun
        break

##
###Exercice 3 : Multiples de 9
###Rédigez un programme qui affiche les nombres de 1 à 100 et qui affiche “Multiple trouvé” après chaque multiple de 9.

nombre = 0
multiples_de_neuf = []

for nombre in range (1,100):
    if nombre % 9 == 0:
        multiples_de_neuf.append(nombre)

print(multiples_de_neuf)        

    
    


#Exercice 4 : Devinette
#Écrivez un programme pour deviner un nombre entre 1 et 30. L'utilisateur est invité à entrer une supposition. Si l'utilisateur se trompe, un nouveau message disant “trop petit” ou “trop grand” est affiché jusqu'à ce que le nombre soit correct. Si le nombre est deviné, l'utilisateur recevra le message "Gagné!" et le programme se terminera.

to_be_guessed = 11

for to_be_guessed in range (1,30):
    guess = int(input("Veuillez deviner un nombre entre 1 et 30 :"))
    
    if guess < to_be_guessed:
        print("Trop petit, reessayez")
    elif guess > to_be_guessed:
        print("Trop grand, reessayez")
    else:
        print("Bravo!!!")
        break

    



#Exercice 5 : Robot
#Considérons un robot qui part du point 0,0.
#Faites évoluer votre robot avec des “input()” dans le plan en lui donnant une des 5 instructions suivantes : haut, bas, gauche, droite, fin. Le robot ne peut avancer que d’une seule unité à la fois.
#Affichez après chaque mouvement la direction vers laquelle le robot pointe et sa position. Jusqu’à ce que l’utilisateur tape “fin” pour sortir du programme.

x_rob, y_rob = 0, 0 

while True :
    request = input("Pour deplacer votre robot, veuillez entrer les instructions suivantes : Haut, Bas, Gauche, ou Droite. Pour l'arreter, tapez : Fin. \n > ").strip().capitalize()
    commands = ["Haut", "Bas", "Gauche", "Droite", "Fin"]
    
    if request not in commands :
       print("Instruction non-valide")
       break 
   
    else :
        if request == "Fin" :
            print ("Vous etes au {}, {}. Merci d'avoir joué".format(x_rob, y_rob))
            break
        elif  request == "Haut" :
            y_rob += 1
            print ("Nouvelle position : {}, {}. \n".format(x_rob, y_rob))
        elif request == "Bas":
            y_rob -=1
            print ("Nouvelle position : {}, {}. \n".format(x_rob, y_rob))
        elif request == "Gauche":
            x_rob -=1
            print ("Nouvelle position : {}, {}. \n".format(x_rob, y_rob))
        else :
            x_rob +=1 
            print ("Nouvelle position : {}, {}. \n".format(x_rob, y_rob))


#Exercice 6 : Pyramide
#Ecrire un programme qui affiche la figure suivante : 
#*
#**
#***
#****
#***** 
#**** 
#*** 
#**
#*
def star_count(x):
    for i in range (0, x):
        line = i * "*"
        print("{} \n".format(line))
#Reverse
    for i in range (x, 0, -1):
        line = i * "*"
        print("{} \n".format(line))


#Exercice 7 : Code de César
#Le code de César​ est une technique pour réaliser des codes secrets en décalant les lettres d’une une plusieurs lettres. En décalant d’une lettre A s’écrit B, le B s’écrit C, etc...
#a. Ecrire un programme qui va encoder un message décalé d’une lettre
#b. Ecrire un programme qui va décoder un message décalé d’une lettre





#Exercice 8 : Password vérification
#Écrire un programme qui vérifie la validité d’un mot de passe suivant les critères suivants :
#- Au moins une Majuscule
#- au moins une minuscule
#- au moins un chiffre
#- longueur minimum de 8 caractères




#Exercice 9 : Calendrier 2020
#Ecrire un programme qui demande à l’utilisateur le jour et le mois en 2020 et qui lui affiche en retour le jour de la semaine (lundi, mardi, etc...)
