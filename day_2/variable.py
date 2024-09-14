#day_2 of python challenge

#variable declaration
first_name = "Mari"
last_name = "Nnanna"
full_name = "Nnanna Mari"
country = "Nigeria"
city = "Abakaliki"
age = 19
year = 2024
is_married = True
is_light_on = True

#declaring multiple variables in a single line
first_name, last_name, full_name, country, city, age  = "Mari", "Nnanna", "Nnanna Mari", "Nigeria", "Abakaliki", 19
print(first_name, last_name, full_name, country, city, age)
print(len(first_name))

#checking data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))

#using the len function
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(country))
print(len(city))

#compare first and last name
print(first_name == last_name)
print(first_name != last_name)
print(first_name > last_name)
print(first_name < last_name)
print(first_name >= last_name)
print(first_name <= last_name)

#comparing the lenght of the first and last name
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) <= len(last_name))

#declaring of numbers
num_one = 5
num_two =3

a = num_one + num_two 
b = num_one - num_two 
c = num_one * num_two
d = num_one / num_two
e = num_one % num_two
f = num_one // num_two
print(a, b, c, d, e, f)

#calcu;ating the area of a circle
pi = 3.14
radius = 30
area = pi * (radius ** 2)
print(area)

#calcu;ating the circumference of a circle
pi = 3.14
radius = 30
circumference = 2 * pi * radius
print(circumference)

#take radius as user input and calculate the area of the circle
pi = 3.14
radius = int(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)
print(area)

#using the built-in function to calculate values
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
full_name = first_name + " " + last_name
print(full_name)
age = int(input("Enter your age: "))



#take radius as user input and calculate the circumference of the circle
radius = int(input("enter radius: "))
circumference = 2 * pi * radius
print(circumference)