"""
List & Tuple
"""
################################################
################################################
# list[]

'list manande reshte az donbale e az maghadir tashkil\
 mishavad amma barkhalafe reshte, taghiir pazir ast'

l = []
print(l, type(l))      # [] <class 'list'> 

l = [5]
print(l)               # [5]

l = ['5']
print(l)               # ['5'] 

l = [5,'7']
print(l)               # [5, '7']

l = [5,'7',[1,2],True]
print(l)               # [5, '7', [1, 2],True]

################

l = []
print(l, type(l))    # [] <class 'list'>

# or:
l = list()
print(l, type(l))    # [] <class 'list'>

l = list([])
print(l, type(l))    # [] <class 'list'>

l = list([5,'5'])
print(l)             # [5, '5']

################

a, b, c = [2, 5, 1]
print(a)            # 2
print(b)            # 5
print(c)            # 1

# or:
l = [2, 5, 1]
a, b, c = l
print(a)            # 2
print(b)            # 5
print(c)            # 1

################

a = [1, 2]
b = [2, 1]
print(a == b)        # False 
print(a is b)        # False

################

s = 'ali.ram.ir'
print(s.split('.'))  # ['ali', 'ram', 'ir']
l = s.split('.')
print(l)             # ['ali', 'ram', 'ir']

################

friends = ['ali','sara','taha']
for f in friends:
    print(f, end=' ')            # ali sara taha

# or:
for i in range(3):
    print(friends[i], end=' ')   # ali sara taha
    
# or:
print(*friends)                  # ali sara taha

################
" *list "

l = [2, 5, 's']
print(*l)                        # 2 5 s

#---------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(combined)

#---------------

def f(a, b, c): 
    print(a, b, c)
    
f(2, 5, 7)

# or:
args = [2, 5, 7]
f(*args)

#---------------

a, b, c, d = [2, 3, 4, 5]
print(a)

# or:
first, *rest = [2, 3, 4, 5]
print(first)  # 2
print(rest)   # [3, 4, 5]
    
################
    
print([7, 8, 9] + [7, 8, 9])  # [7, 8, 9, 7, 8, 9]
print([7, 8, 9] * 2)          # [7, 8, 9, 7, 8, 9]

# but:
l = [7, 8, 9]
for i in range(len(l)):
    l[i] *= 2
print(l)                      # [14, 16, 18]

################

l = [('ali',15), ('asma',17), ('fateme',19)]

for i in l:
    print(i) 
'''
('ali', 15)
('asma', 17)
('fateme', 19)
'''
    
for i,j in l:
    print(i, j)  
'''
ali 15
asma 17
fateme 19
'''
    
for i,j in l:
    print(j,end=' ')   
'15 17 19 '

################
"hazfe ozv haye tekrari"

l = ['a', 'b', 'c', 'c', 'e', 'a']
x = []
for i in l:
    if i not in x:
        x.append(i)
print(x)             # ['a', 'b', 'c', 'e']

# or:
l = ['a', 'b', 'c', 'c', 'e', 'a']
l = list(set(l))
print(l)             # ['c', 'a', 'e', 'b']
l.sort()
print(l)             # ['a', 'b', 'c', 'e']

################
"enumerate(index, vlue)"

l = ['ali', 'asma', 'fateme']

print(list(enumerate(l)))     # [(0, 'ali'), (1, 'asma'), (2, 'fateme')]

for i,v in enumerate(l):
    print(i,v)
'''
0 ali
1 asma
2 fateme
'''

################
"namayeshe motanazere azaye 2 list"

a = [1, 2, 3]
b = ['one', 'two', 'three']
for i in range(len(a)):
    print(a[i],b[i])
'''
1 one
2 two
3 three
'''
#--------------- 

a = [1, 2, 3]
b = ['one', 'two', 'three']
for i,v in enumerate(a):
    print(v,b[i])
'''
1 one
2 two
3 three
'''
#---------------
 
a = [1, 2, 3]
b = ['one', 'two', 'three']
for i,j in zip(a,b):
    print(i,j)
