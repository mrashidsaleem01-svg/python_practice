"""
QT 1 – Even & Odd
Print only even numbers from 1 to 10.
Print only odd numbers from 1 to 10.
Print all even numbers from 1 to 25, but SKIP numbers divisible by 10.
"""

for i in range(1,10):
    if i % 2 == 0:
        print(i)

for i in range(1,10):
    if i % 1 == 0:
        print(i)

for i in range(1,25):
    if i % 10 == 0:
        continue
    if i % 2 == 0:
        print(i)

"""
QT 2 – If / Elif / Else
** Take a number from user and check:

"Positive"

"Negative"

"Zero"**

Ask user for age and print:

"Child" (age < 13)

"Teen" (13–19)

"Adult" (20–60)

"Senior" (above 60)
"""
"""
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


Age = int(input("Enter your age: "))
if Age <= 13:
    print("Child")
elif Age >= 13 and Age <= 19:
    print("Teen")
elif Age >= 20 and Age <= 60:
    print("Adult")
else:
    print("Senior")
    
"""
"""
QT 3 – For Loop Practice
Print numbers 1 to 20 using a for loop.
Print the following pattern using nested loops:
*
* *
* * *
* * * *
Print multiplication table of 5.
"""

for i in range (1,21):
    print (i)

for i in range (1,5):
    for j in range (i):
        print ("*",end=" ")
    print()

for i in range (1,11):
    print (5,"x",i, "=", 5*i)

"""
QT print the marks of every subject for every student.


students = ["rasmo", "Abimir", "DJQ"]
subjects = ["BI", "crypto", "Areamkt"]

for student in students:
    print("student:",student)

    for subject in subjects:
        print("- Subject:",subject)
    print()

emp = {
    "rasmo": ["BI", "SQL", "Excel"],
    "abimir": ["crypto", "blockchain"],
    "DJQ": ["petro", "analysis"]
}

for employee,skills in emp.items():
    print("EMP:",employee)
    for skill in skills:
        print("SKILL:",skill)
    print()
"""

"""
QT 5 – Break & Continue
Print numbers from 1 to 20, but stop the loop when number reaches 12.
Print numbers from 1 to 15, but SKIP multiples of 3.
"""

for i in range(1,20):
    if i == 12:
        break
    print (i)

for i in range(1,15):
    if i % 3 == 0:
        continue
    print (i)

"""
Given the list:
nums = [10, 25, 30, 45, 50]
Print each number and identify if it is Even or Odd.
"""

nums = [10, 25, 30, 45, 50]

for num in nums:
    if num % 2 == 0:
        print(num,"is an Even number",)
    else:
        print(num,"is an Odd number",)

"""
Given the dictionary:
student = {"name": "Rafay", "marks": 85, "city": "Karachi"}
Print the name
Add a new key: "course": "Python"
Update marks to 90
"""
student = {"name": "Rafay", "marks": 85, "city": "Karachi"}

print(student["name"])
student.update({"course": "python"})

student.update({"marks":90})
print(student)