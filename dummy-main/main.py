print("this is bmi claculater")

name = input("enter name")
weight = float(input("enter weight"))
height = float(input("enter height"))

bmi = weight / (height / 100) **2
print(f"your bmi is {bmi:.2f}")

if bmi < 18.5:
    print("skinny")
elif bmi < 24:
    print("normal")
elif bmi < 29.9:
    print("fat")
else:
    print("too fat")