'''
1 one
2 two
3 three
'''

################

l = [6,7,8]
print(max(l))     # 8
print(min(l))     # 6
print(sum(l))     # 21
print(len(l))     # 3

################
"del"

l = [1,2,3,4,5]
print(l)          # [1, 2, 3, 4, 5]
del l[3]
print(l)          # [1, 2, 3, 5] 

l = [1,2,3,4,5]
del l[2:4]
print(l)          # [1, 2, 5] 

l = [1,2,3,4,5]
del l[2:10]
print(l)          # [1, 2] 

l = [1,2,3,4,5]
del l[:]
print(l)          # [] 

l = [1,2,3,4,5]
del l
#print(l)         # NameError: name 'l' is not defined

################################################
# Zip

"zip"

a = [1, 2]
b = ['a', 'b']

print(zip(a, b))          # <zip object at 0x000001D376C13C80> 
print(list(zip(a, b)))    # [(1, 'a'), (2, 'b')]

# or:
x, y = zip(a, b)
print(x)               # (1, 'a')
print(y)               # (2, 'b')

# or:
for i,j in zip(a, b):
    print(i, j)
'''
1 a
2 b
'''
#---------------

a = [1, 2]
b = ['a', 'b']

z = zip(a, b)
print(z)                # <zip object at 0x0000017A8D6368C0>
print(list(z))          # [(1, 'a'), (2, 'b')]
print(list(z))          # []
print(z)                # <zip object at 0x0000017A8D6368C0>
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]

z = zip(a, b)
print(list(z))       # [(1, 'a'), (2, 'b')]
print(list(z))       # []
# x, y = z           # ValueError: not enough values to unpack (expected 2, got 0)

z = zip(a, b)
x, y = z
print(x, y)        # (1, 'a') (2, 'b')
print(list(z))     # []
# x, y = z         # ValueError: not enough values to unpack (expected 2, got 0)

#---------------

a = [1, 2, 3]
b = [-1, -2, -3]
c = ['a', 'b', 'c']
z = zip(a, b, c)
print(list(z))         # [(1, -1, 'a'), (2, -2, 'b'), (3, -3, 'c')]
print(list(z))         # []

# or:
z = zip(a, b, c)
x, y, w = z
print(x)               # (1, -1, 'a')
print(y)               # (2, -2, 'b')
print(w)               # (3, -3, 'c')

# or:
z = zip(a, b, c)
for i,j,k in z:
    print(i, j, k)
'''
1 -1 a
2 -2 b
3 -3 c
'''

################
"unzip"

l = [(1, 'a'), (2, 'b')]
a, b = l
print(a)                # (1, 'a')
print(b)                # (2, 'b')

print(*l)               # (1, 'a') (2, 'b')
print(zip(*l))          # <zip object at 0x0000017A8D336840>
print(list(zip(*l)))    # [(1, 2), ('a', 'b')]

# or:
a, b = zip(*l)
print(a)                # (1, 2)
print(b)                # ('a', 'b')

# or:
for i,j in zip(*l):
    print(i,j)
'''
1 2
a b
'''
#---------------

l = [(1, -1, 'a'), (2, -2, 'b'), (3, -3, 'c')]
u = zip(*l)
print(u)            # <zip object at 0x0000017A8D336B40>

u = zip(*l)
print(list(u))      # [(1, 2, 3), (-1, -2, -3), ('a', 'b', 'c')]
print(list(u))      # []

# or:
u = zip(*l)
a, b, c = u
print(a)            # (1, 2, 3)
print(b)            # (-1, -2, -3)
print(c)            # ('a', 'b', 'c')

# or:
u = zip(*l)
for i,j,k in u:
    print(i,j,k)
'''
1 2 3
-1 -2 -3
a b c
'''

################################################
# slice & Index

l = [5,'7',[3,'a'],True]

print(l[0])              # 5 
print(l[0:1])            # [5]

