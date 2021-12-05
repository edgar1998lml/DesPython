print("Hola Mundo")

# ¿Cuál el código del requerimiento solicitado?
# El objetivo de este ejercicio es imprimir un mensaje: Saludos desde Python

print("Saludos desde Python")

# Declarar Variables en python (Las variables no es necesario declarar el tipo

miVariable = "Hola desde Python Variable"
miVariableNum = 5
miVariableBol = True

print(miVariable)
print(miVariableNum)
print(miVariableBol)

# Variables con operaciones

x = 10
y = 2
z = x + y
print(z)
a = 11
p = z + a
print(p)

# Direccion de memoria
print(id(x))
print(id(y))
print(id(z))

# Tipos de datos
# Numerico
q = 10
print(q)
print(type(x))
# String
w = "Hola Mundo"
print(w)
print(type(w))
# Flotante
e = 10.5
print(e)
print(type(e))
# Boleano
r = True
print(r)
print(type(r))

# ManejoDeCadenas
miGrupoFavorito = "Bullet for my valentine"
print("Mi grupo Favorito es: " + miGrupoFavorito)
miSegundoGrupoFavoriorito = "Metallica"
print("Mis Bandas Favoritas son: " + miGrupoFavorito + " y " + miSegundoGrupoFavoriorito)

print("Mi Grupo Favorito es:", miGrupoFavorito)

# Concatenacion

numero1 = "1"
numero2 = "2"
print(numero1 + numero2)

# Convertir cadena a entero

int(numero1)
int(numero2)
print(int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print(numero1 + numero2)

# Boleanos
miVariableBol = False
print(miVariableBol)

miVariableBol = 3 > 2
print(miVariableBol)

if miVariableBol:
    print("El resultado fue Verdadero")
else:
    print("El resultado es Falso")

miVariableBol = 3 < 2
print(miVariableBol)

if miVariableBol:
    print("El resultado fue Verdadero")
else:
    print("El resultado es Falso")

# Funcion Input
print("Ingresa resultado: ")
resultado = input()
print("Tu resultado es:")
print(resultado)
print("Fin del input")

# Funcion mas corta y mas practica
resultado = input("Escribe un mensaje: ")
print(resultado)
print("Fin del programa")

# Mas funciones input (por defecto el input regresa valores cadena)
numeroUno = input("Escribe un el primer numero: ")
numeroDos = input("Escribe un segundo numero: ")
validar = numeroUno + numeroDos
print("El resultado es: " + validar)

# Como hacer que sea entero
numeroUno = int(input("Escribe un el primer numero: "))
numeroDos = int(input("Escribe un segundo numero: "))
validar = numeroUno + numeroDos
# si el print lo escribes con "+" chocara porque el + intenta concatenar el string con el numero
print("El resultado es: ", validar)

# Actividad preguntarle al usuario como estuvo su dia del 1 al 10 e imprimirlo
validarDia = int(input("Hola, Como estuvo tu dia? (1 al 10): "))
print("Mi dia estuvo de: ", validarDia)

# Actividad 2 imprimir "Titulo" fue escrito por "Autor"
tituloLibro = input("Proporciona el titulo: ")
autorLibro = input("Proporciona el autor: ")
print(tituloLibro + " Fue escrito por " + autorLibro)

# Operadores Aritmeticos
# Suma +, Resta -, Multiplicacion *, Division /, Division entero //, Exponente **, Residuo %
