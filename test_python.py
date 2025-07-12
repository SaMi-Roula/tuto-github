print("Salut mec ! Comment ça va ?")
print("aujourd'hui, on va convertir ensemble les temperatures de Celsius en Fahrenheit et vice versa !")
choix = input("Souhaitez-vous convertir de Celsius en Fahrenheit (1) ou de Fahrenheit en Celsius (2) ? ")
while choix not in  ["1", "2"]:
    choix = input("Veuillez entrer 1 pour Celsius vers Fahrenheit ou 2 pour Fahrenheit vers Celsius : ")
    print("Choix invalide. Veuillez entrer 1 ou 2.")
if choix == "1":
    celcusius = float(input("Entrez la temperature en celsius : "))
    fahrenheit = ((celcusius * 9) /5) + 32
    print(f"La temperature en Fahrenheit est : {fahrenheit}°F")
elif choix == "2":
    fahrenheit = float(input("Entrez la temperature en Fahrenheit : "))
    celsius = ((fahrenheit - 32) * 5) / 9
    print(f"La temperature en Celsius est : {celsius}°C")
else:
    print("Choix invalide. Veuillez entrer 1 ou 2.")