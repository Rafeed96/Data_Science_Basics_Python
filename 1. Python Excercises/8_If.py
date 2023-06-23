## Exercise: Python If Condition
# 1. Using following list of cities per country,
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