print(l[2])              # [3,'a']
print(l[2][1])           # a
print(l[2:3])            # [[3,'a']]
print(l[2:3][0])         # [3,'a']
print(l[2:3][0][1])      # a

print(l[1:3])            # ['7', [3,'a']] 

print(l[:])              # [5, '7', [3,'a'], True]

print(l[::-1])           # [True, [3, 'a'], '7', 5]

#---------------

a = [1, 2, 'a', [[4, 'b'], 6, 7], 3]

print(a[-2])          # [[4, 'b'], 6, 7]
print(a[-2][0])       # [4, 'b']
print(a[-2][0:2])     # [[4, 'b'], 6]
print(a[-2][0][-1])   # b

a[-2][0][-1] = 'c'
print(a[-2][0])       # [4, 'c']

################
"taghire aza"

l = [6,7,8,'9']

print(l)           # [6, 7, 8, '9']
print(l[2])        # 8

l[2] = 10
print(l)           # [6, 7, 10, '9']  

l[3] = 'ali'
print(l)           # [6, 7, 10, 'ali']

l[2:4] = 8,'ram'
print(l)           # [6, 7, 8, 'ram'] 

# but:
s = 'sara'
print(s[1])        # a
# s[1] = 'd'       # string is immutable

#---------------

l = [-1, 2, 'a', 5, 3]
l[1:4] = 0, 1, 2
print(l)              # [-1, 0, 1, 2, 3]

# or:
l = [-1, 2, 'a', 5, 3]
l[1:4] = [0, 1, 2]
print(l)              # [-1, 0, 1, 2, 3]

# or:
l = [-1, 2, 'a', 5, 3]
l[1:4] = {0, 1, 2}
print(l)              # [-1, 0, 1, 2, 3]

# or:
l = [-1, 2, 'a', 5, 3]
l[1:4] = range(3)
print(l)              # [-1, 0, 1, 2, 3]

#---------------

l = [1, 2, 'a', 5, 7]
l[1:4] = 20, 'A', 50
print(l)                # [1, 20, 'A', 50, 7]

# or:
l = [1, 2, 'a', 5, 7]
x, y, z = 20, 'A', 50
l[1:4] = x, y, z
print(l)                # [1, 20, 'A', 50, 7]

# or:
l = [1, 20, 'A', 50, 7]
x, y, z = l[1:4]
print(x)                # 20 
print(y)                # A
print(z)                # 50

################################################
# amalgar haye List

"+"

l1 = [1,2]
l2 = [3,'4']
l = l1 + l2
print(l)        # [1, 2, 3, '4']

################
"*"

l = [7,'ali']
print(l*3)      # [7, 'ali', 7, 'ali', 7, 'ali']

################
"=="

l1 = [7,'ali']
l2 = [7,'ali']
b = l1 == l2
print(b)          # True


l1 = [7,'ali']
l2 = [7,'Ali']
print(l1 == l2)   # False

################
"is"
'har sheie dar python shamele shenase(Identity), noe(Type), meghdar(Value) ast.\
 amalgare is, 2 sheie ra az lahaze yeksan boodane har 3 in ha barresi mikonad,\
 dar hali ke amalgare ==, 2 sheie re dar yeksan boodane Type va Value moghayese mikonad.'

l = [1, 2]
x = l
print(l == x)     # True
print(l is x)     # True
print(l is not x) # False
print(id(l))
print(id(x))


l = [1, 2]
x = l[:]
print(l == x)     # True
print(l is x)     # False
print(id(l))
print(id(x))

################
"in"

l = [1,2,'3',[4,5],True]

print(3 in l)            # False 
print(3 not in l)        # True 

print([1,2] in l)        # False

print([4,5] in l)        # True 

print(True in l)         # True

################################################
# metod haye List

"append(o)"
'sheie o ra be entehaye list ezafe mikonad'

l = [1,2,'3']
print(l)         # [1, 2, '3']
l += [4]
print(l)         # [1, 2, '3', 4]

# or:
l = [1,2,'3']
l.append(4)
print(l)         # [1, 2, '3', 4]
l.append('5')
print(l)         # [1, 2, '3', 4, '5']
# l.append(6,7)  # error

