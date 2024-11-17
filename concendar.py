# Concendar -- Juan García Lanza -- 2º Bachillerato Tecnológico (Febrero 2023)

# Módulo Pickle --> Lo uso para guardar mi lista de conciertos en un archivo .txt (creo una pequeña base de datos en un archivo de texto).

import pickle
conciertos = []
try:
    with open("conciertos.txt", "rb") as archivo:
        conciertos = pickle.load(archivo)
except FileNotFoundError:
    pass

# Funciones --> Aquí defino las funciones, que son las diferentes opciones que puedes hacer en mi programa.

def listar_conciertos():
    if conciertos:
        for c in conciertos:
            print(c)
    else:
        print("No hay ningún concierto, añade alguno en la opción *Añadir un nuevo concierto*")
    print(" ")
        

def listar_conciertos_por_lugar():
    lugar = input("Lugar del que quieres ver los conciertos: ")
    conciertos_filtrados = filter(lambda c: c["lugar"] == lugar , conciertos)
    encontrado = False
    for c in conciertos_filtrados:
        print(c)
        encontrado = True
    if not encontrado:
        print("No se ha encontrado ningún concierto en ese lugar")
    print(" ")
            
    
def añadir_concierto():
    id = input ("Introduce el nombre del concierto: ")
    fecha = input("Introduce la fecha del concierto: ")
    artista = input("Introduce el artista del concierto: ")  
    lugar = input("Introduce el lugar del concierto: ")
    precio = input("Introduce el precio del concierto: ")
    entrada = input("¿Tienes entrada para el concierto? (si o no): ")
    anotacion = input("Introduce alguna anotación del concierto si la necesita: ")

    nuevo_concierto = {"nombre": id, "fecha": fecha, "artista": artista, "lugar": lugar, "precio": precio, "entrada": entrada, "anotacion": anotacion}
    conciertos.append(nuevo_concierto)

    with open("conciertos.txt", "wb") as archivo:
        pickle.dump(conciertos, archivo)
    
    print("Se ha añadido el concierto correctamente")

    print(" ")

    
def eliminar_concierto():
    id = input("Introduce el nombre del concierto que quieres eliminar: ")
    for c in conciertos:
        if c["nombre"] == id:
            conciertos.remove(c)
            print("Se ha eliminado el concierto correctamente")
            break
        else:
            print("No hay ningún concierto con ese nombre")
            break

    with open("conciertos.txt", "wb") as archivo:
        pickle.dump(conciertos, archivo)
    
    print(" ")

# Menú principal --> Es la base del programa, ya que según la opción que elijas, llamará a las funciones que he definido arriba.

def menu():
    while True:
        print("* Menú principal. Seleccione una opción.         Bienvenido a Concendar!")
        print("1) Mis conciertos")
        print("2) Mis lugares")
        print("3) Añadir un nuevo concierto")
        print("4) Eliminar un concierto")
        print("5) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_conciertos()
           
        elif opcion == "2":
            listar_conciertos_por_lugar()

        elif opcion == "3":
            añadir_concierto()
    
        elif opcion == "4":
            eliminar_concierto()
    
        elif opcion == "5": 
            print("Saliendo... Gracias por usar Concendar!")
            break

        else:
            print("Opción no válida, seleccione otra por favor")

menu()