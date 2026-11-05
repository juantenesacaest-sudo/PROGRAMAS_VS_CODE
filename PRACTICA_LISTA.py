notas_estudiante= [10,8,9,5]
notas_estudiante.append(20)
print("Notas del estudiante: ", notas_estudiante)
print("Segunda nota: ", notas_estudiante[1])
notas_estudiante.insert(1, 10)
print("Tamaño: ",len(notas_estudiante))
print("Último: ",notas_estudiante[-1])
print("Suma: ",sum(notas_estudiante))
print("Máximo: ",max(notas_estudiante))
print("Mínimo: ",min(notas_estudiante))
print("Primera nota: ", notas_estudiante[0])
print("Notas 9 y 5: ", notas_estudiante[-3:-1])
print("Se ordena las notas: ", sorted(notas_estudiante))
notas_estudiante.remove(9)
print("Se ordena las notas: ", sorted(notas_estudiante))
print("Notas desde la posición 2: ", notas_estudiante[2:])
print("Primeras 2 notas: ", notas_estudiante[:2])
print("Lista invertida: ", notas_estudiante[::-1])
#=============================== TUPLAS ===========================
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print("Meses del año:", meses)
print("Primer mes: ", meses[0])
print("Último mes: ", meses[-1])
# NO se puede modificar una tupla, meses.append("Mes 13") # Esto generará un error
print("Diccionario:")
datos = {"Nombre": "Juan", 
                "Edad": 18,
                "Sexo": "Masculino",
                "Celular":"0967801346",
                "Notas": [10, 9, 8, 10]}
print(datos)
print("Nombre: ", datos["Nombre"])
print ("Llaves: ", datos.keys())
print("CONJUNTOS")
conjunto_a={1, 5, 4, 6, 8}
conjunto_b={1, 9, 6, 5, 4}
print("Interseccion: ", conjunto_a & conjunto_b)
print("Unión: ", conjunto_a | conjunto_b)