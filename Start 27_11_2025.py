#Start 15 do 31 
i = 0
while i <= 24:
    print(f"Start {i}")
    i += 2
x = 0
for x in range(0,24,2):
    print(f"Start FOR {x}")
    
pow = 1
for exp in range(16):
    print(f"2 у {exp} ступені дорівнює {pow}")
    pow *= 2

print("======================")
for i in range(0,10):
    if i == 5:
        break
    print(f"Working in for. Step  - {i} ")

print("Working out for")
print("======================")
for i in range(0,10):
    if i == 5:
        continue
    print(f"Working in for. Step - {i}")
print("Working out for")
print("======================")
               
lg = -99999999999
counter = 0
while True:
    number = int(input("Обробка break. Введіть число або напишіть 0 для виходу :"))
    if number == 0:
        break
    counter += 1
    if number > lg :
        lg = number
if counter !=0:
    print(f"Найбільше число : {lg}")
else:
    print("Ви не ввели число!!!! ")
print("======================")
               
lg = -99999999999
counter = 0
number = int(input("Обробка continue. Введіть число або напишіть 0 для виходу :"))
    
while number != 0:
    if number == 0:
        continue
    counter += 1
    if number > lg :
        lg = number
    number = int(input("Обробка continue. Введіть число або напишіть 0 для виходу :"))
if counter:
    print(f"Найбільше число : {lg}")
else:
    print("Ви не ввели число!!!! ")

print("======================")

#var1 = int(input("Enter number:"))
#var2 = int(input("Enter number:"))
#var3 = int(input("Enter number:"))    
#var4 = int(input("Enter number:"))
#var5 = int(input("Enter number:"))

#lists = [var1,var2,var3,var4,var5]
#print(lists)
#print(lists[2])
#lists[2] = lists[4]
#print(lists[2])
#print(f"Length lists = {len(lists)}")
#del lists[-2]
#print(lists)
#print(f"Length lists = {len(lists)}")
#print("======================")

lists = []
total = 0
while True:
    number = int(input("Введіть число або напишіть 0 для виходу :"))
    if number == 0:
        break
    lists.append(number)

print(lists)
for i in range(len(lists)):
    print(f"Index lists {i}. Number in {lists[i]}")
    total += lists[i]
print(total)

lists.sort()
print(lists)

#lists.reverse()
#print(lists)

lists1 = lists[2:4]
print(lists1)






