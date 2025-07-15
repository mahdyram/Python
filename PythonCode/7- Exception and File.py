"""
Exception and File
"""
################################################
################################################
# Exception

"""
try:
        { Run this code   
except:
        { Execute this code when there is an exception
""" 

try:
    print(8 / 2)                # 4.0  
except:
    print('error')              

try:
    print(8 / 0)
except:
    print('error')              # error
    
# or:
# print(8 / 0)                  # ZeroDivisionError: division by zero
try:
    print(8 / 0)
except ZeroDivisionError:
    print('error')              # error

# or:
try:
    print(8 / 0)
except ZeroDivisionError as ze:
    print(ze)                   # division by zero     

#---------------

# print(k)                 # NameError: name 'k' is not defined
try:
    print(k)
except NameError as ne: 
    print(ne)              # name 'k' is not defined
    
#---------------

# print('ali' + 2)         # TypeError: can only concatenate str (not "int") to str
try:
     print('ali' + 2)
except TypeError as te:    
    print(te)              # can only concatenate str (not "int") to str
    
#---------------

'bedoone dastoore try va except, bad az\
 khata, kolle barname motavaghef mishavad:'
x = 7
y = 0
# print(x/y)    # division by zero
print(y/x)      # 

# but:
'ba dastoore try va except, bad\
 az khata ham barname edame miyabad:'
try:
    x = 7
    y = 0
    print(x/y)
except:
    print('error')  # error 
print(y/x)          # 0.0

################
"""
try:
        { Run this code   
except:
        { Execute this code when there is an exception
else:
        { No exception? Run this code
"""
  
try:
    x = 8 / 2
except ZeroDivisionError as ze:
    print(ze)            
else:
    print(x)                     # 4

# but:    
try:
    x = 8 / 0
except ZeroDivisionError as ze:
    print(ze)                    # division by zero          
else:
    print(x)  

#---------------      
    
try:
    x = 8 / 2                    # 4.0
    print(x)
except ZeroDivisionError as ze:
    print(ze)            
else:
    print(x)                     # 4

#---------------

try:
    x = int(input('enter x: '))
    y = int(input('enter y: '))
    z = x / y
except:
    print('error')
else:
    print(f'result = {z}')
'''
enter x: 8
enter y: 2
result = 4.0

enter x: 8
enter y: two
error

enter x: 8
enter y: 0
error
'''
################
"""
try:
         { Run this code   
except:
         { Execute this code when there is an exception
else:
         { No exception? Run this code
finally:
         { Always run this code   
"""

try:
    x = 8 / 2
except ZeroDivisionError as ze:
    print(ze)            
else:
    print(x)                     # 4
finally:
    print('byebye')              # byebye

# but:    
try:
    x = 8 / 0
except ZeroDivisionError as ze:
    print(ze)                    # division by zero          
else:
    print(x)  
finally:
    print('byebye')              # byebye
    
#---------------
 
def divide(x, y):
    try:
        r = x / y
    except:
        print('error')
    else:
        print(r)
    finally:
        print('bye')
divide(2, 1)         # 2.0     bye  
divide(4, 0)         # error   bye
divide(2,'j')        # error   bye   

# or:
def divide(x, y):
    try:
        r = x / y
    except TypeError as te:
        print(te)
    except ZeroDivisionError as ze:
        print(ze)
    else:
        print(r)
    finally:
        print('bye')
divide(2, 1)        # 2.0     bye   
divide(4, 0)        # division by zero     bye
divide(2,'j')       # unsupported operand type(s) for /: 'int' and 'str'   bye   

################

v = True
while v:
    try:
        x = int(input('enter a number: '))
    except ValueError:
        print('must type a number')
        again = input('Try again?(N or ...): ')
        if again == 'N':
            print('Ok, see you later')
            v = False
    except KeyboardInterrupt:
        print('\nYou pressed Ctrl+C')
        print('see you later')
        v = False
    else:
        print(x**2)
        v = False
'''
enter a number: 5
25

enter a number: five
must type a number
Try again?(N or ...): N
Ok, see you later

enter a number: five
must type a number
Try again?(N or ...): y
enter a number: 5
25

enter a number: Ctrl+C
You pressed Ctrl+C
see you later
'''

