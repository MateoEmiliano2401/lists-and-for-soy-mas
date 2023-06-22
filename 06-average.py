
grades = [4,5,6,7,8,3,4,5,6,7,2]
position = 0
#Acumulador 
sum = 0
for grade in grades:
    sum += grade
    

print(f"El promedio de la nota es: {sum/len(grades)}")
