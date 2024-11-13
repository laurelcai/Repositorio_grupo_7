import validaciones
import eventos
import crud_historial
import gestor
import ArchivosJson

#lista donde se guardan los ids de los eventos elegidos para luego poder manipular con el evento con mayor facilidad
lista_id=[]


#lista donde se guarda las ubicaciones que el usuario elige previo a la compra
ubicaciones=[]

#matriz con todos los datos de eventos necesarios
diccionario_eventos= ArchivosJson.abrirJson()

#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre
#matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))

#Se encarga de imprimir de manera ordenada y prolija la matriz de eventos
def imprimir_eventos():
    print('-' * 175)
    print(f"{'ID':<10}{'TIPO':<16} {'NOMBRE':25} {'UBICACIÓN':<22} {'FECHA Y HORA':<26}{'ENTRADAS DISPONIBLES':<41}{'AFORO MAXIMO':<20}{'AFORO VENDIDO':<20}")

    for key in diccionario_eventos:
        matriz = diccionario_eventos[key]
        for id, tipo, nombre, ubicacion, fecha, entradas1, entradas2 in matriz:
            # Primera línea de impresión (entrada1)
            entrada1, precio1, capacidad1, vendidos1 = entradas1
            print('-' * 175)
            print(f"{id:<10}{tipo:<16} {nombre:<25} {ubicacion:<23}{fecha:<26}{entrada1:<20}:{precio1:<20}{capacidad1:<20}{vendidos1:<10}")
            entrada2, precio2, capacidad2, vendidos2 = entradas2
            print(f"{'':<102}{entrada2:<20}:{precio2:<20}{capacidad2:<20}{vendidos2:<20}")



def filtrar_precios_eventos(evento_elegido, tipo_evento):
    filtrados = []
    matriz = []
    
    """Entrada: recibe por teclado una eleccion
    Salida: se filtra e imprime la matriz segun lo elegido"""
    id_evento = lista_id[evento_elegido - 1]  # Obtener el id del evento seleccionado
    for key in diccionario_eventos:
        if key == tipo_evento:  # Verificar si el tipo de evento coincide
            matriz = diccionario_eventos[key]  # Obtener la matriz correspondiente al tipo de evento
            filtrados = [fila for fila in matriz if fila[0] == id_evento]  # Filtrar por id_evento

            for id, tipo, nombre, ubicacion, fecha, entradas1, entradas2 in filtrados:
                entrada1, precio1, capacidad1, vendidos1 = entradas1
                entrada2, precio2, capacidad2, vendidos2 = entradas2
                crud_historial.agregar_evento(id, nombre)  # Agregar al historial

                # Calcular y mostrar los porcentajes y precios para las entradas 1 y 2
                porcentaje1 = porcentaje_asistencia(capacidad1,vendidos1)
                
                if porcentaje1 < 100:
                    print(f"1) {entrada1}: {precio1} (vendido:",porcentaje1,"%)")
                else:
                    print(f"1) {entrada1}: sold out")

                porcentaje2 = porcentaje_asistencia(capacidad2,vendidos2)
                
                if porcentaje2 < 100:
                    print(f"2) {entrada2}: {precio2} (vendido:",porcentaje2,"%)")
                else:
                    print(f"2) {entrada2}: sold out")
                
                if porcentaje1 <100 and porcentaje2 <100:
                    return (entrada1,entrada2), id_evento,(capacidad1,capacidad2)
                if porcentaje1 < 100 and porcentaje2 >=100:
                    return (entrada1,0),id_evento,(capacidad1,capacidad2)
                if porcentaje1 >=100 and porcentaje2<100:
                    return (0,entrada2),id_evento,(capacidad1,capacidad2)
                if porcentaje2>=100 and porcentaje1 >=100:
                    return None,None,None

                
            


def filtrar_eventos(elegir):
    lista_id.clear()        
    cont=0
    for key in diccionario_eventos:
        if key == elegir:
            matriz=diccionario_eventos[key]
            for id, tipo, nombre, ubicacion,fecha,entradas1,entradas2 in matriz:
                lista_id.append(id)
                cont=cont+1
                print(cont,")",f"{tipo:<16} {nombre:<22} {ubicacion:<23}{fecha:<26}")
                
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
                bandera_interfaz=1
                return eleccion
        else:
            bandera_interfaz=1
            return 0


def solicitar_tipo_evento():
    bandera_validacion_tipo=0
    while bandera_validacion_tipo==0:
        print("-"*175)
        print('1)Música.')
        print('2)Familia.')
        print('3)Teatro.')
        print('4)Deporte.')
        tipo=input("Seleccione el tipo de evento: ")
        if validaciones.validar(tipo)==1:
            tipo = int(tipo)
            if tipo == 0:
                return gestor.inicio()
            if tipo == 1:
                return 'MUSICA',"1"
            if tipo ==2:
                return 'FAMILIA',"2"
            if tipo==3:
                return 'TEATRO',"3"
            if tipo==4:
                return 'DEPORTE',"4"
        if bandera_validacion_tipo==0:
            print("Tipo de evento inválido.")


