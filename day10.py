#inventory_manager_system
#File handling: using python to work with files. It includes create file, open files,write into files, read from files, updatee the file content, close the file, handle the file errors
inventory={
    "rice":{
        "quantity": 20,
        "price":1500
    },
    "milk":{
        "quantity": 15,
        "price": 1200
    },
    "sugar":{
        "quantity": 10,
        "price": 1800
    }
}
# print(inventory)
print("Current Inventory")
print("---------------------")

# add a new product
product_name=input("Enter the product name: ")
product_name=product_name.strip().lower()
quantity=int(input("Enter quantity"))
price=float(input("Enter the price: "))

# add a new product in the inventory 
inventory[product_name]={
    "quantity": quantity,
    "price": price
}

#file handling: open() and close()
file=open("inventory.txt", "w")

for product_name, details in inventory.items():
    print(f"Product: {product_name}")
    print(f"Quantity: {details['quantity']}")
    print(f"Price: {details['price']}")
    file.write(f"{product_name}, {details['quantity']}, {details['price']}\n")
    file.close()

print("Inventory saved to file")
# #update a product in inventory
# product_to_update=input("Enter the product name to update quantity: ")
# product_to_update=product_to_update.strip().lower()
# if product_to_update in inventory:
#     new_quantity=int("Enter new quantity: ")
#     inventory[product_to_update]["quantity"]=new_quantity
#     print("Product quantity has been updated")
# else: 
#     print("Product not found")

# #remove a product 
# product_to_remove=input("Enter the product name to remove: ")
# product_to_remove=product_to_remove.strip().lower()

# if product_to_remove in inventory:
#     inventory.pop(product_to_remove)
#     print("Product removed")
# else: 
#     print("Product not found")




