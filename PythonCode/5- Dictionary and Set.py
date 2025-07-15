"""
Dictionariy & Set
"""
################################################
################################################
# dict{}

'har ozve dictionary shamele yek andis va yek meghdar\
 ast ke be vasile alamate : az ham joda mishavand.\
 andis ha kelid namide mishavand. pas azaye dictionary\
 az joft haye kelid-meghdar tashkil mishavand.'

d = {}
print(d, type(d))        # {} <class 'dict'>

d = {'ali':19}
print(d)                 # {'ali': 19}

d = {18:'asma'}
print(d)                 # {18: 'asma'}

################

d = {'ali':19,'asma':15} 
print(d)                   # {'ali': 19, 'asma': 15}
print(list(d))             # ['ali', 'asma']

print(d.items())           # dict_items([('ali', 19), ('asma', 15)])
print(list(d.items()))     # [('ali', 19), ('asma', 15)]

print(d.keys())            # dict_keys(['ali', 'asma'])
print(list(d.keys()))      # ['ali', 'asma']
print(list(d))             # ['ali', 'asma']

print(d.values())          # dict_values([19, 15])
print(list(d.values()))    # [19, 15]

################

d = {}
print(d, type(d))              # {} <class 'dict'>

d = dict()
print(d, type(d))              # {} <class 'dict'>

d = dict({})
print(d, type(d))              # {} <class 'dict'> 

d = dict(ali=19, asma=15)
print(d)                       # {'ali': 19, 'asma': 15}

d = dict({'ali':19,'asma':15})
print(d)                       # {'ali': 19, 'asma': 15}

################

d = {2:'two', 3:'three'}
d[1] = 'one'
print(d)               # {2: 'two', 3: 'three', 1: 'one'}

#---------------

d = {}
d['ali'] = 19
d['asma'] = 18
d[20] = 'fateme'
print(d)               # {'ali': 19, 'asma': 18, 20: 'fateme'}

#---------------

d = {'ali': 19, 'asma': 18, 20: 'fateme'}

print(d['ali'])        # 19

print(d[20])           # fateme

d['asma'] = 15
print(d)               # {'ali': 19, 'asma': 15, 20: 'fateme'}

################

d = {'ali': 19, 'asma': 18}
print(list(d.items()))           # [('ali', 19), ('asma', 18)]

#---------------

l = [('ali', 19), ('asma', 18)]
print(dict(l))                   # {'ali': 19, 'asma': 18} 

################

d = {'ali': 19, 'asma': 18}
print(len(d))               # 2
print(min(d.values()))      # 18
print(max(d.values()))      # 19
print(sum(d.values()))      # 37

#---------------

d = {1001: 14, 1002: 17, 1003: 11}
print(len(d))             # 3
print(min(d))             # 1001
print(max(d))             # 1003
print(sum(d))             # 3006

print(min(d.values()))    # 11
print(max(d.values()))    # 17
print(sum(d.values()))    # 42

################
"del"

d = {'ali': 19, 'asma': 18, 20: 'fateme'}

del d['ali']
print(d)       # {'asma': 18, 20: 'fateme'}

del d[20]
print(d)       # {'asma': 18}

################
"enumerate"

d = {'ali': 19, 'asma': 18}

print(list(enumerate(d)))     # [(0, 'ali'), (1, 'asma')]

for i,v in enumerate(d):
    print(i,v)
'''
0 ali
1 asma
'''
#---------------

d = {'ali': 19, 'asma': 18}
for i,v in enumerate(d.values()):
    print(i,v)
'''
0 19
1 18
'''
################
"for in dict"

d = {1: 'one', 2: 'two'}
for k in d:
    print(k, end=' ')       # 1 2 

# or:    
d = {1: 'one', 2: 'two'}
for k in d.keys():
    print(k, end=' ')       # 1 2 
    
#---------------
    
d = {1: 'one', 2: 'two'}
for k in d:
    print(d[k], end=' ')    # one two 
    
# or:
d = {1: 'one', 2: 'two'}
for v in d.values():
    print(v, end=' ')       # one two 

#---------------
    
d = {1: 'one', 2: 'two'}
for k in d:
    print(k,':',d[k])    
'''
1 : one
2 : two
'''

