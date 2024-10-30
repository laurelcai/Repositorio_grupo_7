import validaciones
import load_upload
#matriz con todos los datos de cada compra ralizada
historial=load_upload.cargar_historial()

#lista con los datos necesarios que luego seran agregados a la matriz historial
lista_historial=[0]*6

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

def agregar_usuario(usuario,id):
    lista_historial[0]=id
    lista_historial[1]=usuario

def agregar_evento(id,evento):
    lista_historial[2]=id
    lista_historial[3]=evento

def borrar():
    band=0
    cont=0
    while band==0:
        print("   ",f"{'ID USUARIO':<15}{'USUARIO':<20}{'ID EVENTO':<15}{'EVENTO':<25}{'UBICACIÓN':<30}{'CANTIDAD ENTRADAS COMPRADAS':<10}")
        print('-'*175)
        for id_usuario,usuario,id_evento,evento,ubicacion,cantidad in historial:
            cont=cont+1
            print(cont, ")", f"{id_usuario:<15}{usuario:<20}{id_evento:<15}{evento:<25}{ubicacion:<30}{cantidad:<10}")
        eleccion=input("Cuál es la fila del historial que desea eliminar? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            if eleccion <= len(historial) and eleccion>0:
                eliminado=historial.pop(eleccion-1)
                print("Usted ha eliminado:",eliminado)
                band=1
        if band==0:
            print("Opción incorrecta.")