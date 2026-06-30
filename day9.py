#Strings 
#A sequence of characters. 
word="Python"
#creating strings.'',"",""""""
city='Nairobi'
#triple quotes: for strings that goes multiple lines
message="""Welcome to Python.
Today we are going to learn strings.
Strings are used to stoore text"""
print(message)
#User input:input()=>always give us a string
# username=input("Enter your username: ")
# print(type(username))
#accessing characters in a string
print(message[-1])
word="Jython"
print(word)
#slicing:means getting a part of a string 
#syntax:string[start:stop],string[start,stop,step]
print(word[0:3])
print(word[:4])
print(word[3:])
print(word[:])
print(city[1:6:])# Nairobi=airob
#concatenation: joins strings together 
first_name="Tereziah"
last_name="Mpaera"
full_name=first_name + " " + last_name
print(full_name)
age=25
response="Age: " + str(age)
print(f"Age: {age}")
user="lina_k"
course="Python"
level="Beginner"
print(f"Welcome {user}.You are learning {course} at {level} level")
price=4500.638
print(f"The price of this product is: {price:.2f}")

#upper
print(user.upper())
#lower
print(course.lower())
#title
text="python basics"
print(text.title())
#capitalize
print(text.capitalize())
#strip()removes spaces from the beginning and end of the string
username = "  lina_k  "
print(username)
clean_username=username.strip()
print(clean_username)
#find()returns the index where a value starts
feedback="Learning Python is fun"
print(feedback.find("Javascript"))
#split() break a string into a list
skills="Python,Django,Html,CSS,Javascript"
skills_list=skills.split(",")
print(skills_list)
new_feedback=feedback.replace("Python","Javascript")
print(new_feedback)
#memebership(in and not in operators)
new_message="Python is a powerful language"
print("Python" in new_message)
print("Java" in new_message)
print("Java" not in new_message)
print("Python" not in new_message)
for letter in new_message:
	print(letter)