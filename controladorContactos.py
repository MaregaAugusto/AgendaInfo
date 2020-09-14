from modeloContactos import *
from vistaContactos import *


class ControladorContacto():
    def __init__(self,agenda):
        self.agenda = agenda 
        self.__vistaContacto = Vista()
        self.Home()
    
    def Home(self):
        opcion = self.__vistaContacto.Mostrame()

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
            self.Salir()
    
    def MostrarTodos(self):
        r = contacto.Todas(self.agenda)
        self.__vistaContacto.Resultados(r)
        self.Home()

    def Salir(self):
        self.__vistaContacto.closse()

    def Agregar(self):
        texto = "Agregar"
        dato = self.__vistaContacto.PedirDatos(texto,"nombre","telefono","email")
        p = contacto(self.agenda,dato["nombre"],dato["telefono"],dato["email"])
        p.save()
        self.Home()

    def Eliminar(self):
        texto = "Eliminar"
        dato = self.__vistaContacto.PedirDatos(texto,"nombre")
        contacto.delete(self.agenda,dato["nombre"])
        self.Home()

    def Buscar(self, tex = ''):
        # tex esta para comprobar la existencia cuando tengo que actualizar
        texto = tex or "Buscar" 
        dato = self.__vistaContacto.PedirDatos(texto,"nombre")
        r = contacto.mostrar(self.agenda, dato['nombre'])
        if tex:
            return r
        else:
            self.__vistaContacto.Resultados(r)
            self.Home()
    
    def Actualizar(self):
        texto = "Actualizar"
        existe = self.Buscar(texto)
        if existe:
            dato = self.__vistaContacto.PedirDatos(texto,"nombre","telefono","email")
            p = contacto(self.agenda,
                        (dato["nombre"] or existe[0].nombre),
                        (dato["telefono"] or existe[0].telefono),
                        (dato["email"] or existe[0].email),
                        existe[0].id)
            p.update()
        
        else:
            op = self.__vistaContacto.ErrorActualizar()
            if op:
                self.Agregar()
        self.Home()