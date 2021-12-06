condicion = 'Hola'

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion false')
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