# or:
d = {1: 'one', 2: 'two'}
for k,v in d.items():
    print(k,':',v)
'''
1 : one
2 : two
'''

# or:
d = {1: 'one', 2: 'two'}
for i in d.items():
    print(i)
'''
(1, 'one')
(2, 'two')
'''
################
"Zip"

'zip'

k = ('ali', 'asma', 'amin')
v = (19, 15, 13)

print(dict(zip(k, v)))    # {'ali': 19, 'asma': 15, 'amin': 13}

#---------------
"unzip"

d = {'ali':19, 'asma':15, 'amin':13} 

l = list(d.items())
print(l)                  # [('ali', 19), ('asma', 15), ('amin', 13)]
print(list(zip(*l)))      # [('ali', 'asma', 'amin'), (19, 15, 13)]

k, v = list(zip(*l))
print(k)                  # ('ali', 'asma', 'amin')
print(v)                  # (19, 15, 13)

#---------------

t = ('ali', 'asma', 'amin')
print(list(zip(*t)))      # [('a', 'a', 'a'), ('l', 's', 'm'), ('i', 'm', 'i')]

d = {19:'ali', 15:'asma'} 
print(list(zip(*d)))      # TypeError: 'int' object is not iterable

################
"dict toodartoo"

tel = {'home' : '021-4455' , 
       'mobile' : '0912-1972028'}

person ={'name'     : 'parsa', 
         'age'      : 48 , 
         'children' : ['ali' , 'asma'],
         'phone'    : tel }

print(person['phone'])            # {'home': '021-4455', 'mobile': '0912-1972028'}
print(person['phone']['mobile'])  # 0912-1972028
print(tel['mobile'])              # 0912-1972028
print(person['children'])         # ['ali', 'asma']
print(person['children'][0])      # ali

################################################
# dict saz

d = {k:'*' for k in range(4)}
print(d)
# {0: '*', 1: '*', 2: '*', 3: '*'}


d = {i:str(i) for i in range(4)}
print(d)
# {0: '0', 1: '1', 2: '2', 3: '3'}


d = {i:i**2 for i in range(4)}
print(d)
# {0: 0, 1: 1, 2: 4, 3: 9}

#---------------

x = (1, 2, 3)
y = ('one', 'two', 'three')
l = list(zip(x, y))
print(l)                    # [(1, 'one'), (2, 'two'), (3, 'three')]  
   
d = {k:v  for k,v in l}
print(d)                    # {1: 'one', 2: 'two', 3: 'three'} 
print(dict(l))              # {1: 'one', 2: 'two', 3: 'three'} 


# or:
x = (1, 2, 3)
y = ('one', 'two', 'three')
d = {k:v for k in x for v in y if x.index(k)==y.index(v)}
print(d)     
# {1: 'one', 2: 'two', 3: 'three'}


# but:
x = (1, 2, 3)
y = ('one', 'two', 'three')
d = {k:v for k in x for v in y}
print(d)     
# {1: 'three', 2: 'three', 3: 'three'}

################################################
# sort()

d = {'a': 4, 'b': 3, 'f': 2, 'd': 7, 'c': 1}        
 
print(sorted(d))           # ['a', 'b', 'c', 'd', 'f']
print(sorted(d.keys()))    # ['a', 'b', 'c', 'd', 'f']
print(sorted(d.values()))  # [1, 2, 3, 4, 7]
print(sorted(d.items()))   # [('a', 4), ('b', 3), ('c', 1), ('d', 7), ('f', 2)]

#---------------

n = {'ali' : [12,13,8], 'asma': [15,7,14]}
d = {k:sorted(v)  for k,v in n.items()}
print(d)
# {'ali': [8, 12, 13], 'asma': [7, 14, 15],}

################
"operator"

from operator import itemgetter as ig

d = {'a': 4, 'b': 3, 'f': 2, 'd': 7, 'c': 1}  

print(sorted(d.items()))   
# [('a', 4), ('b', 3), ('c', 1), ('d', 7), ('f', 2)]

print(sorted(d.items(), key=ig(0)))
# [('a', 4), ('b', 3), ('c', 1), ('d', 7), ('f', 2)]

