import json

def abrirJson():
    try:
        # Usar 'with' para abrir el archivo de manera segura
        with open('datoseventos.json', 'r') as eventos_json:
            # Intentar cargar el JSON
            eventos = json.load(eventos_json)
            # Verificar si hay al menos un evento
            if eventos:
                return eventos
            else:
                print("El archivo JSON está vacío.")
                return None
    except FileNotFoundError:
        print("El archivo no se encuentra.")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def guardar(diccionario_eventos):
    try:
        with open('datoseventos.json', 'w') as eventos_json:
            json.dump(diccionario_eventos,eventos_json)
    except:
        print("Archivo no encontrado")