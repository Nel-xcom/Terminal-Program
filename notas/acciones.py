import notas.nota as modelo

#MENSAJES
class Acciones:
    #FORMULARIO CREAR NOTAS
    def crearNota(self, usuario):
        
        print(f"{usuario[1]}! vamos a crear una nueva nota")
        #DATOS DE LA NOTA
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        #CREANDO MODELO DE DATOS
        nota = modelo.Notas(usuario[0], titulo, descripcion)
        #GUARDANDO DATOS EN LA DB
        guardado = nota.guardar()
        #NOTAS CHECKER
        if guardado[0] >= 1:
            print(f"\n Perfecto, la nota {nota.titulo} se ha guardado!")

        else:
            print(f"\n No se ha guardado la nota {usuario[1]}")
    #MOSTRANDO NOTAS
    def mostrar(self, usuario):
        print("\n**********************")
        print(f"Vale {usuario[1]}! Aqui tienes tus notas: \n")
        #MOSTRANDO LAS NOTAS DEL USUARIO LOGUEADO
        nota = modelo.Notas(usuario[0])
        notas = nota.listar()
        #RECORRIENDO LAS NOTAS
        for nota in notas:
            print(f"\n- Titulo: {nota[2]}")
            print(f"- Descripcion: {nota[3]}")
        print("\n**********************")
    #BORRANDO NOTAS
    def borrar(self, usuario):
        print(f"\n {usuario[1]}! Eliminemos la nota")
        #FORMULARIO ELIMINAR
        titulo = input("\n- Introduce el titulo de la nota a borrar: ")
        #ELIMINANDO LA NOTA DEL USUARIO LOGUEADO
        nota = modelo.Notas(usuario[0], titulo)

        eliminar = nota.eliminar(titulo)
        
        if eliminar[0] >= 1:
            print("\n**********************")
            print(f"Hemos borrado la nota: {nota.titulo}")
            print("**********************")

        else:
            print("No pudimos borrar la nota. Intentalo mas tarde")