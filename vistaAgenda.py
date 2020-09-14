import os

class Vista(object):
    
    def __init__(self):
        self.op1 = "Mostrar Todos las Agendas"
        self.op2 = "Buscar Agenda"
        self.op3 = "Modificar Agenda"
        self.op4 = "Eliminar Agenda"
        self.op5 = "Agregar Agenda"
        self.op6 = "Ver Contactos"
        self.op7 = "Salir"

    def Mostrame(self):
        os.system('cls')
        print("-------Soy Menu de Agenda------------")
        print(f"1--{self.op1}")
        print(f"2--{self.op2}")
        print(f"3--{self.op3}")
        print(f"4--{self.op4}")
        print(f"5--{self.op5}")
        print(f"6--{self.op6}")
        print(f"7--{self.op7}")
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
        print("Por favor ingrese los datos para "+texto+" la agenda")
        for d in argu:
            dato[d] = input(d+": ")
        return dato

    def closse(self):
        os.system('cls')
    
    def ErrorActualizar(self):
        print("No existe esa agenda quiere crearla precione cualquier letra")
        return input()