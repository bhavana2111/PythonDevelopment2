#A A A A A A A A A A
#B B B B B B B B B B
#C C C C C C C C C C
#D D D D D D D D D D
#E E E E E E E E E E
#F F F F F F F F F F
#G G G G G G G G G G
#H H H H H H H H H H
#I I I I I I I I I I
#J J J J J J J J J J

input1 = int(input("Enter the number of rows"))
input2 = int(input("Enter the number of columns"))

for i in range(1, input1+1):
    print(str(chr(64+i))*input2)

#J J J J J J J J J J
#I I I I I I I I I I
#H H H H H H H H H H
#G G G G G G G G G G
#F F F F F F F F F F
#E E E E E E E E E E
#D D D D D D D D D D
#C C C C C C C C C C
#B B B B B B B B B B
#A A A A A A A A A A

input1 = int(input("Enter the number of rows"))

for i in range(1,input1+1):
    for j in range(1, input1+1):
        print(chr(64+input1-i+1), end=" ")
    print()