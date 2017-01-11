# A python program for generating the formula of a given sequence.
# Only works for polynomial formulas
# Dependencies: SymPy

import sympy
from sympy.parsing.sympy_parser import parse_expr
import itertools as it

class Sequence(object):
    '''A sequence object'''

    def __init__(self, sequence='1, 3, 5, 7, 217341'):
        self._seq = sequence.replace(' ','').split(',')
        self._seqLen = len(self._seq)

    def generateFormula(self):
        '''Generates a formula for the sequence, returns a sympy object.\nOnly works for polynomial formulas.'''
        tmp = []
        combinations = [i for i in it.combinations([l+1 for l in range(self._seqLen)], self._seqLen-1)]
        for combination, leftOut in zip(combinations, reversed([l+1 for l in range(self._seqLen)])):
            numerator = sympy.expand(parse_expr('*'.join(['(n-{})'.format(element) for element in combination])))
            denominator = parse_expr('*'.join(['({}-{})'.format(leftOut,element) for element in combination]))
            tmp.append(numerator / denominator)
        fractions = []
        for sequenceItem, element in zip(reversed(self._seq), tmp):
            fractions.append(parse_expr(sequenceItem) * element)
        self.formula = sympy.expand(sum(fractions))
        return self.formula

seq = Sequence(input('Input the sequence:'))
print(seq.generateFormula())
