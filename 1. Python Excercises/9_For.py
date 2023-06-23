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

