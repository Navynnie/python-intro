# FUNKCJA zip()
lis1 = [1, 2, 3]
lis2 = ['Latte', 'Espresso', 'Cappucino']
menu = list(zip(lis1, lis2))
print(menu)

# FUNKCJA ENUMERATE()
list = ['x', 'y', 'z']
for index, value in enumerate(list):
    print(index, value)

# FUNKCJA SORTED()
unsorted_list = [5, 31, 17, 44, 8, 26]
sorted_list = sorted(unsorted_list)
print('\nPosortowana lista:')
print(sorted_list)

#Moduł math
import math
#obliczmy pierwiastek kwadratowy z 16.
print(math.pow(3, 7))

#Moduł random - wyświtla losową liczbę w zakresie od 1-100 z jednym miejscem po przecinku
import random
def random_num():
    x = random.uniform(1, 100)
    return round(x, 1)

print (random_num())

#wyjątek ZeroDivisionError, try-except
try:
    wynik = 14 / 0
except ZeroDivisionError:
    print(""
          "Wykryto błąd!!! Dzielenie przez zero!")