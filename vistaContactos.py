import os

class Vista(object):

    def __init__(self):
        self.op1 = "Mostrar Todos los Contactos"
        self.op2 = "Buscar Contacto"
        self.op3 = "Modificar Contacto"
        self.op4 = "Eliminar Contacto"
        self.op5 = "Agregar Contacto"
        self.op6 = "Volver al menu de Agenda"

    def Mostrame(self):
        os.system('cls')
        print("-------Soy Menu de Contacto de ------------")
        print(f"1--{self.op1}")
        print(f"2--{self.op2}")
        print(f"3--{self.op3}")
        print(f"4--{self.op4}")
        print(f"5--{self.op5}")
        print(f"6--{self.op6}")
        return int(input())
    
    def Resultados(self, resultado):
        os.system('cls')
        print("----------Resultado-----------------")
        for r in resultado:
            print(r)
        input()
    
    def PedirDatos(self,texto, *argu):
        os.system('cls')
        dato = dict()
        print("Por favor ingrese los datos para "+texto+" la contacto")
        for d in argu:
            dato[d] = input(d+": ")
        return dato

    def closse(self):
        os.system('cls')
    
    def ErrorActualizar(self):
        print("No existe esa contacto quiere crearla precione cualquier letra")
        return input()