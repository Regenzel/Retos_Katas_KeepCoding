customers = {}
admins = {}
from Reto2_clases import Cliente
from Reto2_clases import Admin

def register_menu():
        print("---Registro---")
        user_rol = input("¿El usuario es administrador o cliente?: ")
        user_name = input("Escriba el nombre de usuario: ")
        password = input("Escriba una contraseña: ")
        if user_rol == "administrador":
            admins[user_name]= password
        elif user_rol == "cliente":
            customers[user_name]= password
        print(f"{customers}{admins}")

def login_menu():
    print("----Inicio de sesión----")
    user_name = input("Nombre de usuario: ")
    if user_name in customers.keys() or user_name in admins.keys():
        password = input("Contraseña: ")
    else:
        print("Introduzca un usuario existente")
    

def general_menu():
    print("-----Sistema de autencicación-----")
    print("1. Registrar nuevo usuario\n2. Iniciar sesión\n3. Salir")
    answer = input("")
    if answer == "1":
        register_menu()
    if answer == "2":
         login_menu()
    if answer == "3": # Opcion de salir
         pass
    
general_menu()



