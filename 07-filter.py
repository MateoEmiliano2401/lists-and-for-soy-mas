grades = [4,5,6,7,8,3,4,5,6,7,2]

#¿Como podriamos filtar los numeros pares e impares?
#pares
even = []
#impares
odd = []

#Es par cuando el resto o residuo de dividir al numero 2 es cero 

for grade in grades:
    if grade % 2 == 0: 
        even.append(grade)
    else:
        odd.append(grade)
    

print(f"los pares son{even}")
print(f"los impares son{odd}")