#---------------

l1 = [1, 2]
l2 = [3, 'ali']
l1 += [l2]
print(l1)        # [1, 2, [3, 'ali']]

# or:
l1 = [1,2]
l2 = [3,'ali']
l1.append(l2)
print(l1)        # [1, 2, [3, 'ali']]

################
"extend(i)"
'azaye sheie i ra be entehaye list ezafe mikonad'

l = [2, 3]
print(l)           # [2, 3]

# l.extend(4)      # error

l.extend('ali')
print(l)           # [2, 3, 'a', 'l', 'i']

l.extend((4,'ali'))  
print(l)           # [2, 3, 'a', 'l', 'i', 4, 'ali']

l.extend([5,'ram'])
print(l)           # [2, 3, 'a', 'l', 'i', 4, 'ali', 5, 'ram']

l.extend({6,'.'})
print(l)           # [2, 3, 'a', 'l', 'i', 4, 'ali', 5, 'ram', '.', 6]

#---------------

l1 = [1, 2]
l2 = [3, 'ali']
l1 = l1 + l2
print(l1)        # [1, 2, 3, 'ali']

# or:
l1 = [1,2]
l2 = [3,'ali']
l1.extend(l2)
print(l1)        # [1, 2, 3, 'ali']

#---------------

l = [1, 2, 3]

a = []
a.append(l)
print(a)      # [[1, 2, 3]] 

b = []
b.extend(l)
print(b)      # [1, 2, 3]

# or:
l = [1, 2, 3]
a, b = [], []
a += [l]
print(a)      # [[1, 2, 3]] 
b += l
print(b)      # [1, 2, 3]

################
"insert(i, o)"
'ozve jadide o ra dar makane i dar list darj mikonad'

l = [1, 2, '3']
print(l)             # [1, 2, '3']

l.insert(1, 1.5)
print(l)             # [1, 1.5, 2, '3']

l.insert(4, '4')
print(l)             # [1, 1.5, 2, '3', '4']

l.insert(5, (5, '6'))
print(l)             # [1, 1.5, 2, '3', '4', (5, '6')]

l.insert(3, [2.5])
print(l)             # [1, 1.5, 2, [2.5], '3', '4', (5, '6')]

################
"remove(v)"
'avvalin voghooe v dar list ra hazf mikonad'

l = [1,2,'3',4,2]
print(l)          # [1, 2, '3', 4, 2]

l.remove(2)
print(l)          # [1, '3', 4, 2]

l.remove('3')
print(l)          # [1, 4, 2]   

# l.remove(5)     # ValueError: list.remove(x): x not in list

################
"pop(i)"
'ozv ba index i ra hazf mikonad va barmigardanad'

l = ['1','2','3','4']
l.pop(2)
print(l)              # ['1', '2', '4']

#or:
l = ['1','2','3','4']
print(l.pop(2))       # 3
print(l)              # ['1', '2', '4']

#or:
l = ['1','2','3','4']
x = l.pop(2) 
print(x)              # 3
print(l)              # ['1', '2', '4']


l = ['1','2','3','4']
print(l.pop())        # 4 : hazfe akharin ozv
print(l)              # ['1', '2', '3']

################
"index(v, n)"
'makane n-omin voghooe v dar list ra barmigardanad'

l = ['1','2','3','4','2']

print(l.index('4'))          # 3 
print(l.index('2'))          # 1 
print(l.index('2', 1))       # 1
print(l.index('2', 2))       # 4 
# print(l.index(7))          # 7 is not in list

################
"count(v)"

l = [1,2,3,'4',2]

print(l.count(2))     # 2
print(l.count('4'))   # 1 

################
"clear()"

l = [1,2,'3']
print(l)         # [1, 2, '3']
l.clear()
print(l)         # []

# or:
l = [1,2,'3']
print(l)         # [1, 2, '3']
del l[:]
print(l)         # []

################
"reverse()"

