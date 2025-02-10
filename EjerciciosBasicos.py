import math

#Imprime en la consola el mensaje "¡Hola, mundo!

print(f'Imprime en la consola el mensaje "¡Hola, mundo!'.center(100, "-"))
print("¡Hola, mundo!")

#Pide al usuario que ingrese su nombre y luego imprímelo junto con un saludo"

print(f'Pide al usuario que ingrese su nombre y luego imprímelo junto con un saludo'.center(100,"-"))
nombre = input('¿Cual es tu nombre? ')
print(f'¡Hola! {nombre}')

#Pide al usuario dos números y muestra la suma.

print(f'Pide al usuario dos números y muestra la suma.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer numero: '))
num2 = int(input(f'Ingresa el segundo numero: '))
print(f'El resultado de tu suma es: {num1 + num2}')

#Pide al usuario dos números y muestra la resta.

print(f'Pide al usuario dos números y muestra la resta.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer numero: '))
num2 = int(input(f'Ingresa el segundo numero: '))
print(f'El resultado de tu resta es: {num1 - num2}')

#Pide al usuario dos números y muestra el producto.

print(f'Pide al usuario dos números y muestra el producto.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer numero: '))
num2 = int(input(f'Ingresa el segundo numero: '))
print(f'El resultado de tu producto es: {num1 * num2}')

#Pide al usuario dos números y muestra el cociente.

print(f'Pide al usuario dos números y muestra el cociente.'.center(100, "-"))
num1 = float(input(f'Ingresa el primer numero: '))
num2 = float(input(f'Ingresa el segundo numero: '))
print(f'El cociente es: {num1 / num2}')

# Pide al usuario dos números (base y exponente) y muestra el resultado de la potencia.

print(f'Pide al usuario dos números (base y exponente) y muestra el resultado de la potencia.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer numero: '))
num2 = int(input(f'Ingresa el segundo numero: '))
print(f'El resultado de tu suma es: {num1 ** num2}')

# Pide al usuario la base y la altura de un triángulo y calcula su área.

print(f'Pide al usuario la base y la altura de un triángulo y calcula su área.'.center(100,"-"))
base= int(input(f'Ingresa la base del triangulo: '))
altura = int(input(f'Ingresa la altura del triangulo: '))
print(f'El área del triangulo es: {num1 * num2 / 2}')


# Pide al usuario el radio de un círculo y calcula su área.

print(f'Pide al usuario el radio de un círculo y calcula su área.'.center(100, "-"))
radio= int(input(f'Ingresa el radio del circulo: '))
cons_pi = math.pi
print(f'El área del circulo es: {cons_pi * radio **2:.2f}')

# Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit.

print(f'Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit.'.center(100, "-"))
celsius = float(input(f'Ingresa la temperatura en grados celsius: '))
fahrenheit = (celsius * 9 / 5) + 32
print(f'La temperatura en grados fahrenheit es: {fahrenheit} grados fahrenheit')

# Pide al usuario tres números y muestra su promedio.

print(f'Pide al usuario tres números y muestra su promedio.'.center(100, "-"))
num1 = int(input(f'Ingresa el primer numero: '))
num2 = int(input(f'Ingresa el segundo numero: '))
num3 = int(input(f'Ingresa el tercer numero: '))
resultado = (num1 + num2 + num3) / 3
print(f'El promedio de los 3 numeros dados es: {resultado:.2f}')

# Pide al usuario una longitud en metros y conviértela a centímetros.

print(f'Pide al usuario una longitud en metros y conviértela a centímetros.'.center(100, "-"))
metros = int(input(f'Ingresa la longitud en metros: '))
print(f'La longitud en centrimetros es: {metros * 100} centimetros')

# Pide al usuario una cantidad de segundos y muestra su equivalente en minutos y segundos.

print(f'PDiide al usuario una cantidad de segundos y muestra su equivalente en minutos y segundos.'.center(100, "-"))
segundos = int(input(f'Ingresa los segundos a mostrar en minutos y segundos: '))
minutos = segundos // 60
segundos_restantes = segundos % 60
print(f'La conversion de segundos es: {minutos} minutos y {segundos_restantes:.2f} segundos.')

# Pide al usuario un número y un porcentaje, y muestra el resultado del porcentaje del número.

print(f'Pide al usuario un número y un porcentaje, y muestra el resultado del porcentaje del número.'.center(100, "-"))
num = float(input(f'Ingresa el numero del que desees calcular el porcentaje: '))
porcentaje = float(input(f'Ingresa el porcentaje que deseas calcular: '))
print(f'El {porcentaje}% de {num} es: {porcentaje / 100 * num} ')

# Pide al usuario un precio y calcula el precio con IVA (16%).

print(f'Pide al usuario un precio y calcula el precio con IVA (16%).'.center(100, "-"))
precio = float(input(f'Ingresa el precio del que quieras obtener el total con IVA(16%): '))
iva = 16
precio_total = precio * (1 + (iva / 100))
print(f'El precio total con IVA(16%) es: {precio_total:.2f}')

# Pide al usuario una longitud en pulgadas y conviértela a centímetros (1 pulgada = 2.54 cm).

print(f'Pide al usuario una longitud en pulgadas y conviértela a centímetros.'.center(100, "-"))
pulgadas = float(input(f'Ingresa tu longitud en pulgadas: '))
print(f'La longitud es: {pulgadas * 2.54} centimetros')

# Pide al usuario una distancia en kilómetros y conviértela a millas (1 km = 0.621371 millas).

print(f'Pide al usuario una distancia en kilómetros y conviértela a millas.'.center(100, "-"))
kilometros = float(input(f'Ingresa la distancia en kilometros: '))
print(f'La distancia es: {kilometros * 0.621371:.2f} millas.')

# Pide al usuario una cantidad en litros y conviértela a galones (1 litro = 0.264172 galones).

print(f'Pide al usuario una cantidad en litros y conviértela a galones.'.center(100, "-"))
litros = float(input(f'Ingresa los litros: '))
print(f'El resultado son: {litros * 0.264172:.2f} galones.')

"""---------------------------------------------FIN DE TAREA----------------------------------------------------"""