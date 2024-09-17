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

ubicaciones=[]
datos_usuario = [["maestro","maestro@email.com", "maestro77", "123456", 11111111, "maestro"]]

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
