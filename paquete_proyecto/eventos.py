import variaciones
import validaciones

def mostrar_ubicacion(evento_elegido):

    """Entrada: Se recibe el evento al cual el usuario desea asistir
    Salida: Se muestra por pantalla los precios y ubicaciones disponibles"""


    print('-' * 175)
    print(" "*3,f"{'UBICACIÓN Y PRECIO':<10}")
    print('-' * 175)

    opciones,ubicacion=variaciones.filtrar_matriz(evento_elegido,0)

    return opciones,ubicacion
           


def comprar(ubicacion,elegir_ubicacion):
            
            """Entrada: se recibe la ubicacion elegida para el usuario
            Salida: se consulta cuantas entradas quiere el usuario y se confirma la compra"""
            
            band=0
            while band==0:
                elegir_cantidad_entradas=input("Cuántas entradas desea comprar? ")
                if validaciones.validar(elegir_cantidad_entradas)==1:
                    print("Usted ha comprado",elegir_cantidad_entradas,"entradas en la ubicación",ubicacion[elegir_ubicacion-1],".")
                    variaciones.agregar_historial(elegir_cantidad_entradas,ubicacion[elegir_ubicacion-1])
                    band=1
                else:
                    print("Opción incorrecta.")
                        
    

def inicio():#se desplieaga un menu para seleccionar los distintos tipos de eventos
    
    """Luego de haber iniciado sesion el usuario,
    Sale: El usuario elije que desea hacer y se devuelve un valor al respecto  """

    band=0
    while band==0:

        print("Tipos de eventos: ")
        print("-"*175)
        print('1)Música.')
        print('2)Familia.')
        print('3)Teatro.')
        print('4)Deporte.')
        print('0)Cerrar sesión.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("-"*175)    
        
        elegir_inicio=input("Seleccione una opción: ")
        if validaciones.validar(elegir_inicio)==1:
            elegir_inicio=int(elegir_inicio)
            if elegir_inicio <= 4 and elegir_inicio >-2:
                if elegir_inicio <5:
                    band=1
                    return elegir_inicio
                    
                if elegir_inicio==-1:
                    print("Adios.")
                    band=1
                    return -1
                if elegir_inicio==0:
                    return 0
            else:
                print("Opción no encontrada.")
        else:
            print("Opción no encontrada.")


def interfaz():# Interfaz que se despliega luego de cada eleccion del cliente

    """Cumple el rol de intermediario entre el paso anterior y el siguiente, para que a la vez el usuario tenga la posibilidad de volver al inicio o salir """

    band=0
    while band==0:
        print('-' * 175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print('-' * 175)

        elegir_interfaz=input("Seleccione una opción: ")
        if validaciones.validar(elegir_interfaz)==1:
            elegir_interfaz=int(elegir_interfaz)

            if elegir_interfaz == 0:
                band=1
                return 0
            
            if elegir_interfaz == -1:
                band=1
                print("Adios.")
                return -1
        else:
            band=1    
            return -2
        
        if band==0:
            band=1
            return elegir_interfaz
            

def eventos(elegir_inicio):#Se muestran los eventos filtrados segun lo seleccionado por el usuario

    """Entrada: Ingresa a la funcion como dato el tipo de evento seleccionado previamente.
        Salida: Sale la impresion de cada evento del respectivo evento elegido previamente"""
    
    print('-' * 175)
    print(" "*3,f"{'TIPO':<20} {'NOMBRE':25} {'UBICACIÓN':<25} {'FECHA Y HORA':<20}")
    print('-' * 175)

    cantidad_de_eventos=variaciones.filtrar_matriz(elegir_inicio,1)

    if cantidad_de_eventos<1:
        print("Todavía no se encontraron eventos, intenta de nuevo más tarde.")

    return cantidad_de_eventos