print(sorted(d.items(), key=ig(1)))
# [('c', 1), ('f', 2), ('b', 3), ('a', 4), ('d', 7)]

print(sorted(d.items(), key=lambda x: x[1]))
# [('c', 1), ('f', 2), ('b', 3), ('a', 4), ('d', 7)]

################################################
# amalgar haye Dictionary

"== & is"

a = {'ali': 19, 'asma': 18}
b = {'asma': 18, 'ali': 19}
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = {'ali': 19, 'asma': 18}
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = a.copy()
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = dict(a)
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = {**a}
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = {k:v for k,v in a.items()}
print(a == b)                 # True
print(a is b)                 # False

a = {'ali': 19, 'asma': 18}
b = a
print(a == b)                 # True
print(a is b)                 # True

################
"in"

d = {'ali': 19, 'asma': 18}

print('ali' in d)                 # True
print('ali' in d.keys())          # True

print(19 in d)                    # False
print(19 in d.values())           # True

print(('asma', 18) in d)          # False
print(('asma', 18) in d.items())  # True
 
################################################
# metod haye Dictionary

"clear()"

d = {'ali': 19, 'asma': 18}
d.clear()
print(d)                    # {}

#---------------
"keys()"

d = {'ali': 19, 'asma': 18}
print(list(d.keys()))       # ['ali', 'asma']

#---------------
"values()"

d = {'ali': 19, 'asma': 18}
print(list(d.values()))     # [19, 18]

#---------------
"items()"

d = {'ali': 19, 'asma': 18}
print(list(d.items()))      # [('ali', 19), ('asma', 18)]

################
"copy()"

d = {'ali': 19, 'asma': 18}
x = d 
print(d == x)                 # True
print(d is x)                 # True
del x['ali']
print(d)                      # {'asma': 18}
print(x)                      # {'asma': 18}

# or:
d = {'ali': 19, 'asma': 18}
x = d 
del d['ali']
print(d)                      # {'asma': 18}
print(x)                      # {'asma': 18}

#---------------

d = {'ali': 19, 'asma': 18}
x = d.copy()
print(d == x)                 # True
print(d is x)                 # False
del x['ali']
print(d)                      # {'ali': 19, 'asma': 18}
print(x)                      # {'asma': 18}

# or:
d = {'ali': 19, 'asma': 18}
x = dict(d)
print(d == x)                 # True
print(d is x)                 # False
del x['ali']
print(d)                      # {'ali': 19, 'asma': 18}
print(x)                      # {'asma': 18}

# or:
d = {'ali': 19, 'asma': 18}
x = {**d}
print(d == x)                 # True
print(d is x)                 # False
del x['ali']
print(d)                      # {'ali': 19, 'asma': 18}
print(x)                      # {'asma': 18}

# or:
d = {'ali': 19, 'asma': 18}
x = {k:v for k,v in d.items()}
print(d == x)                 # True
print(d is x)                 # False
del x['ali']
print(d)                      # {'ali': 19, 'asma': 18}
print(x)                      # {'asma': 18}

################
"get(key)"

d = {'ali': 19, 'asma': 18}
print(d['asma'])                # 18
print(d.get('asma'))            # 18

#---------------

d = {'ali': 19, 'asma': 18}
# print(d['parsa'])             # KeyError
print(d.get('parsa'))           # None
print(d.get('parsa', 'nabood')) # nabood
print(d.get('parsa', 0))        # 0

#---------------
'shomaresh'

s = 'abfabaa'
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
print(d)                        # {'a': 4, 'b': 2, 'f': 1}

#---------------
'shir ya khat'

import random
d = {}
for i in range(10):
    x = random.choice(['shir', 'khat'])
    d[x] = d.get(x, 0) + 1
print(d)  

################
"fromkeys(iterable)"

d = {}  
print(d.fromkeys((1,)))                # {1: None}
print(d.fromkeys((1,),'one'))          # {1: 'one'}
print(d.fromkeys((4,'ali')))           # {4: None, 'ali': None}
print(d.fromkeys((4,'ali'),'*'))       # {4: '*', 'ali': '*'}
print(d.fromkeys((4,'ali'),(0,1)))     # {4: (0, 1), 'ali': (0, 1)}
print(d)                               # {}

