"""
Extra
"""

### string:

a, b = '49'
print(a)               # 4
print(b)               # 9
#a, b = '4925'         # ValueError: too many values to unpack (expected 2)


a, b = input()
'''
a, b = input()
49
'''
print(a)               # 4
print(b)               # 9


#a, b = 49             # TypeError: cannot unpack non-iterable int object
a, b = int(input())    # TypeError: cannot unpack non-iterable int object

#---------------

input().split(' ')
'''
input().split(' ')
4 9
Out[3]: ['4', '9']

input().split(' ')
4 9 1
Out[4]: ['4', '9', '1']
'''

a, b = ['4', '9']
print(a)          # 4
print(b)          # 9


a, b, c = input().split(' ')
a, b, c = int(a), int(b), int(c)
'''
a, b, c = input().split(' ')
4 9 1
'''
print(a)          # 4
print(b)          # 9
print(c)          # 1

#---------------

a, b = input().split(',')
print(int(a) + int(b))
'''
4,9
13
'''

a, b = input().split('+')
print(int(a) + int(b))
'''
4+9
13
'''

a, b = input().split(' ')
print(int(a) + int(b))
'''
4 9
13
'''


a, b, c = map(int, input().split())

#############################################

### Function:

from fractions import Fraction

f = Fraction(6,9)
print(f)
print(f.numerator)
print(f.denominator)

f = Fraction(7,7)
print(f)
print(f.numerator)
print(f.denominator)

################

#تشخیص عدد اول:

def a(b):
    for i in range(2,b-1):
        if b%i==0:
            return 'noaval'
    return 'aval'      
x=int(input('enter x\n'))
print(a(x))

print('--------------')

# morattab kardan 3 adad:
def f(x,y,z):
    a=max(x,y,z)
    c=min(x,y,z)
    for i in (x,y,z):
        if c<i<a:
            b=i
    return (a,b,c)
x=int(input('enter x\n'))
y=int(input('enter y\n'))
z=int(input('enter z\n'))
x,y,z=f(x, y, z)
print(z,y,x)

print('--------------')

# morattab kardan 2 adad ba Swap:
def f(x,y):
    if x>y:
        x,y=y,x
    return x,y
x=int(input('enter x\n'))
y=int(input('enter y\n'))
x,y=f(x, y)
print(x,y)

print('--------------')

# morattab kardan 3 adad ba Swap:
def f(x,y):
    if x>y:
        x,y=y,x
    return x,y

def g(x,y,z):
    if x>y:
        x,y=f(x, y)
    if y>z:
        y,z=f(y,z)
    if x>y:
        x,y=f(x, y)
    return (x,y,z)
x=int(input('enter x\n'))
y=int(input('enter y\n'))
z=int(input('enter z\n'))
print(g(x, y, z))
#or:
x,y,z=g(x, y, z)
print(x,y,z)

print('--------------')

# ????????????
def f(x):
    r=0
    for i in str(x):
        r+=1
    return r

y=0
def g(y,n=f(y)):
    print(n)    # chera n mosavi f(y) nemishe ?
    for i in range(f(y)-n):
        y//=10
    return y%10
h=int(input('enter y\n'))   
print(g(h))

print('--------------')

a=(5,7,'ali',30)
print(len(a))   # 4

print('--------------')

# mesal:
def s(*a):
    r=0
    for i in range(0,len(a)):
        r+=a[i]
    return a,r
print(s(5,3,7))  # ((5, 3, 7), 15)

print('--------------')

def f():
    print('*'*n)
n=int(input(''))
f()

#or:
def f(n):
    print('*'*n)
x=int(input(''))
f(x)

print('--------------')

# motaghayyer haye mahalli:
def f():
    v='ali'
    print(v)
v=input('e: ')
print(v)  
f()

print('--------------')

# global:
def f():
    global a
    a=7
    
a=10
print(a)

f()
print(a)

#or:
a=55
def f():
    global a
    a=7
    return a

print(a)
print(f())
print(a)

print('--------------')

def f():
    global a
    a=7
print(a)    # name 'a' is not defined

#but:
def f():
    global a
    a=7
f()
print(a)      # 7 

#or:
def f():
    global a
    a=7
    print(a)  # 7
a=int(input('en: '))
f()
print(a)      # 7 

print('--------------')

# mohasebe facturiel be vasile function bazgashti:
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
x=int(input('enter x\n'))
print(f(x))

print('--------------')

