# A python program for generating the formula of a given sequence.
# Doesn't work for simple sequences!
# Requires SymPy

import sympy
from sympy.parsing.sympy_parser import parse_expr
import itertools as it

sequence = input('Enter the sequence: ')
if not sequence:
    sequence = '1, 3, 5, 7, 217341'
sequence = sequence.replace(' ','').split(',')

COUNT = 5

allElements = []

combinations = [i for i in it.combinations([l+1 for l in range(COUNT)], COUNT-1)]
for combination, leftOut in zip(combinations, reversed([l+1 for l in range(COUNT)])):
    numerator = sympy.expand(parse_expr('*'.join(['(n-{})'.format(element) for element in combination]), evaluate=False))
    denominator = parse_expr('*'.join(['({}-{})'.format(leftOut,element) for element in combination]), evaluate=False)
    allElements.append(numerator / denominator)

secondaryElements = []
for sequenceItem, element in zip(reversed(sequence), allElements):
    secondaryElements.append(parse_expr(sequenceItem) * element)
    
final = sympy.expand(sum(secondaryElements))

print('An = ' + str(final))
print('A_n = ' + sympy.latex(final))
