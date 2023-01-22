#8.Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable

input("Ingresa tu usuario: ")
contraseña = "PYTHON"
password = input("Introduce la contraseña: ")
if contraseña == password.lower():
    print("La contaseña es correcta")
else:
    print("La contraseña es incorrecta")