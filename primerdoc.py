from random import randint

matriz_eventos=[]


def CRUD():
    i=0
    tipo=0

    while tipo != "SALIR":
        tipo=input("Ingrese el tipo de evento: ")
        tipo=tipo.upper()
        if tipo != "SALIR":    
            matriz_eventos.append([])
            nombre=input("Ingrese el nombre del evento: ")
            nombre=nombre.upper()
            capacidad=int(input("Ingrese su capacidad total: "))
            matriz_eventos[i].extend([tipo,nombre,capacidad])
            i=i+1

def musica():
    filas=len(matriz_eventos)
    columnas=len(matriz_eventos[0])
    print(f"{'TIPO':<10} {'NOMBRE':<10} {'CAPACIDAD':>10}")
    print('-' * 32)
    for i in range(filas):
         if matriz_eventos[i][0] == 'MUSICA':
            for j in range(columnas):
                print(f"{matriz_eventos[i][j]:<10}",end="")
            print()






#que se desea hacer
CRUD()
print('a)Música'.center(10,' '),'b)Familia'.center(10,' '),'c)Teatro'.center(10,' '),'d)Especiales'.center(10,' '))
elegir=input("Seleccione una opción: ")
elegir=elegir.lower()
if elegir == "a":
    musica()

"""
if elegir == "b":

if elegir == "c":

"""
