# Son como listas pero no tiene indice

colors = {'Red', 'Green', 'Blue'}

print(colors)
print(type(colors))
print(dir(colors))

print('Red' in colors)

# Al no tener indice se nos adiciona este valor si un orden en especifico
colors.add('Violet')
print(colors)

colors.remove('Red')
print(colors)

# Nos devuelve el set limpio
colors.clear()
# del colors # podemos eliminarlo por completo
print(colors)