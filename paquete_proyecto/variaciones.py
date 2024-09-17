import validaciones
#lista con los tipos de eventos, luego utilizada para filtrar la matriz
lista_tipo=['musica','familia','teatro','deporte']

lista_id=[]

lista_agregar=[]

#matriz con todos los datos de eventos necesarios
matriz_eventos_desordenada=[
[1001,"musica","Milo J","Estadio de Morón","25 de octubre, 21hs","Platea  $35000","Campo  $28000",],
[1002,"familia","Plim Plim","Quality espacio","5 de octubre, 17.30hs","Campo delantero  $17000","Campo trasero  $11000"],
[1003,"deporte","Argentina vs Bolivia","Más Monumental","15 de Octubre, 21hs","Platea  $120000","Popular  $75000","Palco  $500000"],
[1004,"musica","Buenos Aires Trap","Parque de la Ciudad","7 y 8 de Diciembre","Abono por un dia  $50000","Abono general  $85000"]]

ubicaciones=[]
datos_usuario = [["maestro","maestro@email.com", "maestro77", "123456",1111111 ,1000, "maestro"]]

historial=[]
lista_historial=[0]*6

#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre

matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))


def filtrar_matriz(elegir,a):
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
    id=len(datos_usuario)+1000
    datos_usuario.append([nombre,mail,usuario,contraseña,dni,id,'usuario'])

def validar_usuario(usuario):
    band=0
    for i in range (len(datos_usuario)):
        if datos_usuario[i][2] == usuario:
            band=1
            lista_historial[1]=datos_usuario[i][2]
            lista_historial[0]=datos_usuario[i][5]
            
    if band==0:
        return 0
    else:
        return 1

def validar_contraseña(contraseña):
    band=0
    for i in range (len(datos_usuario)):
        if datos_usuario[i][3] == contraseña:
            band=1
    if band==0:
        return 0
    else:
        return 1        

def agregar_historial(ubicacion,cantidad):
    while len(lista_historial) < 6:
        lista_historial.append(None)
    
    # Asignar valores a los índices específicos
    lista_historial[4] = ubicacion
    lista_historial[5] = cantidad
    
    # Agrega una copia de lista_historial a historial para evitar modificar referencias
    historial.append(lista_historial.copy())
    
    # Imprime para depuración
    print(lista_historial, historial)


def imprimir_historial():
    print(f"{'ID':<12}{'Usuario':<20}{'ID Evento':<12}{'Evento':<20}{'Ubicacion':<15}{'Cantidad entradas compradas':<10}")
    print('-'*100)
    for id_usuario,usuario,id_evento,evento,ubicacion,cantidad in historial:
        print(f"{id_usuario:<12}{usuario:<20}{id_evento:<12}{evento:<20}{ubicacion:<15}{cantidad:<10}")

def imprimir_eventos():
    print('-' * 175)
    print(" "*5, f"{'ID':<10}{'TIPO':<16} {'NOMBRE':22} {'UBICACION':<22} {'FECHA Y HORA':<26}{'ENTRADAS DISPONIBLES':<25}")
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

def borrar():
    band=0
    while band==0:
        imprimir_eventos()
        eleccion=input("Cual es la fila que desea eliminar? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            if eleccion <= len(matriz_eventos) and eleccion>0:
                eliminado=matriz_eventos.pop(eleccion-1)
                print("Usted ha eliminado:",eliminado)
                band=1
        if band==0:
            print("Opcion incorrecta")


def agregar():
    bandera = 0 # Bandera para controlar el bucle de validación del Nombre
    id=len(matriz_eventos)+1000
    lista_agregar.append(id)

    while bandera == 0:
        print("-"*50)
        tipo = input("Ingrese el tipo de evento: ")
        if validaciones.validar(tipo) == 0:
            print("Válido")
            lista_agregar.append(tipo)
            bandera = 1
        else:
            print("Invalido, porfavor ingreselo nuevamente")
    
    bandera=0
    while bandera==0:
        print("-"*50)
        nombre = input("Ingrese el nombre del evento: ")
        if validaciones.validar(nombre) == 0:
            print("Valido")
            lista_agregar.append(nombre)
            bandera=1
        else:
            print("Invalido. Ingreselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*50)
        donde = input("Ingrese donde se realizara el evento: ")
        if validaciones.validar(donde)==0:
            print("Valido")
            lista_agregar.append(donde)
            bandera=1

        else:
            print("Invalido, ingreselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*50)  
        fecha_hora = input("Ingrese la fecha y horario del evento: ")
        if validaciones.validar(fecha_hora)==0:
            print("Valido")
            lista_agregar.append(fecha_hora)
            bandera=1
        else:
            print("Invalido, ingresar nuevamente")
    
    bandera=0
    while bandera==0:
        print("-"*50)
        entradas= input("Ingresar las localidades disponibles y su precio(ingrese salir para finalizar): ").upper()
        if validaciones.validar(entradas)==0:
                if entradas != 'SALIR':
                    print("Valido")
                    lista_agregar.append(entradas)
                else:    
                    bandera=1        
        else:
            print("Invalido, ingresar nuevamente")
        
        # Agregar los datos a la lista
    matriz_eventos.append(lista_agregar)
    print(matriz_eventos)
    lista_agregar.clear()

def tipo_de_usuario(usuario):
    for i in range (len(datos_usuario)):
        if datos_usuario[i][2] == usuario:
            if datos_usuario[i][6]=='maestro':
                return 1
            if datos_usuario[i][6]=='usuario':
                return 0
            
def imprimir_usuarios():
    print( f"{'NOMBRE':<25}{'MAIL':<25} {'USUARIO':20} {'CONTRASEÑA':<20} {'DNI':<10}{'ID':<10}{'TIPO':<10}")
    print('-'*100)
    for nombre,mail,usuario,contraseña,dni,id,tipo in datos_usuario:
        print( f"{nombre:<25}{mail:<25} {usuario:20} {contraseña:<20} {dni:<10}{id:<10}{tipo:<10}")
