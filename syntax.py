variable = 15

if variable > 10:
    print(f"Variable {variable} is greater than 10")
elif variable == 10:
    print(f"Variable {variable} is equal to 10")
elif variable < 10:
    print(f"Variable {variable} is less than 10")
else:
    print(f"Variable {variable} is not a number")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(f"current number: {number}")
    if number == 5:
        break
    
for number in numbers:
    if number % 2 == 0:
        print(f"Skipping number: {number}")
        continue
    print(f"current number: {number}")

for num in range(1, 11):
    print(f"current number in range: {num}")
    if num == 5:
        break
    
count = 0
while count < 10:
    print(f"current count: {count}")
    count += 1
    if count == 5:
        break
    
for i in range(3):
    for j in range(3):
        print(f"i: {i} j: {j}")

        
def recursive(i, j):
    if i < 3:
        if j < 3:
            print(f"i: {i} j: {j}")
            recursive(i, j + 1)
        else:
            recursive(i + 1, 0)
    else:
        return
    
recursive(0, 0)