#Q1) Function to count upper and lower case letters in a string

def count_case(s):
    upper_count = 0
    lower_count = 0
    for ch in s:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    return upper_count,lower_count
s= "Welcome to Bank Of America!"
count_case(s)
print(count_case(s))

#Q2) Write a Python function that takes a list and returns a new list with distinct elements

def remove_dups(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list
print(remove_dups([1,2,2,4,4,10,10,10]))

#Q3) Write a function that checks whether a number is prime or not

def is_prime(num):
    if num < 1:
        return "Not a prime number"
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime number"
    return "Prime"
print(is_prime(2))

#Q4) Write a Python function that takes a list of numbers and prints the even numbers from the list

def print_even(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)
print_even([1,2,3,4,5,6,7,8,9,])

#Q5) Write a function that checks whether a string is a palindrome or not

def is_palindrome(s):
    reversed_string = s[::-1]
    if s == reversed_string:
        return ("Palindrome")
    else:
        return ("Not a palindrome")
print(is_palindrome("madam"))
print(is_palindrome("Rashid"))

#Q6) Write a function that takes a string containing Python code and executes it

def run_code(code):
    exec(code)

run_code("print('hello Rashid')")

#Q7) Write a Python function that takes a list and two indices, and swaps the elements at those indices

def swap_elements(lst,i1,i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
    return lst
print(swap_elements([10,20,30,40],1,3))

#Q8) Write a Python function that calculates the length of a given list

def list_length(my_list):
    length = len(my_list)
    return length
print(list_length([1,2,3,4]))

#Q9) Write a Python function that takes two numbers and returns the maximum of the two

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(maximum(10,5))
print(maximum(15,20))

#Q10) Write a Python function that takes two numbers as parameters and returns the minimum of the two

def maximum(a,b):
    if a < b:
        return a
    else:
        return b
print(maximum(10,5))
print(maximum(15,20))

#Q11) Write a Python function that takes a string, splits it into words, reverses the order of words, and returns the reversed string.

def reverse_words(s):
    words = s.split()
    rs = words [::-1]
    fs = " ".join(words[::-1])
    return fs
print(reverse_words("Hello Rashid"))