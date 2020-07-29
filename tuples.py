# Son mas rapidas que las listas y al ser inmutables son mas seguras ya que no se pueden rescribir
x = (1, 2, 3)

print(type(x))

# constructor
y = tuple((1,2,3))

print(y)

print(dir(y))

# una tupla de un solo elemento no es considerado una tupla por mas de los parentecis
# Para transformarlo en una tupla se necesita poner una coma
z = (1)
t = (1,) # la coma es necesaria para definir una tupla

print(z)
print(t)
print(type(z))
print(type(t))

print(x[1])
# x[4] = 10 # esto ma da un error ya que no se le puede reasignar valores a una tupla


# De esta forma deleteamos la tupla
# del x
# print(x)

# Usos te tuplas
# En un diccionario, se puede usar como una clave
# En este ejemplo usamos una tupla como clave, mostrando la latitud y la longitud de un lugar y como valor el nombre
location = {
  (35.12312, 39.0000): "Tokyo"
}