################################################
# try-except toodartoo

def f(x):
    try:
        print(5 / x)
        try:
            print(q)
        except NameError as ne:
            print(ne)
    except ZeroDivisionError as ze:    
       print(ze)  

f(0)
'division by zero'

f(5)                      
'''
1.0
name 'q' is not defined
'''

################################################
# raise

n = 13
if n == 13:
    raise ValueError()                  # ValueError

# or:
n = 13
if n == 13:
    raise ValueError(13)                # ValueError: 13
    
# or:
n = 13
if n == 13:
    raise ValueError('unlucky number')  # ValueError: unlucky number

#---------------

def f(n):
    try:
        if n == 13:
            raise ValueError('Unlucky Number')
        x = 20 / n
    except ValueError as ve:
        return ve
    except:
        return 'Error'
    else:
        return x

print(f(5))       # 4.0
print(f(13))      # Unlucky Number
print(f(0))       # Error    
print(f('a'))     # Error       

################################################
# assert

'dastoore assert, tolide khata mikonad, be in\
 soorat ke agar ebarate jeloye assert False bood\
 khata dar nazar gerefte mishavad va dastoore\
 except ejra mishavad, va agar True bood, khataii\
 iijad nashode va dastoore else ejra mishavad.'

def f(n):
    try:
        assert n != 13
    except:
        v = 'Unlucky Number' 
    else:
        v = 20 / n  
    return v

print(f(5))       # 4.0
print(f(13))      # Unlucky Number

#---------------
'tabeii ke adade zoj ra 2barabar mikonad:'

def f(n):
    try:
        assert n%2 == 0
    except:
        return 'Not even'    
    else:
        return n*2
        
print(f(6))        # 12
print(f(7))        # Not even


# or:
'be vasile if and else'

def f(n):
    if n%2 != 0:
        print('Not even')
    else:
        print(n*2)  
        
f(6)              # 12
f(7)              # Not even
    
################################################
################################################
# File

"bazkardane file"

"file-variable = open(fileName, mode)"
"mode='r' or None => file matni ra braye khandan(read) baz mikonad(agar az ghabl moojood nabashad, error midahad)"
"mode='w' => file matni ra braye neveshtan(write) baz mikonad(agar az ghabl moojood bashad, anra pak mikonad va sepas baz mikonad)"
"mode='a' => file matni ra braye ezafe kardan(append) baz mikonad(agar az ghabl moojood bashad, matn ra be entehaye an ezafe mikonad)"
"mode='r+'=> file matni ra baraye khandan va neveshtan baz mikonad(ebteda file ra mikhanad va sepas neveshtan ra anjam midahad, agar chizi ra read nakonim, az sefr shoroo be neveshtan mikonad)"

myFile = open("D:/test.txt")          # FileNotFoundError: [Errno 2] No such file or directory: 'D:/test.txt'

try:
    myFile = open("D:/test.txt")
except FileNotFoundError as fe:
    print(fe)                         # [Errno 2] No such file or directory: 'D:/tes3t.txt'   

myFile = open("D:/test.txt", 'w')
myFile = open("D:/test.txt")

################
"neveshtan dar file"

'file-variable.write(data)'

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\n')
myFile.write('droode faravan')

#---------------

'writelines(list)'

l = ['salam be hame', 'droode faravan']
myFile.writelines(l)

################
"bastane file"

'file-variable.close()'

myFile.close()

################

myFile = open("D:/test.txt", 'w')
print(myFile.name)                             # D:/test.txt
print(myFile.mode)                             # w
myFile.write('salam be hame\ndroode faravan')
myFile.close()

################################################
# khandane file

"read(size)"

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
print(myFile.read())
'''
salam be hame
droode faravan
'''

print(myFile.read())               # None

print(open("D:/test.txt").read())            
'''
salam be hame
droode faravan
'''

myFile.close()

#---------------

myFile = open("D:/test.txt", 'w')
myFile = open("D:/test.txt")
print(myFile.read())               # None
myFile.close()           

