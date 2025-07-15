"""
Numpy
"""
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)

import numpy as np
a=np.linspace(10, 15, 5)
print(a)
#or:
a=np.linspace(10, 15, num=5)
print(a)

a=np.linspace(10, 15, 5, endpoint=False)
print(a)

a=np.linspace(10, 15, 5, endpoint=True)
print(a)

a=np.linspace(10, 15, 5, retstep=False)
print(a)

a=np.linspace(10, 15, 5, retstep=True)
print(a)

print('--------')
# numpy.logspase(start, stop, num, endpoint, base, dtype)

import numpy as np
a=np.logspace(1, 1.5, num=5)
print(a)

a=np.logspace(1, 10, num=5, base=2)
print(a)

print('--------')
# numpy.reshape(a, newshape, order)

import numpy as np
a=np.arange(8)
print(a)

b=np.reshape(a, (2,4), order='F')
print(b)

print('--------')

import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.reshape(a, (2,3))
c=a.reshape(3,2)
print(b,'\n\n',c)

print('--------')
# name.flat[:]

import numpy as np
a=np.arange(8).reshape(4,2)
print(a)

b=a.flat[2:3]
print(b)

c=a.flat[2:5]
print(c)

print('--------')
# name.flatten()

import numpy as np
a=np.arange(8).reshape(2,4)
print(a)

b=a.flatten('C')
print(b)

c=a.flatten('F')
print(c)

print('--------')
# numpy.ravel(a, order)

import numpy as np
a=np.arange(6).reshape(2,3)
print(a)

b=np.ravel(a,'C')
print(b)

c=np.ravel(a, order='F')
print(c)

print('--------')

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.ravel(a, order='C')
c=a.ravel('F')
print(b,'\n',c)

print('--------')
# numpy.transpose(a, axes)

import numpy as np
a=np.arange(6).reshape(2,3)
print(a)

b=np.transpose(a)
print(b)

print('--------')
# numpy.swapaxes(a, axis1, axis2)

import numpy as np
a=np.arange(8).reshape(2, 2, 2)
print(a)
print('--------')
b=np.swapaxes(a, 2, 0)
print(b)
print('--------')
c=np.swapaxes(a, 2, 1)
print(c)

print('--------')
# numpy.rollaxis(a, axis, start)

import numpy as np
a=np.arange(8).reshape(2, 2, 2)
print(a)
print('--------')
b=np.rollaxis(a, 2, 1)
print(b)

print('--------')
# numpy.squeeze(a, axis)

import numpy as np
a=np.arange(9).reshape(3, 1, 3)
print(a)
print('--------')
b=np.squeeze(a, 1)
print(b)

print('--------')
# numpy.concatenate((a1, a2, ...), axis)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.concatenate((a,b))
print(c)
print('--------')
d=np.concatenate((a,b), axis=1)
print(d)

print('--------')
# numpy.stack(arrays, axis)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.stack((a,b), axis=1)
print(c)
print('--------')
a=np.array([[1,2],[3,4],[5,6]])
b=np.array([[7,8],[9,10],[11,12]])
c=np.stack((a,b), axis=0)
print(c)

print('--------')
# numpy.hstack(arrays)
# numpy.vstack(arrays)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.hstack((a,b))
d=np.vstack((a,b))
print(c)
print('--------')
print(d)

print('--------')
# numpy.split(a, indices_or_sections, axis)

import numpy as np
a=np.arange(9)
b=np.split(a,3)
print(b)
c=np.split(a,[4,7])
print(c)

print('--------')
# numpy.hsplit(a, indices_or_sections)
# numpy.vsplit(a, indices_or_sections)

import numpy as np
a=np.arange(4).reshape(2,2)
b=np.hsplit(a,2)
print(b)
c=np.vsplit(a,2)
print(c)

print('--------')
# numpy.resize(a, shape)

import numpy as np
a=np.arange(9)
b=np.resize(a, (3,3))
print(b)

print('--------')
# numpy.append(a, values, axis)

import numpy as np
a=np.arange(6).reshape(2, 3)
print(a)
b=np.append(a,[6,7,8])
print(b)
c=np.append(a,[[6,7,8],[9,10,11]])
print(c)
c=np.append(a,[[6,7,8],[9,10,11]],axis=0)
print(c)
c=np.append(a,[[6,7,8],[9,10,11]],axis=1)
print(c)
print('--------')
b=np.array([6,7,8])
c=np.append(a, b)
print(c)
print('--------')
b=np.array([[6,7,8],[9,10,11]])
c=np.append(a, b)
print(c)
c=np.append(a, b, axis=0)
print(c)
c=np.append(a, b, axis=1)
print(c)

print('--------')
# numpy.insert(a, obj, values, axis)

