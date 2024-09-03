#Voila ma façon de ressoudre les exercices , c'est mes premier code python merci d'être indulgent ! 

def exercice_1():
    # Exercice 1: Ecrire un programme en langage Python qui demande à l'utilisateur de saisir son nom et de lui afficher son nom avec un message de bienvenue !
    nom = input("Quel est votre nom? ")
    print(f"Bonjour, {nom}!")
    
def exercice_2():
    # Exercice 2: Ecrire un programme en langage Python qui demande à l'utilisateur de saisir un nombre et de lui afficher son facteuriel.
    a = int(input("Entrez un nombre: "))
    b = int(input("Entrez un autre nombre: "))
    print(f"le resultat est {a + b}")
    
def exercice_3():
    #Ecrire un programme en Python qui demande à l'utilisateur de saisir deux nombres **a** et **b** et de lui afficher leur maximum.
    a = int(input("Entrez un nombre: "))
    b = int(input("Entrez un autre nombre: "))
    print(f"le max est {max(a,b)}")
    
def exercice_4():
    #Ecrire un programme en langage Python qui affiche les 100 premiers nombres entiers
    entier = []
    for i in range(1, 101):
        entier.append(i)
    print(entier)
        
def exercice_5():
    #Ecrire un programme en langage Python qui demande à l'utilisateur de saisir son nombre entier et de lui afficher si ce nombre est pair ou impair.
    nombre = int(input("Ecris un nombre entier :"))
    if nombre % 2 == 0:
        print("pair")
    else:
        print("impair")
        
def exercice_6():
    #Ecrire un programme en langage Python qui demande à l'utilisateur de saisir son âge et de lui afficher le message *"vous êtes Majeur !"* si l’âge tapé est supérieur ou égale à 18 et le message *"vous êtes mineur !"*  si l’âge saisi est inférieur à 18
    age = int(input("Ecris ton age :"))
    if age >= 18:
        print("tu est majeur harry !")
    else:
        print("tu est un enfant harry !")

def exercice_7():
    #Ecrire un programme en Python qui demande à l'utilisateur de saisir 3 nombre **x**, **y** et **z** et de lui afficher leur maximum
    valeurs = input("ecris plusieurs entier séparé par des espaces(1 13 300):")
    liste = valeurs.split()
    maxi = max(liste)
    print(maxi)
    
def exercice_8():
    #Ecrire un programme en Python qui demande à l'utilisateur de saisir un nombre entier **n** et de lui afficher la valeur de la somme *1 + 2 + … + n =*
    valeur = int(input("ecris un entier : "))
    liste = []
    for i in range (1, valeur+1):
        liste.append(i)
    print(sum(liste))

def exercice_9():
    #Ecrire un programme en Python qui demande à l'utilisateur de saisir un nombre entier **n** et de lui afficher *n !*
    n = int(input("entrer un nombre entier : "))    
    factorielle = 1
    for i in range(1, n+1):
        factorielle *= i
    print(f"{n}! = {factorielle}")
    
def exercice_10():
    #Ecrire un programme en Python qui demande à l’utilisateur de saisir le rayon d'un cercle et de lui renvoyer la surface et le périmètre.
    import math
    rayon = float(input("rayon du cercle:"))
    perimetre = 2 * math.pi * rayon
    surface = math.pi * rayon ** 2
    print(f"la sureface : {surface} et le perimetre : {perimetre}")
    
def exercice_11():

    #Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier **n** et de lui afficher tous les diviseurs de ce nombre.
    n = int(input("nombre entier: "))
    
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
        else:
            pass
    print(list)   
    
def exercice_12():
    #1. Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier **n** et de lui afficher la table de multiplication de ce nombre.
    #2. Améliorez le programme afin qu’il affiche les tables de multiplications de tous les nombres compris entre 1 et 9
    
    list = []
    for a in range(1, 10):
        for i in range(1, 11):
            multiplication = a * i
            print(f" {a} x {i} = {multiplication}")
        
def exercice_13():
    #Ecrire un programme en langage Python qui demande à l'utilisateur de saisir deux nombres entiers **a** et **b** et de lui afficher le quotient et le reste de la division euclidienne de a par b.
    a = int(input("ecris un entier:"))
    b = int(input("ecris un autre entier: "))

    calcul = a // b 
    reste = a % b
    
    print(f" quotien entier {calcul} , reste {reste}")
    
def exercice_14():
    #Ecrire un programme en langage Python qui demande à l'utilisateur de saisir un nombre entier **n** et de lui afficher si ce nombre est carré parfait ou non
    n = int(input("ecris un entier:"))
    for i in range(1, int(n**0.5) +1 ):
        if i * i == n:
            print("Carré parfait")
            break
    else:
        print("Essaye encore")
    
def exercice_15():
    #Ecrire un programme en langage Python qui demande à l'utilisateur de saisir un nombre entier **n** et de lui afficher si ce nombre est premier ou non.
    n = int(input("ecris un entier:"))
    
    if n <= 1:
        print("pas premier c'est sur")
        
    elif n == 2 or n == 3:
        print("premier c'est sur")
    
    else:    
        for i in range(2,  int(n**0.5) +1):
            if n % i == 0:
                print("pas premier")
                break
        else:
            print("premier")
    
    
def exercice_16(): 
#Ecrire un programme en langage Python qui permet de parcourir et afficher les caractères d’une variable du type chaine de caractères. Exemple pour **s = "Python"** , le programme affiche les caractères :   
    s = "python"
    for i in s:
        print(i)
    
    
def exercice_17():
    #Ecrire un programme en Python permettant d’afficher pour une chaine de caractères donnée, le nombre d’occurrences de chaque caractère dans la chaine. Exemple pour la chaine de caractère **s = "Python.org"** le programme doit afficher :  
    
    s = "python.org"
    dico = {}
    for i in s:
        if i in dico:
            dico[i] += 1  # Incrémente la valeur associée à la clé i
        else:
            dico[i] = 1  # Ajoute une nouvelle clé i avec la valeur 1
    
    for key in dico:           
        print(f"Le caractère :{key} figure {dico[key]} fois dans la chaine s ")
    
    
def exercice_18():
    #Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère **s** et de lui renvoyer un message indiquant si la chaine contient la lettre **'a'** tout en indiquant sa position sur la chaine. Exemple si l’utilisateur tape la chaine **s = ‘langage’** le programme lui renvoie :  
    #*La lettre 'a' se trouve à la position : 1*  
    #*La lettre 'a' se trouve à la position : 4*
    s = "langage"
    
    position = s.find('a')
    while position != -1:
        print(f"les  position de a sont :{position}")
        position = s.find('a', position + 1)
    





def main():
    choix = input("Entrez le numéro de l'exercice que vous souhaitez exécuter : ")

    # Construction du nom de la fonction dynamiquement
    nom_fonction = f"exercice_{choix}"
    
    # Récupération de la fonction dans le contexte global
    exercice = globals().get(nom_fonction)
    
    if exercice and callable(exercice):
        exercice()
    else:
        print("Choix non valide ou exercice non défini.")

if __name__ == "__main__":
    main()
