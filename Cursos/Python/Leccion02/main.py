operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('Resultado suma: ', suma)
#interpolacion
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

#incremento con asignacion
mivariableDeAsignacion += 2
print(mivariableDeAsignacion)
#ahora con los demas signos aritmeticos
mivariableDeAsignacion -= 3
print(mivariableDeAsignacion)
mivariableDeAsignacion *= 3
print(mivariableDeAsignacion)
mivariableDeAsignacion /= 2
print(mivariableDeAsignacion)

#Operadores de comparacion

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