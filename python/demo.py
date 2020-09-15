
print ("File open and write mode")

file = open("loops.py", "w")
x = file.write()
print(x)

print ("File open and append mode")

file = open("loops.py", "a")
x = file.append()
print(x)
