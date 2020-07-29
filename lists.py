demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

# constructor
number_list = list((1,2,3,4))
print(type(number_list))
print(number_list)

# rango
r = list(range(1,10))
print(r)

# Metodos de una lista
print(dir(colors))

print(len(r))
print(colors[2])

print('green' in colors)
print('violet' in colors)

print(colors)
colors[1] = 'yellow'

colors.append('violet') # en este caso solo podemos pasarle un parametro y este sera agregado asi como esta
colors.extend(['violet', 'yellow']) # con el extend va a agarrar todos los valores adentro de una lista y extenderlos en esta lista 
colors.extend(['pink', 'black']) 

colors.insert(1, 'violet') #le decimos donde queremos que se ponga, usarlo con el len creamos el metodo append

print(colors)

colors.pop() # remover a partir de un indice, por defecto es le ultimo

colors.remove('violet') # remover a partir de un valor

# color.clear() # vaciar lista

colors.sort()
colors.sort(reverse=True)

print(colors.index('red')) #index de un valor

print(colors.count('yellow')) # cuantas veces aparecen 

print(colors)

