import variaciones
import validaciones

def comprar(evento_elegido):#Ultimo paso, en el cual se efectua la confirmacion de las entradas y se elije la ubicacion en el evento

    """Entrada: Se recibe el evento al cual el usuario desea asistir
    Salida: Se muestra por pantalla los precios y ubicaciones disponibles para que el cliente confirme la compra o,
    ya sea que quiera volver al principio, o tambien salir del programa"""

    band=0
    i=0
    while band==0:
        if evento_elegido > 0:

            print('-' * 100)
            print(" "*3,f"{'UBICACION Y PRECIO':<10}")
            print('-' * 100)

            opciones,ubicacion=variaciones.filtrar_matriz(evento_elegido,0)

            elegir_ubicacion=interfaz()
            
            if elegir_ubicacion <= opciones and elegir_ubicacion > 0:
                band=1
                elegir_cantidad_entradas=input("Cuantas entradas desea comprar? ")
                if validaciones.validar(elegir_cantidad_entradas)==1:
                    print("Usted ha comprado",elegir_cantidad_entradas,"entradas en la ubicacion",ubicacion[elegir_ubicacion-1],".")
                else:
                    print("opcion incorrecta")
                    band=0     

            if elegir_ubicacion==0:
                band=1
            
            if band==0:
                print("Ubicacion no encontrada")
    
    band=0
    while band==0:
        bucle=interfaz()
        if bucle == 0 or bucle==-1:
            band=1


def inicio():#se desplieaga un menu para seleccionar los distintos tips de eventos
    
    """Comienza el codigo
    Sale: Una eleccion que deriva a la funcion de eventos,
    y se repite en bucle hasta no conseguir una repuesta correcta """

    band=0
    while band==0:

        print("Tipos de eventos: ")
        print("-"*100)
        print('1)Música')
        print('2)Familia')
        print('3)Teatro')
        print('4)Deporte')
        print('5)Salir')
        print("-"*100)    
        
        elegir_inicio=input("Seleccione una opción: ")
        if validaciones.validar(elegir_inicio)==1:
            elegir_inicio=int(elegir_inicio)
            if elegir_inicio <= 5 and elegir_inicio >0:
                if elegir_inicio <5:
                    eventos(elegir_inicio)
                    band=1
                if elegir_inicio==5:
                    print("Adios")
                    band=1
            else:
                print("Opción no encontrada")
        else:
            print("Opción no encontrada")


def interfaz():# Interfaz que se despliega luego de cada eleccion del cliente

    """Entrada: Una eleccion por teclado
     Salida: Lo redirije al usuario a lo seleccionado,
     ya sea avanzar con el procedimiento, volver o incluso salir del programa en caso de arrepentimiento o equivocacion  """

    band=0
    while band==0:
        print('-' * 100)
        print('0)Inicio'.center(10,' '),'-1)Salir'.center(10,' '))
        print('-' * 100)

        elegir_interfaz=input("Seleccione una opción: ")
        if validaciones.validar(elegir_interfaz)==1:
            elegir_interfaz=int(elegir_interfaz)

            if elegir_interfaz == 0:
                band=1
                inicio()
                return 0
            
            if elegir_interfaz == -1:
                band=1
                print("Adios")
                return 0
        else:
            band=1    
            return -2
        
        if band==0:
            band=1
            return elegir_interfaz
            

def eventos(elegir_inicio):#Se muestran los eventos filtrados segun lo seleccionado por el usuario

    """Entrada: Ingresa a la funcion como dato el tipo de evento seleccionado previamente.
        Salida: Sale la impresion de cada evento del respectivo evento elegido previamente para asi efectuar la comora,
        se repite en bucle hasta conseguir una respuesta adecuada"""
    
    band=0
    while band==0:
        print('-' * 100)
        print(" "*3,f"{'TIPO':<20} {'NOMBRE':25} {'UBICACION':<25} {'FECHA Y HORA':<20}")
        print('-' * 100)

        cantidad_de_eventos=variaciones.filtrar_matriz(elegir_inicio,1)

        if cantidad_de_eventos<1:
            print("Todavia no se encontraron eventos, intenta de nuevo mas tarde")
            band=0

        elegir_interfaz=interfaz()
        if elegir_interfaz <= cantidad_de_eventos and elegir_interfaz >0:
            comprar(elegir_interfaz)
            band=1
        
        if elegir_interfaz==0:
            band=1 

        if band ==0:
            print("ERROR,evento no encontrado")
            band=0


