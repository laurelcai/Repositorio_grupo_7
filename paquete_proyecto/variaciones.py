from validaciones import validar
lista_id=[]
ubicaciones=[]

#Ordenamiento de matriz con criterio, alfabeticamente por artista/nombre
def ordenar(matriz_eventos_desordenada):
    matriz_eventos = sorted(matriz_eventos_desordenada,key=lambda x: (x[2]))
    return matriz_eventos

def filtrar_matriz(matriz_eventos,elegir1,lista,a):
    if elegir1 > 0:
        ubicaciones.clear()
        filtrados = [fila for fila in matriz_eventos if fila[a] == lista[elegir1-1]]
        if a == 0:
            for i in range(5,len(filtrados[0])):
                print(i-4,")",filtrados[0][i])
                ubicaciones.append(filtrados[0][i])
            
            return i-4,ubicaciones
        
        if a ==1:
            cont=0
            lista_id.clear()
            for fila in filtrados:
                if len(filtrados)>0:
                    lista_id.append(fila[0])
                cont=cont+1
                print(cont,")",f"{fila[1]:<20} {fila[2]:25} {fila[3]:<25} {fila[4]:<20}")
            
            return lista_id