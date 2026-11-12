#Declaración de funciones
def saludar():
    print("Hola David Tenesaca")
saludar()
#funcion con parametros
def calcular_edad(anio_nacimiento, anio_actual):        
    print("Edad: ", anio_actual-anio_nacimiento)
a= int(input("ingrese su año de nacimiento: "))
b=int(input("Ingrese el año actual: "))
calcular_edad(a, b)
#funciones con retorno
def calcular_iva(precio, valor_del_iva):
    return precio*valor_del_iva
resultado=calcular_iva(10, 0.15)
print("El iva es: ",resultado)
#funciones con valores con defecto
def calcular_iva(precio, valor_del_iva=0.15):
    return precio*valor_del_iva
resultado=calcular_iva(100)
print("El iva es: ", resultado)
resultado=calcular_iva(100, 0.14)
print("El iva es: ", resultado)
#Funciones con listas
def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print("Es par", e)
        else:
            print("Es impar", e)
lista_de_numero=range(0, 1000, 2)
calcular_par(lista_de_numero)
lista_de_numero=range(5, 0, -1)
for e in lista_de_numero:
    print(e, end=" ")
print("")
#funciones con tuplas * obligatorio
def suma_numeros(*a):
    return sum(a)
print("La suma de los elementos: ",suma_numeros(1,2,3,4))
#Funciones con diccionarios
def estudiantes(**lista_estudiantes):
    suma_total=0
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante ", nombre,"tiene", edad)
        suma_total+=edad
    print(suma_total)
estudiantes(Veronica=20, Juan=25, David=18, Minchala=18, Lumbi=20, Frixon=18, Kevin=21)

"""
MENU DE USUARIOS
1. INGRESE NOMBRES: Mensaje de bienvenida
2. MENU DE PREGUNTAS: le va a presentar las 11 preguntas, pregunta 1: listas, pregunta 2: diccionarios......., 12. salir 13. regresar al menu principal
3. SALIR: 
"""
entrada=""
def saludar(nombre_menu):
    print("Hola ", nombre_menu, " bienvenido a este programa")

def pregunta1():
    print(28*"=","pregunta 1", "="*28)
    print("Que impreme el siguiente texto: ")
    print("texto = ''TEC Azuay''")
    print("print(texto[4:7])")
    print("Opciones: \na. Azua\n b. Azu\n c. Tec\n d. zua")
    texto = "TEC Azuay"
    print(f"La respuesta correcta es: {texto[4:7]}")
    #Incorrecta da AZU

def pregunta2():
    print(28*"=","pregunta 2", "="*28)
    print("¿Qué ocurre al ejecutar el siguiente código?: ")
    print("datos = (10, 20, 30)")
    print("print(texto[4:7])")
    print("datos[1] = 99")
    print("print(datos)")
    print("Opciones: \na. Se produce un TypeError\n b. Se produce un IndexError\n c. Imprime (99, 20, 30)\n d. Imprime (10, 99, 30)")
    """
    datos = (10, 20, 30)
    datos[1] = 99
    """
    print(f"La respuesta correcta es: Se produce un TypeError")

