#7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
print("Ingresa un dos valores: a y b")
print("Obtendremos las operaciones de igualdad, diferencia, mayor o menor")

a= int(input("ingresa 1er valor: "))

b= int(input("ingresa 2do valor: "))

print( "¿Los números son iguales?:", a == b)
print( "¿Los números son diferentes?:", a != b)
print( "¿El primer número es mayor que el segundo?:", a > b)
print( "¿El segundo número es mayor o igual que el primero?:", a >= b)