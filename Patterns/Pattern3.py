#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9 10

input1 = int(input("Enter the number of rows"))
input2 = int(input("Enter the number of columns"))

for i in range(1, input1+1):
    for i in range(1,input2+1):
        print(i,end="")
    print()


#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1
#10 9 8 7 6 5 4 3 2 1

input1 = int(input("Enter the number of rows"))

for i in range(1, input1+1):
    for j in range(1, input1+1):
        print(input1-j+1,end=" ")
    print()