print("example:1")

for values in range(1,10):
    print(values)

print("############")
print("example:2")

for values in range(10):
    print(values)

print("############")
print("example:3")

for values in range(5,50,10):
    if(values==25):
        continue
    print(values)

print("############")
print("example:4")

for values in range(4,30,4):
    if(values==16):
        if(values<18):
            print("values is in the range of 18")
        elif(values==4):
            continue
            print(values)
    else:
        print(values)
