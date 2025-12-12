students = {"Manolo":6, "Javier": 4, "Alfonso": 7}
student_name = ""
student_grade = 0
# Tiene que: AGREGAR estudiantes, QUITAR estudiantes.
# MOSTRAR todos los estudiantes aprobados, BUSCAR estudiantes por nombre y mostrar su promedio.
# SALIR del programa.
def average_grade(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

question = input("¿Agregar estudiantes, quitar estudiantes, mostrar los aprobados o buscar el promedio de uno?" \
"(Responda agregar/quitar/mostrar/buscar/salir)")
# AGREGA a 'students' nuevos estudiantes con sus promedios de notas.
if question == "agregar":
    student_name = input("¿Como se llama el estudiante?: ")
    student_grade1 = input("Ingrese la primera nota: ")
    student_grade2 = input("Ingrese la segunda nota: ")
    student_grade3 = input("Ingrese la tercera nota: ")
    avg = average_grade(float(student_grade1),float(student_grade2),float(student_grade3))
    students[student_name] = avg
    print(students)

# QUITA de 'students' al estudiante que escriba el usuario. 
if question == "quitar":
    student_name = input("¿Como se llama el estudiante?: ")
    students.pop(student_name)
    print(students)
# MUESTRA los estudiantes aprobados.
if question == "mostrar":
    for key,value in students.items():
        if value >= 6:
            print(f"{key}, nota media de: {value}")
# BUSCA al estudiante que el usuario escriba y devuelve su nombre con su respectivo promedio.
if question == "buscar":
    student_name = input("¿Como se llama el estudiante?: ")
    print(f"{student_name}, nota media de: {students.get(student_name)}")
if question == "salir":
    pass