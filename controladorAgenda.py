from modeloAgenda import *
from vistaAgenda import *
from controladorContactos import ControladorContacto


class Controlador():
    def __init__(self):
        self.__vistaAgenda = Vista()
        self.Home()
    
    def Home(self):
        
        opcion = self.__vistaAgenda.Mostrame()

        if opcion == 1:
            self.MostrarTodos()
        elif opcion == 2:
            self.Buscar()
        elif opcion == 3:
            self.Actualizar()
        elif opcion == 4:
            self.Eliminar()
        elif opcion == 5:
            self.Agregar()
        elif opcion == 6:
            self.Contactos()
        elif opcion == 7:
            self.Salir()


    def Contactos(self):
        texto = "ver los Contactos"
        existe = self.Buscar(texto)
        if existe:
            ControladorContacto(existe[0].id)
        else:
            op = self.__vistaAgenda.ErrorActualizar()
            if op:
                self.Agregar()
        self.Home()
    
    def MostrarTodos(self):
        r = agenda.Todas()
        self.__vistaAgenda.Resultados(r)
        self.Home()

    def Salir(self):
        self.__vistaAgenda.closse()

    def Agregar(self):
        texto = "Agregar"
        dato = self.__vistaAgenda.PedirDatos(texto,"propietario")
        p = agenda(dato["propietario"])
        p.save()
        self.Home()

    def Eliminar(self):
        texto = "Eliminar"
        dato = self.__vistaAgenda.PedirDatos(texto,"propietario")
        r = agenda(dato['propietario'])
        r.delete()
        self.Home()

    def Buscar(self, tex = ''):
        # tex esta para comprobar la existencia cuando tengo que actualizar
        texto = tex or "Buscar" 
        dato = self.__vistaAgenda.PedirDatos(texto,"propietario")
        r = agenda(dato['propietario'])
        r = r.mostrar()
        if tex:
            return r
        else:
            self.__vistaAgenda.Resultados(r)
            self.Home()
    
    def Actualizar(self):
        texto = "Actualizar"
        existe = self.Buscar(texto)
        if existe:
            dato = self.__vistaAgenda.PedirDatos(texto,"propietario")
            print(existe[0].id)
            p = agenda((dato["propietario"] or existe[0].propietario), existe[0].id)
            p.update()
        
        else:
            op = self.__vistaAgenda.ErrorActualizar()
            if op:
                self.Agregar()
        self.Home()

#-----Ejecucion-----#
Controlador()