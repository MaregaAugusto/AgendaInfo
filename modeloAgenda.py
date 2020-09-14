from agendaDB import *

class agenda():
    DBS = DB(name = 'AgendaDB')
    tableName = 'agenda'
    def __init__(self,propietario,id = None):
        self.id = id
        self.propietario = propietario
    
    
    def save(self):
        query = "INSERT INTO "+agenda.tableName+"(propietario) VALUES (?)"
        values = (self.propietario)
        agenda.DBS.ejecutar(query, values)

    @classmethod
    def mostrar(cls, busca):
        query = "SELECT * FROM "+agenda.tableName+" WHERE propietario = ?"
        return agenda.DBS.ejecutar(query, busca)


    @classmethod
    def delete(cls, busca):
        query = "DELETE FROM "+agenda.tableName+" WHERE propietario = ?"
        agenda.DBS.ejecutar(query, busca)

    def update(self):
        query = "UPDATE "+agenda.tableName+" SET propietario = ? WHERE id = ? "
        valor = (self.propietario, self.id)
        agenda.DBS.ejecutar(query, valor)

    @classmethod
    def Todas(cls):
        query = "SELECT * FROM "+agenda.tableName
        return agenda.DBS.ejecutar(query)