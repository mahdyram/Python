"""
Condition and Iteration
"""
################################################
################################################
# Condition 

# if

a = -7
if a<0:
    print(a)      # -7
    a = abs(a)
print(a)          # 7  

#---------------

a = -7
if True:
    print(a)      # -7
    a = abs(a)
print(a)          # 7 

#---------------          

a = -7
if 1:
    print(a)      # -7
    a = abs(a)
print(a)          # 7 

#---------------

a = -7
if None:
    print(a)     
    a = abs(a)
print(a)          # -7 

#---------------

a = -7
if a<0: print(a); a=abs(a)   # -7
print(a)                     # 7

################

x = 3
y = 1
if x == 1 or y == 1:
    print(f'{x}**{y} = {x}')  # 3**1 = 3
    print(f'{y}**{x} = {y}')  # 1**3 = 1

# or:
    
x = 3
y = 1
if 1 in (x, y):
    print(f'{x}**{y} = {x}')  # 3**1 = 3
    print(f'{y}**{x} = {y}')  # 1**3 = 1
    
#---------------
    
v ='mardood'
score = 15.5
if score >= 10 and score <= 20:
    v = 'ghabool'
print(v)                    # ghabool

# or:

v ='mardood'
score = 8.5
if 10 <= score <= 20:
    v = 'ghabool'
print(v)                    # mardood

# or:
    
v ='mardood'
score = 13.5
if int(score) in range(10, 20) or score==20:
    v = 'ghabool'
print(v)                    # ghabool

################################################
# if else

a = 20
if a % 2 == 0:
    print('evevn')             # even
else:
    print('odd')
    
# or:  
    
a = 21
if a % 2 == 0: print('evevn')                 
else: print('odd')             # odd

#---------------

names = ['sara', 'taha', 'farshid']
if 'ali' in names:
    print('found')
else:
    print('not found')         # not found
    
################

l = ['a','e','o','i','u']
if 'o' in l:
    s = 'yes'
else: 
    s = 'no'
print(s)                        # yes

# or:
    
l = ['a','e','o','i','u']
s = 'yes' if 'w' in l else 'no'
print(s)                        # no 

#---------------

a = 2
b = 5
if a > b:
    mx, mn = a, b
else: 
    mx, mn = b, a
print(f'max is {mx} and min is {mn}')  # max is 5 and min is 2

# or:
    
a, b = 2, 5
mx, mn = (a, b) if a > b else (b, a)   
print(f'max is {mx} and min is {mn}')  # max is 5 and min is 2

#---------------

grade = 12
s = 'fail' if grade < 10 else 'pass'
print(s)            # pass

#---------------

x = 11
if x>0:
    if x%2==0:
        print('+zoj')
    else:
        print('+fard')                                        # +fard  
else:
    print('manfi')

# or:

x = 11
if x>0:
    print('+zoj' if x%2==0 else '+fard')                      # +fard  
else:
    print('manfi')

# or:

x = 11
print(('+zoj' if x%2==0 else '+fard') if x>0 else 'manfi')    # +fard  
print('+zoj' if x%2==0 else '+fard' if x>0 else 'manfi')      # +fard 

#---------------

n = 5
for i in range(1, 2*n):
    if i <= n:
        print(i*'* ')
    else:
        print((2*n-i)*'* ')

# or:

n = 5
for i in range(1, 2*n): 
    print(i*'* ') if i <= n else print((2*n-i)*'* ') 

################

today = 'holiday'
income = 25000

if today == 'holiday':
   if income > 20000:
       print('shopping')        # shopping
   else:
       print('watch TV')
else:
    print('normal working day')

################################################
# elif (else + if)

score = 75

if score >= 90:
    l = 'A'
else:
  if score >= 80 :
      l = 'B'
  else:
       if score>= 70:
           l = 'C'
       else :
           l = 'D'
print(l)            # C     

# or:   
    
score = 75

if score >= 90:
    l = 'A'
elif score >= 80:
    l = 'B'
elif score>= 70:
    l = 'C'
else:
    l = 'D'
print(l)            # C

#---------------

x = -4
y = 3

if x > 0 and y > 0:
    z = f'{x}*{y} > 0' 
elif x < 0 and y < 0:
    z = f'{x}*{y} > 0'  
elif x == 0 or y == 0:
    z = f'{x}*{y} = 0'                 
else:
    z = f'{x}*{y} < 0'
   
print(z)    # -4*3 < 0

#---------------

age = 47
gender ='M'

if age < 18:
    if gender == 'M':
        v = 'son'
    else:
        v = 'daughter'
elif 18 <= age < 65:
    if gender == 'M':
        v = 'father'
    else:
        v = 'mother'
else:
    if gender == 'M':
        v = 'grandfather'
    else:
        v = 'grandmother'
        
print(v)    # father
                                  
