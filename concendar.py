    #Concendar
conciertos = {}

print("Bienvenido a Concendar!    * Menú principal. Seleccione una opción")
print("1) Mis conciertos")
print("2) Mis lugares")
print("3) Añadir un nuevo concierto")
print("4) Eliminar un concierto")
print("5) Salir")

opcion = input("Seleccione una opción: ")

def listar_conciertos():
    import json
    try:
        with open("conciertos.json", "r") as f:
            conciertos = json.load(f)
    except FileNotFoundError:
        with open("conciertos.json", "w") as f:
            pass
    for c in conciertos:
        print(c)

def listar_conciertos_por_lugar():
    import json
    try:
        with open("conciertos.json", "r") as f:
            conciertos = json.load(f)
    except FileNotFoundError:
        with open("conciertos.json", "w") as f:
            pass
    for c in conciertos:
        print(c)

    lugar = input("Lugar del que quieres ver los conciertos: ")
    conciertos_filtrados = filter(lambda c: c["lugar"] == lugar , conciertos)
    for c in conciertos_filtrados:
        print(c)

def añadir_concierto():
    import json
    try:
        with open("conciertos.json", "r") as f:
            conciertos = json.load(f)
    except FileNotFoundError:
        with open("conciertos.json", "w") as f:
            pass
    for c in conciertos:
        print(c)
    
    id = input("Introduce la ID del concierto: ")
    fecha = input("Introduce la fecha del concierto: ")
    artista = input("Introduce el artista del concierto: ")
    lugar = input("Introduce el lugar del concierto: ")
    precio = input("Introduce el precio del concierto: ")
    entrada = input("¿Tienes entrada para el concierto? (si o no): ")
    anotacion = input("Introduce alguna anotación del concierto si la necesita: ")

    concierto = {
        "id": id,
        "fecha": fecha,
        "artista": artista,
        "lugar": lugar,
        "precio": precio, 
        "entrada": entrada,
        "anotacion": anotacion
    }

    conciertos[id] = concierto

    with open("conciertos.json", "w") as f:
        json.dump(conciertos, f)

def eliminar_concierto():
    import json
    try:
        with open("conciertos.json", "r") as f:
            conciertos = json.load(f)
    except FileNotFoundError:
        with open("conciertos.json", "w") as f:
            pass
    for c in conciertos:
        print(c)
    
    id = input("Introduce la ID del concierto que quieres eliminar: ")
    for c in conciertos:
        if c["id"] == id:
            conciertos.remove(c)
            print("Has eliminado el concierto")
            break
        else:
            print("No hay ningún concierto con ese id")
    with open("conciertos.json", "w") as f:
        json.dump(conciertos, f)    

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