def solicitar_nombre_evento():
    bandera_nombre=0
    while bandera_nombre == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese nombre del evento:")
        nombre_del_evento = gestor.interfaz_gestor()
        if nombre_del_evento != None:
            if validaciones.validar_agregar_nombre_evento(nombre_del_evento) == 1:
                print("Nombre válido.")
                bandera_nombre = 1
                return nombre_del_evento
        else:
            break
        if bandera_nombre ==0:
            print("Nombre inválido, por favor ingréselo nuevamente")


def solicitar_ubicacion_evento():
    bandera_ubicacion_evento=0
    while bandera_ubicacion_evento == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese la localidad/ubicacion del evento: ")
        ubicacion_evento = gestor.interfaz_gestor()
        if ubicacion_evento != None:
            if validaciones.validar_agregar_nombre_evento(ubicacion_evento) == 1:
                print("Ubicacion válida.")
                bandera_ubicacion_evento = 1
                return ubicacion_evento
        else:
            break
        if bandera_ubicacion_evento ==0:
            print("Ubicacion inválida, por favor ingréselo nuevamente.")
             

def solicitar_fecha_hora():
    bandera_fecha=0
    while bandera_fecha == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese la fecha y hora del evento")
        fecha = gestor.interfaz_gestor()
        if fecha != None:
            if validaciones.validar(fecha)==0:
                print("Fecha válida.")
                bandera_fecha = 1
                return fecha
        else:
            break
        if bandera_fecha==0:
            print("Fecha inválida, por favor ingrésela nuevamente.")


def solicitar_entrada():
    bandera_entrada=0
    while bandera_entrada== 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese la entrada del evento:")
        entrada = gestor.interfaz_gestor()
        if entrada != None:
            if validaciones.validar_agregar_nombre_evento(entrada)==1:
                print("Entrada valida")
                bandera_entrada= 1
                return entrada
        else:
            break
        if bandera_entrada==0:
            print("Entrada inválida, por favor ingrésela nuevamente.")


def solicitar_precio_entrada():
    bandera_precio_entrada=0
    while bandera_precio_entrada== 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese el precio de la entrada:")
        precio_entrada = gestor.interfaz_gestor()
        if precio_entrada != None:
            if validaciones.validar(precio_entrada)==1:
                print("Precio de la entrada valido")
                bandera_precio_entrada= 1
                return precio_entrada
        else:
            break
        if bandera_precio_entrada==0:
            print("Precio inválido, por favor ingréselo nuevamente.")


def solicitar_aforo_maximo():
    bandera_aforo_entrada=0
    while bandera_aforo_entrada== 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese el aforo maximo de la entrada:")
        aforo_entrada = gestor.interfaz_gestor()
        if aforo_entrada != None:
            if validaciones.validar(aforo_entrada)==1:
                print("Aforo maximo, de la entrada valido")
                bandera_aforo_entrada= 1
                return aforo_entrada
        else:
            break
        if bandera_aforo_entrada==0:
            print("Aforo inválido, por favor ingréselo nuevamente.")


# Función principal para ingresar todos los datos del evento
def agregar():
    entrada1=[]
    entrada2=[]
    tipo_evento,numero_evento= solicitar_tipo_evento()
    if tipo_evento !=None:
        nombre_evento = solicitar_nombre_evento()
        if nombre_evento !=None:
            ubicacion_evento = solicitar_ubicacion_evento()
            if ubicacion_evento !=None:
                fecha_hora_evento = solicitar_fecha_hora()
                if fecha_hora_evento !=None:
                    tipo_entrada1 = solicitar_entrada()
                    if tipo_entrada1 !=None:
                        valor_entrada1 = solicitar_precio_entrada()
                        if valor_entrada1 !=None:
                            aforo_maximo1 = solicitar_aforo_maximo()
                            if aforo_maximo1 != None:
                                tipo_entrada2 = solicitar_entrada()
                                if tipo_entrada2 !=None:
                                    valor_entrada2 = solicitar_precio_entrada()
                                    if valor_entrada2 !=None:
                                        aforo_maximo2 = solicitar_aforo_maximo()
                                        if aforo_maximo2 != None:
                                            for key in diccionario_eventos:
                                                if key==numero_evento:
                                                    matriz=diccionario_eventos[key]
                                                    numero_evento=int(numero_evento) 
                                                    id=len(matriz)+1000*numero_evento
                                                    entrada1.extend([tipo_entrada1,valor_entrada1,int(aforo_maximo1),0])
                                                    entrada2.extend([tipo_entrada2,valor_entrada2,int(aforo_maximo2),0])
                                                    matriz.append([id, tipo_evento, nombre_evento, ubicacion_evento, fecha_hora_evento, entrada1, entrada2])
                                                    

def agregar_asistencia(id_evento,tipo_evento,ubicacion,cantidad_compradas):
    for key in diccionario_eventos:
        if key == tipo_evento:
            matriz=diccionario_eventos[key]
            for fila in matriz:
                if fila[0]==id_evento:
                    entradas=fila[4+ubicacion]
                    entradas[3]=entradas[3]+cantidad_compradas

def porcentaje_asistencia(aforo,entradas_vendidas):
    porcentaje=entradas_vendidas*100/aforo
    return porcentaje



