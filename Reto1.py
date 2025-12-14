# Tiene que: AGREGAR estudiantes, QUITAR estudiantes.
# MOSTRAR todos los estudiantes aprobados, BUSCAR estudiantes por nombre y mostrar su promedio.
# mostrar TODOS los estudiantes.
# SALIR del programa.
students = {}
student_name = ""
student_grade = 0
continue_program = True
not_correct_name = True
not_valid_grade = True
key_words = ["agregar", "quitar", "mostrar", "buscar", "todos", "salir"]

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
        

while continue_program == True:
    question = input("¿Agregar estudiantes, quitar estudiantes, mostrar los aprobados, mostrar todos o buscar el promedio de uno?" \
    "(Responda agregar/quitar/mostrar/buscar/todos/salir): ")
    # Si la respuesta esta dentro de lo esperado, se ejecuta
    if question in key_words: 
    # AGREGA a 'students' nuevos estudiantes con sus promedios de notas.
        if question == "agregar":
            student_name = input("¿Como se llama el estudiante?: ")    
            while not_valid_grade == True:
                # Mientras que no me de un valor valido entre 0 y 10 no sigue el programa
                student_grade1 = input("Ingrese la primera nota (entre 0 y 10): ")
                student_grade2 = input("Ingrese la segunda nota (entre 0 y 10): ")
                student_grade3 = input("Ingrese la tercera nota (entre 0 y 10): ")
                if student_grade1.isnumeric() and student_grade2.isnumeric() and student_grade3.isnumeric():
                    if 0.0 <= float(student_grade1) <= 10.0 and 0.0 <= float(student_grade2) <= 10.0 and 0.0 <= float(student_grade3) <= 10.0:
                        not_valid_grade = False
                if not_valid_grade == True:
                    print("La nota no esta entre 0 y 10. Repite las notas.")
                    
            avg = average(float(student_grade1),float(student_grade2),float(student_grade3))
            students[student_name] = avg
            print(f'Has añadido a "{student_name}" con promedio de nota de {avg}')

        # QUITA de 'students' al estudiante que escriba el usuario. 
        if question == "quitar":
            student_name = input("¿Como se llama el estudiante?: ")
            students.pop(student_name)
            print(f'Has eliminado a "{student_name}" de la lista')
        # MUESTRA los estudiantes aprobados.
        if question == "mostrar":
            for key,value in students.items():
                if value >= 6:
                    print(f"{key}, nota media de: {value}")
        # BUSCA al estudiante que el usuario escriba y devuelve su nombre con su respectivo promedio.
        if question == "buscar":
            student_name = input("¿Como se llama el estudiante?: ")
            if student_name in students.keys():
                print(f"{student_name}, nota media de: {students.get(student_name)}")
            else:
                print("Ese estudiante no existe.")
        # Muestra TODOS los estudiantes.
        if question == "todos":
            for key,value in students.items():
                print(f"{key}, nota media de: {value}")
        # SALE del programa.
        if question == "salir":
            continue_program = False
    else:
        print("Inserte un valor válido (agregar/quitar/mostrar/buscar/todos/salir)")
