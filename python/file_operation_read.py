print("File open")

file0 = open("functions.py", "r")
x = file0.read()
print(x)
file0.close()

print("File open in text mode")

file1 = open("functions.py", "U")
x = file1.read()
file1.close()



print("File write/create")

file2 = open("sample_1.py", "w+")
x = file2.write("\nHefrfrrfllo_world")
file2.close()


print("File content append")

file3 = open("loops.py", "a")
x = file3.write("\ntes89898")
file3.close()
