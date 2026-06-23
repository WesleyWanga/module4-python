#collection datatypes[lists,tuples,set,dictionary]
#list: a collection used to store multiple values in one variable. They must be ordered,changeable,duplicate values[]
books=["Python Basics", "Javascript Guide", "HTML & CSS", "Flask Fundamentals"]
print(books)
#add item in a list
#method 1: append() add an item to the end of the list
books.append("Introduction to Git and Github")
print(books)
#method2: insert()adds an item at a specific index 
books.insert(1, "Datascience")
print(books)
#remove items from the list 
#method1: remove()
books.remove("HTML & CSS")
print(books)
#method2: pop() removes an item by index
books.pop(4)
print(books)
books.pop()
print(books)
#check list length
# len()
print(len(books))
#loop through a list 
for book in books:
    print(book)

#list with mixed datatypes 
# book_info=["Python Basis",5000,4.5,True]
# student_scores=[4,67,100,89,67,56,90,89]
# print(student_scores)
#tuples: ordered, not changeable, allows duplicate values,()
library_sections=("fiction", "science", "technology","history")
print(library_sections)
print(library_sections[2])
print(library_sections[3])
print(library_sections[-1])
#tuple are not changeable
# library_sections[0]="poetry"
# print(library_sections)
student_names=("Edwin","Tabby","Yasir","Prince","Tabby","Ziza","Tereziah","Okech","Okech")
print(student_names)
#turple method: count() and index()
# print(student_names.count("Yasir"))
# print(student_names.index("Okech"))