l = [1,2,'3',4]
print(l)         # [1, 2, '3',4]
l.reverse()
print(l)         # [4, '3', 2, 1]

#---------------

l = [1,2,'3',4]
print(list(reversed(l)))   # [4, '3', 2, 1]
print(l)                   # [1, 2, '3',4]

################
"sort()"

l = [0, -7, 4, 9, 2]
l.sort()
print(l)               # [-7, 0, 2, 4, 9]

l = [0, -7, 4, 9, 2]
l.sort(reverse=False)
print(l)               # [-7, 0, 2, 4, 9]

l = [0, -7, 4, 9, 2]
l.sort(reverse=True)
print(l)               # [9, 4, 2, 0, -7]

#---------------

l = ['a', 'b', 'c', 'z']
l.sort()
print(l)                   # ['a', 'b', 'c', 'z']

l = ['a', 'b', 'c', 'Z']
l.sort()
print(l)                   # ['Z', 'a', 'b', 'c']

l = ['a', 'b', 'c', 'Z']
l.sort(key=str.lower)
print(l)                   # ['a', 'b', 'c', 'Z'] 

################
"copy"
'zamani taghir dar liste l mojebe taghir dar liste\
 x mishavad ke ebarate (x is l) True bashad. dar in halat,\
 x va l har do be yek shei eshare mikonand.(serfan list)'

x = 2
y = x
print(x == y)     # True   
print(x is y)     # True
y += 1
print(x)          # 2
print(y)          # 3

# but:
x = [3, 4]
y = x
print(x == y)     # True   
print(x is y)     # True
y.append(5)
print(x)          # [3, 4, 5]
print(y)          # [3, 4, 5]

#---------------

l = ['a', 'b', 'c']
x = l
print(x == l)        # True   
print(x is l)        # True
l.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b'] 

# or:
l = ['a', 'b', 'c']
x = l
x.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b'] 

#---------------

l = ['a', 'b', 'c']
x = l.copy()
print(x == l)        # True   
print(x is l)        # False
l.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b', 'c']

# or:
l = ['a', 'b', 'c']
x = l[:]
print(x == l)        # True   
print(x is l)        # False
l.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b', 'c']

# or:
l = ['a', 'b', 'c']
x = list(l)
print(x == l)        # True   
print(x is l)        # False
l.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b', 'c']

# or:
l = ['a', 'b', 'c']
x = [i for i in l]
print(x == l)        # True   
print(x is l)        # False
l.pop()
print(l)             # ['a', 'b'] 
print(x)             # ['a', 'b', 'c']

#---------------

x = 5
a = b = []
print(a == b)     # True   
print(a is b)     # True
a.append(x)
print(a)          # [5] 
print(b)          # [5] 

# but:
x = 5
a, b = [], []
print(a == b)     # True   
print(a is b)     # False
a.append(x)
print(a)          # [5] 
print(b)          # [] 

################################################
# List saz

a = []
for i in range(5):
    a.append(i)
print(a)                              # [0, 1, 2, 3]

# or:
l = [i for i in range(5)]
print(l)                              # [0, 1, 2, 3, 4]

l = [i*3 for i in range(5)]
print(l)                              # [0, 3, 6, 9, 12]

l = [i*i for i in range(5)]
print(l)                              # [0, 1, 4, 9, 16]

l = [abs(i) for i in range(-3,3)]
print(l)                              # [3, 2, 1, 0, 1, 2]

l = [i for i in range(5) if i%2!=0]
print(l)                              # [1, 3]

l = [i for i in range(5) if i%2!=0]
print(l)                              # [1, 3]

#---------------

x = [1,2,'3']
l = [i for i in x]
print(l)                       # [1, 2, '3']
 
x = [1,2,'3']
l = [i*2 for i in x]
print(l)                       # [2, 4, '33'] 

x = [1,2,'3']
l = [i for i in x if i!=2]
print(l)                       # [1, '3']

#---------------

x=['a','b','c']
l=[i.upper() for i in x ]
print(l)                       # ['A', 'B', 'C']

#---------------

