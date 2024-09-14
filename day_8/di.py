#exercise1
dog = {
  "name": "mari",
  "color": "black",
  "breed": "mammal",
  "leg": "two",
  "age": 19
} #creatng an  dog dictionary
del dog 

student = {
  "first_name": "nnanna",
  "last_name": "mari",
  "age": 19,
  "grade": 12,
  "major": "computer science",
  "marital_status": "miss",
  "skill": "crocheting",
  "address": {
    "country": "nigeria",
    "state": "ebonyi",
  }
} #creating a student dictionary that has a nested dictionary

print(len(student)) #using the len function
print(student.get("skill")) #using the get function
#getting the data type the student ("skill") is
print(type(student.get("skill")))

#modiying the data type the student ("skill") 
student["skill"] = "cooking", "studying"
print(student) #printing the updated dictionary

lst = list(student)
print(student) #printing the updated dictionary

#using the item method 
print(student.items())

#deleting an item in a dictionary
del student["skill"]
print(student)


#THANK YOU LORD FOR TODAY
