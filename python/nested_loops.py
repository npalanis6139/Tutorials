x = ["red","green","yellow"]
y = ["ball","bat","light"]
z = ["1","2","3"]

a = 0
b = 0
c = 0

for i in x:
    for j in y:
        for k in z:
            print(x[a],y[b],z[c])
            c+=1
        b+=1
        c=0
    a+=1
    b=0
