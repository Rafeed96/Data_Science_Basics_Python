# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it

height = 48.8
width = 92

aread = height * width

print("Area of the football feild is:",aread)



# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?

packets = 9
chips_cost = 1.49
total = packets * chips_cost
dollar = 20
change = dollar - total
print("The shopkeeper will return $",change,"in change")


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square

length = 5.5

area = length * width
tile_cost = 500

total_bathroom_area = length**2
total_cost_for_tile = total_bathroom_area * tile_cost
print("The total cost to replace the bathroom tiles is:",total_cost_for_tile,"Rs")

# 4. Print binary representation of number 17