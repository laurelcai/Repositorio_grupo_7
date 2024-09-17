import validaciones
import variaciones
import eventos

def inicio():#se desplieaga un menu para seleccionar los distintos tipos de eventos
    
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
        print('5)Gestionar')
        print('0)Cerrar sesión'.center(10,' '),'-1)Salir'.center(10,' '))
        print("-"*100)    
        
        elegir_inicio=input("Seleccione una opción: ")
        if validaciones.validar(elegir_inicio)==1:
            elegir_inicio=int(elegir_inicio)
            if elegir_inicio <= 5 and elegir_inicio >-2:
                if elegir_inicio <6:
                    band=1
                    return elegir_inicio
                    
                if elegir_inicio==-1:
                    print("Adios")
                    band=1
                    return -1
                
                if elegir_inicio==0:
                    return 0
            else:
                print("Opción no encontrada")
        else:
            print("Opción no encontrada")


def gestionar():
        print("-"*100)
        print('1)Imprimir matriz eventos')
        print('2)Imprimir matriz usuarios')
        print('3)Imprimir matriz historial')
        print('4)Agregar evento')
        print('5)Borrar evento')
        band=0
        while band==0:
            eleccion=eventos.interfaz()
            if eleccion==1:
                variaciones.imprimir_eventos()
                band=1
            if eleccion==2:
                variaciones.imprimir_usuarios()
                band=1
            if eleccion==3:
                variaciones.imprimir_historial()
                band=1
            if eleccion==4:
                variaciones.agregar()
                band=1
            if eleccion==5:
                variaciones.borrar()
                band=1
            
            if eleccion==0:
                band=1
                return 0
            
            if eleccion==-1:
                band=1
                return -1

            