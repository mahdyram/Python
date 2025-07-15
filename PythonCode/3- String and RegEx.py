"""
String and RegEx
"""
################################################
################################################
# String

# amalgar haye reshte

"ettesal(+)"

a = 'ali'
b = ' ram'
c = a+b+' sabzevar'
print(c)            # ali ram sabzevar

# or:
a = 'ali'
b = ' ram'
a += b+' sabzevar'
print(a)            # ali ram sabzevar 

################
"tekrar(*)"

a = 'ali '
b = 3
c = a*b
print(c)            # ali ali ali 

################
"boresh([start:end:step])"

s = 'python'
'''
 p  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
'''

#  p  y  t  h  o  n
#  0  1  2  3  4  5

print(s[2])             # t  
print(s[1],s[4])        # y o
print(s[0:2])           # py
print(s[:2])            # py
print(s[3:6])           # hon 
print(s[3:])            # hon 
print(s[3:5])           # ho
print(s[5:6])           # n
print(s[4:1])           # 
print(s[0:6])           # python
print(s[:])             # python
print(s[1:6])           # ython
print(s[1:6:3])         # yo
print(s[::2])           # pto
print(s[::-1])          # nohtyp
print(s[::-2])          # nhy


#  p  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

print(s[len(s)-1])      # n 
print(s[-1])            # n 
print(s[-6])            # p
print(s[-5:-2])         # yth
print(s[-6:-3])         # pyt
print(s[:-3])           # pyt
print(s[-4:-1])         # tho
print(s[-4:])           # thon
print(s[-2:-5])         # 
print(s[-6:])           # python
print(s[-6:-2])         # pyth
print(s[-6:-2:2])       # pt
print(s[5:0:-1])        # nohty
print(s[5::-1])         # nohtyp
print(s[::-1])          # nohtyp
print(s[::-2])          # nhy

#---------------

s = 'abcdefgh'
print(s[1:-4])  # bcd
print(s[-7:4])  # bcd
print(s[::2])   # aceg
print(s[::-1])  # edcba
print(s[::-2])  # eca

#---------------

'har fasele ham yek reshte ast:'

s = 'python '
print(s[5])        # n
print(s[6])        # 
print(repr(s[6]))  # ' '

#---------------

'reshte ha taghir napazirand:'

s = 'python'
print(s[0])    # p
s[0] = 'f'     # 'str' object does not support item assignment

################
"ozviat(in & not in)"

a='sabzevar'
print('z' in a)               # True
print('d' in a)               # False  
print('sa' in a)              # True
print('sb' in a)              # False
print('zeva' in a)            # True
print('s','v' in a)           # s True
print(('s' and 'q') in a)     # False
print(('s' or 'q') in a)      # True
print('s' not in a)           # False
print('q' not in a)           # True
print('sab' not in a)         # False
print(('s' and 'q') not in a) # True

print('s' and 'v' in a)       # True  ??
print('q' and 'v' in a)       # True  ??
print('s' or 'a' in a)        # s     ??
print('q' in a or 's')        # s     ??
print('z' in a or 's')        # True  ??

################
"karakter haye chap nashodani ke ba \ shoroo mishavand"

print('ali\nram')   # satre jadid
print('ali\tram')   # tabe bad
print('ali\a ram')  # booghe system
print('\f')         # pak kardane console(fromfeed)

################
"namayeshe karaktere \ "

print('ali\ram')    # ami

'estefade az \\ '
print('ali\\ram')   # ali\ram

'estefade az r ghable rashte'
print(r'ali\ram')   # ali\ram

################

print("I'm good")          # I'm good
print('I\'m good')         # I'm good

################
"chand khatti"

s = '''salam be doostan
va heme azizane del'''
print(s)                  # salam be doostan
                          # va heme azizane del

# but:
s = 'salam be doostan\
 va heme azizane del'
print(s)                  # salam be doostan va heme azizane del

################################################
# metod haye reshte

"ord & chr"

# horoofe koochak:
" a   b   c  ... y    z\
  97  98  99 ...121  122\
"
print(ord('a'))  # 97
print(ord('z'))  # 122
print(chr(97))   # a
print(chr(122))  # z

