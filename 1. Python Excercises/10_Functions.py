# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is

def calculate_area(base, height):
    area = (1/2)*base*height

    return area

print(calculate_area(5,6))


# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,

def calculate_area2(base, height, shape="triangle"):

    if shape == "triangle":
        area = (1/2)*base*height
    elif shape == "rectangle":
        area = base*height
    else:
        area = (1/2)*base*height

    return area

print(calculate_area2(4,6,"rectangle"))

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***

def shape(num):
    for i in range(0,num):
        for j in range(0,num):
            if i>=j:
                print("*",end=" ")
        print("")

shape(3)