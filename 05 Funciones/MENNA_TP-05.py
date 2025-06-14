# MENNA - TP 05 - Funciones en Python

# 1. Crear una función que imprima "Hola Mundo!" y llamarla
def imprimir_hola_mundo():
    print("¡Hola Mundo!")

imprimir_hola_mundo()


# 2. Función que reciba un nombre y devuelva un saludo
def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))


# 3. Función que reciba datos personales y los imprima
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís?: ")
informacion_personal(nombre, apellido, edad, residencia)


# 4. Funciones para área y perímetro del círculo
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


# 5. Función para convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")


# 6. Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)


# 7. Función para operaciones básicas con dos números
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# 8. Función para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura)}")


# 9. Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresá la temperatura en grados Celsius: "))
print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")


# 10. Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
