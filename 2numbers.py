number1 = 11
number2 = 25

small_number1 = 5
small_number2 = 2

print(number1 + number2)

print(number2 / number1)

# the floor division discards the fractional part
print(number2 // number1)

# the % operator returns the remainder of the division
print(number2 % number1)

# small_number1 to the power of small_number2
print(small_number1 ** small_number2)

from fractions import Fraction
from decimal import Decimal
print( Fraction(16, -10) )

print( Fraction(Decimal('1.1') ))