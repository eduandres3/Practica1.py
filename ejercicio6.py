#6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
#Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.


#n = int(input("Introduce un número entero: "))
#sumas = n * (n + 1) / 2
#print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(sumas))

valor= int(input("Ingrese un valor: "))
suma=0
print(" ")
print("numeros: ")
for i in range(1,valor+1):
    print(i)
    suma=suma+i
print(" ")
print("La suma de los numeros sucesivos es:", suma )


