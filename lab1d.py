#!/usr/bin/env python3

x = 10
y = 2
z = 5

result1 = x + y * z
result2 = (x + y) * z
result3 = x + y * z - x ** 2
result4 = 15 / 3 * 4
result5 = 100 / ((y + y) * z)

print(f'{x} + {y} * {z} = {result1}')
print(f'({x} + {y}) * {z} = {result2}')
print(f'{x} + {y} * {z} - {x} ** 2 = {result3}')
print(f'15 / 3 * 4 = {result4}')
print(f'100 / (({y} + {y}) * {z}) = {result5}')