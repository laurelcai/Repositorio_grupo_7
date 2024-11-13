import validaciones
import crud_historial
import logueo
import load_upload


#matriz con todos datos de cada usuario registrado
datos_usuario = load_upload.cargar_usuarios()


def agregar_usuarios(nombre,mail,usuario,contraseña,dni):
    
    """Entrada: se recibe todos los datos del usuario registrado
    Salida: esos datos que ingresan a la funcion son guardados a la matriz de usuarios"""

    id=len(datos_usuario)+1000
    id=str(id)
    datos_usuario.append([nombre,mail,usuario,contraseña,dni,id,'USUARIO'])


def validar_usuario(usuario):

    """Entrada: Se recibe el usuario que se desea buscar 
    Salida: se busca y se devuelve si el usuario se encuentra en la matriz"""
    
    band=0
    for i in range (len(datos_usuario)):
        if datos_usuario[i][2] == usuario:
            band=1
            crud_historial.agregar_usuario(datos_usuario[i][2],datos_usuario[i][5])
            
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


def borrar_cuenta():
    cont=0
    bandera_borrar_usuario=0
    while bandera_borrar_usuario==0:
        usuario=input("Ingrese su usuario: ")
        contraseña=input("Ingrese se contraseña: ")
        if validar_usuario(usuario)==1 and validar_contraseña(contraseña)==1:
            for fila in datos_usuario:
                if fila[2]==usuario:
                    eliminado=datos_usuario.pop(cont)
                    print("Se ha eliminado el usuario,", eliminado[2])
                    bandera_borrar_usuario=1
                else:
                    print("Usuario no encontrado.")
                cont=cont+1
        else:
            print("Datos inválidos")


def interfaz_logueo():
    bandera_interfaz=0
    while bandera_interfaz==0:
        eleccion=input("")
        if eleccion=='0':
            logueo.inicio_logueo()
            bandera_interfaz=1
        if eleccion=='-1':
            print("Adiós.")
            bandera_interfaz=1
        if bandera_interfaz==0:
            return eleccion


def intentos_contraseña(contador_intentos=0):
    """Función recursiva que solicita una contraseña hasta un máximo de 4 intentos."""
    
    if contador_intentos >= 4:  # Caso base: si ya se han hecho 4 intentos
        print("Su cuenta fue bloqueada por exceso de intentos.Intente más tarde.")
        return 1

    # Solicitar la contraseña al usuario
    print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
    print(f"Contraseña incorrecta, ingresela de nuevo. Le quedan {4 - contador_intentos} intentos: ")
    intentos_de_contra = interfaz_logueo()
    if intentos_de_contra != None:
        # Validar la contraseña
        if validar_contraseña(intentos_de_contra) == 1:
            print("Contraseña correcta.")
            return 0
        else:
            # Incrementar el contador y llamar de nuevo a la función recursivamente
            return intentos_contraseña(contador_intentos + 1)
    else:
        return 2

