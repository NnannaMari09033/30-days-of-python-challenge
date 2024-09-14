#Exercise 1



#python list
thislist = []
this_list = ["banana", 19, "orange", True, "kiwi", 25.5]
print(this_list[0:2:4])
print(this_list)

print(len(this_list)) #using the length fuction
print(thislist)
print(len("kiwi")) #using the length fuction
print(len(this_list)) #using the length function

#using a mixed data type
list = ["Mari", 19, 170, "Mrs"]
list.append(
  {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY"
   } #adding a dictionary to a list
 )
print(list)

Company_list = ["facebook", "twitter", "amazon", "google", "aliexpress", "IBM", "Oracle", "Microsoft"]
print(Company_list)
print(len(Company_list))
print(Company_list[0])
print(Company_list[4])
print(Company_list[7])

Company_list.insert(4,"instagram") #inserting a value to a list
print(Company_list)
#converting a list to a string
str_representation = "facebook", "twitter", "amazon", "google", "aliexpress", "IBM", "Oracle", "Microsoft"
str_representation = str(Company_list) 
print(str_representation)
str_representation.upper()
print(str_representation.upper())
#reconverting a string to a list
# list_from_str = list(str_representation)
# print(list_from_str)

#checking if a certain company exists
if "facebook" in Company_list:
  print("facebook exists in the list")
else:
  print("facebook does not exist in the list")

Company_list.sort()
print(Company_list) #using the sort function
Company_list.reverse()
print(Company_list) #using the reverse function
Company_list.sort(reverse=True)
print(Company_list) #using the sort function that returns values in descending order
print(Company_list[0:3]) #slicing out a section(first three) in Company_list
print(Company_list[-1:]) #slicing out a section(last three) in Company_list
print(Company_list[4])
Company_list.remove("IBM")
print(Company_list) #removing an element from the list
Company_list.pop() 
print(Company_list) #removing an element from the list with the pop function
Company_list.clear()
print(Company_list) #clearing the list

#joining a list
front_end = ["html", "css", "javascript", "react", "git"]
back_end = ["python", "java", "php", "sql", "node.js"]
full_stack = front_end + back_end
print(full_stack)
M = full_stack.copy()
print(M)
full_stack.insert(0, "ruby") #inserting a value 
print(full_stack)



#Exercise 2


age = [19, 20, 19, 24, 30, 45, 50, 21, 25, 26]
age.sort() 
print(age)
#checking for the minimum age

print(min(age))
#checking for the maximum age

print(max(age))
#checking for the average age

print(sum(age)/len(age))

#finding the median age
if len(age) % 2 == 0:
  median1 = age[len(age)//2]
  median2 = age[len(age)//2 - 1]
  median = (median1 + median2) / 2
else:
  median = age[len(age)//2]

#finding the range of the age(min,max)
range_age = max(age) - min(age)
print(range_age)

#comparing the value of the minimum average and maximum average
min_average = sum(age[:len(age)//2]) / len(age[:len(age)//2])
max_average = sum(age[len(age)//2:]) / len(age[len(age)//2:])

print(min_average)
print(max_average)

#finding the range of (maximum minus minimum)
range_max_min = max(age) - min(age)
print(range_max_min)

country = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
#finding the middle country
middle_country = country[len(country)//2]
print(middle_country)

#dividing the country into two parts
country_a = country[:len(country)//2]
country_b = country[len(country)//2:]
print(country_a)
print(country_b)

#creating a dictionary from the country list


country_b = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
C, R, U, F, S, N, D = country_b
print(C)
print(R)
print(U)
print(F)
print(S)
print(N)
print(D)


#THANK YOU LORD FOR TODAY