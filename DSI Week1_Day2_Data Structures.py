#Exercice 1 : Liste de prix.
#
#a. Afficher la phrase complète :
phrase = ["Only", "two", "things", "are", "infinite", "the", "universe", "and", "human", "stupidity", ",", "and", "I'm", "not", "sure", "about", "the", "former", "."]

"""
for element in phrase :
    print(element)
phrase = list(phrase.__str__)
CA, C'EST LES TESTS QUI N'ONT PAS MARCHE
"""

new_phrase = " ".join(phrase)
print(new_phrase) # Le probleme avec la virgule {l'espace d'avant}


#b. Afficher le nombre d’éléments dans la liste

prix= [35, 20, 5, 59, 77, 35, 80, 180, 95, 121, 112]
print(len(prix))


#c. Afficher le prix le plus élevé

print(max(prix))

#d. Afficher le prix le plus bas
print(min(prix))

#e. Afficher le 8ème élément
print(prix[7])

#f. Trier les prix et afficher les 3 plus élevés
prix.sort
print(prix[-3:])
#g. Ajouter les prix suivants : 250, 22, 8

new_list = [250, 22, 8]
prix.extend(new_list)

print(prix)

#h. Afficher la phrase suivante :]

the_smallest = min(prix)

print("Le prix le plus bas est {}.".format(the_smallest))

#i. Afficher la phrase suivante : “”La moyenne des prix est ___”
the_mean = sum(prix)/len(prix)

print("La moyenne des prix est {}.".format(the_mean))



#Exercice 2
#Create the following list

alist = [100, 200, 300, 400, 500]
#a. print the second item ;

print(alist[1])
#b. print the second item using negative indexes ;

print(alist[-4])
#c. count the number of occurrences of the value 200 ;
alist.count(200)

#d. How many items are we in the list?

print(len(alist))

#e. remove last item, propose 3 solutions ;

#FIRST
alist.pop()


#SECOND
alist.remove(500)

#THIRD
del alist[-1]

#f. append an item ;

alist.append(999)
#g. reverse the a list list ;

alist.reverse()

#h. remove second item ;
del alist[1]


#i. add the item [300, 400, 500] in the 3rd position of a list ;
the_item = [300, 400, 500]
alist.insert(2, the_item)

#expected output [100, 200, [3000, 4000, 5000], 300, 400, 600]
#j. then, add [10000] in the 3rd position of the 3rd item of alist list
the_item.insert(2, [10000])
print(alist)

#expected output [100, 200, [3000, [10000], 4000, 5000], 300, 400, 600]




#Exercice 3
#consider the following lists : 
list1 = ["M", "na", "i", "Ago"]
list2 = ["y", "me", "s", "suma"]

zipped_lists = zip(list1, list2)
print(zipped_lists)

better_view = [a + b for a, b in zipped_lists]
print(better_view)

#a. Can you obtain the following output? Then save the output list. The zip function is your friend
#['My', 'name', 'is', 'Agosuma']

#b. from the list above, replace 'name' by 'full name' and 'Agosuma' by ‘Foo Bar’ ;
better_view[1] = "full name"
better_view[-1] = "Foo Bar"

print(better_view)

#c. propose another solution for question b ;
## First take out the last element
better_view.pop()
## Put in the desired element
better_view.append("Foo Bar")

## Take out the second element
better_view.remove("name")

##Put in what we want 
better_view.insert(1, "full name")
print(better_view)

#d. Can you tell the difference between the methods append and extend?
"""
Append ajoute une valeur a la fin d'une liste, extend ajoute une autre liste a la fin de la premiere
"""

#Exercice 4
#a. Consider the following lists, can you create a dict from them? set() and dict() are your friends:
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]

#b. Consider the following dicts, can you merge them? 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#c. Once merged, can you list only the keys? Can you list only the values?
#d. Consider the following dict, replace the key ‘city’, by the key ‘location’, keep the same value ‘Abuja’:
sampleDict = { "name": "Motunde", 
"age": 25,
"salary": 8000, 
"city": "Abuja"}

