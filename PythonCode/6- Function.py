"""
Function
"""
################################################
################################################
# function()

def f():
    print('hello')
f()                 # hello
    
# or:
def f():
    return 'hello'
print(f())          # hello

# or:
def f(n):
    return n
print(f('hello'))   # hello

x = 'salam'
print(f(x))         # salam

################

def f(a):
    a *= 2
    print(a)    
    return a+1
f(5)            # 10   
print(f(5))     # 10 11

r = f(5)        # 10
print(r)        # 11

################

def f(x,y):
    if x > y :
        return x
    return y  
print(f(2,5))            # 5
print(f(2, f(5,3)))      # 5

#---------------

def g(x,y,z):
    return f(x, f(y,z))
print(g(2,5,3))          # 5

################

PI = 3.14

def area(r):
    return PI * r *  r

def circumference(r):
    return 2 * PI * r

def main(x):
    print(area(x))             
    print(circumference(x))   

main(4)    # 50.24  25.12

################

def f(a, b):
    a -=1
    b +=1
    return a, b

r = f(3, 5)
print(r, type(r))   # (2, 6) <class 'tuple'>

x, y = f(3, 5)
print(x)            # 2
print(y)            # 6

################

def add(x: int, y: int) -> int:
    '''
     sum two number
    '''
    print(x+y)
add(2, 3)       # 5 
   
print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(add.__doc__)  
# sum two number

################################################
# argoman haye tabe

"argoman ejbari"

def tavan(a, b):
    return a**b
x, y = 5, 2
print(tavan(x, y))   # 25

################
"argoman ba meghdare pishfarz"

def tavan(a, b=1):
    return a**b
x,y = 5, 2
print(tavan(x))      # 5
print(tavan(y))      # 2
print(tavan(x, y))   # 25

#---------------

# def tavan(b=1, a): # SyntaxError: non-default argument follows default argument
# bad az yek argoman ba meghdare pishfarz, nemitavan argomane ejbari avard.

################
"argoman kelidi"

def f(a, b):
    print(a, b)
    
f(1, 2)         # 1 2
f(a=1, b=2)     # 1 2
f(b=2, a=1)     # 1 2
f(1, b=2)       # 1 2
# f(a=1, 2)     # positional argument follows keyword argument

#---------------

def f(a, b=5, c=7):
    print(a, b, c)
    
f(1)              # 1  5  7
f(1, 3)           # 1  3  7 
f(1, 3, 5)        # 1  3  5
f(1, c=9)         # 1  5  9 
f(b=3, c=5 ,a=1)  # 1  3  5
f(1, b=3, c=5)    # 1  3  5
# f(1, b=2, 5)    # positional argument follows keyword argument
# bad az yek argoman ba meghdare kelidi, nemitavan argomane ejbari avard.

################
'parametr haye bad az *, bayad\
 ba esm seda zade shavand'

def f(a, *, b, c):
    print(a,b,c)
    
f(1, b=2, c=3)     # 1 2 3
# f(1, 2, c=3)     # error
# f(1, 2, 3)       # error

#---------------

def f(a, *, b=2, c=3):
    print(a,b,c)
                                
f(1)             # 1 2 3
f(1, b=8)        # 1 8 3
# f(1, 3, c=4)   # error

#---------------

def f(*, a=3):
    print(a)
    
f()       # 3
f(a=5)    # 5
# f(5)    # error

################
"argoman ba toole motaghayyer"

'vaghti ghabl az parametr, * mizarim\
 mitavan yek tuple ra be tabe ferestad.'

def f(*a):
    print(a)
f(5)              # (5,)
f(5,7,4)          # (5, 7, 4)
f((5,7,4))        # ((5, 7, 4),)
f('ali')          # ('ali',)

t = (2,3,'ali')
f(t)              # ((2, 3, 'ali'),)
f(t, 5)           # ((2, 3, 'ali'), 5) 

#---------------

def f(*a):
    print(a*2)
f(5)              # (5, 5)
f(5,7,4)          # (5, 7, 4, 5, 7, 4)
f((5,7,4))        # ((5, 7, 4), (5, 7, 4))

#---------------

def f(*a):
    print(sum(a))
f(5,7,4)          # 16

#---------------

def f(a, b, *x):
    print(x) 
f(1,2,3,4,5)          # (3, 4, 5)

# def f(a, *x, b):    # TypeError: f() missing 1 required keyword-only argument: 'b'

# def f(*x, a, b):    # TypeError: f() missing 2 required keyword-only arguments: 'a' and 'b'

#---------------

def f(x, *t):
    print(x,t)
f(1,2,3,4)       # 1 (2, 3, 4)


def f(*t, x):
    print(x, t)
