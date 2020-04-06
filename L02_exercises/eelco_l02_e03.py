import math

def list_square_even_power_odd(list_range):
    print([(math.sqrt(list_range.index(i))if (i % 2) == 0 else i ** 2) for i in range(list_range)])

list_square_even_power_odd(100)