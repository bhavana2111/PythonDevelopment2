# 111111
# 222222
# **********

input1 = int(input("Enter the number of rows"))
input2 = int(input("Enter the number of columns"))

for i in range(1,input1+1):
    print(str(i)*input2)


#10 10 10 10 10 10 10 10 10 10
#9 9 9 9 9 9 9 9 9 9
#8 8 8 8 8 8 8 8 8 8
#7 7 7 7 7 7 7 7 7 7
#6 6 6 6 6 6 6 6 6 6
#5 5 5 5 5 5 5 5 5 5
#4 4 4 4 4 4 4 4 4 4
#3 3 3 3 3 3 3 3 3 3
#2 2 2 2 2 2 2 2 2 2
#1 1 1 1 1 1 1 1 1 1

input1 = int(input("Enter the number of rows"))

for i in range(1, input1+1):
    for j in range(1, input1+1):
        print(input1-i+1, end=" ")
    print()