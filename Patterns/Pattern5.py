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


#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A
#J I H G F E D C B A

input1 = int(input("Enter the number of rows"))

for i in range(input1):
    for j in range(input1):
        print(chr(input1+64-j), end=" ")
    print()