f(1,2,3,x=4)     # 4 (1, 2, 3)
f(1,2,3,4)       # f() missing 1 required keyword-only argument: 'x'


def f(*t, x=9):
    print(x,t)    
f(1, 2)          # 9  (1, 2)
f(1, 2, 5, 7)    # 9  (1, 2, 5, 7)
f(1, 2, x=3)     # 3  (1, 2)

#---------------

def f(*s, a='.'):
    return a.join(s)
print(f('ali','ir'))        # ali.ir
print(f('ali','ir',a='/'))  # ali/ir

#---------------

def plus(*a):
    p = sum(a)
    return p
print(plus(3,5,6))    # 14  

# or:
def plus(*a):
    p = 0
    for i in a: p += i
    return p
print(plus(3,5,6))    # 14

# or:
def plus(*a):
    p = 0
    for i in range(len(a)):
        p += a[i]
    return p
print(plus(3,5,6))    # 14    

#---------------
'vaghti ghabl az parametr, ** mizarim\
 mitonim yek dict ro bedim be tabe'

def f(**a):
    print(a)
f(x=5)              # {'x': 5}
f(ali=5, asma=9)    # {'ali': 5, 'asma': 9}

#---------------

def f(a, b , **c):
    print(a,b,c)
f(3, 4, x=5, y=9)   # 3 4 {'x': 5, 'y': 9}
    
#---------------

def f(a, b , *c , **d):
    print(a)  
    print(b)  
    print(c)  
    print(d)  
f(3, 4, 7, 1, 6, x=5, y=7, z=9)  
'''
3
4
(7, 1, 6)
{'x': 5, 'y': 7, 'z': 9}
'''
# def f(a, b , **c , *d):    # Arguments cnnot follow var-keyword arguments

################################################
# anvae motaghayyer ha

"motaghayyer haye mahalli"

def f():
    name = 'ali'
    return name
print(f())        # ali
# print(name)     # name 'name' is not defined

################
"motaghayyer haye sarasari"

name = 'asma'
def f():
    name = 'ali'
    return name
print(f())        # ali
print(name)       # asma

#---------------

def f():
    name = 'ali'
    return name
name = 'asma'
print(f())        # ali
print(name)       # asma

#---------------

def f(n):
    n += '.'
    return n
name = 'asma'
print(f(name))    # asma.
print(name)       # asma

################
"dastoore global"

def f():
    global name
    name = 'ali'
    return name
print(f())        # ali
print(name)       # ali

#---------------

name = 'asma'
def f():
    global name
    name = 'ali'
    return name
print(name)       # asma  (ta ghabl az farakhani tabe, name, asma ast)
print(f())        # ali
print(name)       # ali   (ba farakhani tabe dar khate ghabl, name be ali taghiir mikonad)

#---------------

def f():
    global name
    name = 'ali'
    return name
name = 'asma'
print(name)       # asma 
print(f())        # ali
print(name)       # ali 

#---------------

def f(n):
    global n
# SyntaxError: name 'n' is parameter and global

################
"list va dict taghiir pazirand va niazi\
 be global ya return ham nadarand"

def f(l):
    l[0] -= 1
    l[1] += 1
    return l
lst = [3, 5] 
print(f(lst))     # [2, 6]
print(lst)        # [2, 6]

#---------------

def f(d):
    d['a'] -= 1
    d['b'] += 1  
    return d       
dic = {'a':3, 'b':5}    
print(f(dic))        # {'a': 2, 'b': 6}
print(dic)           # {'a': 2, 'b': 6}

################################################
# lambda

def f(n):
    return n*2
print(f(3))          # 6

f = lambda n: n*2
print(f(3))          # 6

#---------------

f = lambda: 'hello'
print(f())                   # hello

# or:
f = lambda: print('hello')
f()                          # hello

#---------------

add = lambda x, y, z: x+y+z
print(add(2, 3, 7))          # 12

#---------------

f = lambda x, y: (x+y, x-y)
print(f(2, 3))               # (5, -1)

#---------------

namayesh = lambda *x: x
print(namayesh(3,7,1))       # (3, 7, 1)

################################################
# FunctionTools

"map(function, lists)"
'tak take azaye list ra dar motaghayyere tabe migozarad'

l = ['a', 'A']
x = []
for i in l:
    x.append(ord(i))
print(x)               # [97, 65]

# or:
l = ['a', 'A']
m = map(ord, l)
print(list(m))         # [97, 65]

# or:
l = ['a', 'A']
x = list(map(ord, l))
print(x)               # [97, 65]

#---------------

l = ['ali', 'reza']
x = []
for i in l:
    x.append(i.upper())
print(x)                    # ['ALI', 'REZA']

