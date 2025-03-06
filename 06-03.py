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

num = (input("Enter a number: "))
smallest_prime = None
for digit in num:
    digit = int(digit)  
    if digit > 1:  
        is_prime = True
        for i in range(2, digit):
            if digit % i == 0:
                is_prime = False
                break
        
        if is_prime:
            if smallest_prime is None or digit < smallest_prime:
                smallest_prime = digit

if smallest_prime is not None:
    print("Smallest prime digit in the given number:", smallest_prime)
else:
    print("No prime digit found in the given number")
