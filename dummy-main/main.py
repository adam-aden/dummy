print("this is bmi claculater")
while True:
    name = input("enter name")
    if name:
        print()
        break
    else:
        print("enter again")

while True:
    try:
        weight = float(input("enter weight"))
        break
    except ValueError:
            print("enter again")

while True:
    try:
        height = float(input("enter height"))
        break
    except ValueError:
            print("enter again")

bmi = weight / (height / 100) **2
print(f"hi {name}")
print()

print(f"your bmi is {bmi:.2f}")
print()

if bmi < 18.5:
    print("skinny")
elif bmi < 24:
    print("normal")
elif bmi < 29.9:
    print("fat")
else:
    print("too fat")
