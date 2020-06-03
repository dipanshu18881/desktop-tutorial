#TOPIC

"""customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
#print(customer["name"])
print(customer.get("birthdate", "Oct 1 1995")) #no errors
"""

#EXERCISE

phone = input("Phone:")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += numbers.get(ch, "?") + " "
print(output)