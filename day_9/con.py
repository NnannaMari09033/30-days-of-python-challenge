#Conditional statements
#Exercses 1
 
age = int(input("enter your age: "))
if age >=18:
  print("congratulations!, you are eligible to vote")
else:
  print("sorry, you are not eligible to vote")

#comparison using conditional statements
my_age = int(input("enter your age: "))
your_age = int(input("enter your age: "))
if my_age > your_age:
  print("you are older than me with " " year ")
  my_age += 1
  your_age += 1
  print(my_age - your_age)
elif my_age == your_age:
  print("you are the same age as me")
  my_age += 1
  your_age += 1
  print(my_age - your_age)
else:
  print("you are younger than me with " " years ")
  my_age += 1
  your_age += 1
  print(my_age - your_age)


#comparison with numbers
first_num = int(input("enter the number: "))
second_num = int(input("enter the number: "))


if first_num > second_num:
  print(f"{first_num} is greater than {second_num}")
elif first_num == second_num:
  print(f"{first_num} is equal to {second_num}")
else:
  print(f"{second_num} is greater than {first_num}")


#Exercise 2

student_score = int(input("enter the score: "))


if student_score >= 100:
  print("exellent score, Grade: A")
elif student_score >= 80:
  print("very good score, Grade: B")
elif student_score >= 60:
  print("good score, Grade: C")
elif student_score >= 40:
  print("average score, Grade: D")
else:
  print("bad score, Grade: F")



#comparing seasons using a conditional statement

month = int(input("enter the month (1-12) "))


if month == 12 or month == 1 or month == 2:
  print ("Winter")
elif month == 9 or month == 10 or month == 11:
  print("Autum")
elif month == 3 or month == 4 or month == 5:
  print("Spring")
elif month == 7 or month == 8:
  print("Summer")
else:
  print("invalid")


#using dictionary for conditional statement
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
  print('skills' in person)
else:
  print('skill not in person')

#printing out the content of skills in the person dictionary
print(person['skills'][2])

print(person['skills'][0:4])

#using conditional statements to determine if the person 'skills' contains some values

if 'Javascript'and 'React' in person['skills']:
  print('Congratulations!! you are a frontend developer')
  if 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('yayyyy!!!, you are a backend developer')
  if 'skills' in person:
    print('Congratulations, you are a full_stack developer')
else:
  print('You are not a developer')

#using a boolean in declaring a conditional statement
if 'is_married' in person:
  print('you are incorrect')
else:
  print(print('my name is ' + person['first_name'] + ' ' + person['last_name'] + ' and I live in ' + person['country'] + '.'))

#adding a value in a list using conditional statement
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'grape' in fruits:
  print('grape is already in the list')
else:
  fruits.append('grape')
  print(fruits)


#THANK YOU LORD FOR TODAY