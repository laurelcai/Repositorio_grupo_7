from paquete_proyecto.validaciones import validar_dni
from crud_eventos import porcentaje_asistencia
from paquete_proyecto.validaciones import validar_email

def test_porcentaje():
    assert porcentaje_asistencia(10, 5) == 50.0
    
def test_validar_dni():
    assert validar_dni(47057483) == 1
    
def test_validar_email():
    assert validar_email("lvicens@uade.edu.ar")== 1


