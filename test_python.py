print("salut mec!\nque veut tu faire ?")
print("1 - convertir de celcius en fahrenheit")
print("2 - convertir de fahrenheit en celcius")
choix = input("choisis une option (1 ou 2): ")
while choix not in ["1", "2"]:
    print("option invalide, veuillez choisir 1 ou 2")
    choix = input("choisis une option (1 ou 2): ")
if choix == "1":
    celsius = float(input("entrez la temperature en celcius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C est égal à {fahrenheit}°F")
elif choix == "2":
    fahrenheit = float(input("entrez la temperature en fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F est égal à {celsius}°C") 
else:
    print("option invalide, veuillez choisir 1 ou 2")   
print("Merci d'avoir utilisé le convertisseur de température !")
print("Au revoir !")

    