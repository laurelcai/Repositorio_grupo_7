import validaciones
import variaciones


# Función para registrar un nuevo usuario
def registro():
    bandera = 0 # Bandera para controlar el bucle de validación del Nombre

    while bandera == 0:
        print("-"*50)
        nombre = input("Ingrese su nombre completo: ")
        if validaciones.validar_nombre(nombre) == 1:
            print("Nombre válido")
            bandera = 1
        else:
            print("Nombre invalido, porfavor ingreselo nuevamente")
    
    bandera=0
    while bandera==0:
        print("-"*50)
        email = input("Ingrese su email: ")
        if validaciones.validar_email(email) == 1:
            print("Correo valido")
            bandera=1
        else:
            print("Correo invalido. Ingreselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*50)
        print("-Puede contener letras (mayúsculas o minúsculas), números y guiones bajos")
        print("-Debe comenzar con una letra.")
        print("-Puede tener entre 3 y 16 caracteres.")
        print("-No puede contener caracteres especiales como @, #, etc., excepto el guion bajo")
        usuario = input("Ingrese su usuario: ")
        if validaciones.validar_usuario(usuario)==1:
            print("Usuario valido")
            bandera=1
        else:
            print("Usuario invalido, ingreselo nuevamente.")

    bandera=0
    while bandera==0:
        print("-"*50)
        print("Debe tener: entre 8 y 16 caracteres, al menos una letra mayúscula, al menos una letra minúscula,al menos un número ")    
        contraseña = input("Ingrese su contraseña: ")
        if validaciones.validar_contraseña(contraseña)==1:
            print("Contraseña valida")
            bandera=1
        else:
            print("Contraseña invalida, ingresela nuevamente")
    bandera=0
    while bandera==0:
        print("-"*50)
        dni = input("Ingrese su dni: ")
        if validaciones.validar_dni(dni)==1:
                dni = int(dni)
                print("DNI valido")
                bandera=1        
        else:
            print("DNI invalido, por favor ingrese un DNI valido")
    
    variaciones.agregar_usuarios(nombre,email,usuario,contraseña,dni)
    print("Usted se ha registrado correctamente")


def logueo():
    flag = 0  # Bandera para controlar el bucle de validación de la contraseña
    band = 0  # Bandera para controlar la búsqueda del usuario
    i = 0  # Contador para recorrer la lista de usuarios
    while band == 0:
        print("-"*50)
        usuario_logueo = input("Ingrese su usuario para iniciar sesion: ")
        if variaciones.validar_usuario(usuario_logueo)==1:
            band = 1  # Usuario encontrado
            print("Usuario encontrado")
        else:
            print("Datos inexistente, ingrese su usuario nuevamente")

    if band == 1:
        while flag == 0:
            print("-"*50)
            contraseña_logueo = input("Ingrese su contraseña: ")
            if variaciones.validar_contraseña(contraseña_logueo)==1:
                flag=1
            else:
                flag =0
                print("Contraseña incorrecta")    

def inicio_logueo():
    f=0
    while f == 0:
        print("-"*50)
        print('1. Registrarse')
        print('2. Iniciar sesion')
        print('3. Salir')
        print("-"*50)
        seleccion = input("Seleccione una opcion: ")
        if validaciones.validar(seleccion)==1:    
            seleccion=int(seleccion)
            if seleccion>0 and seleccion<=3:
                if seleccion == 1:
                    registro()
                    f=1

                elif seleccion == 2:
                    logueo()
                    print("Sesion iniciada")
                    f=1
                    
                elif seleccion == 3:
                    f = 1  # Termina el bucle principal
                    print("Fin de la operacion")

                return seleccion

        if f==0:
            print("Opcion no encontrada")
    