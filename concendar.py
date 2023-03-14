    #Concendar
import pickle
conciertos = []
try:
    with open("conciertos.txt", "rb") as archivo:
        conciertos = pickle.load(archivo)
except FileNotFoundError:
    pass

# Menú principal

print("* Menú principal.Seleccione una opción.         Bienvenido a Concendar!")
print("1) Mis conciertos")
print("2) Mis lugares")
print("3) Añadir un nuevo concierto")
print("4) Eliminar un concierto")
print("5) Salir")

opcion = input("Seleccione una opción: ")

# Funciones menú

def listar_conciertos():
    for c in conciertos:
        if c == c:
            print(c)
        else:
            print("No hay ningún concierto, añade alguno en la opción *Añadir un nuevo concierto*")
    

def listar_conciertos_por_lugar():
    lugar = input("Lugar del que quieres ver los conciertos: ")
    conciertos_filtrados = filter(lambda c: c["lugar"] == lugar , conciertos)
    for c in conciertos_filtrados:
            print(c)


def añadir_concierto():
    id = input ("Introduce el nombre del concierto: ")
    fecha = input("Introduce la fecha del concierto: ")
    artista = input("Introduce el artista del concierto: ")  
    lugar = input("Introduce el lugar del concierto: ")
    precio = input("Introduce el precio del concierto: ")
    entrada = input("¿Tienes entrada para el concierto? (si o no): ")
    anotacion = input("Introduce alguna anotación del concierto si la necesita: ")

    nuevo_concierto = {"id": id, "fecha": fecha, "artista": artista, "lugar": lugar, "precio": precio, "entrada": entrada, "anotacion": anotacion}
    conciertos.append(nuevo_concierto)

    with open("conciertos.txt", "wb") as archivo:
        pickle.dump(conciertos, archivo)
    
    print("Se ha añadido el concierto correctamente")


def eliminar_concierto():
    id = input("Introduce el nombre del concierto que quieres eliminar: ")
    for c in conciertos:
        if c["id"] == id:
            conciertos.remove(c)
            print("Se ha eliminado el concierto correctamente")
            break
        else:
            print("No hay ningún concierto con ese id")
            break
    with open("conciertos.txt", "wb") as archivo:
        pickle.dump(conciertos, archivo)

# Opciones menú

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

else:
    print("Opción inválida, seleccione otra por favor")