#---------------

myFile = open("D:/test.txt", 'w')
l = ['salam be hame\n', 'droode faravan']
myFile.writelines(l)

myFile = open("D:/test.txt")
s = myFile.read()
print(repr(s))               # 'salam be hame\ndroode faravan'
print(s.split('\n'))         # ['salam be hame', 'droode faravan'] 
myFile.close()      

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\n')
print(myFile.write('droode faravan'))   # 14  =>  tedade karakter haye 'droode faravan'

myFile = open("D:/test.txt")
print(myFile.read())
'''
salam be hame
droode faravan
'''

print(myFile.read())                    # None  => zira esharegar dar payane file ast.
myFile.close() 


myFile = open("D:/test.txt")
print(myFile.read())
'''
salam be hame
droode faravan
'''
#---------------

myFile = open("D:/test.txt", 'w')
l = ['salam be hame\n', 'droode faravan']
myFile.writelines(l)

myFile = open("D:/test.txt")
print(myFile.read(11))        # salam be ha
print(myFile.read(3))         # me
print(myFile.read(7))         # droode 
print(myFile.read(7))         # faravan

myFile = open("D:/test.txt")
print(repr(myFile.read(16)))  # 'salam be hame\ndr'
myFile.close() 

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
myFile1 = open("D:/test1.txt", 'w')
myFile1.write(myFile.read())
myFile1 = open("D:/test1.txt")
print(myFile1.read())
'''
salam be hame
droode faravan
'''

myFile.close()
myFile1.close()

################
"readline()"

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
print(myFile.readlines())      # ['salam be hame\n', 'droode faravan']
print(myFile.readlines())      # [] 
myFile.close()          

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
print(myFile.readline())            # salam be hame
print(myFile.readline())            # droode faravan
print(myFile.readline())            # 

myFile = open("D:/test.txt")
print(repr(myFile.readline()))      # 'salam be hame\n'
print(repr(myFile.readline()))      # 'droode faravan'
print(repr(myFile.readline()))      # ''
myFile.close()        

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
s = myFile.readline()
print(s)                     # salam be hame
print(s)                     # salam be hame

s = myFile.readline()
print(s)                     # droode faravan

s = myFile.readline()
print(s)                     # 

s = myFile.readlines()
print(s)                     # []
myFile.close()

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
print(myFile.readline())       # salam be hame
print(myFile.readlines())      # ['droode faravan']
print(myFile.readlines())      # []
myFile.close() 

#---------------

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
for i in myFile.readlines():
    print(i, end='')
myFile.close()
'''
salam be hame
droode faravan
'''

# or:
myFile = open("D:/test.txt")
for i in myFile:
    print(i, end='')
myFile.close()
'''
salam be hame
droode faravan
'''
################
"mode(a)"

ad = "D:/test10.txt"
t10 = open(ad, 'w')
t10.write('ab\n')
t10 = open(ad)
print(t10.read())
'ab'

t10 = open(ad, 'w')
t10.write('b c')
t10 = open(ad)
print(t10.read())
t10.close()
'b c'


# but:
ad = "D:/test11.txt"
t11 = open(ad, 'a')
t11.write('ab\n')
t11 = open(ad)
print(t11.read())
'ab'

t11 = open(ad, 'a')
t11.write('b c')
t11 = open(ad)
print(t11.read())
t11.close()
'''
ab
b c
'''
################
"mode(r+)"

ad = 'D:/test20.txt'

t20 = open(ad, 'w')
t20.write('abcd')
t20 = open(ad, 'r') 
print(t20.read())          # abcd
    
t20 = open(ad, 'r+') 
t20.read()
t20.write('1234')
    
t20 = open(ad, 'r')
print(t20.read())          # abcd1234
t20.close()

# but:
ad = 'D:/test21.txt'
t21 = open(ad, 'w') 
t21.write('abcd')
    
t21 = open(ad, 'r+')
t21.write('1234')
    
t21 = open(ad, 'r') 
print(t21.read())          # 1234
t21.close()

################################################
# esharegar dar file

"tell()"

