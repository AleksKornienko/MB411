'''names = globals()['__builtins__'].__dict__.keys()
builtins = sorted([name for name in names if not name.startswith('_')])
print(builtins)

import math, sys

from math import sin, pi

import math as m


print(m.sin(m.pi/2))

import sys
for name in dir(sys):
    print(name, end="\t")

from random import random, seed, randint, randrange, choice, sample
seed(0)
print("Using librery random.random")
for i in range(10):

    print(random())
print("Using librery random.randint")
for i in range(10):
    print(randint(1,10000000))
print("Using librery random.randrange")
for i in range(10):
    print(randrange(10000000))
    print(randrange(1,10000000))
    print(randrange(1,100,20))
    print("===========")
print("Using librery random.choice")
lst = ["Red","Black","Green","Gray"]
for i in range(5):
    print(choice(lst))
print("Using librery random.sample")    
for i in range(5):
    print(sample(lst, 3))

from platform import platform, machine, processor, system, version, uname  

print("============")
print(platform())
print(machine())
print(processor())
print(system())
print(version())
print(uname())


x=int(input("Enter X:"))
y=int(input("Enter Y:"))

def calc(x,y):
    print("Calculate - ")
    print(x+y*x**2)

calc(x,y)

def modName(userName):
    newName = userName.upper()
    loginName = userName.lower()
    return newName, loginName
    
name = input("Input ypur name: ")
NameUpper, Logins = modName(name)
print(NameUpper)
print(Logins)


'''
users = [['user1','password'],
         ['ako','123qwe'],
         ['rtx','123qwe123QWE'],
         ['user2','123456789']]
def printInfo(*clients):
    for i in range(len(clients)):
        if i ==0:
            print("login : {}".format(clients[i]))
        elif i == 1:
            print(" password : {}".format(clients[i]))

for user in users:
    printInfo(*user)




















