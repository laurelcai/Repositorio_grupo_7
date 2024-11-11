import crud_eventos
import validaciones
import logueo
import crud_usuarios
import crud_historial

def inicio():#se desplieaga un menu para seleccionar los distintos tipos de eventos
    
    """Luego de haber iniciado sesion el usuario,
    Sale: El usuario elije que desea hacer y se devuelve un valor al respecto  """
    
    print("Tipos de eventos: ")
    print("-"*175)
    print('1)Música.')
    print('2)Familia.')
    print('3)Teatro.')
    print('4)Deporte.')
    print('0)Cuenta.'.center(10,' '),'-1)Salir.'.center(10,' '))
    print("-"*175)    
        
    try:
        band=0
        elegir_inicio=int(input("Seleccione una opción: "))
        if elegir_inicio >0 and elegir_inicio<5: 
            eventos(elegir_inicio)
            band=1                

        if elegir_inicio==-1:
            print("Adios.")
            band=1                    

        if elegir_inicio==0:
            gestion_cuenta()
            band=1
        
        if band==0:
            raise
    
    except:
        print("Error, opcion no encontrada")
        inicio()
       

def eventos(elegir_inicio):#Se muestran los eventos filtrados segun lo seleccionado por el usuario

    """Entrada: Ingresa a la funcion como dato el tipo de evento seleccionado previamente.
        Salida: Sale la impresion de cada evento del respectivo evento elegido previamente"""
    bandera_eventos=0
    while bandera_eventos==0:
        print('-' * 175)
        print(" "*3,f"{'TIPO':<16} {'NOMBRE':22} {'UBICACIÓN':<22} {'FECHA Y HORA':<26}")
        print('-' * 175)
        elegir_inicio=str(elegir_inicio)

        cantidad_de_eventos=crud_eventos.filtrar_eventos(elegir_inicio)

        if cantidad_de_eventos<1:
            print("Todavía no se encontraron eventos, intenta de nuevo más tarde.")
            
        evento_elegido=crud_eventos.interfaz_eventos()
        if evento_elegido != None:
            if evento_elegido >0 and evento_elegido <= cantidad_de_eventos:
                comprar(evento_elegido,elegir_inicio)
                bandera_eventos=1
            else:
                print("Inválido. Opción no encontrada.")
        else:
            break


def comprar(evento_elegido,tipo_evento):

    """Entrada: Se recibe el evento al cual el usuario desea asistir
    Salida: Se muestra por pantalla los precios y ubicaciones disponibles"""
    bandera_comprar=0
    while bandera_comprar==0:
        print('-' * 175)
        print(" "*3,f"{'UBICACIÓN Y PRECIO':<10}")
        print('-' * 175)

        ubicacion=crud_eventos.filtrar_precios_eventos(evento_elegido,tipo_evento)
        elegir_ubicacion=crud_eventos.interfaz_eventos()
        if elegir_ubicacion != None:
            if elegir_ubicacion >0 and elegir_ubicacion <= 2:
                bandera_comprar=1
                band=0
                while band==0:
                    elegir_cantidad_entradas=input("Cuántas entradas desea comprar? ")
                    if validaciones.validar(elegir_cantidad_entradas)==1 and elegir_cantidad_entradas > '0':
                        print("Usted ha comprado",elegir_cantidad_entradas,"entradas en la ubicación",ubicacion[elegir_ubicacion-1][0])
                        crud_historial.agregar_historial(elegir_cantidad_entradas,ubicacion[elegir_ubicacion-1])
                        inicio()
                        band=1
                    else:
                        print("Opción incorrecta.")
                
            if bandera_comprar==0:
                print("Opción no encontrada.")
        else:
            break


def gestion_cuenta():
        bandera_cuenta=0
        while bandera_cuenta==0:
            print("-"*175)
            print('1)Cerrar cesión.')
            print('2)Borrar cuenta.')
            elegir_cuenta=crud_eventos.interfaz_eventos()
            if elegir_cuenta != None:
                    if elegir_cuenta==1:
                        bandera_cuenta=1
                        logueo.inicio_logueo()

                    if elegir_cuenta==2:
                        crud_usuarios.borrar_cuenta()
                        logueo.inicio_logueo()
                        bandera_cuenta=1
            else:
                break
