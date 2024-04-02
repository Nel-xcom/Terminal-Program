#PAQUETES Y LIBRERIAS
import conexion
import datetime
#CONEXION A LA DB
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
#OBJETO NOTAS
class Notas:
    #CONSTRUCTOR
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    #FUNCION GUARDAR NOTAS
    def guardar(self):
        #QUERY
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        #EJECUTANDO QUERY
        cursor.execute(sql, nota)
        #GUARDANDO CAMBIOS
        database.commit()

        return [cursor.rowcount,self]
    #FUNCION MOSTRAR NOTAS
    def listar(self):
        #QUERY
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        #EJECUTANDO QUERY
        cursor.execute(sql)
        #MOSTRANDO DATOS
        result = cursor.fetchall()

        return result
    #FUNCION ELIMIANAR NOTAS
    def eliminar(self, titulo):
        #QUERY
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        #EJECUTANDO QUERY
        cursor.execute(sql)
        #GUARDANDO DATOS
        database.commit()

        return[cursor.rowcount, self]