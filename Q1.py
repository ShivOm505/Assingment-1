# Make a Calculator that will do all the four basic operation at once by taking two numbers as a input at a time

val1 = float(input("Enter the first number: "))
val2 = float(input("Enter the first number: "))

print("The Sum of the numbers is : ", val1 + val2)

print("The Subtraction of the numbers is : ", val1 - val2)

if val2 == 0:
    print("The Division of the numbers is not possible with denominator 0 ")
else:
    print("The Division of the two numbers : ", val1 / val2)

print("The Multiplication of two numbers is : ", val1 * val2)


