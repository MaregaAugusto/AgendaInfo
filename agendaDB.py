import pyodbc

class DB():
    
    def __init__(self,name, server = 'localhost\SQLEXPRESS',
        driver= "SQL Server Native Client 11.0"):
        
        self.name = name
        self.server = server
        self.driver = driver
        self.datos = None

    def conectar(self):
            try:
                self.conexion = pyodbc.connect("DRIVER={"+self.driver+"};"
                                            "Server="+self.server+";"
                                            "DATABASE="+self.name+";"
                                            "Trusted_Connection=yes;")
            except Exception as e:
                # Atrapar error
                print("Ocurrió un error al conectar a SQL Server: ", e)

    def cursor(self):
        self.__cursor = self.conexion.cursor()
    
    def commit(self, query):

        esselect = query.count('SELECT')
        if esselect == 0:
            self.conexion.commit()
    
    def cerrar(self):
        self.conexion.close()
    
    def consulta(self,q,v):
        if v:
            self.__cursor.execute(q,v)
        else:
            self.__cursor.execute(q)

    def obtener_datos(self, query):
        esselect = query.count('SELECT')
        if esselect > 0:
            self.datos = self.__cursor.fetchall()

    def ejecutar(self,query,values = None):
        self.conectar()
        self.cursor()
        self.consulta(query,values)
        self.commit(query)
        self.obtener_datos(query)
        self.cerrar()
        
        return self.datos