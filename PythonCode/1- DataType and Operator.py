"""
Data and Operator
"""
################################################
################################################
# DataType
 
s = 'asma'
print(s)
print(repr(s))
print(s, type(s))    # asma   <class 'str'>

#---------------

i = 2
print(i, type(i))    # 2      <class 'int'>

#---------------

f = 1.2
print(f, type(f))    # 1.2    <class 'float'>

f = 2.
print(f, type(f))    # 2.0    <class 'float'>

#---------------

c = 2+3j
print(c, type(c))    # (2+3j) <class 'complex'>
print(c.real)        # 2.0 
print(c.imag)        # 3.0

#---------------

b = 5>8
print(b, type(b))         # False  <class 'bool'>

b = True
print(b, type(b))         # True   <class 'bool'>

x, y = 12, 15
z = x==y
print(z, type(z))         # False <class 'bool'>

print(0 or 30<5)          # False
print(5>7 or 3<5)         # True
print(5>7 or True)        # True
print(False or True)      # True
print(True or True)       # True
print(False or False)     # False

print(4>2 and 3<5)        # True
print(4>2 and True)       # True 
print(True and True)      # True  
print(False and True)     # False
print(False and False)    # False

#---------------

n = None
print(n, type(n))         # None <class 'NoneType'>

################################################
# Change Type

"str"

print(str(7))           # 7
print(repr(str(7)))     # '7'
print(str(7)*2)         # 77
print(str(7)+2)         # TypeError: can only concatenate str (not "int") to str
 
print(str(3.5))         # 3.5

print(str(2+5j))        # (2+5j)

print(str(True))        # True
print(repr(str(True)))  # 'True'
print(str(4>7))         # False

print(str(None))        # None
print(repr(str(None)))  # 'None'

print(str())            #
print(repr(str()))      # ''
    
################
"int"

print(int('12'))       # 12

print(int(4.7))        # 4

print(int(True))       # 1
print(int(False))      # 0
print(int(5>7))        # 0
print(int())           # 0

print(int(0b10101))    # 21

#---------------

n = '45' 
   
print(n+'6')        # 456
print(int(n)+6)     # 51 

print(n*3)          # 454545
print(int(n)*3)     # 135

#---------------

print(int('10.5'))           # invalid literal for int() with base 10: '10.5'
print(int(float('10.5')))    # 10

################
"float"

print(float('21'))     # 21.0
print(float('21.1'))   # 21.1

print(float(21))       # 21.0

print(float(True))     # 1.0
print(float(False))    # 0.0
print(float())         # 0.0

a = '7e+3'
print(float(a))        # 7000.0

################
"complex"

print(complex('21'))          # (21+0j) 

print(complex(21))            # (21+0j) 
print(complex(0))             # 0j 

print(complex(2.1))           # (2.1+0j) 

a=5; b=7
print(complex(a, b))          # (5+7j)  
print(complex(5, 0))          # (5+0j)  
print(complex(0, 7))          # 7j  

print(complex(False))         # 0j
print(complex(True))          # (1+0j)
print(complex(True, False))   # (1+0j)
print(complex(False, True))   # 1j
print(complex())              # 0j

################
"bool"

print(bool(True))   # True 
print(bool('ali'))  # True 
print(bool(' '))    # True
print(bool(1))      # True
print(bool(5))      # True
print(bool(-2))     # True
print(bool(3.2))    # True
print(bool(3+5j))   # True
print(bool(3>1))    # True


print(bool(False))  # False
print(bool(None))   # False
print(bool(3>5))    # False
print(bool(0))      # False
print(bool())       # False
print(bool(''))     # False
print(bool([]))     # False 
print(bool({}))     # False 
print(bool(()))     # False

################################################
# assign

a = 5; b = 7; name = 'ali'
print(a, b, name)            # 5 7 ali

# or:
    
a, b, name = 5, 7, 'ali'
print(a, b, name)            # 5 7 ali

#---------------

a, b, c = 5           # TypeError: cannot unpack non-iterable int object
a, b, c = 5, 5, 5
print(a, b, c)        # 5 5 5

# or:
    
a = b = c = 5         # assign 5 to a, b and c.
print(a, b, c)        # 5 5 5

#---------------

a = 4 ; b = 7
print(a, b)           # 4 7

x = a
a = b
b = x
print(a, b)           # 7 4 

#---------------

a, b = 4, 7
print(a, b)           # 4 7

a, b = b, a           # assign a value to b and b value to a                   
print(a, b)           # 7 4  

#---------------

a, b = 2, 3
print(a, b)           # 2 3

a, b = b, a+b
print(a, b)           # 3 5

################################################
################################################
# Operator

"Arithmetic Operators"

print(1 + 3)       # 4
print(True + 4)    # 5
print((5>2) + 7)   # 8 
print('a' + 'c')   # ac

print(5 - 3)       # 2

print(2 * 3)       # 6
print('a' * 3)     # aaa

print(3 / 2)       # 1.5
print(4 / 2)       # 2.0

