# Write a program to calculate the factorial of a number using a while loop.
num = 4
if num < 0:
    print("Factorial doesnot exists")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    while num > 1:
        fact = fact * num
        num = num-1
    print(fact)

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# print the tables:
table = int(input("Enter a number: "))
for i in range(1, table + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")