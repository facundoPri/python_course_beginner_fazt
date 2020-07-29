# Primer Ejemplo

# definimos un funcion
# una funcion puede recibir parametros
# Los parametros pueden tener valores por defecto, de este modo podemos evitar errores en el caso de que no se pase un parametro
def hello(name = "Persone"):
  print('Hello '+ name)

# la ejecutamos
hello('Facundo')
hello('Beltran')

# ejemplos de funciones pre construidas
# print()
# dir()
# type()

# Segundo Ejemplo
def add(numOne, numTwo):
  return numOne + numTwo

print(add(10, 30))
print(add(600, 30))

# Tercer Ejemplo (lambda)
# arrow function en python?

add = lambda numOne, numTwo: numOne + numTwo

print(add(30, 50))