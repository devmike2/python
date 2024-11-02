import math
# num = 4

# num2 = 5
# p= num + num2

# print(p)

# var1 = 10
# var2 = 20
# multiply = var1 * var2

# print(multiply)


#========================== BODY WEIGHT CALCULATOR ==============================
weight = float(input("enter your weight"))
height = float(input('enter your height in ft'))
heightInMeter = height * 0.3048
BMI = weight/ math.pow(heightInMeter, 2) 

if (BMI < 18.5):
    print(F'your BMI  is {BMI}, you are underWeight: ')
elif (BMI >=18.5):
    print(F'your BMI  is {BMI}, you are Normal weight:')
elif (BMI >= 25):
    print(F'your BMI  is {BMI}, you are Over weight: ')
elif (BMI >= 30):
    print(F'your BMI  is {BMI}, you are Obese class I: ')
elif (BMI >= 35):
    print(F'your BMI  is {BMI}, you are Obese class II: ')
else:
    print(F'your BMI  is {BMI}, you are Obese class III: ')