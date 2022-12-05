
#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
userInput = input("Enter a string")
output = {}
list = []

for word in userInput.split(" "):
    for alphabet in word:
        print("Word:{} Alphabet:{}".format(word,alphabet))
        if alphabet in output.keys():
            list = output[alphabet]
            list.append(word);
        else :
            list.append(word)
            output[alphabet] = list
        list = []
        break;

for key in output.keys():
    print(str(key) +" ::: "+ str(output[key]),end="")
    print()


#Python Programming Examples on How to Map Two Lists into a Dictionary

list1 = ["Key1","Key2","Key3","Key4""Key5","Key6","Key7"]
list2 = ["Python","Programming","Learning","in","Python","Practice","Website"]

#************Case 1******************
output = {key:value for key,value in zip(list1,list2)}
print(output)
#************Case 2******************

dictBhavana={}

for i in list1:
    for j in list2:
        dictBhavana[i] = j
        list2.remove(j)
        break;

print(dictBhavana)



#*********************************************************************************************************
#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x, x*x)

# Using LIST Comprehension
input= int(input("Enter the last number in range"))


# output = {x:x**2 for x in range(1,input+1)}
# print(output)
#
# #Using for loop
dict = {}
for i in range(1,input+1):
    dict[i] = i**2

print(dict)


#Python Program to Sum All the Items in a Dictionary

input = {'heello': 27, 'this': 282, 'is': 98, 'BTechGeeks': 98, 'online': 123, 'platform': 32, 'for': 38,
                                 'coding': 10, 'students': 81}

#Using items function
sum =0
for key,value in input.items():
    sum+=value

print("Output = ",sum)

#Using sum function

values_list = input.values()
output_sum = sum(values_list)
print("Output using sum function = ",output_sum)



#Program to Find Product of Values of elements in a Dictionary

input_dict = {'jan': 10, 'Feb': 5, 'Mar': 22, 'April': 32, 'May': 6}
output_product=1

for values in input_dict.values():
    output_product*=values

print("Product of items in dictionary = {}".format(output_product))


#Python Program to invert a Dictionary

dictionary ={"monday":1, "tuesday":2, "wednesday":3}
output={value:key for key,value in dictionary.items()}
print("Output dictionary = ",output)


#Intersection of Two Dictionaries via Keys in Python
dictionary1 = {'Hello': 'one', 'this': 'two', 'is': 'three', 'btechgeeks': 'four'}
dictionary2 = {'good': 'five', 'morning': 'six', 'btechgeeks': 'four', 'is': 'three'}

output = {}

output = {key:dictionary1[key] for key in dictionary1 if key in dictionary2}
print("Output dictionary = ",output)


#How to Remove Duplicates from a Dictionary in Python?

input_dict = {1: 100, 2: 90, 3: 80, 4: 100, 5:80}
output_dict = {}

for key,value in input_dict.items():
    if value in output_dict.values():
        pass
    else:
        output_dict.update({key:value})

print("Bhavana output dictionary = ",output_dict)
