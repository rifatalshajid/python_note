
# Touple loop 

# fruits = ("Apple", "Banana", "Cherry", "Mango")

# for i in fruits:
#     print(i)


# for x in range(len(fruits)):

#     print(fruits [x])



# Touple While loop ------------------------------

# fruits = ("Apple", "Banana", "Cherry", "Mango")


# i = 1

# while i< len(fruits):
#     print(fruits[i])

#     i = i +1



# Join Touple ======================

# touple1 = ("a", "b", "c")
# touple2 = (1, 2,3)

# touple3 = touple1 + touple2

# print(touple3)


# touple = touple2 * 2

# print(touple)


# TOuple method===========================


# Count method = 

# thistouple = (1, 2,5,3,5,8,8,6,6,4,5,3,5,6,7,8,9,7,8,4,5,6,2,1,0,1,3)

# print(thistouple.count(6))



# Touple index = 

# del thistouple


# print(thistouple)



# Python sets ----------------------------------------------

# Access set--=

# mylist = {1, False, "Rifat", "Shajid", "Rifat"}


# print("1" in mylist)

# for i in mylist:

#     print(i)



# Set Update ========================

# myset1 = {1, 2, 3, 4, 5}

# myset2 = {"Rifat", "Shajid"}


# myset1.update(myset2)

# print(myset1)


# set item remove --------------


# myset1 = {1, 2, 3, 4, 5}

# myset1.pop()

# print(myset1)


# For loop for set ---------------


# myset1 = {1, 2, 3, 4, 5}

# for i in myset1:
#     print(i)


# Join Sets ----------------------

# myset1 = {1, 2, 3, 4, 5}

# myset2 = {"Rifat", "Shajid"}

# myset3 = myset1.union(myset2)

# print(myset3)



# Python Dictionary  ========================


# studentInfo = {

#     "Rifat" : {

#         "Name": "Rifat",
#         "Locations": "Rajshahi",
#         "Study" : "CSE",
#         "Roll" : 34,
#         "Number" : "01716352797"
#     },

#     "Jihan" : {

#         "Name": "Jihan",
#         "Locations": "Dhaka",
#         "Study" : "EEE",
#         "Roll" : 10,
#         "Number" : "01716352797"
#     },
  
#        "Tutul" : {

#         "Name": "Tutul",
#         "Locations": "Ishwardi",
#         "Study" : "Civil",
#         "Roll" : 101,
#         "Number" : "01716352797"
#     },

#     "Year" : 2025

# }


# Change------

# studentInfo["Year"] = 1999

# print(studentInfo)

# Update the "year" of the car by using the update() method: 


# studentInfo.update({"Tutul":"Tutul is an CSE Student"})

# print(studentInfo["Tutul"])



# Remove -------------------------

# studentInfo.popitem()

# del studentInfo

# print(studentInfo)


# Dictionary loops -----------------------

# for i in studentInfo.items():
#     print(i)

# for i in studentInfo.values():
#     print(i)

# for i in studentInfo.keys():
#     print(i)


# Dictionary copy ---------------------------


# Rifat_details = {
#     "Name": "Rifat Al Shajid",
#     "Roll": 34,
#     "University": "DIU",
#     "Address": "Dhaka, Bangladesh",
#     "Phone Number": "01716352797"

# }

# x = dict(Rifat_details)

# print(x)




# IF ELSE conditions ========================

# a = 20
# b = 20
# c = 80
# d = 50

# if a > b:
#     print("The big number is A")

# elif b > c:
#     print("The big number is B")

# elif c > d:
#     print("The big number is C")

# else:
#     print("The big number is D")


# Python loops ====================================

i = 0
while i < 10:
    print(i)
    if i == 5:
        continue



i = i + 1