#Exercise 1
thistuple = () #creating an empty tuple 
brother = ("prince", "nelsom", "junior", "divine", "wilson")
sister = ("nelo", "unni", "amaka", "nnenna", "mari")
sibling = brother + sister #joining tuple together
print(sibling)
print(len(sibling)) #using the len function
parents= ("Augustina", "Nicolas")
family_members = sibling + parents
print(family_members)


#Exercise 2
#unpacking the sister and brother tuple
sister_name, *sister_rest = sister
brother_name, *brother_rest = brother

fruits = ("apple", "orange", "kiwi", "banana")
vegetable = ("tomato", "carrot", "strawberry")
animal_product = ("chicken", "goat", "monkey", "cow")
food_stuff = fruits + vegetable + animal_product 
print(food_stuff)

#converting a tuple to a list
food_list = list(food_stuff)
print(food_list)
print(food_list[-6])
print(food_list[0:3])
del food_list


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#using conditional statements
if "Estonian" in nordic_countries: 
  print("Estonian is a country in Nordic countries.")
else:
  print("Estonian is not a country in Nordic countries.")

if "Iceland" in nordic_countries:
  print("Iceland is a country in Nordic countries.")
else:
  print("Iceland is not a country in Nordic countries.")

#THANK YOU LORD FOR TODAY