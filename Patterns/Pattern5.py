#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J

input1 = int(input("Enter the number of rows"))
input2 = int(input("Enter the number of columns"))

for i in range(1, input1+1):
    print(str(chr(64+i))*input2)


#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J
#A B C D E F G H I J

input1 = int(input("Enter the number of rows"))
input2 = int(input("Enter the number of columns"))

for i in range(1, input1+1):
    for i in range(1, input2 + 1):
        print(str(chr(64+i)),end="")
    print()