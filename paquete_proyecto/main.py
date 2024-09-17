import logueo
import eventos
import gestor
def run():

    volver_logueo=0
    while volver_logueo==0:#mientras volver_logreo sea 0 se va a volver al menu de logueo

        eleccion,tipo_usuario=logueo.inicio_logueo()#se despliega menu de logueo
        if eleccion==2:

            menu_eventos=0
            while menu_eventos==0:#mientras menu_eventos sea 0 se va a volver al menu de eventos
                if tipo_usuario==0:
                    seleccion=eventos.inicio()#se despliega menu de eventos
                if tipo_usuario==1:
                    seleccion=gestor.inicio()

                if seleccion==0:#cerrar sesion
                    volver_logueo=0
                    menu_eventos=1

                if seleccion==-1:#salir definitivo
                    volver_logueo=1
                    menu_eventos=1
                
                if seleccion==5:
                    menu_gestionar=0
                    while menu_gestionar==0:
                        seleccionar=gestor.gestionar()
                        if seleccionar==0:
                            menu_eventos=0
                            menu_gestionar=1
                        if seleccionar==-1:
                            volver_logueo=1
                            menu_eventos=1
                            menu_gestionar=1

                if seleccion>0 and seleccion<5:

                    mostrar_eventos=0
                    while mostrar_eventos==0:#mientras mostrar eventos sea 0 se mostrara los eventos en bucle

                            cantidad_de_eventos=eventos.eventos(seleccion)#se muestran los eventos disponibles
                            elegir_interfaz=eventos.interfaz()#se elige por teclado el evento
                            if elegir_interfaz <= cantidad_de_eventos and elegir_interfaz >0:
                                
                                mostrar_ubicaciones=0
                                while mostrar_ubicaciones==0:#mientras mostrar_ubicaciones sea 0 se mostrara las ubicaciones disponibles en bucle
                                    
                                    opciones,ubicacion=eventos.mostrar_ubicacion(elegir_interfaz)#se muestra las ubicaciones disponibles
                                    elegir_ubicacion=eventos.interfaz()#se elige la ubicacion 
                                    if elegir_ubicacion <= opciones and elegir_ubicacion > 0:
                                        eventos.comprar(ubicacion,elegir_ubicacion)#se realiza la compra
                                        
                                        salir_o_inicio=0
                                        while salir_o_inicio==0:#mientras no se elija entre salir o volver menu eventos se repetira en bucle
                                            
                                            bucle=eventos.interfaz()#terminado el prodecimiento se consulta si volver al menu eventos o salir

                                            if bucle==0:#volver al menu eventos
                                                menu_eventos=0
                                                mostrar_eventos=1
                                                mostrar_ubicaciones=1
                                                salir_o_inicio=1

                                            if bucle==-1:#salir definitivo
                                                menu_eventos=1
                                                volver_logueo=1
                                                mostrar_eventos=1
                                                salir_o_inicio=1
                                                mostrar_ubicaciones=1
                                        
                                    if elegir_ubicacion == 0:#volver menu eventos
                                        mostrar_ubicaciones=1
                                        menu_eventos=0
                                        mostrar_eventos=1

                                    if elegir_ubicacion==-1:#salir definitivo
                                        mostrar_eventos=1
                                        mostrar_ubicaciones=1
                                        menu_eventos=1
                                        volver_logueo=1
                                    
                                    if mostrar_ubicaciones==0:
                                        print("Ubicacion no encontrada")

                            if elegir_interfaz==0:#volver al menu de eventos
                                menu_eventos=0
                                mostrar_eventos=1
                            
                            if elegir_interfaz==-1:#salir definitivamente
                                mostrar_eventos=1
                                menu_eventos=1 
                                volver_logueo=1

                            if mostrar_eventos == 0:
                                print("ERROR,evento no encontrado")

        if eleccion==3:#salir dfinitivo
            volver_logueo=1


if __name__=="__main__":
    run()