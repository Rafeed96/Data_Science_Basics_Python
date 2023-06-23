# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,

expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?

extra_cost = expense[1] - expense[0]
print("Extra dollars spent compared to January: ", extra_cost)

# 2. Find out your total expense in first quarter (first three months) of the year.

sum = 0
for i in range(0,3):
    sum = sum+ expense[i]
    
print("Expenses for the first quarter: ",sum)

# 3. Find out if you spent exactly 2000 dollars in any month

flag = False
print(" ")
for i in expense:
    if i == 2000:
        flag = True

if flag == True:
    print("Yes")
else:
    print("No")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list




# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this