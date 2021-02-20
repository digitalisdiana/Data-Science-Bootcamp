
import math 

# EXERCISE 1

###Écrivez une définition pour une classe nommée ​Cercle ayant les attributs ​centre et ​rayon​, où le centre est un objet ​Point​ et le rayon est un nombre.
###Instanciez un objet Cercle qui représente un cercle ayant son centre à ​(150, 100)​ et un rayon de ​75. Écrivez une fonction nommée ​point_du_cercle ​qui prend un Cercle et un Point et renvoie Vrai si le
###Point se trouve dans le cercle ou sur sa circonférence.
###Écrivez une fonction nommée ​rect_du_cercle ​qui prend un Cercle et un Rectangle et renvoie Vrai si le rectangle se trouve entièrement dans le cercle ou sur sa circonférence.
###Écrivez une fonction nommée ​rect_chevauche_cercle ​qui prend un Cercle et un Rectangle et renvoie Vrai si l'un des coins du Rectangle se trouve à l'intérieur du cercle. Ou, version plus difficile, retourne Vrai si une partie quelconque du Rectangle se trouve à l'intérieur du cercle.

"""Class Dot"""

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
""" Class Circle"""

class Circle:
    def __init__(self, center: Dot, radius: int):
        self.center = center
        self.radius = radius 
    
    def circumference(radius: int):
        circ = 2 * pi * radius
        return circ
        
    def area(radius: int):
        area = pi * radius**2
    
    def diameter(radius: int):
        diam = 2 * radius
        return diam

"""Class Rectangle"""

class Rectangle:
    def __init__(self, corner: Dot, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height

    def center(corner: Dot, width: float, height: float):
        self.x += 1/2 * width
        self.y -= 1/2 * height
        center = (self.x, self.y)
        return center
        
    def perimeter(width: float, height: float):
        peri = 2 * width * height
        return peri
    
    def area(width: float, height: float):
        area = width * height
        return area

"""Problem Operation Functions"""

def dot_in_a_circle(circle: Circle, dot: Dot):
    if dot in circle.area or dot in circle.circumference:
        return True
    else:
        return False

def rectangle_touching_a_circle(circle: Circle, rectangle: Rectangle):
    if rectangle.area in circle.area : #or if rectangle.area in circle.circumference
        return True
    else:
        return False
        
def rectangle_in_a_circle(circle: Circle, rectangle: Rectangle):
    if rectangle.dot in circle.area:
        return True
    else:
        return False



#EXERCISE 2

###Écrivez une fonction appelée ​mul_time ​qui prend un objet ​Temps ​et un nombre et retourne un nouvel objet T​ emps​ ​, qui contient le produit entre le ​Temps​ ​d'origine et le nombre.

###Ensuite, utilisez ​mul_time pour écrire une fonction qui prend un objet ​Temps qui représente le temps de l'arrivée dans une course, et un nombre qui représente la distance, et retourne un objet ​Temps qui représente le rythme moyen (temps par kilomètre).​




# EXERCISE 3

###Le module ​datetime​ fournit des objets ​time​ qui sont similaires aux objets ​Temps​ de ce chapitre, mais ils fournissent un riche ensemble de méthodes et d'opérateurs. Lisez-en la documentation à l'adresse http://docs.python.org/3/library/datetime.html​.
## 1. Utilisez le module ​datetime​ ​pour écrire un programme qui prend la date actuelle et affiche le jour de la semaine.
## 2. Écrivez un programme qui prend en entrée un anniversaire et affiche l'âge de l'utilisateur et le nombre de jours, heures, minutes et secondes jusqu'à son prochain anniversaire.
## 3. Si deux personnes sont nées deux jours différents, il existe un jour où l'une d'entre elles est deux fois plus âgée que l'autre. C'est leur Jour double. Écrivez un programme qui prend deux dates de naissance et calcule leur Jour double.
## 4. Pour pimenter un peu le défi, écrivez la version plus générale qui calcule le jour où l'une des personnes est n​ ​fois plus âgée que l'autre.




# EXERCISE 4
###Cet exercice est un conte pédagogique sur l'une des erreurs les plus courantes et difficiles à trouver enPython.Écrivezunedéfinitionpouruneclassenommée​Kangaroo(k​angarooestlemotanglais
#pour le kangourou), avec les méthodes suivantes :
## 1. Une méthode ​__init__​ qui initialise un attribut nommé ​pouch_contents​ à une liste vide (le mot anglais ​pouch​ désigne généralement un sac ou une bourse, mais plus précisément ici la poche ventrale dans laquelle la femelle du kangourou abrite son petit) ;
## 2. Une méthode nommée p​ ut_in_pouch​ ​qui prend un objet d'un type quelconque et l'ajoute à ​;
## 3. Une méthode ​qui renvoie une représentation sous forme de chaîne de caractères de l'objet ​et du contenu de la poche.
###Testez votre code en créant deux objets K​angaroo​,enlesattribuantàdesvariablesnommées​kanga et ​roo​ ​, puis en ajoutant ​roo​ ​au contenu de la poche de k​ anga​ ​.