# horoofe bozorg:
" A   B   C  ... Y   Z\
  65  66  67 ... 89  90\
"
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(chr(65))   # A
print(chr(90))   # Z

# gheyre([,{,%,@,...):
print(ord('['))  # 91
print(ord('{'))  # 123
print(ord('%'))  # 37
print(chr(37))   # %

################

s='python'
print(len(s))   # 6
print(max(s))   # y   => ord('y')=121 (max in s)
print(min(s))   # h   => ord('h')=104 (min in s)

################
"repr()"

a = '32'
b = 32

print(a)        # 32
print(b)        # 32

print(repr(a))  # '32'
print(repr(b))  #  32 

#---------------

s = '  ali ram '
print(s)              #   ali ram 
print(repr(s))        # '  ali ram '

#---------------

f = '0012'

a = int(f)
print(a)        # 12

b = str(int(f))
print(b)        # 12

print(repr(a))  # 12
print(repr(b))  # '12'

################

s='PyThon'
print(s.lower())       # python
print(s.upper())       # PYTHON
print(s.swapcase())    # pYtHON

#---------------

s='welcom to python'
print(s.capitalize())  # Welcom to python
print(s.title())       # Welcom To Python

#---------------

s='welcom to python'
print(s.startswith('we'))   # True
print(s.endswith('thon'))   # True

################
"is..."

s='python'
print(s.islower())     # True
print(s.isupper())     # False

#---------------

s='python'
print(s.isalnum())     # True  
print(s.isalpha())     # True

s='python3'
print(s.isalnum())     # True
print(s.isalpha())     # False

s='#python3'
print(s.isalnum())     # False
print(s.isalpha())     # False

#---------------

s='123'
print(s.isdigit())          # True

s='123ali'
print(s.isdigit())          # False

s = '12a3bcd4'
for i in s:
    if i.isdigit() == True:
        print(i,end=' ')    # 1 2 3 4

# or:
s = '12a3bcd4'
x = [i for i in s if i.isdigit() == True]
print(x)  
# ['1', '2', '3', '4']      

# or:
s = '12a3bcd4'
x = [int(i) for i in s if i.isdigit() == True]
print(x)  
# [1, 2, 3, 4]

################
"count()"

s='welcom to python'
print(s.count('o'))         # 3
print(s.count('o',5))       # 2 : az index 5 be bad donbale 'o' migardad (index 5 ra ham barresi mikonad)
print(s.count('o',4))       # 3

################
"find()"

s='welcom to python'
print(s.find('o'))          # 4
print(s.index('o'))         # 4
print(s.find('f'))          # -1
#print(s.index('f'))        # ValueError
print(s.find('o',5))        # 8 : az index 5 be bad donbale 'o' migardad
print(s.find('o',4))        # 4
print(s.find('o',10))       # 14

################
"strip()"

s = '$$pyt$hon$$$'
print(s.strip('$'))     # pyt$hon
print(s.lstrip('$'))    # pyt$hon$$$
print(s.rstrip('$'))    # $$pyt$hon

#---------------

s = '##ali$$$'
print(s.lstrip('#').rstrip('$'))  # ali    
print(s.strip('#$'))              # ali
print(s.strip('# $'))             # ali

#---------------
        
s = 'www.sanjesh.org'
print(s.lstrip('w'))                    # .sanjesh.org
print(s.lstrip('www.'))                 # sanjesh.org
print(s.lstrip('www.').rstrip('.org'))  # sanjesh
print(s.strip('www.org'))               # sanjesh

# but:
s = 'www.osanjeshw.org'  
print(s.lstrip('www.').rstrip('.org'))  # osanjeshw
print(s.strip('www.org'))               # sanjesh

#---------------

s ='  ali  '
print(s)                  #   ali 
print(repr(s))            # '  ali  '
print(s.strip())          # ali
print(s.strip(' '))       # ali
print(repr(s.strip()))    # 'ali'
print(repr(s.strip(' '))) # 'ali'

s ='  ali ram  '
print(s)                  #   ali ram
print(repr(s))            # '  ali ram  '
print(s.strip())          # ali ram
print(repr(s.strip()))    # 'ali ram'

#---------------

