word = '''Design for adaptability:\n The core principle is to design a system from
the ground up to be able to handle different languages and cultural norms.'''
print(word)
print(len(word))
empty = ' '
print(len(empty))
i_am = 'I\m'
print(len(i_am))

str1 = 'a'
str2 = 'b'
print(str1+str2)
print(str2+str1)
print(5 * str1)
print(str2 * 4)
print('===================')
print(ord(str1))
print('===================')
print(chr(188))
print('===================')

for i in range(len(word)):
    print(word[i], end=' ')
print("\n==================")
stalker = 'STALKER'
for i in range(len(stalker)):
    print(stalker[i], end='.')
print("\n==================")
print(word[3:-5])
print("\n==================")
print('to' in word)
print('design' in word)
print('echo' in word)
word = word +"\nHello World"
print(word)
print("\n==================")
print('['+min(stalker)+']')
t = [0,10,5,1]
print(min(t))
print("\n==================")
print('['+max(stalker)+']')
print(max(t))
print("\n==================")
print(stalker.index('R'))

print(word.count('a'))

str3 = 'aBcD'
print(str3.capitalize())
print(stalker.lower())
print(str3.swapcase())
print("\n==================")
if word.endswith("World"):
    print('Yes')
else:
    print('No')
print("\n==================")
if word.startswith("World"):
    print('Yes')
else:
    print('No')
print("\n==================")
print(word.find('to'))
print(word.rfind('ts'))


pythonword = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
\nGuido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions. Beginning with Python 3.5, capabilities and keywords for typing were added to the language, allowing optional static typing. As of 2025, the Python Software Foundation supports Python 3.10, 3.11, 3.12, 3.13, and 3.14, following the project’s annual release cycle and five-year support policy. Earlier versions in the 3.x series have reached end-of-life and no longer receive security updates.
\nPython has gained widespread use in the machine learning community. It is widely taught as an introductory programming language. Since 2003, Python has consistently ranked in the top ten of the most popular programming languages in the TIOBE Programming Community Index, which ranks based on searches in 24 platforms.'''

print(pythonword)
ind = 0
fnd = pythonword.find('Python')
while fnd != -1:
    print(f"Find {ind} Python in index {fnd}")
    fnd = pythonword.find('Python', fnd + 1)
    ind += 1
print("===============")
print(stalker)
print(stalker.islower())
print(stalker.isupper())
print("===============")
number = '24-05678912'
DocType = int(number[len(number)-2:len(number)])
if DocType == 12:
    print(f"Накладна - {number}")
print("===============")
line="12345678_ako_1_2_5"
new_line=line.split('_')
print(len(new_line))

for i  in range(len(new_line)):
    if i == 0:
        nb = new_line[i]
    if i ==1:
        login = new_line[i]
    if i ==2:
        id_proccess = new_line[i]
    if i == 3:
        courent_pages = new_line[i]
    if i ==4:
        all_pages = new_line[i]


print(f"Number Documents - {nb}")
print(f"Login system - {login}")
print(f"Ця сторінка {courent_pages} з всіх сторінок у документі {all_pages}")





