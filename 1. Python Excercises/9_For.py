# 1. After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
tails = 0

for i in result:
    if i == "heads":
        heads = heads + 1
    else:
        tails = tails + 1
print(heads)
print("")

# 2. Print square of all numbers between 1 to 10 except even numbers
val = 0
for i in range(1,11):
    if i % 2 == 1:
        val = i**2
        print(val)
print("")

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]

months = ["Jan", "Feb", "Mar", "Apr", "May"]

expense = 298
flag = False
n = len(expense_list)
print("")
for i in range(0, n):
    if expense == expense_list[i]:
        print(months[i])
        flag = True

if flag == False:
    print("No monthly expense matched !!")





# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

res = ""
f = False
for i in range(1,6):
    print("You completed",i,"km. Are you tired?")
    res = input()

    if res == "yes":
        print("you didn't finish the race")
        f = True
        break
        
    elif res =="no":
        print("great, keep going!!")

if f == False :
    print("Congratulations")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
print("")
for i in range(5):
    for j in range(5):
        if i>=j:
            print("*",end=" ")
    print("")