# or:
l = ['ali', 'reza']
x = list(map(str.upper, l))
print(x)                    # ['ALI', 'REZA']

#---------------

a = [3, 2, 1]
b = [6, 4, 7]
def f(x, y):
    return x+y
l = list(map(f, a, b))
print(l)  
# [9, 6, 8]


# or:
a = [3, 2, 1]
b = [6, 4, 7]
f = lambda x, y: x+y
print(list(map(f, a, b)))  
# [9, 6, 8]


# or:
a = [3, 2, 1]
b = [6, 4, 7]
l = list(map(lambda x, y: x+y, a, b))
print(l) 
# [9, 6, 8]

#---------------

scores = [12, 8, 19, 15, 7]
l = list(map(lambda x: x>9 , scores))
print(l) 
# [True, False, True, True, False]

#---------------

lst = ['radar', 'ali', 'madam', 'php']
palindrome = lambda x: (x == ''.join(reversed(x)))
print(list(map(palindrome, lst))) 
# [True, False, True, True]

#---------------

name  = ['ali', 'reza']
score = [13, 18]
z = zip(name, score)
print(list(z))        
# [('ali', 13), ('reza', 18)]


# or:
name  = ['ali', 'reza']
score = [13, 18]
m = map(lambda x, y: (x,y) , name, score)
print(list(m)) 
# [('ali', 13), ('reza', 18)]

#---------------

def f(x):
    return x + 5

def g(y):
    return y * 2

x = [f, g]
l = [1, 2, 3]

for i in l:
    print(list(map(lambda a: a(i) , x)))
'''
[6, 2]
[7, 4]
[8, 6]
'''
################
"filter(function, lists)"

scores = [12, 8, 19, 15, 7]
f = filter(lambda x: x>9 , scores)
print(list(f)) 
# [12, 19, 15]

#---------------

l = ['radar', 'ali', 'madam' , 'php']
palindrome = lambda x: (x == ''.join(reversed(x)))
print(list(filter(palindrome , l))) 
# ['radar', 'madam', 'php']

#---------------

l = [2, 7, '', 9, {}, 8, [], 12]
print(list(filter(None, l)))       
# [2, 7, 9, 8, 12]

################################################
# sort

lst = [5, 2, 3, 1, 4]
print(sorted(lst))        # [1, 2, 3, 4, 5]

#---------------

d = {'ali':13, 'sara':17, 'taha':15}
print(sorted(d.items(), key=lambda x: x[1]))
# [('ali', 13), ('taha', 15), ('sara', 17)]

d = {'ali':13, 'sara':17, 'taha':15}
print(sorted(d.items(), key=lambda x: x[0]))
# [('ali', 13), ('sara', 17), ('taha', 15)]

#---------------

students = [
            {'id' : 1 ,'name' : 'taha' , 'score': 19},
            {'id' : 6 ,'name' : 'sara' , 'score': 8},
            {'id' : 4 ,'name' : 'omid' , 'score': 15},
            {'id' : 3 ,'name' : 'mahsa', 'score': 19}
           ]

f = lambda x: x['id']
print(sorted(students, key=f))
'''
[{'id': 1, 'name': 'taha', 'score': 19},
 {'id': 3, 'name': 'mahsa', 'score': 19},
 {'id': 4, 'name': 'omid', 'score': 15},
 {'id': 6, 'name': 'sara', 'score': 8}]
'''

f = lambda x: x['score']
print(sorted(students, key=f))
'''
[{'id': 6, 'name': 'sara', 'score': 8}, 
 {'id': 4, 'name': 'omid' , 'score': 15}, 
 {'id': 1, 'name': 'taha' , 'score': 19}, 
 {'id': 3, 'name': 'mahsa', 'score': 19}]
'''
#---------------

student = [
            ( 5 , 'taha' , 19),
            ( 6 , 'sara' , 8),
            ( 4 , 'omid' , 15),
            ( 3 , 'mahsa', 19)
          ]

print(sorted(student, key=lambda x: x[2]))
'''
[(6, 'sara', 8), 
(4, 'omid', 15), 
(5, 'taha', 19), 
(3, 'mahsa', 19)]
'''

print(sorted(student , key=lambda x: x[2] ,reverse=True))
'''
[(5, 'taha', 19), 
(3, 'mahsa', 19), 
(4, 'omid', 15), 
(6, 'sara', 8)]
'''

# or:
    
from operator import itemgetter as ig

print(sorted(student, key=ig(2)))
'''
[(6, 'sara', 8), 
(4, 'omid', 15), 
(5, 'taha', 19), 
(3, 'mahsa', 19)]
'''

print(sorted(student , key=ig(2) ,reverse=True))
'''
[(5, 'taha', 19), 
(3, 'mahsa', 19), 
(4, 'omid', 15), 
(6, 'sara', 8)]
'''