s = 'ali\n  '
print(s)                   # ali
print(repr(s))             # 'ali\n  '
print(repr(s.strip(' ')))  # 'ali\n'
print(repr(s.strip()))     # 'ali'

s = 'asma\tram  '
print(s)                   # asma	ram
print(repr(s))             # 'asma\tram  '
print(repr(s.strip(' ')))  # 'asma\tram'
print(repr(s.strip()))     # 'asma\tram'

################
"join(list-tuple-set)"

print('.'.join(['ali','ram']))  # ali.ram
print('.'.join(('ali','ram')))  # ali.ram
print('.'.join({'ali','ram'}))  # ali.ram

#---------------

a = ['hi', 'ali', 'ram']
print(' '.join(a))              # hi ali ram 

#---------------

a = ['hi', 'ali', 'ram']
print('.'.join(a))              # hi.ali.ram

#---------------

x = 'radan'

print(reversed(x))                # <reversed object at 0x000002421D00CA60>
print(list(reversed(x)))          # ['r', 'a', 'd', 'a', 'r']
print(''.join(reversed(x)))       # nadar
print(x[::-1])                    # nadar

#---------------

n = 'amin'

print('.'.join(n))              # a.s.m.a.
print('.'.join(n[::-1]))        # a.s.m.a.
print('.'.join(reversed(n)))    # a.s.m.a.

################
"split()"

s = 'python'
print(s)               # python
print(repr(s))         # 'python'
print(s.split())       # ['python']     <class 'list'> 
print(s.split('t'))    # ['py', 'hon']
print(s.split(' '))    # ['python']
print(s.split(','))    # ['python']

#---------------

s = 'python.py.ir'
print(s.split('.'))    # ['python', 'py', 'ir']

a, b, c = s.split('.')
print(a)               # python  
print(b)               # py
print(c)               # ir

#---------------

s = 'hi ali ram'
print(s.split())          # ['hi', 'ali', 'ram']
print(s.split(' '))       # ['hi', 'ali', 'ram']

#---------------

s = 'ali\nreza'
print(s)
print(s.split('\n'))      # ['ali', 'reza']
print(s.splitlines())     # ['ali', 'reza']

#---------------

s = 'hi ali\n ram'
print(s.split())          # ['hi', 'ali', 'ram']
print(s.split(' '))       # ['hi', 'ali\n', 'ram']
print(s.splitlines())     # ['hi ali', ' ram']

################
"split & join"

s = 'hi ali ram'
l = s.split()
print(l)               # ['hi', 'ali', 'ram']

print(' '.join(l))     # hi ali ram
print('.'.join(l))     # hi.ali.ram

################
"replace()"

s = 'shirafkan'
print(s.replace('afkan','del'))     # shirdel

#---------------

s = 'heloo'

print(s.replace('h', 'H'))          # Heloo

print(s.replace('o', 'i'))          # helii

print(s.replace('o', 'i', 1))       # helio

print(s.replace('o', ''))           # hel

print(s.replace('o', '', 1))        # helo

#---------------

s = '   he loo  '
print(s.replace(' ', ''))           # heloo

################

s = 'sara'
print(s.ljust(7,'+'))      # sara+++
print(s.rjust(7,'+'))      # +++sara
print(s.center(7,'+'))     # ++sara+

s = '12'
print(s.rjust(5,'0'))      # 00012

s = '12'
print(s.zfill(5))   # 00012
print(s.zfill(3))   # 012

################################################
# format

"format()"

print('{}'.format('ali'))            # ali
print('{0}'.format('ali'))           # ali
print('name is {}'.format('ali'))    # name is ali
print('{} {}'.format('ali',20))      # ali 20
print('{0} {1}'.format('ali',20))    # ali 20
print('{1} {0}'.format('ali',20))    # 20 ali
print('{0} {0}'.format('ali',20))    # ali ali

#---------------

s = '{} & {} ram'.format('ali','asma')  # ali & asma ram
print(s)

#---------------

a, b = 'ali', 20
print('name is {0} and age is {1}'.format(a, b))  # name is ali and age is 20

# or:
a, b = 'ali', 20
s = 'name is {0} and age is {1}'
print(s.format(a, b))                             # name is ali and age is 20

# or:
a, b = 'ali', 20   
print(f'name is {a} and age is {b}')              # name is ali and age is 20

