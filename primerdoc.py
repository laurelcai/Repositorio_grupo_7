from random import randint
import re

#lista con los tipos de eventos, luego utilizada para filtrar la matriz
lista_tipo=['musica','familia','teatro','deporte']

#lista donde luego se guarda el id del evento el cual el cliente se encuentra interesado, para poder trabajar con el mismo de una manera mas agil
lista_id=[]

#matriz con todos los datos de eventos necesarios
matriz_eventos_desordenada=[
[1001,"musica","Milo J","Estadio de Morón","25 de octubre, 21hs","Platea  $35000","Campo  $28000",],
[1002,"familia","Plim Plim","Quality espacio","5 de octubre, 17.30hs","Campo delantero  $17000","Campo trasero  $11000"],
[1003,"deporte","Argentina vs Bolivia","Más Monumental","15 de Octubre, 21hs","Platea  $120000","Popular  $75000","Palco  $500000"],
[1004,"musica","Buenos Aires Trap","Parque de la Ciudad","7 y 8 de Diciembre","Abono por un dia  $50000","Abono general  $85000"]]


#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre
matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))


def validar(entrada):
    if re.match(r"^-?\d+$",entrada):
        return 1
    else:
        return 0


def comprar(elegir1):#Ultimo paso, en el cual se efectua la confirmacion de las entradas y se elije la ubicacion en el evento

    """Entrada: Se recibe el evento al cual el usuario desea asistir
    Salida: Se muestra por pantalla los precios y ubicaciones disponibles para que el cliente confirme la compra o,
    ya sea que quiera volver al principio, o tambien salir del programa"""

    band=0
    i=0
    while band==0:
        if elegir1 > 0:    
            cont=0
            filas=len(matriz_eventos)
            print('-' * 100)
            print(" "*3,f"{'UBICACION Y PRECIO':<10}")
            print('-' * 100)
            for i in range(filas):
                    if matriz_eventos[i][0] == lista_id[elegir1-1]:
                        columnas=len(matriz_eventos[i])
                        b=i
                        for j in range(5,columnas):
                                cont=cont+1
                                print(cont,")",matriz_eventos[i][j])
   
    

        elegir2=interfaz()
        if elegir2 <=cont and elegir2 > 0:
            band=1
            elegir3=input("Cuantas entradas desea comprar? ")
            if validar(elegir3)==1:
                print("Usted ha comwprado",elegir3,"entradas en la ubicacion",matriz_eventos[b][4+elegir2][:7],".")
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
        elegir=input("Seleccione una opción: ")
        if validar(elegir)==1:
            elegir=int(elegir)
            if elegir <= 4 and elegir >0:
                eventos(elegir)
                band=1
            else:
                print("Opción no encontrada")
        else:
            print("Opción no encontrada")


def interfaz():# Interfaz que se despliega luego de cada eleccion del cliente

    """Entrada: Una eleccion por teclado
     Salida: Lo redirije al usuario a lo seleccionado,
     ya sea avanzar con el procedimiento, volver o incluso salir del programa en caso de arrepentimiento o equivocacion  """

    elegir1=0
    band=0
    while band==0:
        print('-' * 100)
        print('0)Inicio'.center(10,' '),'-1)Salir'.center(10,' '))
        print('-' * 100)
        elegir1=input("Seleccione una opción: ")
        if validar(elegir1)==1:
            elegir1=int(elegir1)
            if elegir1 == 0:
                band=1
                inicio()
            if elegir1 == -1:
                band=1
                print("Adios")
            band=1

            return elegir1
        else:
            return -2

    



def eventos(elegir):#Se muestran los eventos filtrados segun lo seleccionado por el usuario

    """Entrada: Ingresa a la funcion como dato el tipo de evento seleccionado previamente.
        Salida: Sale la impresion de cada evento del respectivo evento elegido previamente para asi efectuar la comora,
        se repite en bucle hasta conseguir una respuesta adecuada"""

    band=0
    while band != 1:
        lista_id.clear()
        cont=0
        filas=len(matriz_eventos)
        print('-' * 100)
        print(" "*3,f"{'TIPO':<20} {'NOMBRE':25} {'UBICACION':<25} {'FECHA Y HORA':<20}")
        print('-' * 100)
        for i in range(filas):
            columnas=len(matriz_eventos[i])
            if matriz_eventos[i][1] == lista_tipo[elegir-1]:
                band=2
                cont=cont+1
                lista_id.append(matriz_eventos[i][0])
                print(cont,")",end=" ")
                print(f"{matriz_eventos[i][1]:<20} {matriz_eventos[i][2]:<25} {matriz_eventos[i][3]:<25} {matriz_eventos[i][4]:<20}")
        if band==0:
            print("Todavia no se encontraron eventos, intenta de nuevo mas tarde")
            band=0
        eleccion=interfaz()
        if eleccion <= len(lista_id) and eleccion >0:
            comprar(eleccion)
            band=1
        else:
            if eleccion != 0 and eleccion != -1:
                print("ERROR,vento no encontrado")
            else:
                band=1

#menu principal
inicio()