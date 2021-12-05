operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('Resultado suma: ', suma)
# interpolacion
print(f'Resultado suma: {suma}')

resta = operandoA - operandoB
print(f'Resultado de la Resta: {resta}')

multiplicacion = operandoA * operandoB
print(f'Resultado de la multiplicacion: {multiplicacion}')

division = operandoA / operandoB
print(f'Resultado de la division: {division}')

division = operandoA // operandoB
print(f'Resultado de la division tipo entero: {division}')

modulo = operandoA % operandoB
print(f'Resultado residuo division modulo: {modulo}')

exponente = operandoA ** operandoB
print(f'Resultado expoente: {exponente}')

# Actividad Tarea Ejercicio para calcular area y perimetro de un rectangulo

print("Hola, esta es una prueba de aplicacion")
varAlto = int(input("Hola, por favor ingresa el alto del rectangulo: "))
varAncho = int(input("Ahora ingresa el ancho: "))
calArea = varAlto * varAncho
calPerimetro = (varAlto + varAncho) * 2
print(f'el area del rectangulo es {calArea}')
print(f'el perimetro del rectangulo es {calPerimetro}')

# Operadores de asignacion
miVariableDeAsignacion = 10
print(miVariableDeAsignacion)
mivariableDeAsignacion = miVariableDeAsignacion + 1
print(mivariableDeAsignacion)

# incremento con asignacion
mivariableDeAsignacion += 2
print(mivariableDeAsignacion)
# ahora con los demas signos aritmeticos
mivariableDeAsignacion -= 3
print(mivariableDeAsignacion)
mivariableDeAsignacion *= 3
print(mivariableDeAsignacion)
mivariableDeAsignacion /= 2
print(mivariableDeAsignacion)

# Operadores de comparacion

a = 4
b = 2
resul = a == b
print(resul)
resul = a != b
print(resul)

resul = a < b
print(resul)
resul = a > b
print(resul)
resul = a >= b
print(resul)
resul = a <= b
print(resul)

# Numeros pares o no

a = int(input('Escribe un valor numerico: '))
if a % 2 == 0:
    print(f'El vador de a {a} es numero par')
else:
    print(f'El valor de a {a} es un numero impar')

# Ejercicio Edad
edadAdulto = 18
edad = int(input('Escribe tu edad:'))
if edad >= edadAdulto:
    print(f'Tu edad es {edad} eres mayor de edad')
else:
    print(f'Tu edad es {edad} eres menor de edad')

#Operadores logicos "and,or,not)

atrue = True
btrue = False

resultadotrue = atrue and btrue
print(resultadotrue)

resultadotrue = atrue or btrue
print(resultadotrue)

resultadotrue = not atrue
print(resultadotrue)

resultadotrue = not btrue
print(resultadotrue)

#Actividad Rango
valorRango = int(input('Escribe un valor: '))
valorMinimo = 0
valorMaximo = 10
dentroRango = (valorRango >= valorMinimo) and (valorRango <= valorMaximo)

if dentroRango:
    print(f'Tu valor {valorRango} esta dentro del rango')
else:
    print(f'Tu valor {valorRango} esta fuera del rango')