# or:
d = {} 
x = d.fromkeys(('asma','ali'))
print(x)                               # {'asma': None, 'ali': None}

x['asma'] = 17
x['ali'] = 15
print(x)                               # {'asma': 17, 'ali': 15}

#---------------

print(dict.fromkeys((1,)))             # {1: None}
print(dict.fromkeys((4,'ali')))        # {4: None, 'ali': None}
print(dict.fromkeys((3,4),'one'))      # {3: 'one', 4: 'one'}

# or:
x = dict.fromkeys((3,4))
print(x)                               # {3: None, 4: None} 

#---------------

k = (3, 'ali', 7)
print(dict.fromkeys(k,'*'))   # {3: '*', 'ali': '*', 7: '*'}

a = dict.fromkeys(k)
print(a)                      # {3: None, 'ali': None, 7: None}

#---------------

d = {'ali': 19, 'asma': 18}
k = (3, 5, 7)

a = d.fromkeys(k)
print(a)                     # {3: None, 5: None, 7: None}

#---------------

a = (3, 5, 7)
d = dict.fromkeys(a)
print(d)                     # {3: None, 5: None, 7: None}

# or:
a = (3, 5, 7)
d = {k:None for k in a}
print(d)                     # {3: None, 5: None, 7: None}

################
"setdefault(key, value)" 

d = {1:'one', 2:'two'}
d.setdefault(7)                  
print(d)                         # {1: 'one', 2: 'two', 7: None}

d = {1:'one', 2:'two'}
print(d.setdefault(7))           # None
print(d)                         # {1: 'one', 2: 'two', 7: None}

d = {1:'one', 2:'two'}
print(d.setdefault(7, 'seven'))  # seven
print(d)                         # {1: 'one', 2: 'two', 7: 'seven'}

#---------------

d = {1:'one', 2:'two'}
print(d.setdefault('four',4))    # 4
print(d)                         # {1: 'one', 2: 'two', 'four': 4}

#---------------

d = {1:'one', 2:'two'}
print(d.setdefault(2))           # two
print(d)                         # {1: 'one', 2: 'two'}

d = {1:'one', 2:'two'}
print(d.setdefault(2,'ali'))     # two
print(d)                         # {1: 'one', 2: 'two'}

d = {1:'one'}
print(d.setdefault(2,'ali'))     # ali
print(d)                         # {1: 'one', 2: 'ali'}

#---------------
'shomaresh'

s = 'abfabaa'
d = {}
for i in s:
    d[i] = d.setdefault(i, 0) + 1
print(d)                    
# {'a': 4, 'b': 2, 'f': 1}

################
"pop(key)"

d = {'ali': 19, 'asma': 18}
d.pop('ali')
print(d)                     # {'asma': 18}

d = {'ali': 19, 'asma': 18}
print(d.pop('ali'))          # 19
print(d)                     # {'asma': 18}

#---------------

d = {'ali': 19, 'asma': 18}
# print(d.pop('mahdi'))          # KeyError: 'mahdi'
print(d.pop('mahdi', 'nabood'))  # nabood
print(d.pop(10, 'nabood'))       # nabood

#---------------
'taghir kelid ba pop()'

d = {0:'one', 2:'two'}
d[1] = d.pop(0)
print(d)                 # {2: 'two', 1: 'one'}

# or:
d = {0:'one', 2:'two'}
del d[0]
d[1] = 'one'
print(d)                 # {2: 'two', 1: 'one'}

# but:
d = {0:'one', 2:'two'}
d[1] = 'one'
print(d)                 # {0: 'one', 2: 'two', 1: 'one'}

################
"popitem()"

d = {1:'one', 2:'two', 3:'three'}

d.popitem()
print(d)              # {1: 'one', 2: 'two'}

d.popitem()
print(d)              # {1: 'one'}

#---------------

d = {1:'one', 2:'two', 3:'three'}

print(d.popitem())    # (3, 'three')
print(d)              # {1: 'one', 2: 'two'}

print(d.popitem())    # (2, 'two')
print(d)              # {1: 'one'}

################
"update(m)"

a = {1:'one', 2:'two'}
a.update({3:'three'})
print(a)                # {1: 'one', 2: 'two', 3: 'three'}

