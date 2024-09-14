#using functions
#Exercise1

#summation of two numbers

def sum_num(a, b):
  return a + b
   

print(sum_num(5, 7))

#calculating area of a circle
def area_of_circle(radius):
  return 3.14 * radius ** 2

print(area_of_circle(5))

#adding all the numbers
def add_all_numbers(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(add_all_numbers([1, 2, 3, 4, 5]))

#converting temperatures from celcius to ferinheit 
def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))


#creating a function and telling it to  return seasons
def check_season(month):
  month = input("please enter the month: ")
  if month == 3 and month == 5:
    return "Spring"
  elif month == 6 and month == 8:
    return "Summer"
  elif month == 9 and month == 11:
    return "Autumn"
  else:
    return "Winter"
  
season = ["Spring", "Summer", "Autumn", "Winter"]
print(check_season(season))

#calculating the scope of a linear equation
def calculate_slope(y_intercept, x_intercept):
  if x_intercept == 0:
   
   return "the slope is undefined"
  else:
    slope = (y_intercept - 0) / (x_intercept - 0)
    return slope
  
print(calculate_slope(5, 3))


#calculating a solution set for a quadratic equation
import cmath
def solve_quadratic(a, b, c):
  discriminant = b**2 - 4*a*c
  root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
  root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
  return root1, root2

print(solve_quadratic(-54, 21, 8))


#printing out the each element in a list using the def 
def print_list(lst):
  for item in lst:
    print(item)

print_list(["mari", "Elo", "nelo"])

def reverse_list(lst):
  for item in lst:
    lst.reverse()
    print(item)
  

print(reverse_list(["mari", "Elo", "nelo"]))

#capitalizing a list 
def capitalize_list_item(lst):
  for item in lst:
    lst[lst.index(item)] = item.capitalize()
    return lst

print(capitalize_list_item(["mari", "elo", "nelo"]))


#adding an item to list with def 
def add_value(item):
  my_list = ["mari", "elo", "nelo"]
  my_list.append(item)
  return my_list

print(add_value("zara"))

#removing an item from list with def

lst = ["mari", "elo", "nelo", "zara"]
def remove_item(lst, item):
  if item in lst:
    lst.remove(item)
    return lst
  else:
    return "Item not found"
  
print(remove_item(lst, "zara"))


#addition of numbers using def
def add_numbers(a, b):
  return a + b

print(add_numbers(5, 7))

#sum of odd numbers using def
def sum_odd_numbers(lst):
  total = 0
  for num in lst:
    if num % 2 != 0:
      total += num
  return total

print(sum_odd_numbers([1, 2, 3, 4, 5]))

#sum of even numbers using def
def sum_even_numbers(lst):
  total = 0
  for num in lst:
    if num % 2 == 0:
      total += num
  return total

print(sum_even_numbers([1, 3, 4, 6]))

#Exercise 2
#counting number of even and odd numbers using def
def even_and_odd(num):
  even_count = 0
  odd_count = 0
  for i in range(1, num + 1):
    if i % 2 == 0:
      even_count += 1
    else:
      odd_count += 1

  return even_count, odd_count

print(even_and_odd(80))

#returning a factorial
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))

#an empty fuction with def
def empty_function():
  pass

print(empty_function())

# calculation on statistics
import statistics

def calculate_statistics(numbers):
  mean = statistics.mean(numbers)
  median = statistics.median(numbers)
  mode = statistics.mode(numbers)
  return mean, median, mode

print(calculate_statistics([1, 2, 3, 4, 5]))

#writing a function to check if a number is prime
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

print(is_prime(7))

#writting a function that checks if items are unique
def check_unique(lst):
  return len(lst) == len(set(lst))

print(check_unique([1, 2, 3, 3, 4, 5]))

#writing a function to check if the unique items are of the same data type
def check_same_data_type(lst):
  data_types = set(type(item).__name__ for item in lst)
  return len(data_types) == 1

print(check_same_data_type([1, 2, 3, "four", 5]))

#writting a function that checks if a provided variable is a valid python variable
import keyword

def is_valid_variable(variable_name):
  if not isinstance(variable_name, str):
    return False
  if variable_name.isidentifier():
    return not keyword.iskeyword(variable_name)
  return False

print(is_valid_variable("valid_variable"))

#THANK YOU LORD 