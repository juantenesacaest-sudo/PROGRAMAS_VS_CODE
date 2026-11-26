from persona import Persona
class Docente(Persona):
    def __init__(self, nombre, apellido, cedula, celular, correo, edad, direccion, asignatura,horas):
        super().__init__(nombre, apellido, cedula, celular, correo, edad, direccion)
        self.asignatura = asignatura
        self.horas = horas
        self.valor_hora = 20
        self.salario = 0
    def calcular_salario(self):
        self.salario = self.horas * self.valor_hora
        return self.salario
    def __str__(self):
        return f"{super().__str__()}, Asignatura: {self.asignatura}, Salario: {self.salario}"