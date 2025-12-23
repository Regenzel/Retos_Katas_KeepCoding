class User:
    role = "None" 
    def __init__(self,user,password):
        self.user = user
        self.password = password
    
    def menu(self):
        print("-----Sistema de autencicación-----")
        print("1. Registrar nuevo usuario\n2. Iniciar sesión\n3. Salir")
    

class Customer(User):
    role = "Customer"
    def menu(self):
        print("---Menú de Cliente---")
        print("1. Ver productos\n2. Comprar\n3. Salir")
    
class Admin(User):
    role = "Admin"
    def menu(self):
        print("---Menú de Admin---")
        print("1. Ver lista de usuarios\n2. Crear nuevo usuario\n3. Eliminar usuarios\n4. Salir")