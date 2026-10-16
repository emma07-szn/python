# Dictonary -->is a key value pair


person={
    "Firstname":"John",
    "Lastname":"Carson",
    "Age":20,
    "Favourite_Colour":["blue","green"],
    "salary":50000
}



print(person)


# access the key value
print(person["Age"])
print(person["salary"])


# update the value of dictionary
person["Age"]=34
print(person)

# add a key and Value
person["passport"]="B0078H"
print(person)


# remove an item
del person["Lastname"]
print(person)