import numpy as np
a=np.arange(6).reshape(2, 3)
print(a)
b=np.insert(a,2,[6,7,8])
print(b)
c=np.insert(a,1,[6,7,8],axis=0)
print(c)
print('--------')
a=np.array([1,2,3])
b=np.array([7,8,9])
c=np.insert(a, 0, b)
print(c)
d=np.append(b, a)
print(d)

print('--------')
# numpy.delete(a, obj, axis)

import numpy as np
a=np.arange(6).reshape(2, 3)
print(a)
b=np.delete(a,3)
print(b)
c=np.delete(a,0,axis=1)
print(c)

print('--------')
# numpy.unique(a, return_index, return_inverse, return_counts)

import numpy as np
a=np.array([1,2,3,3,4,5,6,2,7,3,4])
print(np.unique(a))
print(np.unique(a, return_index=True))
print(np.unique(a, return_inverse=True))
print(np.unique(a, return_counts=True))

print('--------')
# numpy.amin(a, axis)
# numpy.amax(a, axis)

import numpy as np
a=np.array([[3,4,5],[8,9,11],[1,0,2]])
print(a,'\n')
b=np.amin(a, axis=1)
print(b)
b=np.amin(a, axis=0)
print(b)
b=np.amax(a, 1)
print(b)
b=np.amax(a, 0)
print(b)

print('--------')
# numpy.median(a, axis)

import numpy as np
a=np.array([[3,4,5],[8,9,11],[1,0,2]])
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

print('--------')
# numpy.mean(a, axis)

import numpy as np
a=np.array([[3,4,5],[8,9,11],[1,0,2]])
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

print('--------')
# numpy.average(a, axis, weights)

import numpy as np
a=np.array([2,4,7,8])
print(np.average(a))
print(np.average(a, weights=[5,6,4,3]))

a=np.arange(6).reshape(2, 3)
print(np.average(a, axis=1, weights=[10,5,15]))

print('--------')
# numpy.var(a, axis)
# var = mean(abs (x - x.mean())**2)

import numpy as np
a=np.array([5,6,12,7,8,3])
print(np.var(a))

print('--------')
# numpy.std(a, axis)
# std = sqrt(mean (abs (x - x.mean())**2))

import numpy as np
a=np.array([5,6,12,7,8,3])
print(np.std(a))

print('--------')
# numpy.sort(a, axis, kind, order)

import numpy as np
a=np.array([[3,2,4],[8,7,9]])
print(np.sort(a))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))

print('--------')
# numpy.copy(a, order, subok)

import numpy as np
a=np.array([[3,6,-5],[1,-3,2],[5,-1,4]])
print(a)
b=a.copy()
print(b)
print(b is a)

print('--------')

import numpy as np
a=np.arange(10, step=2)
b=np.arange(1, 10, 2)
print(a)
print(b)
print('--------')
print(a*b)
print(a>5)
print(np.sqrt(b))

print('----------------')
"""
nemoone e az araye 2 bodi ba 2 satr va 3 sotoon:

a[0,0]  a[0,1]  a[0,2]

a[1,0]  a[1,1]  a[1,2]

1- zakhire sazi ba order='C':
dar in halat araye 2 bodi be soorate satri zakhire mishavad
yani avval anasore satre avval dar hafeze gharar migirand
sapas anasore satre dovvom va hamin ravand edame miyabad.
baraye mesal araye bala(a) be soorate zir dar hafeze
gharar migirad:
a[0,0]  a[0,1]  a[0,2]  a[1,0]  a[1,1]  a[1,2] , ...

2- zakhire sazi ba order='F':
nahve digar zakhiresazi sotooni ast ke ba order='F' neshan
dade mishavad. in model zakhiresazi be soorate zir ast:
a[0,0]  a[1,0]  a[0,1]  a[1,1]  a[0,2]  a[1,2] , ... """

import numpy as np
b=np.arange(1,13).reshape((3,4))
print(b)
print('--------')
c=np.array(b, order='C')
print(c,'\n')
for i in c:
    print(i)
print()
for i in c:
    for j in i:
        print(j,end=' ')
print('\n','--------')
f=np.array(b, order='F')
print(f,'\n')
for i in f:
    print(i)
print()
for i in f:
    for j in i:
        print(j,end=' ')
        
print('--------') 
# numpy.nditer()
'metode nditer anasore araye ra be tartibe\
zakhire shode dar hafeze namayesh midahad'

print('#numpy.nditer:','\n')
b=np.arange(1,13).reshape((3,4))
c=np.array(b, order='C')
print(c)
for i in np.nditer(c):
    print(i,end=' ')
print('\n')
f=np.array(b, order='F')
print(f)
for i in np.nditer(f):
    print(i,end=' ')
    
