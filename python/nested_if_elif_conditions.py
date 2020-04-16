x = 5
y = input("Please enter the value (y):")
z = 10
y=int(y)
if(x==y):
    if(y<z):
        print("Y value is smaller than z")

elif(x<y):
    if(y<z):
        print("Y Value is greater than X and smaller than z")
    else:
        print("Y value is greater than X and Z")
else:
    print("Y value is smaller than x and z")