#---------------

s = 'my name is {}'
print(s.format('ali'))    # my name is ali

# or:
s = 'my name is {}'
n = 'ali'
print(s.format(n))        # my name is ali

s = 'my name is {}'
l = ['ali', 'asma', 'fateme']
for i in l:
    print(s.format(i))
'''
my name is ali
my name is asma
my name is fateme
'''
################
" %s "

r = 'name is %s and age is %s'%('ali', 20)
print(r)

#---------------

a, b = 'ali', 20
r = 'name is {0} and age is {1}'
print(r.format(a, b))                             # name is ali and age is 20

# or:
a, b = 'ali', 20
r = 'name is %s and age is %s'
print(r%(a, b))                             # name is ali and age is 20

#---------------

square = lambda x: x ** 2

for i in range(1, 11):
    print(i, ': ', square(i))

for i in range(1, 11):
    print("%2d: %d" %(i, square(i)))

for i in range(1, 11):
    print("%2d: %3d" %(i, square(i)))

#---------------

square_and_cube = lambda x: (x ** 2, x ** 3)

for i in range(1, 11):
    print("%2d: %s" %(i, square_and_cube(i)))

################
" f'{}' "

print(5+3)                  # 8
print(repr(5+3))            # 8
print(type(5+3))            # <class 'int'>

print(f'{3+5}')             # 8 
print(repr(f'{3+5}'))       # '8'
print(type(f'{3+5}'))       # <class 'str'>

print(str(5+3) == f'{3+5}') # True

#---------------

print('5 + 3 = 5+3')        # 5 + 3 = 5+3
print('5 + 3 =',5+3)        # 5 + 3 = 8
print(f'5 + 3 = {5+3}')     # 5 + 3 = 8

a = 5 ; b = 3
print(f'5 + 3 = {a+b}')     # 5 + 3 = 8

#---------------

n = 10
print('n is', n)           # n is 10
print('n is' + n)          # eror (str cant plus int)
print('n is ' + str(n))    # n is 10
print('n is ' + f'{n}')    # n is 10
print(f'n is {n}')         # n is 10

n = 10
print(str(n) == f'{n}')    # True

#---------------

fn = 'asma' ; ln = 'ram'
print(fn, ln)               # asma ram
print(fn + ln)              # asmaram
print(fn+' '+ln)            # asma ram
print(f'{fn} {ln}')         # asma ram
print(f'{"asma"} {"ram"}')  # asma ram
# print(f'{asma} {ram}')    # error

#---------------

x = 7 ; y = 2
f = x**y
print('f(x, y) =', f)       # f(x, y) = 49
print(f'f{x,y} = {f}')      # f(7, 2) = 49

#---------------

for x in[1,2,3,4]:
    for y in[2,3,4]:
        print(f'{x}**{y} = {x**y}')         # 1**2 = 1 , ...

################

x = 14
print('{:b}'.format(x))    # 1110       
print('{:#b}'.format(x))   # 0b1110

# or:
x = 14
print(f'{x:b}')            # 1110
print(f'{x:#b}')           # 0b1110 

# or:
print(f'{14:b}')           # 1110
print(f'{14:#b}')          # 0b1110  

#---------------

x = 0b1110
print(f'{x:d}')       # 14

#---------------

x = 14
print(f'{x:f}')       # 14.000000
print(f'{x:.2f}')     # 14.00

x = 15.999
print(f'{x:f}')       # 15.999000
print(f'{x:.3f}')     # 15.99
print(f'{x:.2f}')     # 16.00

#---------------

x = 0.83
print(f'{x:%}')       # 83.000000%
print(f'{x:.2%}')     # 83.00%

#---------------

x = 20000000
print(f'{x:,}')       # 20,000,000

#---------------
    
x = 35
print(f'{x:*>6d}')    # ****35
print(f'{x:*<6d}')    # 35****
print(f'{x:*^6d}')    # **35**

################################################
################################################
# RegEx

# search(pattern, string)

"re.search('x', string)"
'aya x dar string vojood darad?'

