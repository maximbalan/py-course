
a = 10
b = 0b1010
c = 0o12
d = 0x0A

print(a, b, c, d)
print(a, bin(b), oct(c), hex(d))

print("*" * 25)

total = 0
i = 0
value = input("Provide a value for the range: ")
while i in range(int(value)):
    print(i)
    if i > 3:
        print("Ooops!")
        break
    i += 1
    total += i
else:
    print(f"The total is: {total}")

#-------------------------------------------------------------
#Sets, Set items are unordered, unchangeable, and do not allow duplicate values.

myset = {"apple", "banana", "cherry"}

#-------------------------------------------------------------
#Lists, List items are ordered, changeable, and allow duplicate values.

countries = [
    "Moldova",
    "Bazil",
    "Canada",
]

countries.append("England")
countries.insert(2, "Argentina")
countries.remove("Canada")
country = countries.pop(1)
countries.sort(reverse=True)


#This creates an alias, editing new list will affect the original list
new_countries_list = countries

#This will create a copy, will not affect the original list
#new_countries_list_copy = countries.copy()
new_countries_list_copy = countries[:]


#List comprehension, creates new list, similar to map
#c_list = [f"{c}:" for c in countries]
c_list = [f"{c}:" for c in countries if c == 'Moldova']

print(c_list)

print(countries, country)

print("*" * 25)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice = list[1:5]
print(slice)

#-------------------------------------------------------------

#Tuples immutable list ex: tuple = (1920, 1080, 27)

#-------------------------------------------------------------

#Dictionaries, key value

language = {"name": "Python", "version": 3}
language["website"] = "www.python.org"
language["extension"] = ".py"