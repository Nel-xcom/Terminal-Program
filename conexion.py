#--MYSQL
import mysql.connector


def conectar():
    ###---CONEXION A LA BASE DE DATOS
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        port = 3306
    )

    #--CURSOR + BUFFERED PARA BUEN MANEJO DE MEMORIA
    cursor = database.cursor(buffered=True)

    return [database, cursor]