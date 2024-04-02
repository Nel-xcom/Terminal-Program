import usuarios.usuario as consultas
import notas.acciones

"""
Usuario
-REGISTRO | LOGIN

Notas
-Crear | Mostrar | Eliminar | Salir
"""
class Acciones:
    #--Resgistro de usuarios
    def registros(self):
        #Formulario
        print("\n¡Comencemos!")
        nombre = input("- Nombre: ").lower()
        apellido = input("- Apellido: ").lower()
        email = input("- Email: ").lower()
        password = input("- Contraseña: ")

        #Almacenar datos de formulario en una variable
        usuario = consultas.Usuario(nombre, apellido, email, password)
        #Usando query de file usuario para guardar datos
        registro = usuario.registrar()
        #Registro existoso
        if registro[0] >= 1:
            print(f"\n¡Gracias {registro[1].nombre}! Ya fuiste registrado")
        #Registro denegado
        else:
            print(f"\nNo te has registrado correctamente.")


    def login(self):
        print("\nUn placer tenerte de vuelta...")
        #Formulario LOGIN
        email = input("Email: ")
        password = input("Contraseña: ")

        #Query identificar usuario
        usuario = consultas.Usuario('', '', email, password)
        ingreso = usuario.identificar()
        #LOGIN existoso
        if email == ingreso[3]:
            print(f"\nBienvenido {ingreso[1]}, te has registrado en el sistema el {ingreso[5]}")
            #Opciones NOTAS
            self.proximasAcciones(ingreso)

    
    def proximasAcciones(self, usuario):
        #Formulario NOTAS
        print("\nAcciones disponibles: \n")
        print("-Para crear notas inserta: 'crear'\n-Para mostrar notas inserta: 'mostrar'")
        print("-Para eliminar notas inserta: 'eliminar'\n-Para salir inserta: 'salir'")

        accion = input("\n-Escribe aqui respuesta: ").lower()
        hazEl = notas.acciones.Acciones()
        #CREANDO NOTAS
        if accion == "crear":
            print("\n¡Comencemos!")
            hazEl.crearNota(usuario)
            self.proximasAcciones(usuario)
        #MOSTRANDO NOTAS
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        #ELIMINANDO NOTAS
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        #SALIR DEL PROGRAMA
        elif accion == "salir":
            print(f"\n## Hasta pronto {usuario[1]} ##")
            exit()        