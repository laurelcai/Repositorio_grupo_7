import re
import gestor
def validar(entrada):#valida que la entrada no sea simplemente numero
    if re.match(r"^-?\d+$",entrada):
        return 1
    else:
        return 0
    
def validar_email(email): 
    validacion_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Expresión regular para validar el formato del email
    if re.match(validacion_email, email):
        return 1
    else:
        return 0
    
def validar_dni(dni): 
    validacion_dni = r'^\d{7,8}$'  # Expresión regular para validar el formato del DNI
    if re.match(validacion_dni, dni):
        return 1
    else:
        return 0

def validar_contraseña(contraseña):# Expresion regular para validar contraseña
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,16}$",contraseña):
        return 1
    else:
        return 0
    
def validar_nombre(nombre):#Expresion regular para validar el nombre del ususario
    if re.match(r"^([a-zA-ZáéíóúÁÉÍÓÚñÑ]+)(\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$", nombre):
        return 1
    else:
        return 0

def validar_usuario(usuario):#Expresion regular para validar el usuario ingrsado
    if re.match(r"^[a-zA-Z][a-zA-Z0-9_]{2,15}$",usuario):
        return 1
    else:
        return 0
    
def validar_tipo():
    bandera_validacion_tipo=0
    while bandera_validacion_tipo==0:
        print('1)Música.')
        print('2)Familia.')
        print('3)Teatro.')
        print('4)Deporte.')
        tipo=input("Seleccione el tipo de evento: ")
        if validar(tipo)==1:
            tipo = int(tipo)
            if tipo == 0:
                return gestor.inicio()
            if tipo == 1:
                return 'MUSICA',1
            if tipo ==2:
                return 'FAMILIA',2
            if tipo==3:
                return 'TEATRO',3
            if tipo==4:
                return 'DEPORTE',4
        else:
            print("Tipo de evento inválido.")


def validar_agregar_nombre_evento(nombre):
    if nombre in ['0', '1']:
        return 1
    
    if re.match(r"^[a-zA-Z][a-zA-Z0-9_ ]{1,14}[a-zA-Z0-9_]$", nombre):
        return 1
    else:
        return 0


def validar_agregar_fecha_evento(fecha):
    if fecha in ['0', '1']:
        return 1
    if re.match(r"^\d{1,2}\sde\s[a-zA-Z]+\s?,\s?\d{1,2}\s?hs$", fecha):
        return 1
    return 0