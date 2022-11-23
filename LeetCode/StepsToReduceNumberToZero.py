input1 = int(input("Enter a number"))

steps = 0
while input1 > 0:
    if(input1%2 == 0):
        input1 = input1/2
    else:
        input1 = input1-1
    steps = steps+1

print("Total steps = ",steps)