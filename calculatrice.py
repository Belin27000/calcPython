
digit_check=False

while not digit_check:
    first_number = input("Entrer un premier nombre :")
    second_number = input("Entrer un deuxième nombre :")
    digit_check=first_number.isdigit() and second_number.isdigit()
    if not digit_check:
        print('Veuillez entrer deux nombres valides')

else:
    resultat = f"Le résultat de l'addition de {first_number} avec {second_number} est égal à {int(first_number) + int(second_number)}"
    print(resultat)

