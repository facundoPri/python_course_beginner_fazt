
# Loop For

# Primer ejemplo
foods = ['apples', 'bread', 'cheese', 'milk', 'banana', 'grapes']

for food in foods:
  if food == 'cheese':
    print(f'You have to buy {food}')
    continue # salteamos lo que se ejecuta abajo por esta iteración y pasamos para el siguiente
  if food == 'milk':
    break # terminamos el loop aca
  print(food)

# Segundo ejemplo
for number in range(1, 10):
  print(number)

# Tercer ejemplo
for letter in 'Hello':
  print(letter)

# Loop While

# Primer ejemplo
count = 4

while count <= 10:
  print(count)
  count = count + 1 # importante, que si no se pone esto tenemos un bucle infinito