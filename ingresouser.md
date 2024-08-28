    datos_usuarios = []

    while True:
        nombre_completo = input("Ingrese su nombre completo: ")
        dni = input("Ingrese su DNI: ")
        email = input("Ingrese su email: ")
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        datos_usuario = [
            f"Nombre Completo: {nombre_completo}",
            f"DNI: {dni}",
            f"Email: {email}",
            f"Usuario: {usuario}",
            f"Contraseña: {contraseña}"
    ]

        datos_usuarios.append(datos_usuario)

        continuar = input("¿Desea ingresar otro usuario? (si/no): ")
        if continuar.lower() != 's':
            break

    for usuario in datos_usuarios:
        print("-" * 20)
        print("\n".join(usuario))
        print("-" * 20)  
