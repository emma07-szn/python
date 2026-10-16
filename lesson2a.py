# List in python
# A list is a collectio of items
items=["Honda","Nissan","Surf","Mazda","Volkswagon"]

# print the list
print(items)


# accessing list items
print(items[2])
print(items[4])

# slicing
# print from index 2to 5
print(items[2:5])

# print from index 3 and above
print(items[3:])




# print upto index 3 
print(items[:3])



# list is mutable -->can be change
items.append("BMW")
print(items)

# inserting items at a specific index
items.insert(2,"Toyota")


print(items)

items.reverse()
print(items)