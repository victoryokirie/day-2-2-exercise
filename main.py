

#Write your code below this line 👇


print("Welcome to the BMI Calculator!")

height = float(input("Please input your height in metres: "))
weight = float(input ("Please input your weight in Kg: "))
height_square = height ** 2

BMI = weight / height_square
BMI_rounded = round(BMI, 1)

print(f"Your BMI is {BMI_rounded} kg/m2")







