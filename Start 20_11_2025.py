#import time
#i=0
#while i <= 10:
    
#    i=i+1
#    print(f"Start {i}")
#    time.sleep(10)
# Ввести числа з клавіатури та знайти найбільше
#lg_num = -9999999999

#num = int(input("Введіть число або -1, щоб зупинити ПЗ: "))
#while num != -1:
#    if num > lg_num:
#        lg_num = num
#    num = int(input("Введіть число або -1, щоб зупинити ПЗ: "))
#print(f"Найбільше число - {lg_num}")
a1 = input("Enter literal - ")
#a1 = "b"
match a1:
    case "a":
        print("Options A")
    case "c":
        print("Options C")
    case "d":
        print("Options D")
    case "b":
        print("Options B")
    case _:
        print("Default - ")
