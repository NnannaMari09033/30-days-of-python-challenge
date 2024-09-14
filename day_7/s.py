#Exercise 1
it_companies = {"Amazon", "Facebook", "Google", "Instagrm"}
print(len(it_companies))  #using the len function
print(it_companies)
it_companies.add("Twitter") #using the add function
print(it_companies)
it_companies.remove("Google") #using the remove function
print(it_companies)


#difference between remove and discard functions
#it_companies.remove("Instagram") #this will raise an error if the element is not in the set
print(it_companies)
it_companies.discard("Instagram") #this will not raise an error if the element is not in the set
print(it_companies)
# to dicard means to get rid of something that is no longer desireable
# to remove means to take something away from the position it occupies

#Exercise 2
A = {"apple", "banana", "cherry", "cheese", "mango"}
B = {"pear", "egg", "kiwi", "orange", "pear"}
C = A | B 
print(C) #union of sets
A.intersection(B)
print(A) #intersection of sets
#checking for disjoint set using an if statement
if A.isdisjoint(B):
    print("A and B are disjoint")
else:
    print("A and B are not disjoint")
A.isdisjoint(B)
print(A) #disjoint of sets
D = B | A 
print(D) #symmetric difference of sets
del D


#Exercise 3
age = 19
print(age)
made = {"me", "she", "her"}
#converting set to list
made_list =list(made) 
print(made_list)

#spliting a set into two eual parts
half = len(made_list) // 2
first_half = made_list[:half]
second_half = made_list[half:]
print(first_half)
print(second_half)
v = {"I am a teacher and I love to inspire and teach people"}
half = len(v) // 2
#first_half = v[:half]
#second_half = v[half:]
print(half)
#print(second_half)


#THANK YOU LORD FOR TODAY!!!!







