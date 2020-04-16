print("Ejercicio 1")
cadena= input()
espacio=cadena.find(" ")
A= int(cadena[:espacio])
B=int(cadena[espacio:])
if(A>=0 and B<=10):
    print(A+B)
