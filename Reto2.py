customers_data = {"Fer":"quetal"}
admins_data = {"Ivan":"hola", "Ferr":"quetal"}
#products = {"Tarjeta Grafica": "700€","CPU": "450€", "Memoria RAM": "9800€"}
from clases_de_Reto2 import User
from clases_de_Reto2 import Customer
from clases_de_Reto2 import Admin
user = User("None", "None")
customers = Customer(customers_data.keys(), customers_data.values())
admin = Admin(admins_data.keys(), admins_data.values())

         
def register_menu():
        continue_register = True
        while continue_register:
            print("---Registro---")
            user_rol = input("¿El usuario es administrador o cliente?\n(1. Admin/2. Cliente): ")
            if user_rol not in "12":
                print("Elija un rol valido (1. Admin/2. Cliente)")
            user_name = input("Escriba el nombre de usuario: ")
            password = input("Escriba una contraseña: ")
            if user_name in customers_data.keys() or user_name in admins_data.keys():
                print("Usuario ya registrado")
            elif user_name not in customers_data.keys() or user_name not in admins_data.keys():
                continue_register = False
                if user_rol == "1":
                    admin = Admin(user_name, password)
                    admins_data[admin.user]= admin.password
                elif user_rol == "2":
                    customer = Customer(user_name, password)
                    customers_data[customer.user]= customer.password
            
        print(f"{customers_data}{admins_data}") # Temporal para comprobaciones

def login_menu():
    print("----Inicio de sesión----")
    user_name = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    if user_name in customers_data and customers_data[user_name] == password:
        continue_customer = True
        while continue_customer:
            customers.menu()
            answer = input("**¿Que opción quiere usar?: ")
            if answer == "1":
                customers.see_products()
            elif answer == "2":
                customers.buy()
            elif answer == "3":
                continue_customer = False
            else:
                print("**Inserte una opción valida**")  
    elif user_name in admins_data and admins_data[user_name] == password:
        continue_admin = True
        while continue_admin:
            admin.menu()
            options = input("**¿Que opción quiere usar?: ")
            if options == "1":
                admin.see_users(customers_data.keys(), admins_data.keys())
            elif options == "2":
                register_menu()
            elif options == "3":
                which_role = input("¿Que rol tiene el usuario? (1. Admin, 2. Cliente): ")
                if which_role == "1":
                    delete_user = input("¿Que usuario quiere eliminar?: ")
                    if delete_user in admins_data.keys():
                        admins_data.pop(delete_user)
                elif which_role == "2":
                    if delete_user in customers_data.keys():
                        customers_data.pop(delete_user)
                print(f"{customers_data}{admins_data}") # Temporal para comprobaciones
            elif options == "4":
                continue_admin = False
            else:
                print("**Inserte una opción valida**")

    else:
        print("Usuario o contraseña incorrecto o inexistente")

def general_menu():
    continue_general = True
    while continue_general:
        print("-----Sistema de autenticación-----")
        print("1. Registrarse\n2. Iniciar sesión\n3. Salir")
        answer = input("**Escriba el numero de opcion que quiera usar: ")
        if answer == "1":
            register_menu()
        if answer == "2":
            login_menu()
        if answer == "3":
            continue_general = False
    
general_menu()
    



