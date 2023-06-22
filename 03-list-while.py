# El while es la estructura de control que ejecuta una serie de sentencias hasta que su condicion no se cumpla 

fruits = ["Chocolate", "Frugele", "Papas fritas"]
position = 0
while position < len(fruits):

    print(fruits[position])
    position = position + 1

print("------------------------------------------------")

for fruit in fruits:
    print(fruit)