import validaciones
import crud_usuarios
import gestor
import eventos


# Función para registrar un nuevo usuario
def registro():

    """Todo usuario que ingresa por primera vez al promgrama debe registrarse
    para poder hacer uso del mismo, y para ello debe completar una serie de peticiones.
    En esta funcion todas esas respuestas/datos son efectuadas y guardados en la matriz usuarios"""

    bandera_nombre= 0 # Bandera para controlar el bucle de validación del Nombre
    while bandera_nombre == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese su nombre completo:")
        nombre = crud_usuarios.interfaz_logueo()
        if nombre != None:
            if validaciones.validar_nombre(nombre) == 1:
                print("Nombre válido.")
                bandera_nombre = 1

                bandera_mail=0
                while bandera_mail == 0:
                    print("-"*175)
                    print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                    print("Ingrese su email: ")
                    mail = crud_usuarios.interfaz_logueo()
                    if mail != None:
                        if validaciones.validar_email(mail) == 1:
                            print("Correo válido.")
                            bandera_mail = 1

                            bandera_usuario=0
                            while bandera_usuario == 0:
                                print("-"*175)
                                print("-Puede contener letras (mayúsculas o minúsculas), números y guiones bajos.")
                                print("-Debe comenzar con una letra.")
                                print("-Puede tener entre 3 y 16 caracteres.")
                                print("-No puede contener caracteres especiales como @, #, etc., excepto el guion bajo.")
                                print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                print("Ingrese su usuario:")
                                usuario = crud_usuarios.interfaz_logueo()
                                if usuario != None:
                                    if validaciones.validar_usuario(usuario)==1:
                                        if crud_usuarios.validar_usuario(usuario)==0:
                                            print("Usuario válido.")
                                            bandera_usuario = 1

                                            bandera_contraseña=0
                                            while bandera_contraseña== 0:
                                                print("-"*175)
                                                print("Debe tener: entre 8 y 16 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número.")    
                                                print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                                print("Ingrese una contraseña:")
                                                contraseña = crud_usuarios.interfaz_logueo()
                                                if contraseña != None:
                                                    if validaciones.validar_contraseña(contraseña)==1:
                                                        print("Contraseña válida.")
                                                        bandera_contraseña = 1
                                                        
                                                        bandera_dni=0
                                                        while bandera_dni == 0:
                                                            print("-"*175)    
                                                            print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
                                                            print("Ingrese se DNI:")
                                                            dni = crud_usuarios.interfaz_logueo()
                                                            if dni != None:
                                                                if validaciones.validar_dni(dni)==1:
                                                                    print("DNI válido.")
                                                                    bandera_dni = 1
                                                                    crud_usuarios.agregar_usuarios(nombre,mail,usuario,contraseña,dni)
                                                                    print("Usted se ha registrado correctamente.")
                                                                    inicio_logueo()
                                                                else:
                                                                    print("DNI inválido, por favor ingréselo nuevamente")
                                                            else:
                                                                break

                                                    else:
                                                        print("Contraseña inválida, por favor ingrésela nuevamente")
                                                else:
                                                    break
                                        else:
                                            print("Usuario en uso, ingrese otro.")
                                    else:
                                        print("Usuario inválido, por favor ingréselo nuevamente")
                                else:
                                    break

                        else:
                            print("Correo inválido, por favor ingréselo nuevamente.")
                    else:
                        break
            else:
                print("Nombre inválido, por favor ingréselo nuevamente")
        else:
            break


def logueo():
    flag = 0  # Bandera para controlar el bucle de validación de la contraseña
    band = 0  # Bandera para controlar la búsqueda del usuario
    """Entrada: se recibe el usuario y contraseña por teclado
    Salida: se controla que el usuario este previamente registrado 
    y se devuelve que tipo de usuario se ingreso(maestro o usuario)"""

    while band == 0:
        print("-"*175)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print("Ingrese su usuario para iniciar sesión:")
        usuario_logueo =crud_usuarios.interfaz_logueo()
        if usuario_logueo != None:
            if crud_usuarios.validar_usuario(usuario_logueo)==1:
                band = 1  # Usuario encontrado
                print("Usuario encontrado.")
            else:
                print("Datos inexistente, ingrese su usuario nuevamente.")
        else:
            break

    if band == 1:
        while flag == 0:
            print("-"*175)
            print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
            print("Ingrese su contraseña:")
            contraseña_logueo =crud_usuarios.interfaz_logueo()
            if contraseña_logueo != None:
                if crud_usuarios.validar_contraseña(contraseña_logueo)==1:
                    flag=1
                    if crud_usuarios.tipo_de_usuario(usuario_logueo)==1:
                        return 1
                    else:
                        return 0
                else:
                    intentos=crud_usuarios.intentos_contraseña()
                    if intentos ==0:
                        flag=1
                        if crud_usuarios.tipo_de_usuario(usuario_logueo)==1:
                            return 1
                        else:
                            return 0
                    if intentos==1 :
                        flag=1
                        inicio_logueo()
                    if intentos ==2:
                        break
            else:
                break
                

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

                elif seleccion == 2:
                    f=1
                    tipo_de_usuario=logueo()
                    if tipo_de_usuario==0:
                        print("Sesión iniciada.")
                        eventos.inicio()
                    
                    if tipo_de_usuario==1:
                        print("Sesión iniciada como gestor.")
                        gestor.inicio()
                    
                elif seleccion == 3:
                    f = 1  # Termina el bucle principal
                    print("Fin de la operación.")
 

        if f==0:
            print("Opción no encontrada.")