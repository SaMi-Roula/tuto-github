import random
nombre=random.randint(1, 100)
devine_nombre=input("Devinez le nombre entre 1 et 100 : ")
i= 0
print("Salut ! Bienvenue dans le jeu de devinette de nombre.")
while int(devine_nombre) != nombre:
    if int(devine_nombre) < nombre:
        print("C'est plus grand !")
    elif int(devine_nombre) > nombre:
        print("C'est plus petit !")
    devine_nombre=input("Essayez encore : ")
    i += 1
print("Vous avez trouvé le nombre en", i, "essais.")
print("Bravo ! Vous avez deviné le nombre :", nombre)
print("Merci d'avoir joué !")