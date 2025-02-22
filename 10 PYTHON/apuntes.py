# APUNTES DE LOS PDF PYTHON

# Hello World en python
print("Hello World")

print("-------------------------------------------------")
# tipos de dato en python

cadena_texto = "Soy una cadena de texto"
numero = 20
booleano = True
tupla = (1,2,3,"cuatro")
diccionario = {"pais":"España","Ciudad":"Madrid"}
array_arreglo = [1,2,"tres",False,diccionario]

print(type(cadena_texto))
print(type(numero))
print(type(booleano))
print(type(tupla))
print(type(array_arreglo))
print(type(diccionario))

print("-------------------------------------------------")

# OPERADORES EN PYTHON

def operadoresAritmeticos(numero1,numero2):
    # Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1*numero2
    division = numero1/numero2
    modulo = numero1%numero2
    potencia = numero1**numero2
    div_entera = numero1//numero2

    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)
    print(modulo)
    print(potencia)
    print(div_entera)

operadoresAritmeticos(24,14)

print("-------------------------------------------------")

def operadoresRelacionales(numero1,numero2):
    # Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false)
    mayor = numero1 >numero2
    menor = numero1 < numero2
    igual = numero1 == numero2
    mayor_igual = numero1 >= numero2
    menor_igual = numero1 <= numero2
    distinto = numero1 != numero2

    print(mayor)
    print(menor)
    print(igual)
    print(mayor_igual)
    print(menor_igual)
    print(distinto)

operadoresRelacionales(14,20)

print("-------------------------------------------------")
# Operadores de asignacion : Se utiliza un operador de asignación para asignar valores a una variable. Esto generalmente se combina con otros operadores

def operadoresAsignacion():
    a = 5  #asignacion 
    print("a",a)
    a += 5 # equivale a: variable + 5 
    print("a",a)
    a -= 5 # equivale a: variable - 5
    print("a",a)
    a *= 5 # equivale a: variable * 5
    print("a",a)
    a /= 5 # equivale a: variable / 5
    print("a",a)
    a %= 5 # equivale a: variable % 5
    print("a",a)
    a **= 5 # equivale a: variable **5
    print("a",a)
    a //= 5 # equivale a: variable // 5
    print("a",a)
operadoresAsignacion()

print("-------------------------------------------------")

def operadoreesLogicos(x,z):
    y = x and z
    o = x or z
    no = not x
    print(y)
    print(o)
    print(no)

operadoreesLogicos(7,5)

print("-------------------------------------------------")


"""
Condicionales en Python:
    - IF   

    if condicion:
        argumentos
    elif:
        argumentos
    else:
        argumentos  
"""    

a = 10
b = 10

if a > b:
    print("A es menor que B")
elif a == b:
    print("A y B son iguales")
else:
    print("A es mayor que B")   

print("-------------------------")

# Condicional While:

numero_while = 1

while numero_while <=10:
    print(numero_while)
    numero_while +=1

print("-------------------------")

# Break y continue

for letra in "Python":
    if letra == "h":
        break
    print ("Letra actual : " + letra)

print("-------------------------")

for letra in "Python":
    if letra == "h":
        continue
    print ("Letra actual : " + letra)

print("-------------------------")

def saludo(nombre):
    print(f"Hola {nombre}")
    
saludo("Timmy")
saludo("Kristy")
saludo("Jackie")
saludo("Liv")

print('--------------------------------')

# Clases

class MiClase:
    atributo1 = "valor1"
    atributo2 = "valor2"
    def __init__(self, argumento1):
        self.argumento1 = argumento1
    def funcion1(self):
        print("Esta es la función 1")

mi_clase = MiClase("Hola")
mi_clase.atributo1
mi_clase.atributo2
mi_clase.argumento1
mi_clase.funcion1()

print('--------------------------------------')

# try y except

try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
except ValueError:
    # Código a ejecutar si se produce una excepción del tipo ValueError
    print("Valor incorrecto.")
except:
    # Código a ejecutar si se produce cualquier tipo de excepción
    print("Se produjo una excepción.")




