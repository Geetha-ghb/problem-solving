# GCD OF TWO NUMBERS:
a = 24
b = 32
gcd = 1 
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i 
print("GCD:" , gcd)

# LCM OF TWO NUMBERS:
a = 15
b = 20
for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print("LCM:", i)  
        break
# SUM OF NON-PRIME NUMBERS:
start = 1
end = 20
non_primes = 0
for num in range(start, end + 1): 
    if num < 2:  
        non_primes += num
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break
    if not is_prime: 
        non_primes += num
print("SUM OF NON-PRIME NUMBERS:",non_primes)

# SUM OF ODD DIGITS:
num = 123456789 
sumodd = 0  
while num > 0:
    digit = num % 10  
    if digit % 2 != 0:  
        sumodd += digit
    num //= 10  
print("SUM OF ODD DIGITS:",sumodd)

# PERFECT NUMBER:A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
#  Example : Perfect Number 28
# Divisors of 28 (excluding itself) → 1, 2, 4, 7, 14
# Sum of divisors = 1 + 2 + 4 + 7 + 14 = 28

num = 28 
sum = 0 
for i in range(1,num):
    if num % i == 0:  
        sum=sum + i
if sum == num:
    print("is a Perfect Number")
else:
    print ("is NOT a Perfect Number")



