import validaciones
#lista con los tipos de eventos, luego utilizada para filtrar la matriz
lista_tipo=['MUSICA','FAMILIA','TEATRO','DEPORTE']

#lista donde se guardan los ids de los eventos elegidos para luego poder manipular con el evento con mayor facilidad
lista_id=[]

#matriz con todos los datos de eventos necesarios
matriz_eventos_desordenada=[[1001,"MUSICA","MILO J","ESTADIO DE MORÓN","25 DE OCTUBRE, 21 HS","PLATEA  $35000","CAMPO  $28000",],
[1002,"FAMILIA","PLIM PLIM","QUALITY ESPACIO","5 DE OCTUBRE, 17.30HS","CAMPO DELANTERO  $17000","CAMPO TRASERO  $11000"],
[1003,"DEPORTE","AREGTINA VS BOLIVIA","MAS MONUMENTAL","15 DE OCTUBRE, 21HS","PLATEA  $120000","POPULAR  $75000","PALCO  $500000"],
[1004,"MUSICA","BUENOS AIRES TRAP","PARQUE DE LA CIUDAD","7 Y 8 DE DICIEMBRE","ABONO POR UN DIA $50000","ABONO GENERAL  $85000"]]

#lista donde se guarda las ubicaciones que el usuario elige previo a la compra
ubicaciones=[]

#matriz con todos datos de cada usuario registrado
datos_usuario = [["maestro","maestro@mail.com", "maestro77", "123456",1111111 ,1000, "MAESTRO"]]

#matriz con todos los datos de cada compra ralizada
historial=[]

#lista con los datos necesarios que luego seran agregados a la matriz historial
lista_historial=[0]*6

#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre
matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))


def filtrar_matriz(elegir,a):

    """Entrada: recibe por teclado una eleccion
    Salida: se filtra e imprime la matriz segun lo elegido"""

    if elegir > 0:
        ubicaciones.clear()
        
        #filtro para realizar la compra de entradas
        if a == 0:
            filtrados = [fila for fila in matriz_eventos if fila[a] == lista_id[elegir-1]]
            for i in range(5,len(filtrados[0])):
                print(i-4,")",filtrados[0][i])
                ubicaciones.append(filtrados[0][i])
                lista_historial[2]=filtrados[0][0]
                lista_historial[3]=filtrados[0][2]
            
            return i-4,ubicaciones
        
        #filtro para mostrar por pantalla los eventos del tipo seleccionado
        if a ==1:
            filtrados = [fila for fila in matriz_eventos if fila[a] == lista_tipo[elegir-1]]
            cont=0
            lista_id.clear()
            for fila in filtrados:
                if len(filtrados)>0:
                    lista_id.append(fila[0])
                cont=cont+1
                print(cont,")",f"{fila[1]:<20} {fila[2]:25} {fila[3]:<25} {fila[4]:<20}")
            
            return len(filtrados)


def agregar_usuarios(nombre,mail,usuario,contraseña,dni):
    
    """Entrada: se recibe todos los datos del usuario registrado
    Salida: esos datos que ingresan a la funcion son guardados a la matriz de usuarios"""

    id=len(datos_usuario)+1000
    datos_usuario.append([nombre,mail,usuario,contraseña,dni,id,'USUARIO'])


def validar_usuario(usuario):

    """Entrada: Se recibe el usuario que se desea buscar 
    Salida: se busca y se devuelve si el usuario se encuentra en la matriz"""
    
    band=0
    for i in range (len(datos_usuario)):
        if datos_usuario[i][2] == usuario:
            band=1
            lista_historial[1]=datos_usuario[i][2]#se guarda en la lista_historial el usuario
            lista_historial[0]=datos_usuario[i][5]#se guarda en lista_historia el id
            
    if band==0:
        return 0
    else:
        return 1


def validar_contraseña(contraseña):

    """Entrada: Se recibe la contraseña que se desea buscar 
    Salida: se busca y se devuelve si la contraseña se encuentra en la matriz"""

    band=0
    for i in range (len(datos_usuario)):
        if datos_usuario[i][3] == contraseña:
            band=1
    if band==0:
        return 0
    else:
        return 1        


def agregar_historial(cantidad,ubicacion):

    """Entrada: se recibe la ubicacion y cantidad de entradas
    Salida: se agregan a la lista los datos ingresado y con la lista ya completa,
    la misma se agrega como fila en la matriz historial"""

    while len(lista_historial) < 6:
        lista_historial.append(None)
    
    # Asignar valores a los índices específicos
    lista_historial[4] = ubicacion
    lista_historial[5] = cantidad
    
    # Agrega una copia de lista_historial a historial para evitar modificar referencias
    historial.append(lista_historial.copy())
    

