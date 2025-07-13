print("Salut !")
print("Un mot de passe valide doit contenir au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial.")

def verifier_mot_de_passe(mdp):
    erreurs = []
    if len(mdp) < 8:
        erreurs.append("❌ Le mot de passe doit contenir au moins 8 caractères.")
    if not any(c.isupper() for c in mdp):
        erreurs.append("❌ Il faut au moins une lettre majuscule.")
    if not any(c.islower() for c in mdp):
        erreurs.append("❌ Il faut au moins une lettre minuscule.")
    if not any(c.isdigit() for c in mdp):
        erreurs.append("❌ Il faut au moins un chiffre.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in mdp):
        erreurs.append("❌ Il faut au moins un caractère spécial.")
    return erreurs

while True:
    # Demander un mot de passe valide
    while True:
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")
        erreurs = verifier_mot_de_passe(mot_de_passe)

        if not erreurs:
            print("✅ Le mot de passe est valide.\n")
            break
        else:
            print("Le mot de passe est invalide pour les raisons suivantes :")
            for erreur in erreurs:
                print(erreur)
            print("Veuillez réessayer.\n")

    # Demander si l'utilisateur veut refaire un autre mot de passe
    reessayer = input("Voulez-vous créer un nouveau mot de passe ? (o/n) : ").lower()
    while reessayer not in ['o', 'n']:
        reessayer = input("Réponse invalide. Entrez 'o' pour oui ou 'n' pour non : ").lower()

    if reessayer == 'n':
        print("Merci d'avoir utilisé le vérificateur de mot de passe ! À bientôt.")
        break
    print("Recommençons !\n")
    