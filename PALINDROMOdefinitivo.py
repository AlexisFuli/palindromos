#Programa de verificacion de palindromos
#crea un programa que verifique si una palabra ingresada por el usuario es un palindromo
#palabra que se lee y se escribe  de ambos sentidos

def Pertenece_palindromo(palabra):
    palabra = str(palabra).lower()
    return palabra == palabra[::-1] 
while True:
    palabra=input("Ingresa una palabra: ")
    if Pertenece_palindromo(palabra):
        print("La palabra ingresada es un palindromo.")
        break 
    else:
        print("La palabra ingresada no es un palindromo.")
