#interactive version of bubble sort
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: ")) #the number of elements

for i in range(num):
    val = float(input("Enter a list element: ")) #prompts the use to enter the elements as much as the number they specified
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1): #it iterates through the list
        if my_list[i] > my_list[i + 1]: #it compares the current element with the next element
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

