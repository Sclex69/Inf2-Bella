pfor char in "Python":
    print(char)

for x in range (5):
    print("Hello")


for char in reversed("Computer"):
    print(char)

for char in enumerate("Science"):
    print (char)

count = 0
for char in "experience teaches slowly":
    if char == "e":
        count +=1
print(count)

count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in "Programming is powerful":
    if char in vowels:
        print(char)

text= "Artificial Intelligence"
list1=""
for i in range(0,len(text),2):
    list1 +=text[i]
print(list1)

text="Python"
list1=""
for i in range(0,len(text),1):
    list1 +=text[i]
    print(list1)

