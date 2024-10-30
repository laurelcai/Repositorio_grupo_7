import validaciones
import eventos
import crud_historial
import gestor

#lista donde se guardan los ids de los eventos elegidos para luego poder manipular con el evento con mayor facilidad
lista_id=[]


#lista donde se guarda las ubicaciones que el usuario elige previo a la compra
ubicaciones=[]

#matriz con todos los datos de eventos necesarios
diccionario_eventos={1:[[1001,"MUSICA","MILO J","ESTADIO DE MORÓN","25 DE OCTUBRE, 21 HS",("PLATEA" , "$35000"),("CAMPO" , "$28000")],[1002,"MUSICA","BUENOS AIRES TRAP","PARQUE DE LA CIUDAD","7 Y 8 DE DICIEMBRE",("ABONO POR UN DIA","$50000"),("ABONO GENERAL","$85000")]],
                    2:[[2001,"FAMILIA","PLIM PLIM","QUALITY ESPACIO","5 DE OCTUBRE, 17.30HS",("CAMPO DELANTERO" , "$17000"),("CAMPO TRASERO" , "$11000")]],
                    3:[],
                    4:[[4001,"DEPORTE","ARGENTINA VS BOLIVIA","MAS MONUMENTAL","15 DE OCTUBRE, 21HS",("PLATEA",  "$120000"),("POPULAR" , "$75000")]]}

#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre
#matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))

#Se encarga de imprimir de manera ordenada y prolija la matriz de eventos
def imprimir_eventos():

    print('-' * 175)
    print(f"{'ID':<10}{'TIPO':<16} {'NOMBRE':25} {'UBICACIÓN':<22} {'FECHA Y HORA':<26}{'ENTRADAS DISPONIBLES':<25}")


    for key in diccionario_eventos:
        matriz=diccionario_eventos[key]
        for id, tipo, nombre, ubicacion,fecha,entradas1,entradas2 in matriz:
            print('-' * 175)
            entrada,precio=entradas1
            entrada2,precio2=entradas2
            print(f"{id:<10}{tipo:<16} {nombre:<25} {ubicacion:<23}{fecha:<26}{entrada:<}:{precio}")
            print(f"{'':<102}{entrada2}:{precio2}")


def filtrar_precios_eventos(evento_elegido,tipo_evento):
    filtrados=[]
    matriz=[]
    """Entrada: recibe por teclado una eleccion
    Salida: se filtra e imprime la matriz segun lo elegido"""
    
    for key in diccionario_eventos:
        if key == tipo_evento:
            matriz=diccionario_eventos[key]    
            filtrados = [fila for fila in matriz if fila[0] == lista_id[evento_elegido-1]]
            for id, tipo, nombre, ubicacion, fecha, entradas1, entradas2 in filtrados:
                crud_historial.agregar_evento(id,nombre)
                print(1,")",entradas1[0],":",entradas1[1])
                print(2,")",entradas2[0],":",entradas2[1])
            
            return (entradas1,entradas2)
                

def filtrar_eventos(elegir):
    lista_id.clear()        
    cont=0
    for key in diccionario_eventos:
        if key == elegir:
            matriz=diccionario_eventos[key]
            for id, tipo, nombre, ubicacion,fecha,entradas1,entradas2 in matriz:
                lista_id.append(id)
                cont=cont+1
                print(cont,")",f"{tipo:<16} {nombre:<22} {ubicacion:<22}{fecha:<26}")
                
            return len(matriz)


