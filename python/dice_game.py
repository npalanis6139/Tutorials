import random
print "Lets Play a dice game"

a = "b"

while a =="b":
      roll = random.randint(1,6)
      if roll == 1:
          print "-----------"
          print "|          |"
          print "|    0     |"
          print "|          |"
          print "------------"



      if roll == 2:
           print "-----------"
           print "|          |"
           print "|   0 0    |"
           print "|          |"
           print "------------"


      if roll == 3:
           print "-----------"
           print "|    0     |"
           print "|    0     |"
           print "|    0     |"
           print "------------"


      if roll == 4:
           print "-----------"
           print "| 0    0   |"
           print "|          |"
           print "| 0     0  |"
           print "------------"



      if roll == 5:
             print "-----------"
             print "| 0    0   |"
             print "|    0     |"
             print "| 0     0  |"
             print "------------"


      if roll == 6:
             print "-----------"
             print "| 0     0  |"
             print "| 0     0  |"
             print "| 0     0  |"
             print "------------"

      a = input("Press b to continue")
