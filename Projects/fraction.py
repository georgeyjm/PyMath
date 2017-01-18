import math

class Fraction(object):
    '''A fraction object'''

    def __init__(self, numerator, denominator):
        types = [type(numerator), type(denominator)]
        if not (types in ([float,float],[int,int]) or (float in types and int in types)):
            raise ValueError('invalid numeric value')
        self._numer = numerator
        self._denom = denominator

    def simplify(self, division=True):
        '''Returns the simplified fraction.
        If division is true, it will return the value of the fraction if it is an integer.'''
        if not isinstance(self._numer, int) or not isinstance(self._denom, int):
            floatDigit = max([str(self._numer)[::-1].find('.'), str(self._denom)[::-1].find('.')])
            self._numer = int(self._numer*10**floatDigit)
            self._denom = int(self._denom*10**floatDigit)
        if division and (self._numer / self._denom).is_integer():
            return int(self._numer / self._denom)
        gcd = math.gcd(self._numer, self._denom)
        return self._numer//gcd, self._denom//gcd

#Example Usage:
frac = Fraction(3,12)
print(frac.simplify())