#borra la fila que se ingrese por teclado y a su vez la muestra
def borrar():
    cont=0
    band=0
    while band==0:
        print('-' * 175)
        print('1)Música.')
        print('2)Familia.')
        print('3)Teatro.')
        print('4)Deporte.')
        print('-' * 175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Seleccione el tipo de evento:")
        tipo=gestor.interfaz_gestor()
        if tipo != None:
            if validaciones.validar(tipo)==1:
                tipo=int(tipo)
                for key in diccionario_eventos:
                    if key == tipo:
                        band=1
                        matriz=diccionario_eventos[key]
                        print('-' * 175)
                        print(f"{'ID':<10}{'TIPO':<16} {'NOMBRE':25} {'UBICACIÓN':<22} {'FECHA Y HORA':<26}{'ENTRADAS DISPONIBLES':<25}")
                        for id, tipo, nombre, ubicacion,fecha,entradas1,entradas2 in matriz:
                            cont=cont+1
                            print('-' * 175)
                            entrada,precio=entradas1
                            entrada2,precio2=entradas2
                            print(cont,")",f"{id:<10}{tipo:<16} {nombre:<25} {ubicacion:<23}{fecha:<26}{entrada:<}:{precio}")
                            print(f"{'':<106}{entrada2}:{precio2}")
                
                        eleccion=input("Cual es la fila que desea eliminar? ")
                        if validaciones.validar(eleccion)==1:
                            eleccion=int(eleccion)
                            eliminado=matriz.pop(eleccion-1)
                            print("Usted ha eliminado:",eliminado)
                            band=1
            else:
                print("Opción incorrecta.")
        else:
            band=1

#Se solicitan por teclado los datos necesarios para asi poder agregar un evento mas a la matriz de eventos
def agregar():
    tipo,tipo_diccionario=validaciones.validar_tipo()
    bandera_nombre= 0 # Bandera para controlar el bucle de validación del Nombre
    while bandera_nombre == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese nombre del evento:")
        nombre_del_evento = gestor.interfaz_gestor()
        if nombre_del_evento != None:
            if validaciones.validar_agregar_nombre_evento(nombre_del_evento) == 1:
                print("Nombre válido.")
                bandera_nombre = 1
                bandera_ubicacion_evento=0
                while bandera_ubicacion_evento == 0:
                    print("-"*175)
                    print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                    print("Ingrese la localidad/ubicacion del evento: ")
                    ubicacion_evento = gestor.interfaz_gestor()
                    if ubicacion_evento != None:
                        if validaciones.validar_agregar_nombre_evento(ubicacion_evento) == 1:
                            print("Ubicacioon válida.")
                            bandera_ubicacion_evento = 1
                            bandera_fecha=0
                            while bandera_fecha == 0:
                                print("-"*175)
                                print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                print("Ingrese la fecha y hora del evento")
                                fecha = gestor.interfaz_gestor()
                                if fecha != None:
                                    if validaciones.validar_agregar_fecha_evento(fecha)==1:
                                        print("Fecha válida.")
                                        bandera_fecha = 1
                                        bandera_entrada1=0
                                        while bandera_entrada1== 0:
                                            print("-"*175)  
                                            print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                            print("Ingrese la ubicacion del evento:")
                                            entrada1 = gestor.interfaz_gestor()
                                            if entrada1 != None:
                                                if validaciones.validar_agregar_nombre_evento(entrada1)==1:
                                                    print("Ubicacion valida")
                                                    bandera_entrada1= 1
                                                    bandera_entrada2=0
                                                    while bandera_entrada2 == 0:
                                                        print("-"*175)    
                                                        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                                        print("Ingrese la ubicacion del envento y su precio: ")
                                                        entrada2 = gestor.interfaz_gestor()
                                                        if entrada2 != None:
                                                            if validaciones.validar_agregar_nombre_evento(entrada2)==1:
                                                                print("Ubicacion válida.")
                                                                bandera_entrada2 = 1
                                                                print("Usted se ha registrado correctamente.")
                                                                for key in diccionario_eventos:
                                                                   if key==tipo_diccionario:
                                                                        matriz=diccionario_eventos[key] 
                                                                        id=len(matriz)+1000*tipo_diccionario
                                                                        matriz.append([id, tipo, nombre_del_evento, ubicacion_evento, fecha, entrada1, entrada2])
                                                                gestor.inicio()
                                                            else:
                                                                print("Ubicacion inválida, por favor ingréselo nuevamente")
                                                        else:
                                                            break

                                                else:
                                                    print("Ubicacion inválida, por favor ingrésela nuevamente")
                                            else:
                                                break
                                        
                                else:
                                    break

                        else:
                            print("Ubicacion inválida, por favor ingréselo nuevamente.")
                    else:
                        break
            else:
                print("Nombre inválido, por favor ingréselo nuevamente")
        else:
            break


def interfaz_eventos():
    bandera_interfaz=0
    while bandera_interfaz==0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        eleccion=input("Seleccione una opcion: ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)

            if eleccion==0:
                eventos.inicio()
                bandera_interfaz=1
            
            if eleccion==-1:
                print("Adiós.")
                bandera_interfaz=1
            
            if bandera_interfaz==0:
                return eleccion
        else:
            return 0