#e. Consider the following dict, change Akpaya salary to 6000 
sampleDict = {
'emp1': {'name': 'Abgena', 'salary': 7500}, 
'emp2': {'name': 'Akpaya', 'salary': 8000}, 
'emp3': {'name': 'Kokou', 'salary': 6500} 
}

sampleDict["emp2"]["salary"] = 6000

print sampleDict

#Exercice 5
#a. Create a tuple containing one element ;
my_tuple = ("A", )
#b. Consider the following tuple, can you unpack them? In 2
#variables? In 3 variables? In 4 variables? 

aTuple = (10, 20, 30, 40)
me, him, her, them = aTuple

print(aTuple)
print(me, him, her, them)

#c. Consider the following tuples, can you swap them? 
tuple1 = (11, 22)

tuple2 = (99, 88)


tuple3 = tuple2

tuple2 = tuple1

tuple1 = tuple3

print(tuple1, tuple2)
#￼￼
#￼￼￼￼d. Consider the following variables, can you print their respective types:

sampleSet = {"Yellow", "Orange", "Black"} 
sampleList = ["Blue", "Green", "Red"]
#e. Can you update sampleSet, by adding the content of sampleList. The dir function is your friend ;
#f. Consider the following sets, can you find the intersection? 
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#g. Can you tell how to merge those 2 sets?
#Sets contiennent des elements a valeur unique





#Exercice 6
#a. Soit la variable suivante, transformez la en liste de caractères:
#sentence = "In her entire life, Habiba has never seen such a big rain" .
#b. À partir de la liste de caractères, retirez tous les doublons.

def splitter(phrase):
    split_list = [c for c in phrase if not c.isspace()]
    return split_list


spaceless_sent = splitter(sentence)
spaceless_sent

unique_char = set(spaceless_sent)
unique_char


#Exercice 7 : Doublons
#Enlever les doublons dans la liste suivante et afficher la liste dédoublonnée.
pays = ['senegal', 'ghana', 'mali', 'burkina-faso', 'mali', 'kenya', 'senegal']

unique_pays = set(pays)
unique_pays


#Exercice 8 : Palindrome
#Faire un programme qui vérifie si un mot est un Palindrome.

 def palindrome_detector():
    word = input("Entrez votre mot : ")
    if word == word[::-1]:
        return "{} est bien un Palindrome".format(word)
    else:
        return "Nope, desole"
 


#Exercice 9 : Code MORSE
#Écrire un encodeur et décodeur de code morse. Aller sur ​cette page pour trouver l'équivalent en Morse de l'alphabet Francais.




#Exercice 10 : Bataille Navale
#Créer la variable bateau qui comprend la position de l’ensemble des bateaux de l’utilisateur A.
#Soit 2 bateaux sur 2 cases, 2 bateaux de 3 cases, 1 bateau de 4 cases.
#Demander à l’utilisateur B de tirer sur une position (exemple B3). avec un input.
#Le programme doit répondre “Touché” ou “Dans l’eau”.



#Exercice 11 : Place de Cinéma
ferie = True 
prix = 0
days = {"week" : ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"], "weekend" : ["Samedi", "Dimanche"]}
day = str(input("Veuillez indiquer le jour : ")).capitalize()
age = int(input("Veuillez indiquer votre age : "))

def price_calculator():
    
    while ferie == True:
        prix = prix + 800
        
        for day in days["week"]:
            if day == "Mercredi" and age < 22:
                prix += 2700 - 1150
                print("Le prix est {}.".format(prix))
            else :
                prix += 2700
                print("Le prix est {}.".format(prix))
        
        for day in days["weekend"]:
            if day == "Samedi":
                if age < 14 and age > 65:
                    prix += 2700 + 1450 - 975
                    print("Le prix est {}.".format(prix))
                else:
                    prix += 2700 + 1450
                    print("Le prix est {}.".format(prix))
            if day == "Dimanche":
                if age < 14 and age > 65:
                    prix += 2700 + 1200 - 975
                    print("Le prix est {}.".format(prix))
                else:
                    prix += 2700 + 1200
                    print("Le prix est {}.".format(prix))
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

￼￼￼￼

