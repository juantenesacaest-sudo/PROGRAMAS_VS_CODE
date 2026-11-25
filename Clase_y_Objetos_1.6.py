#Crear una clase
class Libro:
    pass
libro1=Libro()
print(type(libro1))
class Libro:
    #Contructor ↓
    def __init__(self, nombre, autor, estado, lista_libros):
        self.nombre=nombre
        self.autor=autor
        self.estado=estado
        self.lista_libros=lista_libros
    #Metodo ↓
    def mostrar(self):
        print(self.nombre,"|Autor: ", self.autor, "|Estado: ", self.estado)
    def cambiar_estado(self, estado1):
        self.estado=estado1
    #ToString() ↓
    def __str__(self):
        return f"Nombre del libro: {self.nombre}| → |Autor: {self.autor}| → |Estado: {self.estado:<12}|"

    def mostrar_lista(self):
        for i in self.lista_libros:
            print(i)

libro2=Libro("Python intermedio", "David Tenesaca", "Disponible", ["Python básico", "Python intermedio"])
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("Prestado")
print(libro2)
libro2.cambiar_estado("Disponible")
print(libro2)
print(libro2.nombre)
libro2.mostrar_lista()