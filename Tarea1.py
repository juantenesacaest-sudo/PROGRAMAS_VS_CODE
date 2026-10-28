print ("¡Hola, mundo!")
print ("Bienvenido a Python David")
print (2+3)
suma=0
a=5
b=6
suma=a+b
print ("Suma: ", suma)
print (type (suma))
print (type ("David"))
promedio = 8.5
print (type (promedio))
# Para poder comentar
"""
Las tres comillas permiten hacer comentarios de varias líneas
"""
#Se agrega comas para ir agregando el texto a diferencia de java que era +
"""
sep se usa para separar los elementos que se imprimen, 
por defecto es un espacio pero se puede cambiar a cualquier otro caracter
"""
print ("Suma", suma,"A", a, "B", b, sep = " - ")
print ("Hola", "David", "Bienvenido a Python", promedio, sep = "-> ")

#input se usa para pedir los datos al usuario en vez del scanner de java
nombre = input("Ingresa tu nombre: ")
print ("Hola", nombre, "Bienvenido a Python :D")
edad = int (input ("Ingrese su edad: "))
print ("Su edad es: ", edad)
saldo = float (input ("Ingrese su saldo: "))
print ("Su saldo es: ", saldo)
#Una f antes de las comillas permite hacer interpolación de variables, es decir, poner variables dentro de un string
print (f"Su saldo es: {saldo}")

"""
la identación es importante en python, ya que define los bloques de código, 
a diferencia de java que se usan llaves y el : en python indica que se va a crear un bloque de código
"""
if saldo < 10:
    print ("Es pobre")
else:
    print ("Es rico")