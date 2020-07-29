# Prestar atencion a los espacios ya que en python si son importantes
# Despues de los dos puntos solo se va a tomar en cuenta lo que este abajo con un espacio o mejor un tab

# Primer ejemplo
x = 10

if x < 20 :
  print('x is less than 20')
else:
  print('x is greater than 20')


# Segundo ejemplo
color = 'blue'

if color == 'red':
  print('the color is red')
elif color == 'blue':
  print('the color is blue')
else:
  print('the color is not red or blue')

# Tercer ejemplo
name = 'Facundo'
lastname = 'Prieto'

if name == 'Facundo':
  if lastname == 'Prieto':
    print('You are Facundo Prieto')
  else:
    print('Your name is Facundo but I do not know your lastname')
else:
  print('You are not Facundo')

# Cuarto ejemplo (operador lógico and)
if x > 2 and x <= 10:
  print('x is greater than two and less or equal than ten ')
if x > 2 or x <= 20:
  print('x is greater than two or less or equal to twenty')
if (not(x == y )):
  print('x is different than y')