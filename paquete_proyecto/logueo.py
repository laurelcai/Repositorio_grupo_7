import validaciones
import variaciones


# Función para registrar un nuevo usuario
def registro():

    """Todo usuario que ingresa por primera vez al promgrama debe registrarse
    para poder hacer uso del mismo, y para ello debe completar una serie de peticiones.
    En esta funcion todas esas respuestas/datos son efectuadas y guardados en la matriz usuarios"""

    bandera = 0 # Bandera para controlar el bucle de validación del Nombre

    while bandera == 0:
        print("-"*175)
        nombre = input("Ingrese su nombre completo: ")
        if validaciones.validar_nombre(nombre) == 1:
            print("Nombre válido.")
            bandera = 1
        else:
            print("Nombre inválido, por favor ingréselo nuevamente")
    
    bandera=0
    while bandera==0:
        print("-"*175)
        email = input("Ingrese su email: ")
        if validaciones.validar_email(email) == 1:
            print("Correo válido.")
            bandera=1
        else:
            print("Correo invalido, por favor ingréselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*175)
        print("-Puede contener letras (mayúsculas o minúsculas), números y guiones bajos.")
        print("-Debe comenzar con una letra.")
        print("-Puede tener entre 3 y 16 caracteres.")
        print("-No puede contener caracteres especiales como @, #, etc., excepto el guion bajo.")
        usuario = input("Ingrese su usuario: ")
        if validaciones.validar_usuario(usuario)==1:
            if variaciones.validar_usuario(usuario)==0:
                print("Usuario válido.")
                bandera=1
            else:
                print("Usuario en uso, ingrese otro.")
        else:
            print("Usuario inválido, ingreselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*175)
        print("Debe tener: entre 8 y 16 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número.")    
        contraseña = input("Ingrese su contraseña: ")
        if validaciones.validar_contraseña(contraseña)==1:
            print("Contraseña válida.")
            bandera=1
        else:
            print("Contraseña inválida, ingrésela nuevamente.")
    bandera=0
    while bandera==0:
        print("-"*175)
        dni = input("Ingrese su DNI: ")
        if validaciones.validar_dni(dni)==1:
                dni = int(dni)
                print("DNI válido.")
                bandera=1        
        else:
            print("DNI inválido, por favor ingrese un DNI válido.")
    
    variaciones.agregar_usuarios(nombre,email,usuario,contraseña,dni)
    print("Usted se ha registrado correctamente.")


def logueo():
    flag = 0  # Bandera para controlar el bucle de validación de la contraseña
    band = 0  # Bandera para controlar la búsqueda del usuario
    """Entrada: se recibe el usuario y contraseña por teclado
    Salida: se controla que el usuario este previamente registrado 
    y se devuelve que tipo de usuario se ingreso(maestro o usuario)"""

    while band == 0:
        print("-"*175)
        usuario_logueo = input("Ingrese su usuario para iniciar sesión: ")
        if variaciones.validar_usuario(usuario_logueo)==1:
            band = 1  # Usuario encontrado
            print("Usuario encontrado.")
        else:
            print("Datos inexistente, ingrese su usuario nuevamente.")

    if band == 1:
        while flag == 0:
            print("-"*175)
            contraseña_logueo = input("Ingrese su contraseña: ")
            if variaciones.validar_contraseña(contraseña_logueo)==1:
                flag=1
            else:
                flag =0
                print("Contraseña incorrecta.")
                
    if variaciones.tipo_de_usuario(usuario_logueo)==1:
        return 1
    else:
        return 0


def inicio_logueo():

    """Primer menú, el cual muestra por pantalla las opciones previo al ingreso al programa,
     y a su vez con respecto a lo elegido redirige al usuario a la funcion correspondiente"""

    f=0
    while f == 0:
        print("-"*175)
        print('1) Registrarse.')
        print('2) Iniciar sesión.')
        print('3) Salir.')
        print("-"*175)
        seleccion = input("Seleccione una opción: ")
        if validaciones.validar(seleccion)==1:    
            seleccion=int(seleccion)
            if seleccion>0 and seleccion<=3:
                if seleccion == 1:
                    registro()
                    f=1
                    return seleccion,0

                elif seleccion == 2:
                    f=1
                    tipo_de_usuario=logueo()
                    if tipo_de_usuario==0:
                        print("Sesión iniciada.")
                        return seleccion, 0
                    
                    if tipo_de_usuario==1:
                        print("Sesión iniciada como gestor.")
                    
                        return seleccion, 1
                    
                elif seleccion == 3:
                    f = 1  # Termina el bucle principal
                    print("Fin de la operación.")

                    return seleccion, 0

        if f==0:
            print("Opción no encontrada.")
