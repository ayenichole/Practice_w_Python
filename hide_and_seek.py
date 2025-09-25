import time

# Write a for loop that counts to five.
for i in range(0,6):

    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississipi")
    # Body of the loop - use: time.sleep
    time.sleep

# Write a print function with the final message.
print("Ready or not, here I come!")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