print(3 // 2)      # 1
print(4 // 2)      # 2

print(17 % 5)      # 2

print(2 ** 3)      # 8 
print(6 ** 0)      # 1
print(0 ** 0)      # 1

print(5<<1)        # 10
print(5<<3)        # 40
print(5*(2**3))    # 40

################
'Operator Precedence'

print(8 - 2 * 3)            # 2
print(1 + 3 * 4 / 2)        # 7.0
print(16 / 2 ** 3)          # 2.0
print(2 ** 2 ** 3)          # 256

################
"Assignment Operator"

x = 4
x = x + 2
print(x)     # 6

x = 4
x += 2    
print(x)     # 6

y = 8
y /= 2   
print(y)     # 4.0

################
"Comparison Operators"

print(2 == 3)                       # False
print(2 != 3)                       # True
print('j'=='j')                     # True
print('j'=='J')                     # False

print(2 < 3)                        # True
print('a'>'A')                      # True
print('a'>'f')                      # False
print('a'<'f')                      # True
print('a'<'F')                      # False
print('a'>'F')                      # True

################
"Logical Operators"

print(1<3 or 4>5)                   # True
print(1<3 and 4>5)                  # False
print(not 1<3)                      # False
print(not True)                     # False

#---------------
'Short-circuit'

print(1 >= 2 and (5/0) > 2)         # False
print(3 >= 2 and (5/0) > 2)         # ZeroDivisionError: division by zero

print(7 >= 3 or (5/0) > 2)          # True
print(3 >= 7 or (5/0) > 2)          # ZeroDivisionError: division by zero

################
"Membership Operators"

x = [1, 2, 3, 4, 5]
print(3 in x)              # True
print(3, 5 in x)           # 3 True
print([3, 5] in x)         # False
print(7 and 5 in x)        # True
print(7 in x and 5 in x)   # False 
print(7 in x or 5 in x)    # True

print(24 not in x)         # True

#---------------

s = 'ali.ram'
print('a' in s)          # True
print('R' in s)          # False
print('li' in s)         # True
print('.ra' in s)        # True 

################################################
# Decimal (dah-dahi)

'python aadadi az ghabile 0.1, 0.2 va 0.3 ra be soorate 0.10000000000000001,\
 0.20000000000000001 va 0.30000000000000001 neshan midahad ke daghighan \
 barabare anha nistand. in mozoo gahi mojebe khataye manteghi mishavad.'

a = 0.2 + 0.2 + 0.2

print(a)                       # 0.6000000000000001
print(a == 0.6)                # False


'az in roo dar python yek sheye jadid be name Decimal tarrahi shode ast.\
 in sheye dar majoole decimal gharar darad.'
 
from decimal import Decimal

a = Decimal('0.6')
b = Decimal('0.2')

print(a, b)                    # 0.6 0.2
print(a == b+b+b)              # True

################################################
# aadade kasri  

'baraye eijade ashyae kasri(aadade gooya), az sheye Fraction estefade mishavad.\
 in sheye dar majoole fraction ghara darad.'

from fractions import Fraction

a, b = 7, 3
f = Fraction(a, b)

print(f)                 # 7/3
print(f == 7/3)          # False
print(int(f))            # 2 
print(float(f))          # 2.3333333333333335
print(7/3)               # 2.3333333333333335
print(float(f) == 7/3)   # True

################################################
# Id

'Every object in python is stored somewhere in memory.\
 We can use id() to get that memory address.'

s1 = 'farshid'
s2 = 'farshid'

print(id(s1))
print(id(s2))
print(id(s1) == id(s2))          # True
print(s1 == s2)                  # True

################################################
# Mathematics

print(abs(-4))             # 4

print(pow(2, 3))           # 8

print(divmod(8, 4))        # (2, 0)
print(divmod(9, 4))        # (2, 1)

print(round(2.6))          # 3
print(round(2.5))          # 2
print(round(2.3))          # 2
print(round(3.6))          # 4
print(round(3.5))          # 4
print(round(3.3))          # 3

print(pow.__doc__)         # about pow

################
"math"

import math

dir(math)
dir(math)[-2]              # 'trunc'
help(math.trunc)

print(math.trunc(2.7))     # 2
print(math.floor(2.7))     # 2
print(math.ceil(2.3))      # 3 

print(math.factorial(4))   # 24
print(math.sin(5))         # -0.9
print(math.log2(32))       # 5.0
print(math.log10(32))      # 1.505149978319906
print(math.log(32))        # 3.4657359027997265

print(math.fmod(9, 4))     # 1.0
print(math.gcd(9, 4))      # 1
print(9 % 4)               # 1

print(math.fabs(-4))       # 4.0
print(abs(-4))             # 4

print(math.sqrt(4))        # 2.0
print(math.pow(2, 3))      # 8.0
print(pow(2, 3))           # 8

print(math.e)              # 2.718281828459045
print(math.pi)             # 3.141592653589793
print(f'{math.pi :.2f}')   # 3.14













  

 
