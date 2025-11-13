# Loop through each character in the string "Python" and print it
for char in "Python":
    print(char)

# Loop 5 times and print "Hello" each time
for x in range(5):
    print("Hello")

# Loop through the string "Computer" in reverse order and print each character
for char in reversed("Computer"):
    print(char)

# Loop through the string "Science" with index and character, printing tuples (index, char)
for char in enumerate("Science"):
    print(char)

# Count how many times 'e' appears in the string
count = 0
for char in "experience teaches slowly":
    if char == "e":
        count += 1
print(count)

# Print all vowels in the string
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in "Programming is powerful":
    if char in vowels:
        print(char)

# Take every second character from the string "Artificial Intelligence"
text = "Artificial Intelligence"
list1 = ""
for i in range(0, len(text), 2):
    list1 += text[i]
print(list1)

# Build the string character by character from "Python" and print after each addition
text = "Python"
list1 = ""
for i in range(0, len(text), 1):
    list1 += text[i]
    print(list1)
