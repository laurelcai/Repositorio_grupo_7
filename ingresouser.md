    datos_usuarios = []
    id_usuario = 1

    def registrar_usuario():
        global id_usuario
        while True:
            nombre_completo = input("Ingrese su nombre completo: ")
            dni = input("Ingrese su DNI: ")
            email = input("Ingrese su email: ")
            usuario = input("Ingrese su usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            datos_usuario = [
                id_usuario,  
                nombre_completo,
                dni,
                email,
                usuario,
                contraseña
        ]

            datos_usuarios.append(datos_usuario)

            id_usuario += 1

            continuar = input("¿Desea ingresar otro usuario? (s/n): ")
            if continuar.lower() != 's':
                break

    def iniciar_sesion():
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        for datos in datos_usuarios:
            if datos[4] == usuario and datos[5] == contraseña:
                print("Inicio de sesión exitoso.")
                return True
        print("Usuario o contraseña incorrectos.")
        return False

    while True:
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            if iniciar_sesion():
                break
        elif opcion == '3':
            break
        else:
            print("Datos no registrados. Ingrese nuevamente.")