#or:
    
age = 47
gen = 'm'

if age < 18:
    v = 'son' if gen =='m' else 'daughter'
elif 18 <= age < 65:
    v = 'father' if gen =='m' else 'mother'
else:
    v = 'grandfather' if gen =='m' else 'grandmother'
    
print(v)    # father

################
"agar dastoore if ejra shavad, digar soraghe elife\
 nemiravad hatta agar sharte elife dorost bashad."

a = 70
if a>10:
    print('a')     # a
elif a>20:
    print('b')

#---------------
    
a = 70
if a>10:
    print('a')     # a
if a>20:
    print('b')     # b

################################################
################################################
# Iteration

# for

for i in range(5):
    print(i)                              # 0/1/2/3/4
  
# or:
    
for i in range(5):
    print(i, end=' ')                     # 0 1 2 3 4
  
# or:    
    
for i in range(5): print(i, end=' ')      # 0 1 2 3 4  

# or: 
    
x = [i for i in range(5)]
print(x, type(x))                         # [0, 1, 2, 3, 4] <class 'list'>

for i in x: print(i, end='')              # 01234

#---------------

x = [j for j in range(5,10,2)]
print(x)                                  # [5, 7, 9]  

#---------------

x = [i for i in range(9,2,-3)]
print(x)                                  # [9, 6, 3]

#---------------

x = [i for i in range(9,2,-3) if i%2!=0]
print(x)                                  # [9, 3]

################

x = 0
a = [1, 2, 3]
b = [10, 20, 30]
for i in range(3):
    x+=a[i]*b[i]
print(x)                                    # 140

# or:

a = [1, 2, 3]
b = [10, 20, 30]
print(sum([a[i]*b[i] for i in range(3)]))   # 140

#---------------

l = []
n = int(input())
for i in range(n):
    l.append(int(input()))

# or:

l = [int(input()) for _ in range(int(input()))]

################

name = 'farshid'
for i in name:
    print(i, end=' ')        # f a r s h i d
    
# or:
    
name = 'farshid'
a = [i for i in name] 
print(a)                     # ['f', 'a', 'r', 's', 'h', 'i', 'd']

#---------------

n = 'mahdi'
s = ''
for i in n:
    s = i+s    
print(s)                              # idham

# or:  
    
n = 'mahdi'
s = ''
for i in n[::-1]:
    s += i
print(s)                              # idham

# or:
    
n = 'mahdi'
for i in n[::-1]:
    print(i, end='')                  # idham

# or:
    
n = 'mahdi'
for i in range(len(n)):
    print(n[len(n)-1-i], end='')      # idham
    
# or:
    
n = 'mahdi'
for i in range(len(n)-1, -1, -1):
    print(n[i], end='')               # idham

#---------------

name = 'amin'
s = ''
for i in name:
    s += i+'.'    
print(s)                     # a.m.i.n.

# or:
    
name = 'amin'
s = ''
for i in name:
    s = i+'.'+s    
print(s)                     # n.i.m.a.

#--------------- 
     
name = 'python'    
c = 0 
for i in name:
    c += 1
    
print(c)                     # 6
print(len(name))             # 6

#---------------

s = 'alireza'    
c = 0 
for i in s:
    if i =='a': c+=1
    
print(c)                     # 2
print(list(s).count('a'))    # 2
 
#---------------   

name = 'farshid'
v = 'a,e,i,o,u'
c = 0
for i in name:
    if i in  v:
        print(i, end=' ')        # a i 
        c += 1
print(c)                         # 2

# or:  
    
name = 'farshid'
v = 'a,e,i,o,u'
l = [i for i in name if i in v]
print(l)                         # ['a', 'i']

#--------------- 

name = 'mahdyram'
s = ''
for i in name:
    s += i+' '
    print(s)

#--------------- 

mx = 0
for i in range(4):
    a = int(input())
    if a > mx:
        mx = a
print(mx) 

################ 
"hafeze dar halghe for"

name = 'ali'
for i in name:
    print(i, end=' ')        # a l i 
print(i)                     # i 

# or:
    
l = ['fateme', 'asma', 'ali']
for x in l:
    print(x, end=' ')   # fateme asma ali
print(x)                # ali

################  
"for too-dar-too"   

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=' ')
    print()
'''
1 2 3 
1 2 3 
1 2 3
''' 
#---------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, end=' ')
    print()
'''
1 1 1 
2 2 2 
3 3 3 
''' 
#---------------

for i in range(1, 4):
    for j in range(i):
        print(j, end=' ')
    print()
'''
0 
0 1 
0 1 2 
'''
#---------------

for i in range(1, 4):
    for j in range(i):
        print(i, end=' ')
    print()
'''
1 
2 2 
3 3 3 
'''

################ 
"break"

