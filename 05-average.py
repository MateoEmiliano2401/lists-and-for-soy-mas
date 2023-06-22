

grades = []
menu_option = ""

while menu_option != "3":
    print("calculadora de promedios")
    print("1. Agregar nota")
    print("2. Caldular promedio")
    print("3. Salir")

    menu_option = input()
    
    if menu_option == "1":
        number = float(input("Ingresa la nota: \n"))
        grades.append(number)
    elif menu_option == "2":
        #sumar todas la notas y dividir por la cantidad
        #acumulador 
        sum = 0
        for grade in grades:
            sum += grade
        print(f"El promedio de las notas es: {sum/len(grades)}")
    elif menu_option == "3":
        print("Chaucito")
    else:
        print("Ingrese una opcion valida")
    