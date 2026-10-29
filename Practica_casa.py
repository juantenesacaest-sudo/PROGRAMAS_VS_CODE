print ("hola mundo")
nombre = input ("Ingrese su nombre: ")
print ("Hola, ", nombre)
edad = int (input("Ingrese su edad: "))
if edad>=18:
    print ("Bienvenido al mejor programa del mundo :D")
    saldo = float (input ("Ingrese su saldo: "))
    pobre = saldo <10 and saldo >0
    rico = saldo > 10 and saldo < 100
    if pobre:
        print ("Es pobre")
        print ("pobrecito", "el ", nombre, "tiene un saldo de", saldo, sep = " - ")
    else:
        if rico:
            print ("Es rico")
        else:
            print ("Es millonario")
else:
    print ("Lo sentimos, no tiene la mayoria de edad para poder entrar")
    exit(0)