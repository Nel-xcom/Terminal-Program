#--LIBRERIAS
from usuarios import acciones

#--MENSAJE INICIAL
print("""
######################      
   ## Bienvenido ##\n
Elige una de las siguentes opciones:\n
- Iniciar sesión
- Regitrarme
""")

#--ACCIONES
hazEl = acciones.Acciones()

#--USER ANSWEAR
accion = input(": ").lower()

#--CREAR REGISTRO
if accion == "registrarme":
    hazEl.registros()
#--LOGIN
elif accion == "iniciar sesion":
    hazEl.login()