#Se encarga de impprimir de manera ordenada y prolija la matriz historial
def imprimir_historial():

    print(f"{'ID USUARIO':<15}{'USUARIO':<20}{'ID EVENTO':<15}{'EVENTO':<25}{'UBICACIÓN':<30}{'CANTIDAD ENTRADAS COMPRADAS':<10}")
    print('-'*175)
    for id_usuario,usuario,id_evento,evento,ubicacion,cantidad in historial:
        print(f"{id_usuario:<15}{usuario:<20}{id_evento:<15}{evento:<25}{ubicacion:<30}{cantidad:<10}")


#Se encarga de imprimir de manera ordenada y prolija la matriz de eventos
def imprimir_eventos():
    print('-' * 175)
    print(" "*5, f"{'ID':<10}{'TIPO':<16} {'NOMBRE':22} {'UBICACIÓN':<22} {'FECHA Y HORA':<26}{'ENTRADAS DISPONIBLES':<25}")
    print('-' * 175)

    for i in range(len(matriz_eventos)):
        columnas=(len(matriz_eventos[i]))
    # Convierte posibles listas en strings usando str() o elige un elemento dentro de la lista
        print(f"{i+1:>3}) "
          f"{str(matriz_eventos[i][0]):<10} "
          f"{str(matriz_eventos[i][1]):<16} "
          f"{str(matriz_eventos[i][2]):<22} "
          f"{str(matriz_eventos[i][3]):<22} "
          f"{str(matriz_eventos[i][4]):<25}", end=" ")

        for j in range(5,columnas):
            print(f"{str(matriz_eventos[i][j]):<27}",end="")
        print()


#borra la fila que se ingrese por teclado y a su vez la muestra
def borrar():
    band=0
    while band==0:
        imprimir_eventos()
        eleccion=input("Cuál es la fila que desea eliminar? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            if eleccion <= len(matriz_eventos) and eleccion>0:
                eliminado=matriz_eventos.pop(eleccion-1)
                print("Usted ha eliminado:",eliminado)
                band=1
        if band==0:
            print("Opción incorrecta.")


#Se solicitan por teclado los datos necesarios para asi poder agregar un evento mas a la matriz de eventos
def agregar():
    bandera = 0 # Bandera para controlar el bucle de validación del Nombre
    id=len(matriz_eventos)+1000

    while bandera == 0:
        print("-"*175)
        tipo = input("Ingrese el tipo de evento: ").upper()
        if validaciones.validar(tipo) == 0:
            print("Válido.")
            bandera = 1
        else:
            print("Inválido, porfavor ingréselo nuevamente.")
    
    bandera=0
    while bandera==0:
        print("-"*175)
        nombre = input("Ingrese el nombre del evento: ").upper()
        if validaciones.validar(nombre) == 0:
            print("Válido.")
            bandera=1
        else:
            print("Inválido. Ingréselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*175)
        donde = input("Ingrese donde se realizará el evento: ").upper()
        if validaciones.validar(donde)==0:
            print("Válido.")
            bandera=1

        else:
            print("Inválido, ingréselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*175)  
        fecha_hora = input("Ingrese la fecha y horario del evento: ").upper()
        if validaciones.validar(fecha_hora)==0:
            print("Válido.")
            bandera=1
        else:
            print("Inválido, ingresélo nuevamente.")
    
    bandera=0
    while bandera==0:
        print("-"*175)
        entradas= input("Ingrese las localidades disponibles y su precio: ").upper()
        if validaciones.validar(entradas)==0:
            print("Válido.") 
            bandera=1
        else:
            print("Inválido, ingréselo nuevamente.")
    
    
    bandera=0
    while bandera==0:
        print("-"*175)
        entradas2= input("Ingresar las localidades disponibles y su precio: ").upper()
        if validaciones.validar(entradas2)==0:
            print("Válido.")  
            bandera=1
        else:
            print("Inválido, ingréselo nuevamente.")
        # Agregar los datos a la lista
    matriz_eventos.append([id,tipo,nombre,donde,fecha_hora,entradas,entradas2])



def tipo_de_usuario(usuario):

    """Entrada:se recibe el usuario 
    Salida: se verifica y devuelve el tipo de usuario que se logueo"""

    for i in range (len(datos_usuario)):
        if datos_usuario[i][2] == usuario:
            if datos_usuario[i][6]=='MAESTRO':
                return 1
            if datos_usuario[i][6]=='USUARIO':
                return 0


#Se encarga de imprimir de manera ordenada y prolija la matriz de usuarios
def imprimir_usuarios():
    print( f"{'NOMBRE':<25}{'MAIL':<25} {'USUARIO':20} {'CONTRASEÑA':<20} {'DNI':<10}{'ID':<10}{'TIPO':<10}")
    print('-'*175)
    for nombre,mail,usuario,contraseña,dni,id,tipo in datos_usuario:
        print( f"{nombre:<25}{mail:<25} {usuario:20} {contraseña:<20} {dni:<10}{id:<10}{tipo:<10}")
