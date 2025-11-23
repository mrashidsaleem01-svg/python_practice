"""
QT] Print employee age and salary.
emp_age = 30
emp_salary = 45000.75
"""

emp_age = 30
emp_salary = 4500.75
print(emp_age, emp_salary)
"""
QT] What is the data type of each variable?
a = 10
b = 10.5
c = "Hello"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {7, 8, 9}
h = {"name": "Faizan", "age": 25}
i = None
"""

a = 10
b = 10.5
c = "Hello"
d = True
e = [1, 2, 3]
f = (4, 5, 6)
g = {7, 8, 9}
h = {"name": "Faizan", "age": 25}
i = None

print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

"""
QT ]Convert Data Types
Write a Python program to convert:
● Integer to float
● Float to integer
● Integer to string
● String to integer
"""

a= 10
print (float(a))

b=10.5
print (int(b))

c= 15
print(str(c))
print(type(str(c)))

d= "10"
print(int(d))

"""
QT]
employee = {
"name": "sana",
"age": 27,
"department": "IT",
"salary": 50000
}
1]Print employee name.
2]Print employee salary.
3]Add a new key "city": "Mumbai".
4]Update salary to 55000.
5]Delete the "department" key.
6]Print all keys.
7]Print all values.
8]Use .get("age") to access age.
"""

employee = {
"name": "sana",
"age": 27,
"department": "IT",
"salary": 50000
}

print(employee["name"])
print(employee["age"])
employee.update({"city": "Mumbai"})
employee.update({'salary': 55000})
del employee["department"]
print(employee)
print(employee.keys())
print(employee.values())
print(employee.get("age"))
employee.update({"bonus": "5000"})
print(employee)
newdic_emp=employee.copy()
print(newdic_emp)

"""
QT] employees = ["Ali", "Sara", "Faizan", "Afsha"]
1] Print the first employee.
2] Print the last employee.
3] Add "Rafay" to the list.
4] Remove "Sara" from the list.
5] Change "Ali" to "Ahmed".
6] Print total number of employees.
7] Sort the list alphabetically.
8] Print employees from index 1 to 3.
"""

employees = ["Ali", "Sara", "Faizan", "Afsha"]

print(employees[0])
print(employees[-1])
employees.append("Rafay")
print(employees)
employees.pop(1)
print(employees)
employees[0]= "Ahmed"
print(len(employees))
print(sorted(employees))
print(employees[1:3])


"""
1] Print the second department.
2] Print the last department.
3] Check if "IT" is in the tuple.
4] Find the index of "Finance".
5] Count how many times "HR" appears.
"""
departments = ("HR", "Finance", "IT", "Marketing")
print(departments[1])
print(departments[-1])
print("IT" in departments)
print(departments.index("Finance"))
print(departments.count("HR"))