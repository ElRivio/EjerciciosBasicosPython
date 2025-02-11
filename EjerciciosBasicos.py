import math
""" importa libreria interna de python para el uso de pi """

# Ejercicio 1: Imprime en la consola el mensaje "¡Hola, mundo!"
print(f'Imprime en la consola el mensaje "¡Hola, mundo!"'.center(100, "-"))
"""
Muestra en consola las instrucciones del ejercicio y, con .center, centra el texto
añadiendo guiones a los lados. Esto se aplica en todos los ejercicios.
"""
print("¡Hola, mundo!")
"""Imprime el mensaje escrito en la cadena de texto."""


# Ejercicio 2: Pide al usuario que ingrese su nombre y luego imprímelo junto con un saludo
print(f'Pide al usuario que ingrese su nombre y luego imprímelo junto con un saludo'.center(100, "-"))
nombre = input('¿Cuál es tu nombre? ')
"""
Pide al usuario ingresar su nombre y lo almacena en la variable "nombre".
"""

print(f'¡Hola! {nombre}')
"""
f-string (f'') sirve para usar el valor de las variables dentro de llaves {} en una línea.
En este caso, se mostrará el valor de "nombre".
"""


# Ejercicio 3: Pide al usuario dos números y muestra la suma
print(f'Pide al usuario dos números y muestra la suma.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer número: '))
num2 = int(input(f'Ingresa el segundo número: '))
print(f'El resultado de tu suma es: {num1 + num2}')
"""
Solicita al usuario dos números, los suma y muestra el resultado.
"""


# Ejercicio 4: Pide al usuario dos números y muestra la resta
print(f'Pide al usuario dos números y muestra la resta.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer número: '))
num2 = int(input(f'Ingresa el segundo número: '))
print(f'El resultado de tu resta es: {num1 - num2}')
"""
Solicita al usuario dos números, los resta y muestra el resultado.
"""


# Ejercicio 5: Pide al usuario dos números y muestra el producto
print(f'Pide al usuario dos números y muestra el producto.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer número: '))
num2 = int(input(f'Ingresa el segundo número: '))
print(f'El resultado de tu producto es: {num1 * num2}')
"""
Solicita al usuario dos números, los multiplica y muestra el resultado.
"""


# Ejercicio 6: Pide al usuario dos números y muestra el cociente
print(f'Pide al usuario dos números y muestra el cociente.'.center(100, "-"))
num1 = float(input(f'Ingresa el primer número: '))
num2 = float(input(f'Ingresa el segundo número: '))
print(f'El cociente es: {num1 / num2}')
"""
Solicita al usuario dos números, los divide y muestra el resultado.
"""


# Ejercicio 7: Pide al usuario dos números (base y exponente) y muestra el resultado de la potencia
print(f'Pide al usuario dos números (base y exponente) y muestra el resultado de la potencia.'.center(100, "-"))
num1 = int(input(f'Ingresa la base: '))
num2 = int(input(f'Ingresa el exponente: '))
print(f'El resultado de la potencia es: {num1 ** num2}')
"""
Solicita al usuario una base y un exponente, calcula la potencia y muestra el resultado.
"""


# Ejercicio 8: Pide al usuario la base y la altura de un triángulo y calcula su área
print(f'Pide al usuario la base y la altura de un triángulo y calcula su área.'.center(100, "-"))
base = int(input(f'Ingresa la base del triángulo: '))
altura = int(input(f'Ingresa la altura del triángulo: '))
print(f'El área del triángulo es: {base * altura / 2}')
"""
Solicita al usuario la base y la altura de un triángulo, calcula su área y muestra el resultado.
"""


# Ejercicio 9: Pide al usuario el radio de un círculo y calcula su área
print(f'Pide al usuario el radio de un círculo y calcula su área.'.center(100, "-"))
radio = int(input(f'Ingresa el radio del círculo: '))
cons_pi = math.pi
print(f'El área del círculo es: {cons_pi * radio ** 2:.2f}')
"""
Solicita al usuario el radio de un círculo, calcula su área usando π (pi) y muestra el resultado.
"""


# Ejercicio 10: Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit
print(f'Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit.'.center(100, "-"))
celsius = float(input(f'Ingresa la temperatura en grados Celsius: '))
fahrenheit = (celsius * 9 / 5) + 32
print(f'La temperatura en grados Fahrenheit es: {fahrenheit} grados Fahrenheit')
"""
Solicita al usuario una temperatura en grados Celsius, la convierte a Fahrenheit y muestra el resultado.
"""


