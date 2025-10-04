#experimenting with exceptions
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
except:
    print('Something is not quite right.')

# a similiar example of exception handling
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")

#an example handling multiple exceptions in one clause
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError): #here two exceptions are handled in one clause
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

   #offtopic but understanding this spacing stuff
print("hello", end='🔥 ')
print("world")
     



