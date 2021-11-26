# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height ** 2)

if BMI < 18:
  message = "You are underweight."

elif BMI < 22:
  message = "You are normal weight."

elif BMI < 28:
  message = "You are slightly overweight."

elif BMI < 33:
  message = "You are obses."

else:
  message = "You are clinically obses."

  


print(f"Your BMI is {BMI}, {message}")



