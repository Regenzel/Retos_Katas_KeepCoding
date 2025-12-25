customers_data = {"Fer":"quetal"}
admins_data = {"Ivan":"hola", "Fer":"quetal"}
from clases_de_Reto2 import User
from clases_de_Reto2 import Customer
from clases_de_Reto2 import Admin
user = User("None", "None")
customers = Customer(customers_data.keys(), customers_data.values())
admin = Admin(admins_data.keys(), admins_data.values())

         
def register_menu():
        print("---Registro---")
        user_rol = input("¿El usuario es administrador o cliente?: ")
        user_name = input("Escriba el nombre de usuario: ")
        if user_name in customers_data.keys() or user_name in admins_data.keys():
            print("Usuario ya registrado")
        password = input("Escriba una contraseña: ")
        
        if user_rol == "admin":
            admin = Admin(user_name, password)
            admins_data[admin.user]= admin.password
        elif user_rol == "cliente":
            customer = Customer(user_name, password)
            customers_data[customer.user]= customer.password
            
        print(f"{customers_data}{admins_data}") # Temporal hasta que funcione todo bien

def login_menu():
    print("----Inicio de sesión----")
    user_name = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    if user_name in customers_data.keys() and password in customers_data.values(): # Arreglar login
        customers.menu()
    elif user_name in admins_data.keys() and password in admins_data.values(): # Arreglar login
        admin.menu(customers_data.keys(), admins_data.keys())
    else:
        print("Introduzca un usuario existente")


def general_menu():
    print("-----Sistema de autencicación-----")
    print("1. Registrarse\n2. Iniciar sesión\n3. Salir")
    answer = input("**Escriba el numero de opcion que quiera usar: ")
    if answer == "1":
        register_menu()
    if answer == "2":
        login_menu()
    if answer == "3":
        pass
    
general_menu()
    



