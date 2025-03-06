# 1. Find the sum of odd digits in a given number

n=int(input("enter the numbers:"))
odd_sum = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 1:
        odd_sum += digit
    n //= 10
print("sum of odd digits in a given number",odd_sum)    

# 2. Print all the Armstrong numbers in given range:
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in range(start, end + 1):
    a = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** a
        temp //= 10
    if num == sum:
        print(num)
        
# 3. Find the smallest prime digit in a given number

num = int(input("Enter a number: "))
smallest_prime_digit = 10
while num > 0:
    digit = num % 10
    if digit in (2, 3, 5, 7) and digit < smallest_prime_digit:
        smallest_prime_digit = digit
    num //= 10
if smallest_prime_digit == 10:
    print("No prime digits found.")
else:
    print("The smallest prime digit is:", smallest_prime_digit)