myFile = open("D:/test.txt", 'w')
myFile.write('salam be hame\ndroode faravan')

myFile = open("D:/test.txt")
print(myFile.tell())          # 0
print(myFile.read(13))        # salam be hame
print(myFile.tell())          # 13
print(myFile.read())          # droode faravan
print(myFile.tell())          # 31
myFile.close()

#---------------

myFile = open("D:/test.txt")
print(myFile.read(3))         # sal
print(myFile.tell())          # 3
print(myFile.read(6))         # am be 
print(myFile.tell())          # 9
print(myFile.read(4))         # hame
print(myFile.tell())          # 13
myFile.close()

################
"seek()"

myFile = open("D:/test.txt", 'w')
myFile.write('ab\nc d')

myFile = open("D:/test.txt")
print(myFile.read(7))                      
'''
ab
c d
'''

print(myFile.tell())          # 7 
print(myFile.read(1))         # None

myFile.seek(0)
print(myFile.tell())          # 0
print(myFile.read(1))         # a
print(myFile.tell())          # 1

myFile.seek(1)
print(myFile.read(1))         # b

myFile.seek(2)
print(myFile.read(1))         # None
myFile.seek(2)
print(repr(myFile.read(1)))   # '\n'

myFile.seek(3)
print(myFile.read(1))         # None
myFile.seek(3)
print(repr(myFile.read(1)))   # '\n'

myFile.seek(4)
print(myFile.read(1))         # c

myFile.seek(5)
print(myFile.read(1))         # None

myFile.seek(6)
print(myFile.read(1))         # d
myFile.close()

################################################
# with...as

'ba in dastoor, digar niazi be dastoore close() nist va daroon an vojood darad'

myFile = open("D:/test.txt", 'w')
myFile.write('ab\nc d')

myFile = open("D:/test.txt")
print(myFile.read())                      
'''
ab
c d
'''
myFile.close()

# or:
with open("D:/test.txt", 'w') as myFile:
    myFile.write('ab\nc d')
    
with open("D:/test.txt") as myFile:
    print(myFile.read())
'''
ab
c d
'''
# print(myFile.read())      # ValueError: I/O operation on closed file

################

name = "D:/test.txt"
name1 = "D:/test1.txt"

with open(name, 'w') as myFile, open(name1, 'w') as myFile1:
    myFile.write('salam be hame\ndroode faravan\n')
    myFile1.write('ab\nc d')
    
with open(name, 'a') as myFile, open(name1) as myFile1:
    myFile.write(myFile1.read())
    
with open(name) as myFile:
    print(myFile.read())
'''
salam be hame
droode faravan
ab
c d
'''
################

name1 = 'd:/l1.txt'
name2 = 'd:/l2.txt'
name3 = 'd:/l3.txt'

with open(name1, 'w') as f1:
    f1.write('ali\nsara\n')
    
with open(name2, 'w') as f2:
    f2.write('taha\nomid')
    
with open(name1) as f1 , open(name2) as f2:
      data1 = f1.read()
      data2 = f2.read()

with open(name3, 'w') as f3:
    f3.write(data1 + data2)
    
with open(name3) as f3:
    data3 = f3.read()

print(data3) 
'''
ali
sara
taha
omid
'''
################

l = ['yes','no','no','yes','yes','yes','no']
name = 'd:/lst.txt'

with open(name, 'w') as f:
    for i in l:
        f.write(i+'\n')

with open(name) as f:
    print(f.read())

# or:
for i in range(0, len(l)-1):
    l[i] += '\n'
    
with open(name, 'w') as f:
    f.writelines(l)
    
with open(name) as f:
    print(f.read())
f.close()

with open(name)  as f:
     l = f.readlines() 
print(l)                      
# ['yes\n', 'no\n', 'no\n', 'yes\n', 'yes\n', 'yes\n', 'no']

x = []
for i in l:
    x.append(i.strip())
print(x)
# ['yes', 'no', 'no', 'yes', 'yes', 'yes', 'no']

#---------------

c1 = 0
c2 = 0
with open(name, 'r') as f:      
     for x in f:
         print(x)
         if x == 'yes':
            c1 += 1
         elif x == 'no':
             c2 += 1
