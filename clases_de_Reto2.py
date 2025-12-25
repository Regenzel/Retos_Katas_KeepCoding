class User:
    role = "None" 
    def __init__(self,user,password):
        self.user = user
        self.password = password
    

class Customer(User):
    role = "Customer"
    def menu(self):
        print("---Menú de Cliente---")
        print("1. Ver productos\n2. Comprar\n3. Salir")
        #options = input("**Escriba el numero de opcion que quiera usar: ")
    def see_products(self):
        print("---Productos---")
        print("1. Tarjeta Gráfica: 700€\n2. CPU: 450€\n3. Memoria RAM: 9800€\n4. Salir")
    def buy(self):
        print("---Comprar---")
        print("1. Tarjeta Gráfica: 700€\n2. CPU: 450€\n3. Memoria RAM: 9800€\n4. Salir")
        options = input("**¿Que quiere comprar? (elija numero): ")
        if options == "1":
            print("---Productos---")
            print("1. Tarjeta Gráfica: 700€\n2. CPU: 450€\n3. Memoria RAM: 9800€\n4. Salir")
        elif options == "2":
            print("---Comprar---")
            print("1. Tarjeta Gráfica: 700€\n2. CPU: 450€\n3. Memoria RAM: 9800€\n4. Salir")
            buy = input("**Escriba el numero del producto que quiera comprar: ")
            if buy == "1":
                print("Tarjeta grafica adquirida")
            elif buy == "2":
                print("CPU adquirida")
            elif buy == "3":
                print("Memoria RAM adquirida")
            elif buy == "4":
                pass

class Admin(User):
    role = "Admin"
    def menu(self):
        print("---Menú de Admin---")
        print("1. Ver lista de usuarios\n2. Crear nuevo usuario\n3. Eliminar usuarios\n4. Salir")
    def see_users(self,customers,admins):
        print("-Los admins son: ")
        for admin in admins:
            print(admin)
        print("-Los clientes son: ")
        for customer in customers:
            print(customer)
    #elif options == "2":
        # Ver la manera de acceder al menu de registro en esta opcion
            pass