import math

#Day 2: 30 Days of Python programming
 
# Level 1

person = {
    "first_name": "Tunea",
    "last_name": "Iulia",
    "country": "Romania",
    "city": "Timisoara",
    "age": 27,
    "year": 1998,
    "is_married": "no",
    "is_true": True,
    "is_light_on": False,
    "employment": ("Teacher", True)
}
for key, value in person.items():
    print(key, "is",type(value))

# Print the number of characters in the person's first name
print(len(person["first_name"]))
print(len(person["first_name"]) > len(person ["last_name"]))

# 4

num_one=5
num_two=4
total=num_one+num_two
print(total)

# 5
diff= num_one-num_two
print(diff)

# 6

product = num_one * num_two
print (product)
# 7

division = num_one / num_two
print(division)
# 8

remainder = num_one % num_two
print(remainder)

# 9

exp = num_one ** num_two
print(exp)

# 11

floor_division = num_one // num_two
print(floor_division)

# 12

radius = float(input("Insert radius of the circle: ")) # 30
circum_of_circle = math.pi * 2 * radius
area_of_circle = math.pi * radius**2
print(f"Circumference:{circum_of_circle}")
print (f"Area: {area_of_circle}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your Country of origin: ")
age = int(input("Enter your age (must be an integer): "))

print(f"{first_name}{last_name} is from {country} and is {age} years old.")