import re
s = 'Python is a programming language.'
m = re.search('programming', s)
print(m)                         # <re.Match object; span=(12, 23), match='programming'>
print(type(m))                   # <class 're.Match'>
print(bool(m))                   # True
print(m.span())                  # (12, 23)  =>  baze makani kalame programing
print(m.start())                 # 12
print(m.end())                   # 23 
print(m.group())                 # programming
print(m.group(0))                # programming
print(m.groups())                # ()

#---------------

s = 'Python is a programming language.'
m = re.search('are', s)
print(m)                         # None
print(type(m))                   # <class 'NoneType'>
print(bool(m))                   # False

################  
"re.search('^x', string)"
'aya string ba x shoroo mishavaf?'

s = 'Python is a programming language.'
m = re.search('^is', s)
print(m)                     # None

if m:
    print('yes')                
else:
    print('no')              # no  

#---------------

s = 'Python is a programming language.'
m = re.search('^Pyt', s)
print(m)                         # <re.Match object; span=(0, 3), match='Pyt'>
print(m.group())                 # Pyt

if m:
    print('yes')             # yes
else:
    print('no')      
    
################  
"re.search('x$', string)"
'aya string ba x tamam mishavaf?'

s = 'Python is a programming language.'
m = re.search('language.$', s)
print(m)                          # <re.Match object; span=(24, 33), match='language.'>

#---------------

s = 'Python is a programming language.'
m = re.search('guage.$', s)
print(m)                          # <re.Match object; span=(27, 33), match='guage.'>

################    

x = 'phone number 091212123344 and another 02122334455 number.'

m = re.search('(\w)', x)
print(m)                  # <re.Match object; span=(0, 1), match='p'>
print(m.group())          # p
print(m.group(0))         # p
print(m.groups())         # ('p',)

#---------------

m = re.search('(\w+)', x)
print(m)                  # <re.Match object; span=(0, 5), match='phone'>
print(m.group())          # phone
print(m.group(0))         # phone
print(m.groups())         # ('phone',)

#---------------

m = re.search('(\d)', x)
print(m)                  # <re.Match object; span=(13, 14), match='0'>
print(m.group())          # 0

#---------------

m = re.search('(\d+)', x)
print(m)                  # <re.Match object; span=(13, 25), match='091212123344'>
print(m.group())          # 091212123344

#---------------

m = re.search('(\w+) (\d+)', x)
print(m)                        # <re.Match object; span=(6, 25), match='number 091212123344'>
print(m.groups())               # ('number', '091212123344') => <class 'tuple'>
print(m.group())                # number 091212123344
print(m.group(0))               # number 091212123344
print(m.group(1))               # number
print(m.group(2))               # 091212123344

#---------------

m = re.search('number (\d)', x)
print(m)                        # <re.Match object; span=(6, 14), match='number 0'>
print(m.group())                # number 0
print(m.groups())               # ('0',)
print(m.group(1))               # 0

#---------------

m = re.search('number (\d+)', x)
print(m)                        # <re.Match object; span=(6, 25), match='number 091212123344'>
print(m.group())                # number 091212123344
print(m.groups())               # ('091212123344',)
print(m.group(1))               # 091212123344

################################################
# findall(pattern, string)

x = 'phone number 091212123344 and another 02122334455 number.'

m = re.findall('\w+', x)
print(m)                         # ['phone', 'number', '091212123344', 'and', 'another', '02122334455', 'number']

print(re.findall('\d+', x))      # ['091212123344', '02122334455']

print(re.findall('\w+ \d+', x))  # ['number 091212123344', 'another 02122334455']

print(re.findall('\d+ \w+', x))  # ['091212123344 and', '02122334455 number']

print(re.findall('[0-9]+', x))   # ['091212123344', '02122334455']

print(re.findall('[0-2]+', x))   # ['0', '121212', '02122']

#---------------  

name = 'Farshid Shirafkan'
print(re.findall('z', name))       # []
print(re.findall('r', name))       # ['r', 'r']
print(re.findall('[a-f]', name))   # ['a', 'd', 'a', 'f', 'a']

#---------------

name = 'Farshid Shirafkan'
print(re.findall('r[^i]', name))   # ['rs', 'ra']         =>  az harfe r ta harfe i be andaze yek harf
print(re.findall('r[^ ]', name))   # ['rs', 'ra']         =>  az harfe r ta space be andaze yek harf
print(re.findall('r[^ ]*', name))  # ['rshid', 'rafkan']  =>  az harfe r ta space
print(re.findall('r[^i]*', name))  # ['rsh', 'rafkan']    =>  az harfe r ta harfe i

