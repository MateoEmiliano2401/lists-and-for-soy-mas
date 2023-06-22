#cada estudiante del arreglo students tiene sus calificaciones en el arreglo grades, manteniendo su posicion
students = ["Ignacia", "Poulette","Vane","Jazz","tuguitugui"]
grades = [[5,6,4,5,6],[5,6,7,4,5],[5,6,4,5,6],[4,5,6,5,4],[5,6,4,5,6]]
#Se pide un programa que imprima el nombre de la estudiante, junto con el promedio de sus notas.


position = 0
while position < len(students):
    student = students[position] #str
    student_grades = grades[position] #list
    sum = 0
    position_two = 0
    while position_two < len(student_grades):
        sum += student_grades[position_two]
        position_two += 1
    position +=1 
    print(f"El promedio de la estudiante {student} es: \n {sum/len(grades)}")
            