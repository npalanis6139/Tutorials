a = [10,20,30,40,50,60,70,80,90]
first = 0
last = len(a)-1
status = False
s = int(input("enter the number to search"))
while ( first<=last and not status):
    mid = (first+last)//2
    if (a[mid]==s):
        status = True
    elif (s<=a[mid]):
        last = mid - 1
    else:
        first = mid + 1
if (status == True):
    print("the value %d present in the position %d"%(s,mid+1))
else:
    print("Value not present in the given list")