#---------------

name = 'Farshid Shir afkan'
print(re.findall('\s+', name))     # [' ', ' ']  =>  space ha
print(re.findall('\S+', name))     # ['Farshid', 'Shir', 'afkan']  =>  gheyre space ha

#---------------

s = 'From ali@gmail.com to sara@yahoo.com'
print(re.findall('\S+@\S+', s))    # ['ali@gmail.com', 'sara@yahoo.com']  =>  estekhraje email ha az matn

#---------------

text = "He was carefully disguised but captured quickly by police."
t = re.findall(r"\w+ly", text)
print(t)                           # ['carefully', 'quickly']

################
"finditer"

text = "He was carefully disguised but captured quickly by police."
f = re.finditer(r"\w+ly", text)
print(f)                         # <callable_iterator object at 0x000001B0C2277610>
print(type(f))                   # <class 'callable_iterator'>
for m in f:
     print(m.span(), m.group())
'''
(7, 16) carefully
(40, 47) quickly
'''

################################################
# split(pattern, string, maxsplit)

s = 'From ali@gmail.com to sara@yahoo.com'

print(s.split())                   # ['From', 'ali@gmail.com', 'to', 'sara@yahoo.com']
print(re.split('\ ', s))           # ['From', 'ali@gmail.com', 'to', 'sara@yahoo.com']
print(re.split('\s', s))           # ['From', 'ali@gmail.com', 'to', 'sara@yahoo.com']
print(re.split('\s', s, 1))        # ['From', 'ali@gmail.com to sara@yahoo.com']
print(re.split('\s', s, 2))        # ['From', 'ali@gmail.com', 'to sara@yahoo.com']
print(re.split('\@', s))           # ['From ali', 'gmail.com to sara', 'yahoo.com']

################################################ 
# sub(pattern, repl, string, count)

s = 'ali-asma-fateme'
print(s.replace('-', '*'))     # ali*asma*fateme
print(re.sub('\-', '*', s))    # ali*asma*fateme
print(re.sub('\-', ' ', s))    # ali asma fateme
print(re.sub('\-', '', s))     # aliasmafateme

#---------------

s = 'ali ram'
print(re.sub('\ ', '.', s))    # ali.ram
print(re.sub('\s', '.', s))    # ali.ram

#---------------

txt = 'Python is a programming language.'
print(re.sub('\s', '_', txt))             # Python_is_a_programming_language.
print(re.sub('\s', '_', txt, 2))          # Python_is_a programming language.   \s: space ha
print(re.sub('\S', '*', txt))             # ****** ** * *********** *********   \S: gheyre space ha

#--------------- 

phone = '0912-197-12345'
print(re.sub('\d', '#', phone))    # ####-###-#####   \d: digit ha
print(re.sub('\D', '#', phone))    # 0912#197#12345   \D: gheyre digit ha

#---------------  

p = '  farsh id   '

r = re.sub('^\s+', '', p)
print(repr(r))              # 'farsh id   ' 

r = re.sub('\s+$', '', p)
print(repr(r))              # '  farsh id'

r = re.sub('\s', '', p)
print(repr(r))              # 'farshid'

r = p.replace(' ', '')
print(repr(r))              # 'farshid'

print(repr(p.strip(' ')))   # 'farsh id'

################  
"subn"

s = 'ali-asma-fateme/ram' 
r = re.subn('-', '.', s)
print(r)                     # ('ali.asma.fateme/ram', 2)  2: tedade jaygozini ha
print(type(r))               # <class 'tuple'>

#---------------

s = 'ali-asma-fateme/ram' 
r = re.subn('/', '*', s)
print(r)                     # ('ali-asma-fateme*ram', 1)





#74523523894############%^%^^^^^^^^

a = 73
b = 29
s = str(a) + str(b)
print(s)


a = 73
b = 29
s = '%s%s' % (a, b)
print(s)


print('%.f'%(31.5621))
print(round(31.5621))
print('%.f'%(31.4621))
print(round(31.4621))