# or:
a = {1:'one', 2:'two'}
a[3] = 'three'
print(a)                # {1: 'one', 2: 'two', 3: 'three'}

#---------------
'taghire value ba update()'

a = {1:'one', 2:'two'}
a.update({1:'yek'})
print(a)                # {1: 'yek', 2: 'two'}

# or:
a = {1:'one', 2:'two'}
a[1] = 'yek'
print(a)                # {1: 'yek', 2: 'two'}

#---------------

a = {1:'yek', 2:'two'}
b = {1:'one', 3:'three'}
a.update(b)
print(a)                # {1: 'one', 2: 'two', 3: 'three'}

a = {1:'yek', 2:'two'}
b = {1:'one', 3:'three'}
b.update(a)
print(b)                # {1: 'yek', 3: 'three', 2: 'two'}

################
'namayeshe value'

d = {1:'one', 2:'two'}
print(d[2])                # two
print(d)                   # {1: 'one', 2: 'two'}

d = {1:'one', 2:'two'}
print(d.get(2))            # two
print(d)                   # {1: 'one', 2: 'two'}

d = {1:'one', 2:'two'}
print(d.setdefault(2))     # two
print(d)                   # {1: 'one', 2: 'two'}

d = {1:'one', 2:'two'}
print(d.pop(2))            # two
print(d)                   # {1: 'one'}

################
"taghire ajzaye a'za"

'taghir kelid'

d = {0:'one', 2:'two'}
d[1] = d.pop(0)
print(d)                 # {2: 'two', 1: 'one'}

# or:
d = {0:'one', 2:'two'}
del d[0]
d[1] = 'one'
print(d)                 # {2: 'two', 1: 'one'}

#---------------
'taghire value'

a = {1:'three', 2:'two'}
a.update({1:'one'})
print(a)                 # {1: 'one', 2: 'two'}

# or:
a = {1:'three', 2:'two'}
a[1] = 'one'
print(a)                 # {1: 'one', 2: 'two'}

# or:
a = {1:'three', 2:'two'}
del d[1]
d[1] = 'one'
print(d)                 # {2: 'two', 1: 'one'}

################
"combine"

d1 = {'x' : 3 , 'y': 2 , 'z':1}
d2 = {'w' : 8 , 't': 7 }

d = d1.copy()
d.update(d2)
print(d)          # {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}

# or:
d = {}
for i in (d1, d2):
    d.update(i)
print(d)          # {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}  

# or:
d = {**d1, **d2} 
print(d)          # {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}

################################################
################################################
# set()
'set ha az anvae namonazzam va taghiirpazir\
 dar python hastand.'

s = {}
print(s, type(s))      # {} <class 'dict'>

s = {4}
print(s, type(s))      # {4} <class 'set'>

s = {'4'}
print(s, type(s))      # {'4'} <class 'set'>

s = {7,'4'}
print(s, type(s))      # {'4', 7} <class 'set'>

s = {3,5,1,4,2,6,7}
print(s)               # {1, 2, 3, 4, 5, 6, 7}

#---------------

s = {5, (1,2), True}
print(s)                    # {True, (1, 2), 5}

#s = {5, [1,2], True}       # unhashable type: 'list'
#s = {True, {1: 'one'},5}   # unhashable type: 'dict'
#s = {5, {1,2}, True}       # unhashable type: 'set'

#---------------

s = {5, (1,2), True}
# print(s[2])               # 'set' object is not subscriptable

################

s = set()
print(s, type(s))           # set() <class 'set'>

# s = set(5)                # TypeError: 'int' object is not iterable

print(set('ali'))           # {'l', 'a', 'i'}

print(set(range(1,8,3)))    # {1, 4, 7}

print(set((5,'ali')))       # {'ali', 5}

print(set([5, 'ali']))      # {'ali', 5}

print(set({5,'ali'}))       # {'ali', 5}  

################

s = {1, 2, 3, 2, 1, 1, 4} 
print(s)                      # {1, 2, 3, 4}

s = {1, 2, 3, True, 2, 1, 4} 
print(1 == True)              # True
print(s)                      # {1, 2, 3, 4}

s = {2, 3, True, 2, 1, 4} 
print(s)                      # {True, 2, 3, 4}

#---------------