x = [i for i in range(5)]
l=[i**3 for i in x if i%2==0]
print(x)                       # [0, 1, 2, 3, 4]
print(l)                       # [0, 8, 64]

#---------------

x = [1,2,3]
y = ['a','b','c']
l = []  
for i in x:
    for j in y:
        l.append(i*j)
print(l)
# ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']


# or:
x = [1,2,3]
y = ['a','b','c']
l = [i*j for i in x for j in y]
print(l)     
# ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']

#---------------

x = [1,2,3]
y = ['a','b','c']
l = []  
for i in x:
    for j in y:
        if x.index(i)==y.index(j):
            l.append(i*j)
print(l)     # ['a', 'bb', 'ccc']


# or:
x = [1,2,3]
y = ['a','b','c']
l = [i*j for i in x for j in y if x.index(i)==y.index(j)]
print(l)     # ['a', 'bb', 'ccc']

################################################
# matrix

m  = [[1,2,3],
      [4,5,6],
      [7,8,9]]
print(m)                # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

################
"satr ha"

for i in m[0]:
    print(i, end=' ')   # 1 2 3
    
# or:
l = m[0]
print(l)                # [1, 2, 3]

################
"majmooe satr ha" 
  
for i in m:
    print(sum(i),end=' ')     # 6  15  24
    
# or:
l = [sum(i) for i in m]
print(l)                      # [6, 15, 24]
    
################   
"sotoone ha" 

for i in m:
    print(i[0],end=' ') # 1  4  7
    
# or:
l = [i[0] for i in m]
print(l)                # [1, 4, 7]

################
"majmooe sotoon ha"

l = []    
for i in range(3):
    s = 0
    for j in m:
        s += j[i]
    l.append(s)
print(l)                           # [12, 15, 18]

#---------------

for i in range(3):
    l = [j[i] for j in m]
    print(sum(l), end=' ')         # 12 15 18
    
# or:
x = []
for i in range(3):
    x.append(sum(j[i] for j in m))
print(x)                           # [12, 15, 18]
    
################
"ghotre asli"

x = 0
for i in m:
    print(i[x],end=' ')          # 1  5  9
    x += 1
    
#---------------

for i in range(3) :
    print(m[i][i], end=' ')      # 1  5  9
    
# or:
l = [m[i][i] for i in range(3)]
print(l)                         # [1, 5, 9]
    
################   
"ghotre faree"

x = len(m) - 1
for i in m:
    print(i[x], end=' ')          # 3  5  7
    x -= 1 
    
#---------------

for i in range(3):
    print(m[i][2-i],end=' ')      # 3  5  7
    
# or:
l = [m[i][2-i] for i in range(3)]
print(l)                          # [3, 5, 7]

################################################
# Array   

'majmooe beham peyvaste va motavali az khane\
 haye hafeze ke darbardarande anasori hamnoe ast.'
 
"array(typecode, [initializer])"

from array import array
 
a = array('i',[3,4,5])
print(a)                   # array('i', [3, 4, 5])
print(type(a))             # <class 'array.array'>
print(list(a))             # [3, 4, 5]
for i in a:
    print(i, end=' ')      # 3 4 5

#---------------

a = array('d',[3,4,5])
print(a)                   # array('d', [3.0, 4.0, 5.0])

#---------------

a = array('i')
print(a)                 # array('i')
print(list(a))           # []

#---------------

a = array('i',[5,6,7,8])
print(a[0])                 # 5 
a[3] = 9
print(a)                    # array('i', [5, 6, 7, 9])  

################

a = array('i',[1,2,3,4])
print(min(a))              # 1
print(max(a))              # 4
print(sum(a))              # 10
print(len(a))              # 4

################

a = array('i')
a.append(7)
print(a)                 # array('i', [7])
a.append(True)
print(a)                 # array('i', [7, 1])
a.append(False)
print(a)                 # array('i', [7, 1, 0])

