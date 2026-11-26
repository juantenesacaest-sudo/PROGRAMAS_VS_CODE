class Persona:
    def __init__(self, nombre, apellido, cedula, celular, correo, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.celular = celular
        self.correo = correo
        self.edad = edad
        self.direccion = direccion
    def validar_edad(self):
        if self.edad >= 18:
            return "Mayor de edad"
        else:
            return "Menor de edad"
    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}, Cédula: {self.cedula}, Edad: {self.edad}, dirección: {self.direccion}, Celular: {self.celular}, Correo: {self.correo}"
