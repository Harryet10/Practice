print(bool(1))  
print(bool("hello"))  
print(bool([1, 2, 3]))  

print(bool(0))  
print(bool(""))  
print(bool([]))  

x = 20
print(x != 50)
print(x==20)

number = 10
if number > 5:
    print("Number is greater than 5.")

    number = 10

if number > 10:
    print("Number is greater than 10.")
elif number > 5:
    print("Number is greater than 5 but not greater than 10.")
else:
    print("Number is 5 or less.")


score = 85

if score >= 70:
    grade = 'Distinction'
elif score >= 60:
    grade = 'Merit'
elif score >= 50:
    grade = 'Pass'
else:
    grade = 'Fail'
print(f"Your grade is {grade}.")

count = 0
while count < 10:
    print("Count is:", count)
    count += 1



count = 0
while True:
    print(count)
    count += 1
    if count >= 3:
         break
print("loop ended")