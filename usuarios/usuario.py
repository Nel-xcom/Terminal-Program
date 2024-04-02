#--LIBRERIAS
import conexion
import datetime
import hashlib


#--DB CONNECT + CURSOR
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

#--CLASE DATOS DEL USUARIO
class Usuario:


    #--CREANDO UNA INSTANCIA
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password


    #--REGISTRAR USUARIO
    def registrar(self):
        #-FECHA DE CREACION
        creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #--CIFRAR CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #--QUERY SQL
        query = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        #--DEFINIENDO LOS DATOS
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), creation_date)

        #--TESTEANDO BLOQUE SENSIBLE
        try:
            #--EJECUTANDO QUERY
            cursor.execute(query, usuario)
            #--GUARDANDO DATOS
            database.commit()
            result = [cursor.rowcount, self]
        #--CAPTURANDO EXCEPCION
        except:
            result = [0, self]

        return result

    #--LOGIN DE USUARIO
    def identificar(self):
        #--CONSULTA PARA COMPROBAR SI EXISTE EL USUARIO
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #--CIFRAR CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #--DATOS PARA LA CONSULTA
        usuario = (self.email, cifrado.hexdigest())

        #--EJECUTANDO QUERY
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
    