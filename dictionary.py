#dictionary: stores datea in key-value pairs. They are ordered,changeable, uses keys to access values,keys must be unique()
book={
    "title":"Python Basics",
    "author":"M.Carter",
    "price": 5000,
    "available":True
}
print(book)
print(book["title"])
print(book["price"])

#get()
print(book.get("publisher"))

#update a dictinary value
book["price"]=6000
print(book)
#add anew key-value pair
book["category"]="Programming"
print(book)
#pop: remove a key_value pair 
book.pop("available")
print(book)
#keys(): returns all keys
print(book.keys())
#values(): returns all the values in the dictionary
print(book.values())
#items(): returns key_value pairs
print(book.items())
#loop through a dictionary
for key,value in book.items():
    print(f"{key}:{value}")