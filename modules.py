# own modules
# thirds party modules (pip modules)
# python modules

# python modules example
# Buscando python modules en google aparece una enorme lista con todos ellos

import datetime # importamos la biblioteca entera
from datetime import timedelta, date # importamos apenas el modulo que queremos

print(datetime.date.today())
print(date.today())
print(timedelta(minutes=100))

# Own Modules example

import fmath
from fmath import add, subtract

fmath.add(1,3)
subtract(1,2)

# thirds party modules
# buscar por Pypi en google
# En Archlinux yay -S python-pip
# Instalemos colorama
# pip install colorama

from colorama import Fore, Style #, init
# init(convert = True) # para windows
print(Fore.RED + 'Hello World')