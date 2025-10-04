#basic bmi calculator
def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))
print(bmi(62,1.70))
print(bmi(75,1.85))

#extended version of the bmi calculator that checks for irregular inputs
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

#using feet and inches and pounds
#has two functions one for converting pounds to kg and feet and inches to meters
# then returning the bmi

def ft_and_inch_to_m(ft, inch = 0.0): #there is a fixed point value for inch if you dont want to enter it
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None   #returns nothing if the input is invalid

    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) #invocation of a multi-parameter function