favorite = {'ali':'python', 'sara':'java', 'asma':'R', 'fateme':'python'}

for language in favorite.values():
    print(language, end=' ')            # python java R python 
    
# or:
for language in set(favorite.values()):
    print(language, end=' ')            # python java R

# or:
print(set(favorite.values()))           # {'python', 'java', 'R'}

################

s = {('a', 1), ('b', 2), ('c', 3)}
for i in s:
    print(i)
'''
('b', 2)
('c', 3)
('a', 1)
'''
#---------------

s = {('a', 1), ('b', 2), ('c', 3)}
for k,v in s:
    print(k,v)
'''
b 2
c 3
a 1
'''
#---------------

s = {('a', 1), ('b', 2), ('c', 3)}
d = {k:v for k,v in s}
print(d)
"{'b': 2, 'c': 3, 'a': 1}"

################

a = {1, '4'}
b = {'4', 1}
print(a == b)        # True
print(a is b)        # False

################

s = {6, 8, 7}
print(max(s))     # 8
print(min(s))     # 6
print(sum(s))     # 21
print(len(s))     # 3

################
"set saz"

s = {i for i in range(5)}
print(s)                  # {0, 1, 2, 3, 4}

#---------------

l = [1, 3, 5]
s = {i**2 for i in l}
print(s)                  # {1, 9, 25}

################################################
# amalgar haye set

"in"

s = {3, 4, '5'}
print(5 in s)        # False
print(3 not in s)    # False

################
"=="

a = {3, 4, '5'}
b = {4, '5', 3}
c = a
print(a == b)   # True
print(a == c)   # True
print(b == c)   # True

################
"is"

a = {3, 4, '5'}
b = {4, '5', 3}
c = a
print(a is b)   # False
print(a is c)   # True
print(b is c)   # False

################
"|"
'ejtema'

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # {1, 2, 3, 4, 5}

################
"&"
'eshterak'

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)   # {3}

################
"-"
'tafazol'

a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)   # {1, 2}

################
"^"
'tafazole motagharen'

a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)         # {1, 2, 4, 5}

# or:
a = {1, 2, 3}
b = {3, 4, 5}
print((a-b)|(b-a))   # {1, 2, 4, 5}

################
"<"
'zirmajmooe'

a = {2, 3}
b = {2, 3, 4}
print(a < b)       # True
print(b < a)       # False

################################################
# metod haye set

"union(s)" 'E'
'|'

a = {1,2,3}
b = {3,4,5}

a.union(b)          # nothing
print(a.union(b))   # {1, 2, 3, 4, 5}
print(a|b)          # {1, 2, 3, 4, 5}

u = a.union(b) 
print(u)            # # {1, 2, 3, 4, 5}

#---------------

s = {1,2,3}.union({3,4,5})
print(s)                   # {1, 2, 3, 4, 5}

#---------------

a = {1, 2}
b = {2, 3}
c = {3, 4}

print(set.union(a, b, c))  # {1, 2, 3, 4}

u = set.union(a, b, c)
print(u)                   # {1, 2, 3, 4} 

u = a.union(b, c)
print(u)                   # {1, 2, 3, 4} 

################
"update(s)" 'A'

a = {1,2,3}
b = {3,4,5}
a.update(b)
print(a)         # {1, 2, 3, 4, 5}
print(b)         # {3, 4, 5}

s = set()
x = range(5)
s.update(x)
print(s)         # {0, 1, 2, 3, 4}

s = set()
r ='ali'
s.update(r)
print(s)         # {'l', 'a', 'i'} 

s = set()
l = [11, 22]
s.update(l)
print(s)         # {11, 22}

s = set()
t = (77, 88)
s.update(t)
print(s)         # {88, 77}

s = set()
d = {'one':1 , 'two':2}
s.update(d)
print(s)         # {'two', 'one'}

s = set()
x = {1,2,3}
s.update(x)
print(s)         # {1, 2, 3}

################
"intersection(s)" 'E'
'&'

a = {1,2,3}
b = {3,4,5}
a.intersection(b)          # nothing
print(a.intersection(b))   # {3}
print(a & b)               # {3}

#---------------

s = set.intersection({2,3,4},{3,4,5})
print(s)     # {3, 4}