def pregunta3():
    print(28*"=","pregunta 3", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("print(''ab'' * 3)")
    print("Opciones:\n a. Error\n b. ababab\n c. ab ab ab\n d. ab3")
    print(f"La respuesta correcta es: {'ab'*3}")

def pregunta4():
    print(28*"=","pregunta 4", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("print(int(9.99))")
    print("Opciones:\n a. 9.99\n b. 9\n c. Error\n d. 10")
    print(f"La respuesta correcta es: {int(9.99)}")

def pregunta5():
    print(28*"=","pregunta 5", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("frase = ''aprendo Python en TEC''")
    print("print(len(frase.split()))")
    print("Opciones:\n a. 3\n b. 4\n c. 13\n d. 1")
    frase = "aprendo Python en TEC"
    print(f"La respuesta correcta es: {len(frase.split())}")

def pregunta6():
    print(28*"=","pregunta 6", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("notas = {''Ana'': 10, ''Luis'': 8}")
    print("for nombre, nota in notas.items():")
    print("    print(f''{ nombre}:{nota}'', end='' '')")
    print("Opciones:\n a. Ana:10 Luis:8\n b. ('Ana', 10)('Luis', 8)\n c. 10 8\n d. Ana Luis")
    notas = {"Ana": 10, "Luis": 8}
    for nombre, nota in notas.items():
        print(f"{nombre}:{nota}", end=" ")
    print("")
    print("La repuesta correcta es: Ana:10 Luis:8")

def pregunta7():
    print(28*"=","pregunta 7", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("for i in range(3, 0, -1):")
    print("    print(i, end=" ")")
    print("Opciones:\n a. 3 2 1 0\n b. 3 2 1\n c. Nada\n d. 1 2 3")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print("")
    print("La respuesta correcta es: 3 2 1")

def pregunta8():
    print(28*"=","pregunta 8", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("total = 0")
    print("n = 1")
    print("while n <= 5:")
    print("    total += n")
    print("    n += 1")
    print("print(total)")
    print("Opciones:\n a. 15\n b. 5\n c. 21\n d. 10")
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    print(f"La respuesta correcta es: {total}")

def pregunta9():
    print(28*"=","pregunta 9", "="*28)
    print("¿Qué imprime el siguiente código?: ")
    print("suma = 0")
    print("for n in range(1, 5):")
    print("    if n % 2 != 0:")
    print("        continue")
    print("    suma += n")
    print("print(suma))")
    print("Opciones:\n a. 0\n b. 10\n c. 6\n d. 4")
    suma = 0
    for n in range(1, 5):
        if n % 2 != 0:
            continue
        suma += n
    print(f"La respuesta correcta es: {suma}")

def pregunta10():
    print(28*"=","pregunta 10", "="*28)
    print("¿Cuántas veces se imprime «*» en el siguiente código?: ")
    print("for i in range(3):")
    print("    for j in range(2):")
    print("        print(''*'', end="")")
    print("Opciones:\n a. 9\n b. 6\n c. 3\n d. 5")
    for i in range(3):
        for j in range(2):
            print("*", end="")
    print()
    print("La respuesta correcta es: 6")

def pregunta11():
    print(28*"=","pregunta 11", "="*28)
    print("Validar contraseña")
    print(
        "Pida una contraseña y verifique que cumpla todas estas reglas:\n"
        "- Tener al menos 8 caracteres.\n"
        "- Tener al menos un dígito.\n"
        "- Tener al menos una letra mayúscula.\n\n"
        "Recorra la cadena con for (o use any).\n"
        "Muestre 'Contraseña segura' o la lista de reglas que no cumple.\n\n"
        "Escriba su código Python completo en el cuadro de respuesta.\n"
        "Respete la sangría de 4 espacios.")
    print(f"La respuesta correcta es: ")
    print(
        'clave = input("Contraseña: ")\n'
        '# Escriba su solución aquí\n'
        'errores = []\n'
        'largo = len(clave)\n\n'
        'if largo < 8:\n'
        '    errores.append("Debe tener al menos 8 caracteres")\n\n'
        'tiene_digito = False\n'
        'tiene_mayusculas = False\n'
        'for i in clave:\n'
        '    if i.isdigit():\n'
        '        tiene_digito = True\n'
        '    if i.isupper():\n'
        '        tiene_mayusculas = True\n\n'
        'if not tiene_digito:\n'
        '    errores.append("Debe tener al menos un dígito")\n\n'
        'if not tiene_mayusculas:\n'
        '    errores.append("Debe tener al menos una mayúscula")\n\n'
        'if len(errores) == 0:\n'
        '    print("Contraseña segura")\n'
        'else:\n'
        '    print("La contraseña no cumple con los requisitos")\n'
        '    for o in errores:\n'
        '        print("-", o)')
    print("Va a funcionar de la siguiente manera: ")    
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

salir=False
while not salir:
    print(28*"X","MENU DE USUARIO", "X"*28)
    entrada=input("Ingrese una opción: 1. Saludo, 2. Menu de preguntas, 3. Salir: ")
    opcion=int(entrada)
    if opcion==1:
        nombre_menu=input("Ingrese su nombre: ")
        saludar(nombre_menu)
    elif opcion==2:
        entrada_2=""
        while True:                            
            print(28*"*","MENU DE PREGUNTAS", "*"*28)
            print("OPCIONES DE PREGUNTA")
            entrada_2=input("INGRESE LOS SIGUIENTES NÚMEROS PARA VER LAS PREGUNTAS CON SUS RESPUESTAS\n"
                "1. PREGUNTA NÚMERO 1\n"
                "2. PREGUNTA NÚMERO 2\n"
                "3. PREGUNTA NÚMERO 3\n"
                "4. PREGUNTA NÚMERO 4\n"
                "5. PREGUNTA NÚMERO 5\n"
                "6. PREGUNTA NÚMERO 6\n"
                "7. PREGUNTA NÚMERO 7\n"
                "8. PREGUNTA NÚMERO 8\n"
                "9. PREGUNTA NÚMERO 9\n"
                "10. PREGUNTA NÚMERO 10\n"
                "11. PREGUNTA NÚMERO 11\n"
                "12. SALIR DEL PROGRAMA \n"
                "13. REGRESAR AL MENU PRINCIPAL\n"
                "INGRESE UNA OPCIÓN: "
                )
            opcion_2=int(entrada_2)
            if opcion_2==1:
                pregunta1()
            elif opcion_2==2:
                pregunta2()
            elif opcion_2==3:
                pregunta3()
            elif opcion_2==4:
                pregunta4()
            elif opcion_2==5:
                pregunta5()
            elif opcion_2==6:
                pregunta6()
            elif opcion_2==7:
                pregunta7()
            elif opcion_2==8:
                pregunta8()
            elif opcion_2==9:
                pregunta9()
            elif opcion_2==10:
                pregunta10()
            elif opcion_2==11:
                pregunta11()
            elif opcion_2==12:
                print("Gracias por usar este programa")
                salir=True
                break
            elif opcion_2==13:
                print("Saliendo al menu principal..........")
                break
            else:
                print("Esa opción no es válida >:C")                                            
    elif opcion==3:
        print("Gracias por usar este programa")
        salir=True
    else:
        print("Ese número no es válido")