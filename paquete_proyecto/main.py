import variaciones
import validaciones


#lista con los tipos de eventos, luego utilizada para filtrar la matriz
lista_tipo=['musica','familia','teatro','deporte']

lista_id=[]


#matriz con todos los datos de eventos necesarios
matriz_eventos_desordenada=[
[1001,"musica","Milo J","Estadio de Morón","25 de octubre, 21hs","Platea  $35000","Campo  $28000",],
[1002,"familia","Plim Plim","Quality espacio","5 de octubre, 17.30hs","Campo delantero  $17000","Campo trasero  $11000"],
[1003,"deporte","Argentina vs Bolivia","Más Monumental","15 de Octubre, 21hs","Platea  $120000","Popular  $75000","Palco  $500000"],
[1004,"musica","Buenos Aires Trap","Parque de la Ciudad","7 y 8 de Diciembre","Abono por un dia  $50000","Abono general  $85000"]]

matriz_eventos=variaciones.ordenar(matriz_eventos_desordenada)






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

            opciones,ubicacion=variaciones.filtrar_matriz(matriz_eventos,evento_elegido,lista_id,0)

            elegir_ubicacion=interfaz()
            if elegir_ubicacion <= opciones and elegir_ubicacion > 0:
                band=1
                elegir_cantidad_entradas=input("Cuantas entradas desea comprar? ")
                if validaciones.validar(elegir_cantidad_entradas)==1:
                    print("Usted ha comprado",elegir_cantidad_entradas,"entradas en la ubicacion",ubicacion[elegir_ubicacion-1],".")
                else:
                    print("opcion incorrecta")
                    band=0        
            else:
                print("Ubicacion no encontrada")
    
    band=0
    while band==0:
        fin=interfaz()
        if fin==-1 or fin==0:
            band=1
        if band==0:
            print("ERROR")


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
        print("-"*100)    
        elegir_inicio=input("Seleccione una opción: ")
        if validaciones.validar(elegir_inicio)==1:
            elegir_inicio=int(elegir_inicio)
            if elegir_inicio <= 4 and elegir_inicio >0:
                eventos(elegir_inicio)
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
            
            if elegir_interfaz == -1:
                band=1
                print("Adios")
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

        lista=variaciones.filtrar_matriz(matriz_eventos,elegir_inicio,lista_tipo,1)
        lista_id.clear()
        for i in lista:
            lista_id.append(i)
    
        if len(lista_id)<1:
            print("Todavia no se encontraron eventos, intenta de nuevo mas tarde")
            band=0

        elegir_interfaz=interfaz()
        if elegir_interfaz <= len(lista_id) and elegir_interfaz >0:
            comprar(elegir_interfaz)
            band=1

        if band ==0:
            print("ERROR,evento no encontrado")
            band=0


#menu principal
inicio()