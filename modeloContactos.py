from agendaDB import *

class contacto():
    DBS = DB(name = 'AgendaDB')
    tableName = 'contacto'
    def __init__(self,agenda,nombre,telefono,email,id = None):
        self.id = id
        self.agenda = agenda
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    
    def save(self):
        query = "INSERT INTO "+contacto.tableName+"(agenda,nombre,telefono,email) VALUES (?,?,?,?)"
        values = (self.agenda,self.nombre,self.telefono,self.email)
        contacto.DBS.ejecutar(query, values)

    def mostrar(self):
        query = "SELECT * FROM "+contacto.tableName+" WHERE agenda = ? AND nombre = ?"
        valor = (self.agenda, self.nombre)
        return contacto.DBS.ejecutar(query, valor)

    def delete(self):
        query = "DELETE FROM "+contacto.tableName+" WHERE agenda = ? AND nombre = ? "
        valor = (self.agenda, self.nombre)
        contacto.DBS.ejecutar(query, valor)

    def update(self):
        query = "UPDATE "+contacto.tableName+" SET nombre = ?, telefono = ?, email = ? WHERE id = ? "
        valor = (self.nombre, self.telefono, self.email, self.id)
        contacto.DBS.ejecutar(query, valor)

    @classmethod
    def Todas(cls, miagenda):
        query = "SELECT * FROM "+contacto.tableName+" WHERE agenda = ?"
        return contacto.DBS.ejecutar(query, miagenda)