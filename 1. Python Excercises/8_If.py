## Exercise: Python If Condition
# 1.1 Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = 'Dhaka'
city = city.lower()

if city in india:
    print("You are in India")
elif city in pakistan:
    print("You are in Pakistan")
elif city in bangladesh:
    print("You are in Bangladesh")
else:
    print("You are in planet Earth")

print("")

## Exercise: Python If Condition
# 1.2 Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#     Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = "dhaka"
city2 = "karachi"

if city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
elif city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
else:
    print("They don't belong to same country")



## Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

