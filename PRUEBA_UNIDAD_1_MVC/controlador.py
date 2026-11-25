class ControladorMedicamentos:
    def __init__(self, modelo, vista):
        self.modelo=modelo
        self.vista=vista
    def ejecutar(self):
        opcion=""
        while True:
            opcion=self.vista.menu()
            if opcion == "1":
                try:
                    nombre, precio, cajas=self.vista.agregar_medicamento()
                    mensaje = self.modelo.registrar_funcion(nombre, precio, cajas)                    
                    self.vista.mostrar_mensaje(mensaje)
                except (ValueError) as e:
                    self.vista.error("=============================== Error al registrar: ",e," ===============================")
            elif opcion == "2":
                try:
                    self.vista.mostrar_medicamentos(self.modelo.listarFunciones)
                except:
                    self.vista.error("=============================== Error al cargar la lista ===============================")
            
            elif opcion == "3":
                try:
                    codigo, cantidad= self.vista.vender_medicamento()

                    mensaje=self.modelo.vender_medicamentos(codigo, cantidad)
                    if mensaje==True:
                        print("=============================== Operación exitosa ===============================")
                        self.vista.mostrar_mensaje(mensaje)
                    else:
                        print("=============================== Error al querer vender medicamentos ===============================")
                except ValueError as e:
                    self.vista.error("Error al vender: ",e)
            elif opcion == "4":
                print("=============================== Programa finalizado ===============================")
                break
            else:
                print("=============================== Opción no válida ===============================")