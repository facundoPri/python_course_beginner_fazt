myStr = "Hello World"

# con dir podemos ver todas las propiedades que tiene una string
print(dir(myStr))

# Algunos Metodos
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Bye'))
print(myStr.replace('Hello', 'Bye').upper())
print(myStr.count('l'))
print(myStr.count(' '))
print(myStr.startswith('He'))
print(myStr.endswith('world'))
print(myStr.split()) # Por defecto separa por espacio
print(myStr.split("o"))
print(myStr.find('o'))
print(len(myStr))
print(myStr.index('e'))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[0])

# Concatenacion en strings
name = 'Facundo'
print('My name is ' + name)
print(f'My name is {name}')
print('My name is {0}'.format(name))