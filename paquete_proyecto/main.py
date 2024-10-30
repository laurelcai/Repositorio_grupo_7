import logueo
import load_upload
from crud_usuarios import datos_usuario
from crud_historial import historial

def main():
    logueo.inicio_logueo()
    load_upload.guardar_usuarios(datos_usuario)
    load_upload.guardar_historial(historial)

if __name__=="__main__":
    main() 