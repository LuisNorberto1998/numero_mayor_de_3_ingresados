"""
Prgrama que calcula cual es el numero mayor de los tres que se ingresaron
"""
print "Ingresa 3 numeros"
numero1 = int(raw_input("Numero 1: "))#Numero 1
numero2 = int(raw_input("Numero 2: "))#Numero 2
numero3 = int(raw_input("Numero 3: "))#Numero 3
if numero1 >= numero2 and numero1 >= numero3: #Condiciona si el numero 1 es mayor o igual que el numero 2 y 3
    print numero1 #Imprime el numero 1
elif numero2 >= numero1 and numero2 >= numero3: #Condiciona si el numero 2 es mayor o igual que el numero 1 y 3
    print numero2 #Imprime el numero 2
elif numero3 >= numero1 and numero3 >= numero2:  #Condiciona si el numero 2 es mayor o igual que el numero 1 y 2
    print numero3 #Imprime el numero 2

