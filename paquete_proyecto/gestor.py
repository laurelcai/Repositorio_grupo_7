import validaciones
import variaciones
import eventos

def inicio():#se desplieaga un menu para seleccionar los distintos tipos de eventos
    
    """Luego de haber iniciado sesion el usuario maestro,
    Sale: El usuario maestro elije que desea hacer y se devuelve un valor al respecto  """

    band=0
    while band==0:

        print("Tipos de eventos: ")
        print("-"*175)
        print('1)Música.')
        print('2)Familia.')
        print('3)Teatro.')
        print('4)Deporte.')
        print('5)Gestionar.')
        print('0)Cerrar sesión.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("-"*175)    
        
        elegir_inicio=input("Seleccione una opción: ")
        if validaciones.validar(elegir_inicio)==1:
            elegir_inicio=int(elegir_inicio)
            if elegir_inicio <= 5 and elegir_inicio >-2:
                if elegir_inicio <6:
                    band=1
                    return elegir_inicio
                    
                if elegir_inicio==-1:
                    print("Adios.")
                    band=1
                    return -1
                
                if elegir_inicio==0:
                    return 0
            else:
                print("Opción no encontrada.")
        else:
            print("Opción no encontrada.")


def gestionar():

    """Luego del usuario maestro decidir que quiere gestionar el programa, 
    se muestra por pantalla las multiples opciones, y a su vez con respecto a lo elegido
    redirige al usuario a la funcion correspondiente
    """

    print("-"*175)
    print('1)Imprimir matriz eventos.')
    print('2)Imprimir matriz usuarios.')
    print('3)Imprimir matriz historial.')
    print('4)Agregar evento.')
    print('5)Borrar evento.')
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

            