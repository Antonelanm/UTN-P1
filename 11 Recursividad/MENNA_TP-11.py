# Ejercicio 1: Factorial recursivo y mostrar todos desde 1 hasta n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales():
    numero = int(input("Ingresá un número entero positivo: "))
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

# Ejercicio 2: Serie de Fibonacci recursiva
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    n = int(input("Ingresá hasta qué posición desea mostrar la serie de Fibonacci: "))
    for i in range(n + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def probar_potencia():
    base = int(input("Ingresá la base: "))
    exponente = int(input("Ingresá el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4: Conversión decimal a binario

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario():
    numero = int(input("Ingresá un número decmal positivo: "))
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario if binario else '0'}")

# Ejercicio 5: Palíndromo recursivo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    palabra = input("Ingresá una palabra sin espacios ni tildes: ").lower()
    print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")

# Ejercicio 6: Suma de dígitos recursiva

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    numero = int(input("Ingresá un número entero positivo: "))
    print(f"La suma de tus dígitos es: {suma_digitos(numero)}")

# Ejercicio 7: Contar bloques de una pirámide

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    nivel = int(input("Ingresá el número de bloques en el nivel más bajo: "))
    print(f"Se necesitan {contar_bloques(nivel)} bloques en total.")

# Ejercicio 8: Contar dígitos

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def probar_contar_digito():
    numero = int(input("Ingresa un número entero positivo: "))
    digito = int(input("Ingresá el dígito que deseás contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")


