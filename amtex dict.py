#dictionary
#we can access it by key and values

students={"name":"vicky","age":25,"course":["maths","english"]}
students["phone"]=7373139358 #to add the new value in dictionary
print(students)
print(students["name"])
print(students.get("phone"))

#to delete the dictionary
students.pop("name") #using pop delete method
print(students)

del students["age"] # using del method we delete it
print(students)

#to access the key and value using for loop
for key,values in enumerate(students.items()):
    print(key,values)