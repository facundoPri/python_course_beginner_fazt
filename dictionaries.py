# Es un array
# Son un conjunto de claves y valores

product = {
  'name': 'book',
  'quantity': 3,
  'price': 4.99
}

person = {
  'first_name': 'Facundo',
  'last_name': 'Prieto'
}

print(product)
print(type(product))
print(dir(product))

print(person.keys())
print(person.items())

# del person # deleteamos el diccionario
person.clear() # Lo limpiamos
print(person)

# Diccionarios adentro de una lista
products = [
  {"name": 'book', "price": 10.99},
  {'name':"laptop", "price": 1000}
]

print(products)