#---------------

s = {1,2,3}.intersection({2,3,4},{3,4,5})
print(s)     # {3}

################
"intersection_update(s)" 'A' 

a = {1,2,3}
b = {3,4,5}
a.intersection_update(b)
print(a)                 # {3}
print(b)                 # {3, 4, 5}

s = {1,2,3}
s.intersection_update({3,4,5})
print(s)                 # {3}

################
"isdisjoint(s)" 'E'
'esteghlal'

a = {1, 2}
b = {3, 4}
print(a.intersection(b))  # set()
print(a.isdisjoint(b))    # True

a = {1, 2}
b = {2, 3}
print(a.intersection(b))  # {2}
print(a.isdisjoint(b))    # False

print({0,1,2}.isdisjoint({3,4,5}))   # True
print({1,2,3}.isdisjoint({2,3,4}))   # False

################
"difference(s)" 'E'
'-'

a = {1,2,3}
b = {3,4,5}
a.difference(b)           # nothing

print(a.difference(b))    # {1, 2}
print(a - b)              # {1, 2}

#---------------

s = {1,2,3}.difference({2,3,4})
print(s)    # {1}

#---------------

s = set.difference({1,2,3}, {2,3,4})
print(s)    # {1}

################
"difference_update(s)" 'A'

a = {1,2,3}
b = {3,4,5}
a.difference_update(b)
print(a)                     # {1, 2}
print(b)                     # {3, 4, 5}

#---------------

s = {1,2,3}
s.difference_update({3,4,5},{1,6})
print(s)                     # {2}

################
"symmetric_difference(s)" 'E'
'^'

a = {1, 2, 3}
b = {3, 4, 5}

s = a.symmetric_difference(b)
# or:
s = set.symmetric_difference(a, b)
print(s)       
# {1, 2, 4, 5}

################
"symmetric_difference_update(s)" 'A'

s = {1, 2, 3}
s.symmetric_difference_update({3, 4, 5})
print(s)       
# {1, 2, 4, 5}

################
"issubset(s)"
'<'

print({2,3,4,5,6}.issubset({2,3,4}))           # False

print(set.issubset({2,3,4}, set(range(2,7))))  # True

################
"issuperset(s)"
'>'

print({2,3,4,5,6}.issuperset({2,3,4}))          # True

print(set.issuperset({2,3,4}, set(range(2,7)))) # False

################
"clear()"

s = {1, '2', 'ali'}
s.clear()
print(s)            # set()

################
"add(element)"

s = {1, '2', 'ali'}
s.add(2)
s.add('ali')
print(s)            # {1, 2, '2', 'ali'}

################
"discard(element)"

s = {1, '2', 'ali'}
s.discard('ali')
s.discard(2)
print(s)            # {1, '2'}

################
"remove(element)"

s = {1, '2', 'ali'}
s.remove('ali')
# s.remove(2)       # KeyError
print(s)            # {1, '2'}

################
"copy()"

s = {1, '2', 'ali'}
x = s.copy()
print(x)            # {1, '2', 'ali'}
print(s == x)       # True
print(s is x)       # False 

################
"pop()"

s = {1, '2', 'ali'}

s.pop()
print(s)            # {'2', 'ali'}

s.pop()
print(s)            # {'ali'}

s.pop()
print(s)            # set()
# s.pop()           # 'pop from an empty set'

#---------------

s = {1, 'asma', 'ali'}
print(s.pop())         # 1
print(s)               # {'asma', 'ali'}
print(s.pop())         # asma
print(s)               # {'ali'}

################
"frozenset()"

'set ha taghiir pazir hastand, yani mitavan ba metod haye add(),\
 pop(),... azaii ra be majmooe ezafe ya hazf kard. ba estefade az\
 frozenset mitavan majmooe(set) e sakht ke taghiir napazir bashad.\
 frozenset daraye metod haye bala mibashad (be joz anhaii ke dar\
 majmooe taghiir eijad mikonand). '

s = frozenset({1, '2', 'ali'})
print(s)                       # frozenset({'ali', 1, '2'})
print(type(s))                 # <class 'frozenset'>

# s.pop()                      # error
print(s.difference({1,3}))     # frozenset({'2', 'ali'})


































