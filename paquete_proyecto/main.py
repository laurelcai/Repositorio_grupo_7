import logueo
import eventos

def run():
    band=0
    while band==0:
        eleccion=logueo.inicio_logueo()
        if eleccion==2:
            eventos.inicio()
            band=1
        if eleccion==3:
            band=1


if __name__=="__main__":
    run()