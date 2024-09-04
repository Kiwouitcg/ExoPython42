#1) Exercice 1 : bonjour - print(), range()
#Ecrire un programme qui affiche "bonjour".
#Bis : Mettre ce programme dans une fonction bonjour() qui prend en paramètres le nombre de fois que la fonction affichera "bonjour" et tester cette fonction.
def exercice_1():
    def bonjour(n):
        for _ in range(n):
            print("bonjour")
        
    n = int(input("Combien de bonjours ? : "))
    bonjour(n)
        
#2) Exercice 2 : input(), float(), math.pi, **, print()
#Écrire un programme qui demande à l'utilisateur de rentrer un rayon et la hauteur, puis qui calcule le volume d'un cône droit.
#Bis : Mettre ce programme dans une fonction volume_cone() et tester cette fonction.
def exercice_2():
    import math
    def volume_cone():
        r = float(input("rayon ? : "))
        h = float(input("hauteur ? : "))
        calcul = (1/3) * math.pi * r**2 * h
        
        print(calcul)
    volume_cone()
#3) Exercice 3 : input(), float(), print()
#Écrire un programme qui demande à l'utilisateur son poids et sa taille et qui calcule son IMC (trouver la formule sur internet).
#Bis : Mettre ce programme dans une fonction imc() et tester cette fonction.
def exercice_3():
    def imc():
        poids = int(input("poid ? : "))
        taille = float(input("taille ? :"))
        calcul = poids / (taille ** 2)
        print(calcul)
    imc()
#4) Exercice 4 : les distances - input(), float(), print()
#Écrire une fonction qui convertit en mètres par seconde et en km/h une vitesse fournie en paramètres par l'utilisateur en miles/heure (1 mile = 1609 mètres). Ce résultat sera retourné par la fonction.
def exercice_4():
    v = float(input("miles/heure ? : "))
    km_h = v * 1.60934
    m_h = v * 1609.34
    print(f" pour {v} Miles par heures on obitent en KM/H => {km_h} en M/H =>{m_h}")


#5) Exercice 5 : input(), int(), if, else, print(), %
#Écrire un programme qui demande à l'utilisateur de rentrer un entier n positif et qui affiche PAIR s'il est divisible par 2, IMPAIR sinon.
#Bis : Mettre ce programme dans une fonction pair() et tester cette fonction.
def exercice_5():
    def pair():
        n = int(input("entier positif : "))
        if n % 2 == 0:
            print("pair")
        else:
            print("impair")
    pair()
#6) Exercice 6 : random.randint(), input(), int(), for, if, else, print()
#Écrire un programme en python pour réviser ses tables de multiplication.
#Le programme tire au hasard deux entiers entre 0 et 10 et demande à l'utilisateur de donner leur produit.
#Si l'utilisateur répond juste, il gagne un point. S'il répond faux, il perd un point.
#On interrogera 5 fois l'utilisateur.
#Le programme affiche à la fin le score de l'utilisateur.
def exercice_6():
    import random
    
    score = 0
    for i in range(5):
            tirage1 = random.randint(0, 10)
            tirage2 = random.randint(0, 10)
            rep = tirage1 * tirage2
            print(f"{tirage1} multiplié par {tirage2} ?")
            r = int(input("tas réponse : "))
            if r == rep:
                print("+1 point")
                score +=1
            else: print('raté')
        
    print(f"ton score final est de {score} ! ")



#7) Exercice 7 : Devine un nombre - random.randint(), input(), int(), if, else, while, break, print()
#L'ordinateur tire un nombre entier au hasard entre 0 et 100.
#L'utilisateur doit le trouver et pour cela propose des valeurs.
#L'ordinateur indique pour chaque valeur proposée si la valeur est trop petite, trop grande ou s'il a trouvé.
#a) Écrire un programme en Python pour jouer à ce jeu.
#b) Modifier le programme pour qu'il s'arrête si l'utilisateur n'a pas trouvé au bout de 10 coups.
#c) Mettre ce programme dans une fonction plus_ou_moins() qui prendra en paramètres :
#le nombre min et max de la plage de tirage du nombre au hasard
#le nombre de coups maximum

def exercice_7():
    min = 0
    max = 100
    nombrederound = 10
    def plus_ou_moins(a,b,c):
        import random
        tirage = random.randint(a, b)
        for i in range(c):
            reponse = int(input("un nombre est tiré au sort , trouve le : "))
            if tirage == reponse: 
                print("gg tu as trouvé")
                break
            elif tirage < reponse:
                print("nan cherche plus petit")
            elif tirage > reponse:
                print(" nan chercher plus grand")
    plus_ou_moins(min,max,nombrederound)

#8) Exercice 8 : random.randint(), input(), int(), if, else, while, print()
#Écrire un programme qui tourne indéfiniment et qui demande à l'utilisateur de rentrer un nombre entier compris dans une plage définie aléatoirement (par exemple, entrer un nombre compris entre 12 et 34).
#Si le nombre entré est en dehors de la plage, le programme l'affiche et redemande à nouveau un nombre dans la même plage.
#Si le nombre entré est dans la plage, on félicite l'utilisateur et le programme reprend avec une nouvelle plage.

def exercice_8():
    import random
    while True:
        plage1 = random.randint(0, 100)
        plage2 = random.randint(0, 100)
        if plage1 > plage2:
            plage1, plage2 = plage2, plage1
        if plage1 == plage2:
            continue
        reponse = int(input("trouve la plage : "))
        if reponse in range(plage1, plage2):
            print('chammpiiionn')
        else: print("try again")



#9) Exercice 9 : input(), float(), while, if, else, print(), len(), max(), min(), sum()
#Écrire un programme permettant d'entrer des notes d’élèves sur 20 jusqu’à ce que l’utilisateur saisisse une note vide. Cette fonction retourne le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes.
def exercice_9():
    notes = [] 
    while True:
        add = (input("entrer les notes ici : "))
        if add == '':
            break
        addconv = float(add)
        notes.append(addconv)
    total = len(notes)
    notesmini = min(notes)
    notesmax= max(notes)
    moyenne = sum(notes) / len(notes)
    print(f"nombre de notes : {total}, note mini : {notesmini}, note maxi: {notesmax}, la moyenne {round(moyenne, 2)}")

#10) Exercice 10 : join()
#Écrivez un script qui demande à l'utilisateur une chaîne de caractères.
#Le script recopie la chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
#Par exemple, "gaston" devra devenir "g*a*s*t*o*n".
def exercice_10():
    n = input("ecris un mot : ")
    final = '*'.join(n)
    print(final)



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