print(c1, c2)             # 0  =>  zira x ha dar file f, barabare yes\n , no\n hastand na yes , no.      


# or:
c1 = 0
c2 = 0
with open(name, 'r') as f:      
     for x in f:
         print(x)
         if x == 'yes\n':
            c1 += 1
         elif x== 'no\n':
             c2 += 1
print(c1)                # 4         
print(c2)                # 3


# or:
c1 = 0
c2 = 0
with open(name, 'r') as f:      
     for i in f:
         x = i.strip()
         print(x)
         if x == 'yes':
            c1 += 1
         elif x== 'no':
             c2 += 1
print(c1)                # 4         
print(c2)                # 3


# or:
c1 = 0
c2 = 0
with open(name, 'r')  as f:
     l = f.readlines() 
     print(l)      
     for i in l:
         x = i.strip()
         if x == 'yes':
            c1 += 1
         else :
            c2 += 1
print(c1)                # 4         
print(c2)                # 3


# or:
d = dict()
with open(name) as f:
    for i in f:
        w = i.strip()
        print(w)
        d[w] = d.get(w, 0) + 1
print(d)                            # {'yes': 4, 'no': 3}  

################################################

"json"

import json

d = {'k1':'v1' , 'k2':'v2'}
js = json.dumps(d)
print(js)            # {"k1": "v1", "k2": "v2"}

#---------------

d = {'k1':'v1' , 'k2':'v2'}
print(json.dumps(d , indent = 2))
'''
{
  "k1": "v1",
  "k2": "v2"
}
'''
#---------------

d = {'k1':'v1' , 'k2':'v2'}
print(json.dumps(d, indent = 2, separators = (';','= ')))
'''
{
  "k1"= "v1";
  "k2"= "v2"
}
'''
#---------------

d = {'k1':'v1', 'k2':'v2'}

with open('d:/j.json', 'w') as f:
    json.dump(d, f)
    
with open('d:/j.json') as f:
    print(json.load(f))             # {'k1': 'v1', 'k2': 'v2'}

################
"csv"

import csv

x  = ['Name', 'Age'] 
r1 = ['ali', 35]
r2 = ['taha', 10]
r3 = ['mahsa', 40]

with open('d:/a.csv','w') as f:
    w = csv.writer(f)
    w.writerow(x)
    w.writerows([r1,r2,r3])
    
with open('d:/a.csv') as f:
    r = csv.reader(f)
    print(list(r))      # [['Name', 'Age'], [], ['ali', '35'], [], ['taha', '10'], [], ['mahsa', '40'], []]

with open('d:/a.csv', newline = '\n') as f:
    r = csv.reader(f)
    print(list(r))      # [['Name', 'Age'], ['ali', '35'], ['taha', '10'], ['mahsa', '40']]

with open('d:/a.csv', newline = '\n') as f:
    r = csv.reader(f)
    for i in r:
        print('   '.join(i))
'''
Name   Age
ali   35
taha   10
mahsa   40
'''

# or:
import pandas as pd
a = pd.read_csv('d:/a.csv')
print(a)
'''
    Name  Age
0    ali   35
1   taha   10
2  mahsa   40
''' 

# or:
a = pd.read_csv('d:/a.csv')
a.to_csv('d:/b.csv', sep=',', index=False)
b = pd.read_csv('d:/b.csv')
print(b)
'''
    Name  Age
0    ali   35
1   taha   10
2  mahsa   40
''' 
################################################
# amale systemi bar rooye file

"remove()"
'os.remove(fileName)'

import os

p = "D:/test.txt"
with open(p, 'w') as myFile:
    myFile.write('abc')
    
print(os.path.exists(p))    # True
os.remove(p)
print(os.path.exists(p))    # False

#---------------

l = ["l1.txt", "l2.txt", "l3.txt", "lst.txt", "j.json", "a.csv", "b.csv", "test1.txt", "test10.txt", "test11.txt", "test20.txt", "test21.txt"]
for i in l:
    os.remove(f"D:/{i}")


















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    