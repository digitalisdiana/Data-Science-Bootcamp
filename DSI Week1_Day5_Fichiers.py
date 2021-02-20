# EXERCISE 1: Poésie
###A partir du fichier “poesie.txt”
## a. Créer un fichier “mapoesie_01.txt” qui reprend l’ensemble de la poésie contenue dans le fichier “poesie.txt” en lui ajoutant à la fin une dernière ligne “Afin que le monde sache que je sais programmer en Python”
## b. Créer un fichier “mapoesie_02.txt”

un_poeme = """
 When love beckons to you, follow him,
 Though his ways are hard and steep.
 And when his wings enfold you yield to him,
 Though the sword hidden among his pinions may wound you.
 And when he speaks to you believe in him,
 Though his voice may shatter your dreams as the north wind lays waste the garden.

 For even as love crowns you so shall he crucify you. Even as he is for your growth so is he for your pruning.
 Even as he ascends to your height and caresses your tenderest branches that quiver in the sun,
 So shall he descend to your roots and shake them in their clinging to the earth.
 Like sheaves of corn he gathers you unto himself
 He threshes you to make your naked.
 He sifts you to free you from your husks.
 He grinds you to whiteness.
 He kneads you until you are pliant;
 And then he assigns you to his sacred fire, that you may become sacred bread for God’s sacred feast.

 All these things shall love do unto you that you may know the secrets of your heart, and in that knowledge become a fragment of Life’s heart.

 But if in your heart you would seek only love’s peace and love’s pleasure,
 Then it is better for you that you cover your nakedness and pass out of love’s threshing-floor,
 Into the seasonless world where you shall laugh, but not all of your laughter, and weep, but not all of your tears.
 Love gives naught but itself and takes naught but from itself.
 Love possesses not nor would it be possessed;
 For love is sufficient unto love.

 When you love you should not say, “God is in my heart,” but rather, “I am in the heart of God.”
 And think not you can direct the course of love, for love, if it finds you worthy, directs your course.

 Love has no other desire but to fulfil itself.
 But if you love and must needs have desires, let these be your desires:
 To melt and be like a running brook that sings its melody to the night.
 To know the pain of too much tenderness.
 To be wounded by your own understanding of love;
 And to bleed willingly and joyfully.
 To wake at dawn with a winged heart and give thanks for another day of loving;
 To rest at the noon hour and meditate love’s ecstasy;
 To return home at eventide with gratitude;
 And then to sleep with a prayer for the beloved in your heart and a song of praise upon your lips.

"""

my_line = "Afin que le monde sache que je sais programmer en Python"

with open("/Users/digitalisdiana/Documents/DSInt Scripts/poesie.txt", "w+") as poeme_original :
    poeme_original.writelines(un_poeme)

with open("poesie.txt", "a") as poeme_modifie :
    poeme_modifie.write(my_line)
    

# EXERCISE 2 : Gestion des contacts
###A partir du fichier contact_list.csv

my_contacts = [("nom,", "prenom,", "numero,", "email,", "etat\n"),
               ("Styles,", "Harry,", "123,", "hstyles@harvard.com,", "NY\n"),
("Malik,", "Zane,", "456,", "zmalik@yahoo.com,", "CO\n"),
("Tomlinson,", "Louis,", "789,", "ltomlinson@gmail.com,", "OR\n"),
("Horan,", "Naill,", "101,", "nhoran@gmail.com,", "NY\n"),
("Bieber,", "Justin,", "112,", "jbieber@yahoo.com,", "CA\n"),
("Gibran,", "Kahlil,", "131,", "kgibran@gmail.com,", "NY\n"),
("Trump,", "Donald,", "415,", "dtrump@gmail.com,", "ID\n"),
("Nsukami,", "Patrick,", "161,", "pnsukami@gmail.com,", "NJ\n"),
("Mane,", "Sadio,","718,", "smane@aol.com,", "CT\n"),
("Longbottom,", "Nevill,", "192,", "lnevill@gmail.com,", "ID\n"),
("Collins,", "Hope,", "021,", "hcollins@aol.com,", "CA\n")]

with open("/Users/digitalisdiana/Documents/DSInt_Scripts/contact_list.csv", "w+") as full_contacts :
    for line in my_contacts:
        full_contacts.writelines(line)

###from contact_list, create NY_contact_list

with open("/Users/digitalisdiana/Documents/DSInt_Scripts/NY_contacts.csv", "w+") as contacts_NY :
    with open("/Users/digitalisdiana/Documents/DSInt_Scripts/contact_list.csv", "r") as full_contacts :
        for line in full_contacts:
            line = line.split(",")
            if line[-1] == "NY\n": #of if line[-1].strip() == "NY"
                contacts_NY.writelines(line)
    

## b. Afficher une synthèse du fichier de contact avec les éléments suivants :
## i. - nombre total de contacts

def number_of_contacts():
    with open("contact_list.csv", "r") as contacts:
        line_count = 0
        while True:
            for line in contacts:
                line_count += 1
                if line == "\n":
                    break
            return line_count - 1    

contacts_counted = number_of_contacts()
print(contacts_counted)


## ii. - nombre d’email par domaine d’adresse (combien d’email en @yahoo.com, en @gmail.com, etc...)

## iii. - nombre de contacts dans chaque ETAT (NY, CA, etc.)




# EXERCISE 3 : Publipostage

###Nous souhaitons envoyer un message personnalisé à chacun de nos contacts. Le message personnalisé est le suivant :
#Bonjour <<prénom>> <<nom>>,
#Nous vous rappelons que vous êtes actuellement abonnés à notre newsletter avec l’email <<email>>.
#Vous recevrez donc un email de notre part chaque mois.
#Si vous souhaitez vous désabonner, merci de bien vouloir écrire à
#l’adresse suivante : ​desabo@pythondit.com Bien cordialement,
#L’équipe Python with DIT
#￼￼Créer un fichier “publipostage.txt” qui comprend l’ensemble des messages à envoyer aux contacts avec l’email d’envoi. Les premières lignes du fichier “publipostage.txt” doivent ressembler à ceci :
#Destinataire : ​lpaprocki@hotmail.com Bonjour Lenna Patrocki,
#Nous vous rappelons que vous êtes actuellement abonnés à notre newsletter avec l’email lpaprocki@hotmail.com.
#Vous recevrez donc un email de notre part chaque mois.
#Si vous souhaitez vous désabonner, merci de bien vouloir écrire à
#l’adresse suivante : ​desabo@pythondit.com Bien cordialement,
#L’équipe Python with DIT





# EXERCISE 4 : Dédoublonnage
###Il y a malheureusement beaucoup de noms en double dans le fichier “liste_doublon.csv”. Créer un fichier sans les doublons et l’appeler “liste_ok.csv”




# EXERCISE 5 : Ajout de la désignation des produits
###Le fichier “achats.csv” contient le nom des clients et l’ID du produit acheté. Malheureusement dans ce fichier on ne comprends pas tout de suite ce que le client a acheté si l’on ne connaît pas l’ID du produit.
###Pour pallier à cela, créer un fichier “achats_designation.txt” qui contient une colonne supplémentaire avec la désignation du produit acheté.
###Le lien entre le nom des produits et les références se trouve dans le fichier id_designation.csv
