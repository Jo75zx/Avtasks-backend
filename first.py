int = 45
fl = 3.14
boo = True
str = "Hello, World!"
none = None
print(f"{int} {type(int)}")
print(f"{fl} {type(fl)}")
print(f"{boo} {type(boo)}")
print(f"{str} {type(str)}")
print(f"{none} {type(none)}")

list = [1, 2, 3, 4, 'five']
print(f"{list} {type(list)}")
tuple = (1, 2, 3, 4, 'five')
print(f"{tuple} {type(tuple)}")
set = {1, 2, 3, 4, 4, 4, 4, 4, 'five'}
print(f"{set} {type(set)}")
dict = {'one': 1, 'two': 2, 'three': 3}
print(f"{dict} {type(dict)}")
print(dict['two'])

x=5
if x>0:
    print(f"x is positive")
    

y=80
if y>50:
    print(f"y is greater than 50")
else:
    print(f"y is less than or equal to 50")

grade = 90
if grade >= 90:
    print(f"Grade: {grade} - A")
elif grade >= 80:
    print(f"Grade: {grade} - B")
elif grade >= 70:
    print(f"Grade: {grade} - C")
else:
    print(f"Grade: {grade} - D")

ff=[1, 2, 3, 4, 5]
for i in ff:
    print(f"Value: {i}")

for i in range(1, 6):
    print(f"Value: {i}")

x = 5
while x > 0:
    print(f"x is {x}")
    x -= 1

for i in range(10):
    if i == 7:
        print(f"Found 7!")
        continue
    if i == 3:
        continue
    if i == 9:
        break
    print(f"Value: {i}")