print ("Get datetime details")
import datetime
x = datetime.datetime.now()
print(x)


print ("Get Year details")
import datetime
x = datetime.datetime.now()
print(x.year)

print ("Get month details")
import datetime
x = datetime.datetime.now()
print(x.month)

print ("Create own datetime")
import datetime
x = datetime.datetime(2020,7,12)
print(x)

print ("Get full details using Strftime method")
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%c"))
print(x.strftime("%f"))
print(x.strftime("%j"))
print(x.strftime("%M"))
print(x.strftime("%m"))
print(x.strftime("%p"))
print(x.strftime("%S"))
print(x.strftime("%U"))
print(x.strftime("%w"))
print(x.strftime("%W"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%X"))
print(x.strftime("%x"))
print(x.strftime("%Z"))
print(x.strftime("%z"))
