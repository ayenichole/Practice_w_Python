#check if the year is a leap year or not
def is_year_leap(year):
    
    if (year % 4 == 0):
        return True
    else:
        return False
    
print (is_year_leap(1900))
print (is_year_leap(2000))
print (is_year_leap(1987))
print (is_year_leap(2016))

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
        

# a better and more accurate version for checking a leap year
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
        
print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2016))
print(is_year_leap(1987))

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
