#concatenating strings
a = "thirty "
b = "days "
c = "of "
d = "python "
print(a, b, c, d)

e = "coding "
f = "for "
g = "all "
together = e + f + g
h = together + "comapny "
print(together)
print(h)
print(len("company"))


#using build_in functions
h.upper()
print(h.upper())
h.lower()
print(h.lower())
together.capitalize()
print(together.capitalize())
together.swapcase()
print(together.swapcase())
together.title()
print(together.title())
print(together[0:6]) #slicing values
#checking if a value is in coding for all
together.find("coding")
print(together.find("coding"))
print(together.replace("coding", "python"))
print(together.split())
socialmediaplatform = "facebook, google, microsoft, apple, ibm, amazon"
socialmediaplatform.split()
print(socialmediaplatform.split())
print(together[0])
print(together[1])
print(together[-4])
MAN = "CODING FOR EVERYONE "
print(MAN[0])
print(MAN[4])
print(MAN.rfind("f"))
rfm = "you cannot end a word with because because because is a conjuncion "
print(rfm[27:35])
print(rfm.rindex("b"))
print(rfm.rindex("on"))
print(rfm[27:50]) #coding for all supports substring
#removing trailing whitespace
print(rfm.strip())
i = "30daysofpython"
j = "30_days_of_python"
print(i.isidentifier())
print(j.isidentifier())
framework = ["python","css","javascript","c##", "c++"]
result = " ".join(framework)
print(result)
mari = ("i\nam\nenjoying\nthis\npython\nchallenge\n") #using escape sequence new line
print(mari)
elo = "i\n just\n wonder\n what\n is\n next\n" #using escape sequence new line
print(elo)
print("name\tage\tcountry\t city\tstate\t") 
print("mari\t19\tnigeria\t abakaliki\tebonyi\t") #tab means 8 spaces

#using string formatting mmethod to calculate the area of a circle
radius = 5
pi = 3.14
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f}.")
a = 8
b = 6
print(f"{a} + {b} = {a} + {b}")
print(f"{a} - {b} = {a} - {b}")
print(f"{a} * {b} = {a} * {b}")
print(f"{a} / {b} = {a} / {b}")
print(f"{a} % {b} = {a} % {b}")
print(f"{a} ** {b} = {a} ** {b}")
print(f"{a} // {b} = {a} // {b}")
print(f"{a} & {b} = {a} & {b}")
print(f"{a} | {b} = {a} | {b}")
print(f"{a} ^ {b} = {a} ^ {b}")
#we did it lol





#using f-string to format strings
name = "John"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