print('--------') 
# numpy.reshape()

b=np.arange(1,10).reshape((3,3))
print(b,'\n')
f=np.reshape(b.flatten(), (3,3), 'F')
print(f,'\n')
print(np.transpose(b))

print('--------')

b=np.arange(1,13).reshape((3,4))
print(b.flatten(),'\n')
c=np.reshape(b.flatten(), newshape=(3,4), order='C')
print(c,'\n')
f=np.reshape(b.flatten(), (3,4), 'F')
print(f)

print('--------')

print(f)
for i in np.nditer(f):
    print(i,end=' ')
print('\n')
f2=np.array(f, order='C')
print(f2)
for i in np.nditer(f2):
    print(i,end=' ')
print('\n','--------') 
    
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a,'\n')
b=a.flatten().reshape((3, 2),order='F')
print(b,'\n')
b=a.reshape((2, 3),order='F')
print(b,'\n')
b=a.reshape((3, 2),order='F')
print(b)
print('--------')
a=np.array([[1,2],[3,4],[5,6]])
print(a,'\n')
b=a.reshape((2,3),order='F')
print(b)    

print('--------')  
# 3D

import numpy as np
a=np.arange(1,37).reshape((4,3,3))
print(a) 
print('--------')   
for i in a:
    print(i,'\n')
print('--------')
print()
for i in a:
    for j in i:
        print(j,'\n')    
print('--------')
for i in a:
    for j in i:
        for k in j:
            print(k,end=' ')
print('\n','--------')   
print(a)
print(a[0,0,0])   
print(a[0,2,2])  
print(a[1,0,0])       
print(a[3,2,2])       
print('--------')   
c=np.array(a, order='C')
print(c)
for i in np.nditer(c):
    print(i,end=' ')
print('\n','--------')
f=np.array(a, order='F')
print(f)
for i in np.nditer(f):
    print(i,end=' ')     

print('----------------')
# numpy.matlib
# tarife araye 2 bodi

import numpy.matlib
import numpy as np
a=np.matlib.matrix([[1,2],[3,4],[5,6]])
print(a,'\n')
a=np.matlib.zeros((3,4))
print(a,'\n')
a=np.matlib.ones((4,3))
print(a,'\n')
a=np.matlib.eye(3)
print(a)
a[0,2]=3
a[2,0]=int(input('enter a number:\n'))
print(a)

print('--------')
# meghdardehi be anasore araye 2 bodi

# meghdardehi dar hengame tarife araye(mostaghim):
import numpy.matlib
import numpy as np
a=np.matlib.matrix([[1,2,3],[4,5,6]])
print(a,'\n')

# meghdardehie mojazza be har khane:
a=np.matlib.zeros((2,2))
print(a,'\n')
a[0,0]=1 ; a[0,1]=2 ; a[1,0]=3 ; a[1,1]=4
print(a,'\n')

# meghdardehi ba halghe toodartoo:
a=np.matlib.zeros((2,3))
for i in range(0,2):
    for j in range(0,3):
        a[i,j]=int(input('enter a number:\n'))
print(a)

print('--------')
# namayeshe maghadire anasore araye 2 bodi

# namayeshe mojazzaye har khane:
import numpy.matlib
import numpy as np
a=np.matlib.matrix([[1,2],[3,4]])
print(a)
print(a[0,0],a[0,1],'\n',a[1,0],a[1,1],'\n')

# namayeshe anasore araye ba halghe toodartoo:
a=np.matlib.matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
for i in range(0,3):
    for j in range(0,4):
        print(a[i,j],end='\t')
    print()

print('--------')
# numpy.matlib.empty(shape, dtype, order)

import numpy.matlib
import numpy as np
a=np.matlib.empty((2,2))
print(a)

print('--------')
# numpy.matlib.rand(shape, dtype, order)

import numpy.matlib
import numpy as np
a=np.matlib.rand((4,2))
print(a)

print('--------')
# numpy.matlib.zeros(shape, dtype, order)

import numpy.matlib
import numpy as np
a=np.matlib.zeros((2,3))
print(a)

print('--------')
# numpy.matlib.ones(shape, dtype, order)

import numpy.matlib
import numpy as np
a=np.matlib.ones((3,2))
print(a)

print('--------')
# numpy.matlib.identity(n, dtype)

import numpy.matlib
import numpy as np
a=np.matlib.identity(3)
print(a,'\n')
a=np.matlib.identity(4)
print(a)

print('--------')
# numpy.matlib.eye(n, m, k, dtype)

