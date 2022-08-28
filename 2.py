import array

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

# array vs list **
a = array.array('i', [1, 2, 3])
for i in a:
    print(i,end="")


# a = array.array('i', [1, 2, 3,'string'])
# for i in a:
#     print(i,end="")

# LIST**
print("\n")
print("List...")
b=[1,2,3,"string"]
for item in b:
    print(item)















