'mabna'
'adade sahih ra mitavan dar mabnaye 2, mabnaye 8 va mabnaye 16 bayan kard.'

'adade mabnaye 2 ra bayad ba 0b ya 0B shoroo nemood:'
a = 0b1101
print(a)        # 13

'adade mabnaye 8 ra bayad ba 0o ya 0O shoroo nemood:'
a = 0o743
print(a)        # 483

'adade mabnaye 16 ra bayad ba 0x ya 0X shoroo nemood:'
a = 0xb7d
print(a)        # 2941


'dar python tavabeei baraye tabdile yek adad az mabnaye 10 be mabnaye 2, 8 va 16 vojood darand:'

# bin(): yek adade mabnaye 10 ra be adade mabnaye 2 tabdil mikonad:
a = 7
print(bin(a))   # 0b111

# oct(): yek adade mabnaye 10 ra be adade mabnaye 8 tabdil mikonad:
a = 18
print(oct(a))   # 0o22

# hex(): yek adade mabnaye 10 ra be adade mabnaye 16 tabdil mikonad:
a = 20
print(hex(a))   # 0x14

# int(): yek adade az yek mabna ra be mabnaye 10 tabdil mikonad:
a = 0x14
print(int(a))   # 20

####################################################

'Bitwise Operators'
"amalgar haye bity, amalgar hayi hastand ke bar rooye bit haye dade kar mikonand"

""" a=13  ==>  bin(a)   ==>        1 1 0 1 => 8+4+1=13  =>  bim(a) = 0b1101 
                            ... 16 8 4 2 1                                   """

a = 13
print(bin(a))                      # 0b1101

b = 14
print(bin(b))                      # 0b1110

# amalgare &, and
'in amalgar, 2 amalvand ra bit be bit ba ham '&' biti mikonad.\
 natije and biti zamani 1 ast ke har 2 bit 1 bashand'
c = a | b
print(bin(c))                      # 0b1111

# amalgare |, or
c = a & b
print(bin(c))                      # 0b1100

# amalgare ^, xor ya enhesarie biti
'natije ^ zamani 1 ast ke 2 bit, mokhalefe ham bashand.'
c= a ^ b
print(bin(c))                      # 0b0011 

# amalgare ~, naghize biti
'in amalgar ghabl az yek amalvand miayad va tamame bit haye yeke\
 an ra be sefr, va bit haye sefre an ra be yek tabdil mikonad.'
a=10
b=~a
print(bin(a))
print(bin(b))    #??

# amalgare <<, shift be chap
'in amalgar meghdare amalvande samte chap ra be tedade\
 amalvande samte rast, be samte chap shift midahad.'
a = 12
z = a << 2
print(bin(a))                      # 0b1100
print(bin(z))                      # 0b110000
print(z)                           # 48
print(a * (2**2))                  # 48

a = 7
b = 4
z = a << b
print(bin(a))                      # 0b111
print(bin(z))                      # 0b1110000
print(z)                           # 112
print(a * (2**b))                  # 112

# amalgare >>, shift be rast
a = 12
z = a >> 2
print(bin(a))                      # 0b1100
print(bin(z))                      # 0b11
print(z)                           # 3
print(a // (2**2))                 # 3

a = 18
print(bin(a))                      # 0b10010
print(bin(a >> 3))                 # 0b10
print(a >> 3)                      # 2
print(a // (2**3))                 # 2


################################

a = 5
b = 3

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)  # a = 3, b = 5

################################

# دریافت ورودی
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# پیدا کردن مختصات نقطه چهارم
x4 = x1 ^ x2 ^ x3  # از خواص XOR برای پیدا کردن مختصات x استفاده میکنیم
y4 = y1 ^ y2 ^ y3  # از خواص XOR برای پیدا کردن مختصات y استفاده میکنیم

# چاپ مختصات نقطه چهارم
print(x4, y4)

################################

n = [4, 1, 2, 1, 2]
x = 0
for i in n:
    x = x ^ i
    #x^=i

print("عدد یکتا:", x)  # خروجی: 4














