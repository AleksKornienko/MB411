#a1 = float(input("Введіть число А:"))
#b1 = float(input("Введіть чсило В:"))
#c = str(a1 + b1)
#print("Результат - "+c)

print("Hello - "+ 3*" Hello " + " - Hello")

print("+" + 10 * "-" + "+")
print(("|"+" "*10 + "|\n")*5, end ="")
print("+" + 10 * "-" + "+")


A1 = int(input("Введіть число А:"))
B1 = int(input("Введіть число В:"))
print(A1==B1)
A2=A1
print(f"Результат присваивания двух значень ({A1} - {B1}) - {A2}")
print(f"Результат порівнянь двух значень ( {A1} - {B1} )  - {A1==B1}")
print(f"Результат двух значень ( {A1} >= {B1} )  - {A1>=B1}")
print(f"Результат двух значень ( {A1} != {B1} )  - {A1!=B1}")
print("============================")
if A1==B1:
    print(f"OK -  ( {A1} - {B1} )  - {A1==B1}")
    print("Happy")
else:
    print(f"NG -  ( {A1} - {B1} )  - {A1==B1}")
    
if A1>=B1:
    print(f"Ok - ( {A1} >= {B1} )  - {A1>=B1}")
    print("Happy")
else:
    print(f"NG - ( {A1} >= {B1} )  - {A1>=B1}")
    
if A1!=B1:
    print(f"Ok ( {A1} != {B1} )  - {A1!=B1}")
    print("Happy")
else:
    print(f"NG ( {A1} != {B1} )  - {A1!=B1}")


print("=======================")
num1 = int(input("Введіть перше число - "))
num2 = int(input("Введіть друге число - "))
num3 = int(input("Введіть трете число - "))

larg_num = num1

if num2 > larg_num:
    larg_num = num2
if num3 > larg_num:
    larg_num = num3
    
print(f"Найбільше число {larg_num}")

    
