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

    def mostrar(self):
        query = "SELECT * FROM "+agenda.tableName+" WHERE propietario = ?"
        valor = self.propietario
        return agenda.DBS.ejecutar(query, valor)

    def delete(self):
        query = "DELETE FROM "+agenda.tableName+" WHERE propietario = ?"
        valor = (self.propietario)
        agenda.DBS.ejecutar(query, valor)

    def update(self):
        query = "UPDATE "+agenda.tableName+" SET propietario = ? WHERE id = ? "
        valor = (self.propietario, self.id)
        agenda.DBS.ejecutar(query, valor)

    @classmethod
    def Todas(cls):
        query = "SELECT * FROM "+agenda.tableName
        return agenda.DBS.ejecutar(query)