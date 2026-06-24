#Sets: stores unique values. they are unordered, changeable, does not allow duplicates, uses{}
courses={"Introduction to programming", "Cybersecurity Basics","C++ Programming", "Mobile Development"}
print(courses) 
#add item to a set 
#add(): add one item
courses.add("Datascience")
print(courses)
#update(): add multiple items to set 
courses.update({"AI", "Machine Learning"})
print(courses)
#remove
courses.remove("Introduction to programming")
print(courses)
# courses.remove("Python Basics")
# print(courses)
#dicard: remooves but if the item does not exist there is no error but for this one if the item doe not exist it gives an error
courses.discard("C++ Programming")
print(courses)
#set operations 
#union: combine values from 2 sets
online_courses={"Introduction to programming", "Cybersecurity Basics","C++ Programming", "Mobile Development", "AI", "UI Design"}
offline_courses={"Mobile Development", "Machine Learning", "AI", "UI Design"}
all_courses=online_courses.union(offline_courses)
print(all_courses)
#intersection: return values found in both sets
common_courses=online_courses.intersection(offline_courses)
print(common_courses)
#difference: returns values in one set but not the other one
online_only=online_courses.difference(offline_courses)
print(online_only)
