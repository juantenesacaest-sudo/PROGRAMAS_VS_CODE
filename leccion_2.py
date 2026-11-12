"""
EJERCICIO 1

¿Qué imprime el siguiente código?

texto = "TEC Azuay"
print(texto[4:7])

a. Azua
b. Azu
c. Tec
d. zua

LA RESPUESTA CORRECTA ES AZU
"""
print(30*"=", "EJERCICIO 1")
texto = "TEC Azuay"
print(texto[4:7])


"""
EJERCICIO 2

¿Qué ocurre al ejecutar el siguiente código?

datos = (10, 20, 30)
datos[1] = 99
print(datos)

a. Se produce un TypeError
b. Se produce un IndexError
c. Imprime (99, 20, 30)
d. Imprime (10, 99, 30)

da TypeError
"""
print(30*"=", "EJERCICIO 2")
datos = (10, 20, 30)
datos[1] = 99
print(datos)


"""
EJERCICIO 3
¿Qué imprime el siguiente código?

print("ab" * 3)

a. Error
b. ababab
c. ab ab ab
d. ab3

La respuesta correcta es ababab
"""
print(30*"=", "EJERCICIO 3")
print("ab" * 3)


"""
EJERCICIO 4

¿Qué imprime el siguiente código?

print(int(9.99))

a. 9.99
b. 9
c. Error
d. 10

La respuesta correcta es 9
"""
print(30*"=", "EJERCICIO 4")
print(int(9.99))


"""
EJERCICIO 5

¿Qué imprime el siguiente código?

frase = "aprendo Python en TEC"
print(len(frase.split()))

a. 3
b. 4
c. 13
d. 1

La respuesta correcta es 4
"""
print(30*"=", "EJERCICIO 5")
frase = "aprendo Python en TEC"
print(len(frase.split()))


"""
EJERCICIO 6
¿Qué imprime el siguiente código?

notas = {"Ana": 10, "Luis": 8}
for nombre, nota in notas.items():
    print(f"{nombre}:{nota}", end=" ")

a. Ana:10 Luis:8
b. ('Ana', 10) ('Luis', 8)
c. 10 8
d. Ana Luis

La respuesta correcta es Ana:10 Luis:8
"""
print(30*"=", "EJERCICIO 6")
notas = {"Ana": 10, "Luis": 8}
for nombre, nota in notas.items():
    print(f"{nombre}:{nota}", end=" ")
print("")


"""
EJERCICIO 7
¿Qué imprime el siguiente código?

for i in range(3, 0, -1):
    print(i, end=" ")

a.3 2 1 0
b. 3 2 1
c. Nada
d. 1 2 3

La respuesta correcta es: 3 2 1 
"""
print(30*"=", "EJERCICIO 7")
for i in range(3, 0, -1):
    print(i, end=" ")
print("")


"""
EJERCICIO 8

¿Qué imprime el siguiente código?

total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)

a. 15
b. 5
c. 21
d. 10

La respuesta correcta es: 15
"""
print(30*"=", "EJERCICIO 8")
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)


"""
EJERCICIO 9

¿Qué imprime el siguiente código?

suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)

a. 0
b. 10
c. 6
d. 4

La respuesta correcta es: 6
"""
print(30*"=", "EJERCICIO 9")
suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)


"""
EJERCICIO 10

¿Cuántas veces se imprime «*» en el siguiente código?

for i in range(3):
    for j in range(2):
        print("*", end="")

a. 9
b. 6
c. 3
d. 5

La respuesta correcta es: 6
"""
print(30*"=", "EJERCICIO 10")
for i in range(3):
    for j in range(2):
        print("*", end="")
print("")


"""
EJERCICIO 11

Ejercicio 2. Validar contraseña

Pida una contraseña y verifique que cumpla todas estas reglas: tener al menos 8 
caracteres, al menos un dígito y al menos una letra mayúscula. Recorra la 
cadena con for (o use any). Muestre Contraseña segura o la lista de reglas que no 
cumple.

Escriba su código Python completo en el cuadro de respuesta. Respete la 
sangría de 4 espacios.
"""
# Escriba su solución aquí
print(30*"=", "EJERCICIO 11")
clave = input("Contraseña: ")
errores = []
largo = len(clave)

if largo < 8:
    errores.append("Debe tener al menos 8 caracteres")

tiene_digito=False
tiene_mayusculas=False
for i in clave:
    if i.isdigit():
          tiene_digito=True
    if i.isupper():
          tiene_mayusculas=True
if not tiene_digito:
    errores.append("Debe tener almenos un dígito")
if not tiene_mayusculas:
    errores.append("Debe tener al menos una mayuscula")
if len(errores) == 0:
    print("Contraseña segura")
else:
    print("La contraseña no cumple con los requisitos")
    for o in errores:
        print("-", o)