#a.append(4, 5)          # TypeError: array.append() takes exactly one argument (2 given)
#a.append('a')           # TypeError: 'str' object cannot be interpreted as an integer
#a.append([4, 5])        # TypeError: 'list' object cannot be interpreted as an integer

#---------------

a = array('i',[1,2,3])        
a.extend([4, 5])
print(a)                      # array('i', [1, 2, 3, 4, 5])

#---------------

a = array('i',[1,2,3,1,2,1])
print(a.count(1))             # 3

#---------------

a = array('i',[1,2,3,1,2,1])
print(a.index(2))             # 1
print(a.index(2, 3))          # 4

#---------------

a = array('i',[10,20,30,40,50])
a.insert(3, 8)
print(a)                    # array('i', [10, 20, 30, 8, 40, 50])
a.insert(6, 8)
print(a)                    # array('i', [10, 20, 30, 8, 40, 50, 8])

#---------------

a = array('i',[1,2,3,1,2,1])
a.remove(2)
print(a)                    # array('i', [1, 3, 1, 2, 1])
a.remove(2)
print(a)                    # array('i', [1, 3, 1, 1])

#---------------
 
a = array('i',[1,2,3,1,2,1])
print(a.pop(2))             # 3.0
print(a)                    # array('d', [1.0, 2.0, 1.0, 2.0, 1.0])

#---------------

a = array('i',[1,2,3,4])
a.reverse()
print(a)                    # array('d', [4.0, 3.0, 2.0, 1.0])

#---------------

a = array('I',[1,2,3,4])
print(a.typecode)           # I
    
################################################
################################################ 
# tuple()
'tuple ha moshabeh list ha hastand, ba in\
 tafavot ke manande reshte ha taghiir napazirand'

t = ()
print(t, type(t))           # () <class 'tuple'>

#---------------

t = (5)
print(t, type(t))           # 5 <class 'int'>
t = 5
print(t, type(t))           # 5 <class 'int'>

t = 5,
print(t, type(t))           # (5,) <class 'tuple'>
t = (5,)
print(t, type(t))           # (5,) <class 'tuple'>

t = ('73')
print(t, type(t))           # 73 <class 'str'>
t = '73',
print(t, type(t))           # ('73',) <class 'tuple'>
t = ('73',)
print(t, type(t))           # ('73',) <class 'tuple'>

#---------------

t = (5,'73', 0)
print(t, type(t))           # (5, '73', 0) <class 'tuple'>

t = 5, '73', 0
print(t, type(t))           # (5, '73') <class 'tuple'>

#---------------

t = (5,'73',[1,2],(3,4),True)
print(t, type(t))           # (5, '73', [1, 2], (3, 4), True) <class 'tuple'>

################

t = ()
print(t, type(t))    # () <class 'tuple'>

# or:
t = tuple()
print(t, type(t))    # () <class 'tuple'>

#---------------

# t = tuple(5)       # 'int' object is not iterable
t = tuple('7')          
print(t)             # ('7',)
t = tuple('741')          
print(t)             # ('7', '4', '1')
print(tuple('ali'))  # ('a', 'l', 'i')

# t = tuple((5))     # 'int' object is not iterable
t = tuple((5,))    
print(t)             # (5,)
t = tuple([5])          
print(t)             # (5,)
t = tuple({5})          
print(t)             # (5,)

#---------------

t = tuple([5,7,'9'])          
print(t)                # (5, 7, '9')

t = tuple((5,7,'9'))          
print(t)                # (5, 7, '9')

#---------------

t = tuple(range(4))
print(t)                # (0, 1, 2, 3)

################

a, b, c = 2, 5, 1
print(a)            # 2
print(b)            # 5
print(c)            # 1

# or:
a, b, c = (2, 5, 1)
print(a)            # 2
print(b)            # 5
print(c)            # 1

# or:
t = (2, 5, 1)
a, b, c = t
print(a)            # 2
print(b)            # 5
print(c)            # 1

#---------------

# a, b, c = (3, 4, 6, 7, 8)    # ValueError: too many values to unpack (expected 3)
a, b, *c = (3, 4, 6, 7, 8)
print(a)                       # 3
print(b)                       # 4
print(c)                       # [6, 7, 8]

