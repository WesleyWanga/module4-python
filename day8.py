account={
    "username": "coder_2026",
    "email": "coder@gmail.com",
    "role": "admin",
    100:"xxxxx"
}
rating_messages={
    5.0:"Excelent",
    4.0: "Very Good",
    3.0: "Good"
}
# wrong_dictionary={
#     ["A",1]: "Reserved"
# }
print(account["username"])
name="Maya" # each character has an index
age=25
is_active=True
skills=["Python", "HTML", "CSS"]
coordinates=(10,40)
#mutable and immutable
#mutable(lists,dictionaries,set)
skills[1]="Javascript"
print(skills)
#Immutable: value cannot be changed (strings, integers, floats, boolean, tuples, None)
# name[1]="i"
# print(name)
name="Alice"
print(name)
print(hash("username"))
print(hash(100))
print(hash(5.0))
print(hash("A"))
