#declaring variables
Age = 19
Height = 170.5
vector = 2 + 10j

#calculating the area of a triangle
triangle_base = int(input("enter the base of the triangle: "))
triangle_height = int(input("enter the height of the triangle: "))
area_of_triangle = 0.5 * triangle_base * triangle_height
print(area_of_triangle)

#calculating the perimeter of a triangle
side_1 = int(input("enter the side of the triangle: "))
side_2 = int(input("enter the side of the triangle: "))
side_3 = int(input("enter the side of the triangle: "))
perimeter_of_triangle = side_1 + side_2 + side_3
print(perimeter_of_triangle)

#calculating the area of a rectangle
lenght = int(input("enter the length of the triangle: "))
width = int(input("enter the width of the triangle: "))
area_of_rectangle = lenght * width
print(area_of_rectangle)

#calculating the perimeter of a rectangle
lenght = int(input("enter the length of the triangle: "))
width = int(input("enter the width of the triangle: "))
perimeter_of_rectangle = 2 * (lenght + width)
print(perimeter_of_rectangle)

#calculating the radius of the circle
pi = 3.14
radius = int(input("enter the radius of the triangle: "))
area_of_circle = pi * (radius ** 2)
print(area_of_circle)

#calculating the circumference of the circle
pi = 3.14
radius = int(input("enter the radius of the triangle: "))
circumference_of_circle = 2 * pi * radius
print(circumference_of_circle)

#calculating slope
x_intercept = int(input("enter the x-intercept of the triangle: "))
y_intercept = int(input("enter the y-intercept of the triangle: "))
slope = y_intercept / x_intercept
slope = 2 * x_intercept - 2
print(slope)
 
#calculating gradient 
x_intercept1 = 2
y_intercept1 = 2
x_intercept2 = 6
y_intercept2 = 10
gradient = (y_intercept2 - y_intercept1) / (x_intercept2 - x_intercept1)
print(gradient)

#calculating the euclidean distance
x1 = 2
y1 = 2
x2 = 6
y2 = 10
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(euclidean_distance)

#comparing between the slopes in # line 43 and line 50
x_intercept1 = 2
y_intercept1 = 2
x_intercept2 = 6
y_intercept2 = 10
gradient1 = (y_intercept2 - y_intercept1) / (x_intercept2 - x_intercept1)
gradient2 = 2 * x_intercept - 2

#random values
x = 2
y = 3
sum = y*(x**2 + 6*x + 9)
print(sum)

#using the length function
list = ["python", "dragon"]
print(len(list[0]))

#making a false statement
list = ["python", "dragon"]
if "python" in list:
  print("true")
elif "dragon" == "python":
  print("true")
else:
  print("false")

#using and operators
a = "dragon"
b = "python"
if 'on'in "dragon" and "python":
  print("true")
else:
  print("false")

#using the in operator
a = "dragon"
b = "python"
if 'on'in "dragon":
  print("true")
else:
  print("false")

#float and string convert
a = "dragon"
b = "python"
print(len(b)) #printing the length
#string to float no gree

#checking if a number is even or not using python
varname = 4
if varname % 2:
  print("odd")
else:
  print("even")

#checking with floor divison
a = 7 // 3
b = 2.7
print(a)
if 7 // 3 == 2.7:
  print("true")
else:
  print("false")

#checking data type
a = 10
b = "10"
c = 9.8
print(type(a))
print(type(b))
print(type(c))
if c == a:
  print("true")
else:
  print("false")

#using input functions
work_hours = int(input("enter the number of work hours: "))


