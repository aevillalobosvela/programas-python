""" INF 3811 A - Ingenieria de Software II

    Univ. Villalobos Vela Alvaro Edwin

    Realizar funciones y clases 5 las que deseen  """

# Ejercicio 1
# Clase calculadora con funciones para dos valores ingresados

""" class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "No se puede dividir por cero"


valor1 = int(input("Primer valor: "))
valor2 = int(input("Segundo valor: "))
calc = Calculadora()
print("suma:", calc.suma(valor1, valor2))
print("resta:", calc.resta(valor1, valor2))
print("multiplicacion:", calc.multiplicacion(valor1, valor2))
print("division:", calc.division(valor1, valor2))
 """

# Ejercicio 2
# Clase estudiante para adjuntar calificaciones de estudiantes


""" class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def calificar(self, calificacion):
        self.calificaciones.append(calificacion)


estudiante = Estudiante("Maria")
estudiante.calificar(90)
estudiante.calificar(85)
estudiante.calificar(60)
print(estudiante.calificaciones) """


# Ejercicio 3
# Contador de palabras mediante funcion

""" def contador_de_palabras(texto):
    palabras = texto.split()
    print(palabras)
    return len(palabras)


texto = "La Universidad Técnica de Oruro, es una Institución Pública y Autónoma consolidada como líder en la educación"
cant_palabras = contador_de_palabras(texto)
print(f"El texto tiene {cant_palabras} palabras.") """

# Ejercicio 4
# Factorial de un numero mediante funcion recursiva


""" def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("valor: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}") """

# Ejercicio 5
# Convertidos de temperatura celsius a fahrenheit


""" def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = int(input("Celsius: "))
fahrenheit = convertir_temperatura(celsius)
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.") """
