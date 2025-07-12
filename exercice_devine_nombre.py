import random

def jouer():
    print("Salut ! Bienvenue dans le jeu de devinette de nombre.")
    nombre = random.randint(1, 100)
    essais = 0
    max_essais = 6

    while essais < max_essais:
        try:
            devine = int(input(f"Essai {essais + 1}/{max_essais} – Devinez le nombre entre 1 et 100 : "))
            if devine < 1 or devine > 100:
                print("Veuillez entrer un nombre entre 1 et 100.")
                continue
            essais += 1

            if devine < nombre:
                print("C'est plus grand !")
            elif devine > nombre:
                print("C'est plus petit !")
            else:
                print(f"Bravo ! Vous avez deviné le nombre {nombre} en {essais} essai(s) !")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    else:
        print(f"Dommage ! Le nombre était {nombre}. Essayez encore une fois plus tard.")

# === Boucle de rejouabilité ===
while True:
    jouer()
    rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
    while rejouer not in ['o', 'n']:
        rejouer = input("Réponse invalide. Veuillez entrer 'o' pour oui ou 'n' pour non : ").lower()
    if rejouer == 'n':
        print("Merci d'avoir joué ! À bientôt.")
        break