# Ejercicio 11: Pide al usuario tres números y muestra su promedio
print(f'Pide al usuario tres números y muestra su promedio.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer número: '))
num2 = int(input(f'Ingresa el segundo número: '))
num3 = int(input(f'Ingresa el tercer número: '))
resultado = (num1 + num2 + num3) / 3
print(f'El promedio de los 3 números dados es: {resultado:.2f}')
"""
Solicita al usuario tres números, calcula su promedio y muestra el resultado.
"""


# Ejercicio 12: Pide al usuario una longitud en metros y conviértela a centímetros
print(f'Pide al usuario una longitud en metros y conviértela a centímetros.'.center(100, "-"))
metros = int(input(f'Ingresa la longitud en metros: '))
print(f'La longitud en centímetros es: {metros * 100} centímetros')
"""
Solicita al usuario una longitud en metros, la convierte a centímetros y muestra el resultado.
"""


# Ejercicio 13: Pide al usuario una cantidad de segundos y muestra su equivalente en minutos y segundos
print(f'Pide al usuario una cantidad de segundos y muestra su equivalente en minutos y segundos.'.center(100, "-"))
segundos = int(input(f'Ingresa los segundos a mostrar en minutos y segundos: '))
minutos = segundos // 60
segundos_restantes = segundos % 60
print(f'La conversión de segundos es: {minutos} minutos y {segundos_restantes:.2f} segundos.')
"""
Solicita al usuario una cantidad de segundos, la convierte a minutos y segundos, y muestra el resultado.
"""


# Ejercicio 14: Pide al usuario un número y un porcentaje, y muestra el resultado del porcentaje del número
print(f'Pide al usuario un número y un porcentaje, y muestra el resultado del porcentaje del número.'.center(100, "-"))
num = float(input(f'Ingresa el número del que desees calcular el porcentaje: '))
porcentaje = float(input(f'Ingresa el porcentaje que deseas calcular: '))
print(f'El {porcentaje}% de {num} es: {porcentaje / 100 * num} ')
"""
Solicita al usuario un número y un porcentaje, calcula el porcentaje del número y muestra el resultado.
"""


# Ejercicio 15: Pide al usuario un precio y calcula el precio con IVA (16%)
print(f'Pide al usuario un precio y calcula el precio con IVA (16%).'.center(100, "-"))
precio = float(input(f'Ingresa el precio del que quieras obtener el total con IVA(16%): '))
iva = 16
precio_total = precio * (1 + (iva / 100))
print(f'El precio total con IVA(16%) es: {precio_total:.2f}')
"""
Solicita al usuario un precio, calcula el precio con IVA (16%) y muestra el resultado.
"""


# Ejercicio 16: Pide al usuario una longitud en pulgadas y conviértela a centímetros (1 pulgada = 2.54 cm)
print(f'Pide al usuario una longitud en pulgadas y conviértela a centímetros.'.center(100, "-"))
pulgadas = float(input(f'Ingresa tu longitud en pulgadas: '))
print(f'La longitud es: {pulgadas * 2.54} centímetros')
"""
Solicita al usuario una longitud en pulgadas, la convierte a centímetros y muestra el resultado.
"""


# Ejercicio 17: Pide al usuario una distancia en kilómetros y conviértela a millas (1 km = 0.621371 millas)
print(f'Pide al usuario una distancia en kilómetros y conviértela a millas.'.center(100, "-"))
kilometros = float(input(f'Ingresa la distancia en kilómetros: '))
print(f'La distancia es: {kilometros * 0.621371:.2f} millas.')
"""
Solicita al usuario una distancia en kilómetros, la convierte a millas y muestra el resultado.
"""


# Ejercicio 18: Pide al usuario una cantidad en litros y conviértela a galones (1 litro = 0.264172 galones)
print(f'Pide al usuario una cantidad en litros y conviértela a galones.'.center(100, "-"))
litros = float(input(f'Ingresa los litros: '))
print(f'El resultado son: {litros * 0.264172:.2f} galones.')
"""
Solicita al usuario una cantidad en litros, la convierte a galones y muestra el resultado.
"""

"""---------------------------------------------FIN DE TAREA----------------------------------------------------"""