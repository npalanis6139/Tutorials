def temp(c):
    f = (9/5)*c + 32
    return print (f)


def len(m,s):
    h = m/60 + s/3600
    return print (h)

c = input("Please enter Celsius value")
c = int(c)
temp(c)

m = input("please enter minutes value:")
m = int(m)
s = input("please enter seconds value:")
s = int(s)
len(m,s)
