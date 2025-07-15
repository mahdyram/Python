a = input()
l=[]
for j in range(int(a)):
    a, b , h = input().split(" ")
    a, b , h = int(a), int(b), int(h)
    x = 0
    n = 0
    while 1:
        n+=1
        x+=a
        if x>= h:
            l.append(n)
            break
        x-=b
for i in l: print(i)




