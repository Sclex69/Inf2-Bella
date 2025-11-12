student= {"name": "Alex","grade": "A","age": "18"}
print(student["grade"])
print(student["age"])

student["school"] = "Greenwood High"
student["grade"] = "A+"
del student["age"]


Capitals={"Slovakia": "Bratislava","Germany": "Berlin","Ukraine": "Kyiv"}
for key in Capitals:
    print(Capitals[key])
for value in Capitals:
    print(Capitals[value])
if "Germany" in Capitals:
    print("germany is in countries")
for key, value in Capitals.items():
    print("the capital of" ,key,"is ",value,".")

students = {
    "Alice": {"age": 16, "grade": "A"},
    "Bob": {"age": 17, "grade": "B"}
}
print(students["Bob"]["grade"])
students["Charlie"] = {"age": 15, "grade": "A"}
students["Alice"]["grade"] = "A+"

for name,grade in students.items():
    print("Name:" ,name,"grade: ",students[name]["grade"])

sentence = "the cat and the dog"
words = {}

sentence = sentence.split()

for x in sentence:
    words[x] = words.get(x, 0) + 1

print(words)


species_one = "ACCTACAGATGGTGAATATCTCCCTGCGAGTGTTGTCTCGACCCAATGCTCAGGAGCTTCCTAGCATGTACCAGCGCCTAGGGCTGGACTACGAGGAACGAGTGTTGCCGTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAATGCCTCACAGCTGATCACCCAGCGGGCCCAG"
species_two = "ATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAATGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTACGAGGAGCGAGTGCTGCCGTCCATTGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACTCAACGGGCCCAG"
species_three = "ACCTGCAGATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAACGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTATGAGGAGCGAGTGCTGCCCTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACCCAGCGGGCCCAG"
species_four = "ACCTGCAGATGGTGAACATCTCCCTGCGCGTCCTCACCCGCCCCAATGCTGCAGAGCTGCCCAGCATGTATCAGCGCCTGGGCCTGGACTACGAGGAGCGAGTCCTGCCCTCCATCGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAATTCAACGCCTCGCAGCTCATCACACAGAGAGCCCAG"

def spocitanie(y):
    species = {}
    for x in y:
        species[x] = species.get(x, 0) + 1
    print(species)
spocitanie(species_one)
spocitanie(species_two)
spocitanie(species_three)
spocitanie(species_four)

