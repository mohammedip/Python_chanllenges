print("Enter your information please")

name = input("name : ")

try:
    salaire = int(input("salaire horaire  : "))
except ValueError:
    print("you need to enter a number")
    quit()

try:
    nombre_heures = int(input("nombre d'heures travaillées : "))
except ValueError:
    print("you need to enter a number")
    quit()

if(nombre_heures <= 40):
    result = salaire * nombre_heures
else:
    result = (40 * salaire)+((nombre_heures-40) * (salaire * 1.5)) 

print(f"hello {name} you earn this month {result}")


