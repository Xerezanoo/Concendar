    #Concendar
#Menú
def mostrar_menu(nombre, opciones):  
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1', funcion1),
        '2': ('Opción 2 >', submenu),
        '3': ('Opción 3', funcion3),
        '4': ('Salir', salir)
    }

    generar_menu('Menú principal', opciones, '4') 


def submenu():
    opciones = {
        'a': ('Opción a', funcionA),
        'b': ('Opción b', funcionB),
        'c': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'c') 


def funcion1():
    print('Has elegido la opción 1')


def funcion2():
    print('Has elegido la opción 2')


def funcion3():
    print('Has elegido la opción 3')


def funcionA():
    print('Has elegido la opción A')


def funcionB():
    print('Has elegido la opción B')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()