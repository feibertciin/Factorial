# Factorial.py
# Implementación con bucle
def factorial_bucle(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# Implementación recursiva
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Usando el módulo math
import math
numero = 5
resultado = math.factorial(numero)
print(f"El factorial de {numero} es {resultado}")