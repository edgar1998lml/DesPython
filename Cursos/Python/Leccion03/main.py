condicion = 'Hola'

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion no reconocida')

#Actividad

numero = int(input('Proporciona un valor entre 1 y 3: '))

if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Numero proporcionado: {numero} - {numeroTexto}')

#Actividad

condicionAct = False

#if condicionAct:
#    print('Condicion verdadera')
#else:
#    print('Condicion falsa')

print('Condicion verdadera') if condicionAct else print('Condicion falsa')

#Calcular mes

mes = int(input('Proporciona mes del año (1-12)'))
estacion = None
if mes == 1:
    estacion = 'Enero'
elif mes == 2:
    estacion = 'Febrero'
elif mes == 3:
    estacion = 'Marzo'
elif mes == 4:
    estacion = 'Abril'
elif mes == 5:
    estacion = 'Mayo'
elif mes == 6:
    estacion = 'Junio'
elif mes == 7:
    estacion = 'Julio'
elif mes == 8:
    estacion = 'Agosto'
elif mes == 9:
    estacion = 'Septiembre'
elif mes == 10:
    estacion = 'Octubre'
elif mes == 11:
    estacion = 'Noviembre'
elif mes == 12:
    estacion = 'Diciembre'
else:
    print('Numero de mes invalido')
print(f'Su mes seleccionado es: {estacion}')

#Tarea calificaciones

calificacion = int(input('Escriba la calificacion: '))

if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion <= 9:
    print('B')
elif 7 <= calificacion <= 8:
    print('C')
elif 6 <= calificacion <= 7:
    print('D')
elif 0 <= calificacion <= 6:
    print('F')
else:
    print('Valor desconocido')