import numpy.matlib
import numpy as np
a=np.matlib.eye(3)
print(a,'\n')
a=np.matlib.eye(3,4)
print(a,'\n')
a=np.matlib.eye(3,4,1)
print(a,'\n')
a=np.matlib.eye(3,3,0)
print(a,'\n')
a=np.matlib.eye(3,3,1)
print(a,'\n')
a=np.matlib.eye(3,3,2)
print(a,'\n')
a=np.matlib.eye(3,3,-1)
print(a,'\n')
a=np.matlib.eye(n=3,M=3,k=-2)
print(a,'\n')
a=np.matlib.eye(3,k=1)
print(a)

print('--------')
# gabre khatty dar numpy

''' yek mesale mashhood, halle yek dastgahe moadele
ast ke mitavanim an ra be forme matris bayan konim:
                         
3x + 6x - 5z = 12       |3  6  -5| |x| |12| 
x - 3y + 2z = -2   ==>  |1  -3  2|.|y|=|-2|  
5x - y + 4z = 10        |5  -1  4| |z| |10|

    ==>  AX=B  ==>  X=A^(-1).B
'''
import numpy as np
A=np.matrix([[3,6,-5],[1,-3,2],[5,-1,4]])
B=np.matrix([[12],[-2],[10]])
X=A**(-1)*B
print(X)

''' hame matris ha varoonpazir nistand, pas in shive
baraye yaftane pasokhe dastgah hamvare amali nakhahad bood.
mitavan ba estefade az numpy.linalg.svd ke mamoolan dar
varoon kardane matris haye bad-vaz'e khoob kar mikonad,
in moshkel ra hal kard.

amaliate bala bedoone estefade az zir-kelase numpy.matrix
ghabele anjam ast. zir-kelase numpy.matrix dar kelase
numpy.array gharar darad. ya'ni mesale bala bedoone
farakhanie kelase numpy.matrix be soorate zir ghabele
piadesazi ast:
'''
# numpy.linalg.solve(a, b)
''' in metod yek dastgah ra be soorat matris daryaft
karde, an ra hal mikonad:'''
import numpy as np
A=np.array([[3,6,-5],[1,-3,2],[5,-1,4]])
B=np.array([12,-2,10])
X=np.linalg.solve(A, B)
print(X)
# or:
B=np.array([[12],[-2],[10]])
X=np.linalg.solve(A, B)
print(X)

print('or:')

# numpy.linalg.inv(a)
''' in metod maghloob(ma'koos-A^(-1)) matris ra hesab mikonad,
matrise ma'koos barabar ba hasel zarbe matrise asli
dar matrise hamani ast.''' 
import numpy as np
A=np.array([[3,6,-5],[1,-3,2],[5,-1,4]])
B=np.array([12,-2,10])
A1=np.linalg.inv(A)
X=np.dot(A1, B)
print(X)
# or:
X=np.matmul(A1, B)
print(X)
# or:
X=np.linalg.inv(A).dot(B)
print(X)
# or:
# X=np.linalg.inv(A).matmul(B) ??

print('--------')
# numpy.matmul(a, b)
''' in metod hasel zarbe 2 matris ra barmigardanad.'''

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print(np.matmul(a, b))

a=np.array([1,2,3])
b=np.array([10,20,30])
print(np.matmul(a, b))

a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print(a)
print(b,'\n')
print(a*b,'\n')
print(np.matmul(a, b),'\n')
print(np.matrix(a)*np.matrix(b),'\n')

print('--------')
# numpy.dot(a, b)
''' in metod hasel zarbe 2 aray ra barmigardanad. baraye
bordar haye 2 bo'di(2D), hasel zarbe matris ra midahad.
vali baraye araye 1 bo'di, zarbe dakhelie bordar ha ast.'''

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print(np.dot(a, b))

a=np.array([1,2,3])
b=np.array([10,20,30])
print(np.dot(a, b))     # ??
print(a*b)

print('--------')
# numpy.vdot(a, b)
''' in metod majmooe hasel zarbe 2 aray ra barmigardanad.
agar araye ha chand bo'di bashand, an ha ra be araye 1 bo'di
tabdil mikonad va majmooe hasel zarbe an ha ra barmigardanad.'''

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print(np.vdot(a, b))

a=np.array([1,2,3])
b=np.array([10,20,30])
print(np.vdot(a, b))

print('--------')
# numpy.inner(a, b)
''' in metod baraye araye 1 bo'di zarbe dakhelie 2 araye
ra barmigardanad. vali baraye araye haye chand bo'di
hasel jam'e zarbe mehvar ha ra barmigardanad:
    
a=|1  2|  b=|10  20|  ==>  inner(a,b)=|50=1*10+2*20   110=1*30+2*40|
  |3  4|    |30  40|                  |110=3*10+4*20  250=3*30+4*40| 
'''
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print(np.inner(a, b))

a=np.array([1,2,3])
b=np.array([10,20,30])
print(np.inner(a, b))

print('--------')






