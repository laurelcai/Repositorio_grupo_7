import validaciones
import crud_usuarios
import eventos
import crud_eventos
import crud_historial


def inicio():

    """Luego del usuario maestro decidir que quiere gestionar el programa, 
    se muestra por pantalla las multiples opciones, y a su vez con respecto a lo elegido
    redirige al usuario a la funcion correspondiente
    """
    band=0
    while band==0:
        print("-"*175)
        print('1)Imprimir matriz eventos.')
        print('2)Imprimir matriz usuarios.')
        print('3)Imprimir matriz historial.')
        print('4)Agregar evento.')
        print('5)Borrar evento.')
        print("-"*175)
        print('0)Cuenta.'.center(10,' '),'-1)Salir.'.center(10,' '))

        eleccion=input("Seleccione una opción: ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
        if eleccion==1:
            crud_eventos.imprimir_eventos()
        if eleccion==2:
            crud_usuarios.imprimir_usuarios()
        if eleccion==3:
            crud_historial.imprimir_historial()
        if eleccion==4:
            crud_eventos.agregar()
        if eleccion==5:
            crud_eventos.borrar()
            
        if eleccion==0:
            band=1
            eventos.gestion_cuenta()
            
        if eleccion==-1:
            band=1
            print("Adiós.")


def interfaz_gestor():
    bandera_interfaz=0
    while bandera_interfaz==0:
        eleccion=input("")
        if eleccion=='0':
            inicio()
            bandera_interfaz=1
        if eleccion=='-1':
            print("Adiós.")
            bandera_interfaz=1
        if bandera_interfaz==0:
            return eleccion