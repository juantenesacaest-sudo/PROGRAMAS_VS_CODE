#Primera forma
from modelo import*
#Segunda forma
from vista import VistaOperacion
from controlador import ControladorMedicamentos

print("Hola mundo :D")
modelo = Lista_funciones()
vista = VistaOperacion()
controlador = ControladorMedicamentos(modelo, vista)
controlador.ejecutar()