print(sorted(student , key=ig(2, 0) ))
'''
[(6, 'sara', 8), 
(4, 'omid', 15),
(3, 'mahsa', 19), 
(5, 'taha', 19)]
'''

################################################
# Generators

def f():
    return 3, 4, 5
print(f(), type(f()))  # (3, 4, 5) <class 'tuple'>


def f():
    return 3
    return 4
    return 5
print(f())             # 3

# but:  
def f():
    yield 3
    yield 4
    yield 5
print(f())             # <generator object f at 0x000001DFA5F63AB0>
print(list(f()))       # [3, 4, 5]
print(tuple(f()))      # (3, 4, 5)

#---------------

def f(x, y):
    yield x*y
    yield x+y
print(list(f(5, 7)))  # [35, 12]
a, b = list(f(5, 7))
print(a)              # 35
print(b)              # 12 

#---------------

def f():
    for i in range(1,4):
        return i**3
print((f()))             # 1

# but:
def f():
    for i in range(1,4):
        yield i**3
print(list(f()))         # [1, 8, 27]
    
################################################
# Decorators

def s():
    print('hello world')

def decor(func):
    def y():
        print('===========')
        func()
        print('===========')
    return y

decor(s)()
'''
===========
hello world
===========
'''

# or:
    
def decor(func):
    def y():
        print('===========')
        func()
        print('===========')
    return y

@decor
def s():
    print('hello world')

s()
'''
===========
hello world
===========
'''

################################################
# tavabe bazgashti (recursive function)

'''
iterative:
            n! = 1*2*3*...*n
            
recursive:
            n! = n * (n-1)!
            .
            .
            .
            1! = 1

3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1
'''
def fact(n):
    f = 1
    if n == 0 :
        print(1)
    else:
        for i in range(1, n+1):
             f *= i
        print(f)
fact(3)                # 6       


# or:
def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)
print(fact_rec(3))     # 6

#---------------
'''
2*3 = 2 + (2*2) = 2 + 4 = 6
2*2 = 2 + (2*1) = 2 + 2 = 4
2*1 = 2
'''
def mul(x,y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + mul(x,y-1)
    
print(mul(2,3))    #6 

#---------------
'''
2 ** 3 =  2 * (2**2) = 2 * 4 = 8
2 ** 2 =  2 * (2**1) = 2 * 2 = 4
2 ** 1 =  2
'''
def pow_rec(x,y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x * pow_rec(x,y-1)
    
print(pow_rec(3,2))  # 9

#---------------
'[2, 4, 5, 6, 7] => sum=24'

def sum_lst(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_lst(lst[1:])    

a = [2, 4, 5, 6, 7]
print(sum_lst(a))       # 24 = 2+4+5+6+7

#---------------
'345 => sum=12'

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(int(n/10)) 

print(sum_digits(345))  # 345 = 3+4+5=12

################
"Fibonacci"

'fibonacci(10): 0, 1, 1, 2, 3, 5, 8'

def fibo(n):
    r = []
    a = 0
    b = 1
    while a < n:
        r.append(a)
        a, b = b, a+b
    return r
print(fibo(10))         # [0, 1, 1, 2, 3, 5, 8]


#---------------
'fibonacci(4): 3'

def fibo_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
print(fibo_rec(4))   # 3  

l = []
i = 0
while True:
    if fibo_rec(i)<10:
        l.append(fibo_rec(i))
        i += 1
    else:
        break
print(l)             # [0, 1, 1, 2, 3, 5, 8] 

################
"BinarySearch"

def search_recursive(lst, x, start=0, end=len(lst)-1):
    if start > end:
        return None
    mid = (start + end) // 2
    if x == lst[mid]:
        return mid
    if x < lst[mid]:
        return search_recursive(lst, x, start, mid - 1)
    return search_recursive(lst, x, mid + 1, end)

a = [2, 4, 7, 12, 19, 25, 38]
print(len(a))                   # 7
print(len(a)//2)                # 3
print(a[len(a)//2])             # 12

print(search_recursive(a, 19))     # 4
print(search_recursive(a, 4))      # 1
print(search_recursive(a, 20))     # False

#---------------
'estefade az halghe while be jaye tabe bazgashti'

def search_iterative(lst, x):
    start = 0
    end = len(lst)-1
    
    while start <= end:
        mid = (start + end) // 2
        if x == lst[mid]:
            return mid
        if x < lst[mid]:
            end = mid-1
        else:
            start = mid+1
            
a = [2, 4, 7, 12, 19, 25, 38]
print(search_iterative(a, 19))     # 4
print(search_iterative(a, 4))      # 1
print(search_iterative(a, 20))     # False










