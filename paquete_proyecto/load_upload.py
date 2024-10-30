
def cargar_usuarios():
    matriz=[]
    try:
        with open(r"C:\Users\pc\Desktop\UADE\proyecto_progra1\paquete_proyecto\datos_usuarios.txt","r",encoding="UTF-8") as archivo:
            flag=0
            while flag ==0:
                line=archivo.readline()
                if line == '':
                    flag=1
                else:
                    line=line.strip()
                    usuario=line.split(";")
                    matriz.append(usuario)
            return matriz

    except FileNotFoundError:
        print("El archivo no existe. Se comenzará con listas vacías.")
        return []
    except EOFError:
        print("El archivo está vacío. Se comenzará con listas vacías.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")


def guardar_usuarios(matriz_usuarios):
    try:
        with open(r"C:\Users\pc\Desktop\UADE\proyecto_progra1\paquete_proyecto\datos_usuarios.txt","w",encoding="UTF-8")  as archivo:
            lineas = [f'{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]};{fila[5]};{fila[6]}\n' for fila in matriz_usuarios]
            archivo.writelines(lineas)    
            print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_historial():
    matriz=[]
    try:
        with open(r"C:\Users\pc\Desktop\UADE\proyecto_progra1\paquete_proyecto\datos_historial.txt","r",encoding="UTF-8") as archivo:
            flag=0
            while flag ==0:
                line=archivo.readline()
                if line == '':
                    flag=1
                else:
                    line=line.strip()
                    historial=line.split(";")
                    matriz.append(historial)
            return matriz

    except FileNotFoundError:
        print("El archivo no existe. Se comenzará con listas vacías.")
        return []
    except EOFError:
        print("El archivo está vacío. Se comenzará con listas vacías.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")


def guardar_historial(matriz_historial):
    try:
        with open(r"C:\Users\pc\Desktop\UADE\proyecto_progra1\paquete_proyecto\datos_historial.txt","w",encoding="UTF-8")  as archivo:
            lineas = [f'{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]};{fila[5]}\n' for fila in matriz_historial]
            archivo.writelines(lineas)    
            print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")