#Exerciise 1

nums = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10
]

#using loops
even_nums = []
for n in nums:
  if n % 2 == 0:
    even_nums.append(n)
print(even_nums)
#using a for loop
for num in nums:
  print(num)
  if num == 9:
    break

#using a while loop

i = 1
while i <= 10:
  print(i)
  i += 1
  if i == 6:
    break

#iterating from 10 to 0
for i in range(10, -1):
  print(i)

i = 10
while i >= 0:
  print(i)
  i -= 1

#writung a loop that makes 7 calls to print
from functools import reduce 
words= "A", "stitch", "in", "time", "saves","nine", "but", "does", "not", "save", "you"
def combine_words(inital_value, words):
  print("inital_value" + "___ " + words)
  return inital_value + " " + words

result = reduce(combine_words, words)

print(result)

#using nested loops to create ######
for i in range(5):
  for j in range(5):
    print("# ", end=" ")

  print()

#telling a number to multiply itself using loops
# I DON'T GET IT 


#Iterating over a list using loop
list1 = ["Python", "Numpy","Pandas","Django", "Flask"]
for i in list1:
  print(i)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
even_nums = []
odd_nums = []
sum_nums = []
sum_nums_odd = []
sum_nums_even = []
for n in nums:
  if n % 2 == 0:
    even_nums.append(n)
    print(even_nums)
  else:
    print(n)
  
for n in nums:
  if n % 2 != 0:
    odd_nums.append(n)
    print(odd_nums)
  else:
    print(n)

  sum_nums.append(n)
  print("Sum of numbers:", sum(sum_nums))
  sum_nums_odd.append(n) if n % 2!= 0 else None
  sum_nums_even.append(n) if n % 2 == 0 else None
  print("Sum of odd numbers:", sum(sum_nums_odd))
  print("Sum of even numbers:", sum(sum_nums_even))
 
#Using list comprehension to create even and odd numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
even_nums = [n for n in nums if n % 2 == 0]
odd_nums = [n for n in nums if n % 2 != 0]

print(even_nums)
print(odd_nums)


countries = [
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

#printing countries with land at the end
for country in countries:
  if country.endswith('land'):
    print(country)


#reversing the order of list using loops
list1 = ["Python", "Numpy","Pandas","Django", "Flask"]
reversed_list = []
for i in range(len(list1)-1, -1, -1):
  reversed_list.append(list1[i])

print(reversed_list)

#THANK YOU GOD
