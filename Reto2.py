customers_data = {}
admins_data = {}
from clases_de_Reto2 import User
from clases_de_Reto2 import Customer
from clases_de_Reto2 import Admin
user = User("None", "None")
customers = Customer(customers_data.keys(), customers_data.values())
#admin = Admin()

def general_menu():
    user.menu()
    answer = input("**¿Que quieres hacer?: ")


def register_menu():
        print("---Registro---")
        user_rol = input("¿El usuario es administrador o cliente?: ")
        user_name = input("Escriba el nombre de usuario: ")
        password = input("Escriba una contraseña: ")
        if user_rol == "admin":
            admin = Admin(user_name, password)
            admins_data[admin.user]= admin.password
        elif user_rol == "cliente":
            customer = Customer(user_name, password)
            customers_data[customer.user]= customer.password
            
        print(f"{customers_data}{admins_data}")

def login_menu():
    print("----Inicio de sesión----")
    user_name = input("Nombre de usuario: ")
    if user_name in customers_data.keys() or user_name in admins_data.keys():
        password = input("Contraseña: ")
    else:
        print("Introduzca un usuario existente")
    

    
    