for i in range(6):
    if i == 3 :
        break
    else:
        print(i, end=' ')    # 0 1 2 
        
# or:
    
for i in range(6):
    if i == 3:
        break
    print(i, end=' ')        # 0 1 2
    
# or:    
    
for i in range(6):
    print(i, end=' ')        # 0 1 2 3
    if i == 3:
        break

################
"continue"   

for i in range(6):
    if i == 3:
        continue
    else:
        print(i, end=' ')    # 0 1 2 4 5
        
# or:
    
for i in range(6):
    if i == 3:
        continue
    print(i, end=' ')        # 0 1 2 4 5
    
# or:
    
for i in range(6):
    print(i, end=' ')        # 0 1 2 3 4 5
    if i==3:
        continue 

################################################
# while
      
i = 1      
while i <= 3:
    print(i, end=' ')     # 1 2 3
    i += 1  
   
#---------------

n = 7
while n != 3:
    print(n, end=' ')    # 7 6 5 4 
    n -= 1
    
# or:
    
n = 7
while n != 3:
    n -= 1
    print(n, end=' ')    # 6 5 4 3  
        
#---------------

s = 'asma@gmail'
i = 0
while s[i] != '@' :
   print(s[i], end='')    # asma
   i += 1

# or:

s = 'asma@gmail'
i = 0
while True:
   if s[i] == '@' :
       break
   print(s[i], end='')    # asma
   i += 1

# or:
    
s = 'asma@gmail'
for i in range(len(s)):
    if s[i] == '@' :
        break
    print(s[i], end='')   # asma
    
# or:
    
s = 'asma@gmail'
for i in s:
    if i == '@' :
        break
    print(i, end='')      # asma
    
#---------------

a = 5
while a>0:
    print(a, end=' ')    # 5 4 3 2 1 
    a -= 1

# or:
    
a = 5
while True:
    print(a, end=' ')    # 5 4 3 2 1 
    a -= 1
    if a<=0:
        break
    
# or:
    
a = 5
v = True
while v:
    print(a, end=' ')    # 5 4 3 2 1 
    a -= 1
    if a<=0:
        v = False

#---------------

x = 41
a = x//2
v = 'aval'
while a > 1:
    if x%a == 0:
        v = 'gh-aval'
        break
    else:
        a -= 1
print(v)

# or:
    
x = 41 
v = 'aval'
for i in range(2, x//2+1):
    if x%i == 0:
        v = 'gh-aval'
        break
print(v)

#---------------

n = 3957
mx = 0
while n > 0:
    if n%10 > mx:
        mx = n%10
    n //= 10
print(mx)             # 9      

# or:

n = 3957
mx = 0
for i in range(len(str(n))):
    if n%10 > mx:
        mx = n%10
    n //= 10
print(mx)             # 9

# or:

n = 3957
mx = 0
for i in str(n):
    if int(i) > mx:
        mx = int(i)
print(mx)             # 9

################
'hengame estefade az halghe for dar list ya..., bayad moraghebe\
 nokte zir dar peymayesh dar list va index ha bashim.\
 dalile in moshkel: for bar rooye indexe statice aza\
 kar mikonad darhali ke while har bar list morede nazar\
 ra bar asase akharin vaziatash chek mikonad.'

x = ['a', 'b', 'c', 'd', 'e', 'f']
for i in x:
    x.pop()
print(x)          # ['a', 'b', 'c']

# or:
    
x = ['a', 'b', 'c', 'd', 'e', 'f']
for i in x:
    x.remove(i)
print(x)          # ['b', 'd', 'f']

#---------------
'baraye halle in moshkel 2 rah vojood darad, yeki taghire\
 for be shekle zir'
    
x = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(x)
for i in range(n):
    x.pop()
print(x)          # []

# or:
    
x = ['a', 'b', 'c', 'd', 'e', 'f']
y = []
n = len(x)
for i in range(n):
    y.append(x.pop())
print(x)   # []
print(y)   # ['f', 'e', 'd', 'c', 'b', 'a']

# or:
    
x = ['a', 'b', 'c', 'd', 'e', 'f']
y = []
n = len(x)
for i in range(n):
    y.append(x.pop(0))
print(x)   # []
print(y)   # ['a', 'b', 'c', 'd', 'e', 'f']

#---------------
'rahe digar estefade az while be jaye for'

print(bool([]))     # False
print(bool(['a']))  # True

x = ['a', 'b', 'c', 'd', 'e', 'f']
while x:
    x.pop()
print(l)            # []

# or:
    
x = ['a', 'b', 'c', 'd', 'e', 'f']
y = []
while x:
    y.append(x.pop())
    
print(x)                  # []
print(y)                  # ['f', 'e', 'd', 'c', 'b', 'a']
print(list(reversed(y)))  # ['a', 'b', 'c', 'd', 'e', 'f']

    












