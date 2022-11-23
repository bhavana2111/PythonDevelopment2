rows = int(input("Enter number of rows"))

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *

for i in range(1, rows+1):
    print(i*("*"), sep=" ")
    print()

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()



# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9
# 10 10 10 10 10 10 10 10 10 10

for i in range(1, rows+1):
    for j in range(1, i+1):
        print((str(i))+"\t",end="")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(str(j)+"\t", end= "")
    print()


# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G
# H H H H H H H H
# I I I I I I I I I
# J J J J J J J J J J

for i in range(1, rows+1):
    print(chr(64+i)*i, end="")
    print()


# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G
# A B C D E F G H
# A B C D E F G H I
# A B C D E F G H I J

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(chr(64+j)+"\t", end="")
    print()


# * * * * * * * * * *
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(rows,0,-1):
    print(i*"*", end="")
    print()


# 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4
# 5 5 5 5 5 5
# 6 6 6 6 6
# 7 7 7 7
# 8 8 8
# 9 9
# 10


j=1
for i in range(rows,0,-1):
    print(str(j)*i,sep=" ")
    print()
    j+=1






# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


for i in range(rows,0,-1):
    for j in range(1,i):
        print(str(j)+"\t", end="")
    print()



# A A A A A A A A A A
# B B B B B B B B B
# C C C C C C C C
# D D D D D D D
# E E E E E E
# F F F F F
# G G G G
# H H H
# I I
# J

j=65
for i in range(rows,0,-1):
    print((chr(j)*i),end="")
    print()
    j+=1


# A B C D E F G H I J
# A B C D E F G H I
# A B C D E F G H
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A


for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()




# 10 10 10 10 10 10 10 10 10 10
# 9 9 9 9 9 9 9 9 9
# 8 8 8 8 8 8 8 8
# 7 7 7 7 7 7 7
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1


j=rows
for i in range(rows,0,-1):
    print((str(j)+" ")*i,end="")
    print()
    j-=1


# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2
# 10 9 8 7 6 5 4 3
# 10 9 8 7 6 5 4
# 10 9 8 7 6 5
# 10 9 8 7 6
# 10 9 8 7
# 10 9 8
# 10 9
# 10

inc = 0
for i in range(rows,0,-1):
    for j in range(rows,inc,-1):
        print((str(j)+" "),end="")
    print()
    inc += 1




# J J J J J J J J J J
# I I I I I I I I I
# H H H H H H H H
# G G G G G G G
# F F F F F F
# E E E E E
# D D D D
# C C C
# B B
# A

for i in range(rows,0,-1):
    print((chr(i+64)+" ")*i,end="")
    print()


# J I H G F E D C B A
# J I H G F E D C B
# J I H G F E D C
# J I H G F E D
# J I H G F E
# J I H G F
# J I H G
# J I H
# J I
# J

inc=0
for i in range(rows,0,-1):
    for j in range(rows,inc,-1):
        print(chr(64+j)+" ",end="");
    print()
    inc+=1


