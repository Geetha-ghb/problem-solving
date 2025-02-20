# Write a program to find the greatest of three numbers:
a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
if a >= b and a >= c:
    print(a,"is a greatest number")
elif b >= a and b >= c:
    print(b,"is a greatest number")
else:
    print(c,"is a greatest number")

# Check if a year is a leap year:

year = int(input("enter the year"))
if year % 4 == 0:
    print(year, "is a leap Year")
elif year % 400 == 0:       
    print(year, "is a leap year")
else:
    print("Not a leap year")

# Calculate the grade of a student based on the marks they score:

score = float(input("Enter the number"))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
else:
    print("Fail")

# Write a program to check if three sides length form a valid triangle.

a = float(input("Enter the number"))
b = float(input("Enter the number"))
c = float(input("Enter the number23"))
if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        print("The given sides form a valid triangle")
    else:
        print("The given sides do not form a valid traingle")
else:
    print("Invalid")