a, *b, c = (3, 4, 6, 7, 8)
print(a)                       # 3
print(b)                       # [4, 6, 7]
print(c)                       # 8

#---------------

s = 'ali'
t = tuple(s)
print(t)
a, b, c = s
print(a)       # a
print(b)       # l
print(c)       # i  

# or:
a, b, c = tuple('ali')
print(a)               # a
print(b)               # l
print(c)               # i  

#---------------

a, b, c = tuple(range(3,10,3))
print(a)                       # 3
print(b)                       # 6
print(c)                       # 9  
 
################
  
a = (1, 2)
b = (2, 1)
print(a == b)        # False 
print(a is b)        # False

################
"enumerate(index, vlue)"

t = ('ali', 'asma')

print(list(enumerate(t)))   # [(0, 'ali'), (1, 'asma')]

for i,v in enumerate(t):
    print(i,v)
'''
0 ali
1 asma
'''

################

t = (5,'7',[3,'a'],True)

print(t[0])            # 5 
print(t[0:1])          # (5,)
print(t[2])            # [3,'a']
print(t[2][:])         # [3,'a']
print(t[2][0])         # 3
print(t[2][0:1])       # [3]
print(t[2:3])          # ([3,'a'],)
print(t[::-1])         # (True, [3, 'a'], '7', 5)

print(t[0])            # 5
# t[0] = 10            # 'tuple' object does not support item assignment

################
"tuple saz"

l = [1, 3, 5]
t = (i for i in l)
print(t)                  # <generator object <genexpr> at 0x000002C68A019BE0>
print(tuple(t))           # (1, 3, 5)

# or:
l = [1, 3, 5]
t = tuple(i for i in l)
print(t)                  # (1, 3, 5)

#---------------

t = (i for i in range(5))
print(t)                        # <generator object <genexpr> at 0x000002C68A018520>
print(tuple(t))                 # (0, 1, 2, 3, 4)

# or:
t = tuple(i for i in range(5))
print(t)                        # (0, 1, 2, 3, 4)

################################################

t = (1, 9, 2)    
print(t*2)                 # (1, 9, 2, 1, 9, 2)
print(sum(t))              # 12
print(max(t))              # 9
print(min(t))              # 1
print(len(t))              # 3
print(9 in t)              # True
print(2 not in t)          # False
print(t.count(2))          # 1
print(t.index(9))          # 1
#t.reversed               # AttributeError: 'tuple' object has no attribute 'reversed'
print(tuple(reversed(t)))  # (2, 9, 1)

################
"index(value, start, stop)"

t = ('red', 12, 'blue', 12, 'red', 12)
print(t.index('blue'))                 # 2
print(t.index('red'))                  # 0
print(t.index('red', 0))               # 0
print(t.index('red', 1))               # 4
print(t.index('red', 4))               # 4
#print(t.index('red', 1, 3)            # ValueError: tuple.index(x): x not in tuple

################################################
"remove ? "

t = (4, 7, 2, 9, 8)
t = list(t)
t.remove(2)
t = tuple(t)
print(t)         # (4, 7, 9, 8)

################
"append ? "

t = (4, 6)
t += (9,)
print(t)         # (4, 6, 9)

# or:
t = (4, 6)
t = list(t)
t.append(9)
t = tuple(t)
print(t)         # (4, 6, 9)

################
"extend ? "

a = (2, 3)
b = (4, 5)
a += b
print(a)         # (2, 3, 4, 5)     

# or:
a = (2, 3)
b = (4, 5)
a, b = list(a), list(b)
a.extend(b)
a = tuple(a)
print(a)         # (2, 3, 4, 5)

################

t = ('a','b','d','e','f')
t = t[2:]
print(t)                   # ('d', 'e', 'f')

#---------------

t = ('a','b','d','e','f')
t = t[:2] + ('c',) + t[2:]
print(t)                   # ('a', 'b', 'c', 'd', 'e', 'f')








