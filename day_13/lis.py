#Exercise 1
#flitering out the negative values
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
num = [i for i in numbers]
print(num[0:4])
print(type(num))
#flattening the numbers in list of list of lists to one dimension
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(type(list_of_lists))
flattened_list = [number for sublist1 in list_of_lists for sublist2 in sublist1 for number in sublist2]

print(flattened_list) 

# #using list comprehension to create a list of tuples
# num2 = [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# ]
# print(num2)
num = [i for i in range(9)]
print(num)

#flattening the contries list in list of tuple with list  comprehension
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_country = [country for sublist in countries for country in sublist]

print(flattened_country)

#changing the following list to list of dictionary
countries2 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries2 = [{'country': country[0], 'capital': country[1]} for sublist in countries2 for country in sublist]
print(countries2)

#changing the name list of list to list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = [' '.join(name) for sublist in names for name in sublist]
print(names_concatenated)
names_dict = [{'name': name[0], 'lastname': name[1]} for sublist in names for name in sublist]
print(names_dict)

#using a lambda function to print slope 
slope = lambda y_intercept, x_intercept: (y_intercept - 0) / (x_intercept - 0)
print(slope(5, 2))

#OUR HELP IS IN THE NAME OF THE LORD 
#THANK YOU LORD FOR TODAY 