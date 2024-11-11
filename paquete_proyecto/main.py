import logueo
import load_upload
from crud_usuarios import datos_usuario
from crud_historial import historial
import ArchivosJson
from crud_eventos import diccionario_eventos

def main():
    logueo.inicio_logueo()
    load_upload.guardar_usuarios(datos_usuario)
    load_upload.guardar_historial(historial)
    ArchivosJson.guardar(diccionario_eventos)

if __name__=="__main__":
    main() 