# namayeshe maghloobe adade khande shode ba «tabe bazgashti»:
def f(x):
    a=x%10
    if x==0:
        return ''
    return str(a)+f(x//10)
x=int(input('enter x\n'))
print(int(f(x)))

print('--------------')

# joda kardane bakhshe ashari va sahihe adad:
import math
x=float(input('enter x\n'))
a=math.floor(x)
z=x-a
print(a,z)    # why???
print(a,'%f'%z)

print('--------------')

# vroodi:523  &  khrooji:3^(2^(5))
def f(y):
    a=y%10
    b=y//10
    if y==0:
        return 1
    return a**f(b)
x=int(input('enter x\n'))
print(f(x))

# vali chera in yeki nemishe??????
def f(y):
    if y==0:
        return 1
    return y%10**f(y//10)
x=int(input('enter x\n'))
print(f(x))

print('--------------')

def f(x):
    a=x%10
    b=x//10
    if x==0:
        return 10
    return a<f(b)
print(f(321))     # False ??????? (1<2<3<10)

print('--------------')

# barname e ke bozorgtarin onsore har satr az araye ra namayesh dahad:
def m():
    import numpy as np
    x=np.array([[2,1,3],[6,5,4],[7,8,9]])
    print(x,'\n')
    for i in x:
        r=0
        for j in i:
            r+=1
            if r==1:
                a=j
            if j>a:
                a=j
        print(a,end='\n')
m()

#or:
import numpy as np
x=np.array([[2,1,3],[6,5,4],[7,8,9]])
print(np.amax(x,axis=1))

print('--------------')

'''barname e shamele 3 tabe: tabe A 5 adad ra khande
va dar araye e gharar midahad, tabe B har araye e ra
ke be an dahim az koochak be bozorg morattab mikonad,
tabe main az do tabe ghabli yekja bahre mibarad'''

from array import array
def A():
    a=array('i',[])
    for i in range(5):
        x=int(input('enter x\n'))
        a.append(x)
    return a
def B(x):
    for i in range(5):
        for j in range(i+1,5):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    return x
def main():
    c=A()
    print(c)
    return c,B(c)  # chera returne c ba printe c yeki nist?
print(main())

print('--------------')

"barname e ke adade dakhele yek reshte ra ba ham jam konad va neshan dahad"

s = '12a3bcd4'
k = 0
for ch in s:
    if ch.isdigit() == True:
        k += int(ch)
print(k)         # 10 : 1+2+3+4

print('--------------')

"barname pak kardane sefr haye ghable adad"

s = '127.02.0.001'
b = s.split('.')
a = '.'.join([str(int(i)) for i in b])
print(a)   # 127.2.0.1

print('--------------')
# isinstance(obj, type a tuple of types or a union)

print(isinstance('3', tuple))  # False
print(isinstance([], list))    # True
print(isinstance(3.2, float))  # True

print('--------------')

# random
import random
print( random.randint(1,5))      # انتخاب رندم از "رنج" 1 تا 5
print( random.choice([1,2,3]))   # انتخاب رندم از "لیست" 1و2و3
a = [1,2,3,4]
random.shuffle(a)                # bor zadan  
print(a)

import random
a=random.randint(3, 7)
print(a)

for i in range(5):
    r=random.randint(-10, 10)
    print(r,end=' ')

print('--------------')

import random
n = random.randrange(0,10)
f = 'no'
while  f == 'no' :
    a = int(input('enter:'))
    if a < n :
        print('>')
    elif a > n:
        print('<')
    else:
        print('correct')
        f = 'yes'
        
#or:  
import random
n = random.randrange(0,10)    
while  True:
    a = int(input('enter:'))
    if a < n :
        print('>')
    elif a > n:
        print('<')
    else:
        print('correct')
        break

print('--------------')

l = []
x = ''
while x != 'n':
    s = 'enter a number: '
    l.append(int(input(s)))
    x = input('countinu?(n/y): ')
print(f'mean is {sum(l)/len(l)}')

# or:
l = []
v = True
while y:
    s = 'enter a number: '
    l.append(int(input(s)))
    x = input('countinu?(n/y): ')
    if x == 'n':
        v = False
print(f'mean is {sum(l)/len(l)}')

# or:
l = []
while True:
    s = 'enter a number: '
    l.append(int(input(s)))
    x = input('countinu?(n/y): ')
    if x == 'n':
        break
print(f'mean is {sum(l)/len(l)}')


########################

"morattabsazie tavizi"

a=[1,7,3,9,5,2,4]
n=7
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

########################

"jostojooye meghdar dar araye"

a=array('i',[])
n=int(input('enter n\n'))
for i in range(n):
    x=int(input('enter x\n'))
    a.append(x)
print(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

# jostojooye khatti(tartibi):
v=int(input('enter v\n'))
for i in a:
    if i==v:
        print('index v=',a.index(i))
        
# jostojooye dodoii:
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==v:
        print('index v=',mid)
        break
    elif a[mid]<v:
        low=mid+1
    else:
        high=mid-1

#################
"shir ya khat"

import random
d = {'shir': 0, 'khat': 0}
for i in range(10):
    d[random.choice(list(d.keys()))] += 1
print(d)    

#---------------

import random
d = {}
for i in range(10):
    x = random.choice(['shir', 'khat'])
    d[x] = d.get(x,0) + 1
print(d)    

################

import random
print(random.randint(1,10))

from random import randint
print(randint(1, 10))

################

print(range(5))     # range(0, 5)
r = range(5)
print(r, type(r))   # range(0, 5) <class 'range'>
print(list(r))      # [0, 1, 2, 3, 4]
print(tuple(r))     # (0, 1, 2, 3, 4)
print(set(r))       # {0, 1, 2, 3, 4}

print(list(range(3, 9, 3)))  # [3, 6]

################

list('abc')

list(range(4))


################


from functools import reduce
 
def do_sum(x1, x2): return x1 + x2

x = reduce(do_sum, [1, 2, 3, 4])
print(x)




########################################
# Good questions


"majmooe zarb motnazere azaye 2 list ba n ozv"

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
for i in range(n):
    x+=a[i]*b[i]
print(x)

# or:

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum([a[i]*b[i] for i in range(n)]))

#################

"کلید چراغ"

n = int(input())
z = s = -1
for i in range(n):
    x = int(input())
    if x!=s:
        z+=1
    s = x
print(z)

# or:

n = int(input())
z = 0
for i in range(n):
    x = int(input())
    if i==0:
        s = x
        continue
    if x!=s:
        z+=1
    s = x
print(z)

# or:

n = int(input())
z = 0
l = []
for i in range(n):
    l.append(int(input()))
    if i==0:
        continue
    if l[i]!=l[i-1]:
        z+=1
print(z)

###############################################

"yaftane nafare dovvom daneshjoye bartar az lahaze moaddel"

n = int(input())
max1 = max2 = 0
for i in range(n):
    s, m = map(float, input().split())
    if i==0:
        max1, id1 = m, s
    else:
        if m>max1:
            max1, max2 = m, max1
            id1, id2 = s, id1
        elif m>max2:
            max2, id2 = m, s
     
print(f'dovvomin daneshjoye bartar: {int(id2)} ba moaddele {max2}.')

###############################################

"chape n ozve avval az dnbale fibonachi"

n = int(input())
a = b = 1
print(a, b, end=' ')
for i in range(2, n):
    print(a+b, end=' ')
    a, b = b, a+b

# use list:

n = int(input())
l = [1, 1]
for i in range(n-2):
    l.append(l[i]+l[i+1])
print(*l)

###############################################

"max 3 number"

a, b, c = map(int, input().split())
x = a if a>b else b
x = c if c>x else x
print(x)

# use function

def max2(x, y):
    return x if x>y else y
def max3(a, b, c):
    return max2(a, max2(b, c))
print(max3(8, 20, 5))

###############################################

"sort 3 number"

a, b, c = map(int, input().split())
if a<b:
    a, b = b, a
if c>=a:
    a, b, c = c, a, b
elif c>b:
    b, c = c, b
print(a, b, c)

###############################################

"majmooe 10 jomle avvale donbale: 1/(x) - 1/(x+2x^2) + 1/(x+2x^2+3x^3) - 1/(x+2x^2+3x^3+4x^4) ..."

x = int(input())
s = 0
for i in range(1, 11):
    m = 0
    for j in range(1, i+1):
        m += j*x**j
    s += (-1)**(i+1)*1/m
print(s)

# one loop

sum1 = sum2 = 0
for i in range(1, 11):
    sum2 += i*x**i
    sum1 += (-1)**(i+1)*1/sum2
print(s)

###############################################

a = '234'
s = sum(list(map(int, list(a))))
print(s)  # 9













