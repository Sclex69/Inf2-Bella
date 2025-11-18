from dataclasses import replace  # (Not used, but imported)

# Basic dictionary example
student = {"name": "Alex", "grade": "A", "age": "18"}

print(student["grade"])  # Prints the student's grade
print(student["age"])    # Prints the student's age

# Adding a new key-value pair
student["school"] = "Greenwood High"

# Updating an existing value
student["grade"] = "A+"

# Removing a key-value pair
del student["age"]


# Dictionary of countries and capitals
Capitals = {"Slovakia": "Bratislava", "Germany": "Berlin", "Ukraine": "Kyiv"}

# Loop through keys
for key in Capitals:
    print(Capitals[key])  # Print each capital

# Loop through keys again (same result as above)
for value in Capitals:
    print(Capitals[value])

# Check if key exists
if "Germany" in Capitals:
    print("germany is in countries")

# Loop through keys and values
for key, value in Capitals.items():
    print("the capital of", key, "is", value, ".")


# Nested dictionary (dictionary inside a dictionary)
students = {
    "Alice": {"age": 16, "grade": "A"},
    "Bob": {"age": 17, "grade": "B"}
}

print(students["Bob"]["grade"])  # Accessing nested value

# Add a new student
students["Charlie"] = {"age": 15, "grade": "A"}

# Update existing student's grade
students["Alice"]["grade"] = "A+"

# Print all student names and grades
for name, grade in students.items():
    print("Name:", name, "grade:", students[name]["grade"])


# Count word occurrences in a sentence
sentence = "the cat and the dog"
words = {}

sentence = sentence.split()  # Split sentence into words

for x in sentence:
    words[x] = words.get(x, 0) + 1  # Count occurrences

print(words)


# DNA sequences
species_one = "ACCTACAGATGGTGAATATCTCCCTGCGAGTGTTGTCTCGACCCAATGCTCAGGAGCTTCCTAGCATGTACCAGCGCCTAGGGCTGGACTACGAGGAACGAGTGTTGCCGTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAATGCCTCACAGCTGATCACCCAGCGGGCCCAG"
species_two = "ATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAATGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTACGAGGAGCGAGTGCTGCCGTCCATTGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACTCAACGGGCCCAG"
species_three = "ACCTGCAGATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAACGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTATGAGGAGCGAGTGCTGCCCTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACCCAGCGGGCCCAG"
species_four = "ACCTGCAGATGGTGAACATCTCCCTGCGCGTCCTCACCCGCCCCAATGCTGCAGAGCTGCCCAGCATGTATCAGCGCCTGGGCCTGGACTACGAGGAGCGAGTCCTGCCCTCCATCGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAATTCAACGCCTCGCAGCTCATCACACAGAGAGCCCAG"


def spocitanie(y):
    """Count nucleotide frequencies in a DNA sequence.

    Args:
        y (str): DNA sequence consisting of the letters A, T, C, and G.

    Returns:
        None: Prints a dictionary showing each nucleotide count.
    """
    species = {}
    for x in y:  # Count each nucleotide
        species[x] = species.get(x, 0) + 1
    print(species)


spocitanie(species_one)
spocitanie(species_two)
spocitanie(species_three)
spocitanie(species_four)


def complementary(y):
    """Generate the complementary DNA strand.

    DNA base pairs:
        A ↔ T
        C ↔ G

    Args:
        y (str): DNA sequence.

    Returns:
        None: Prints the complementary sequence.
    """
    species = ""
    for x in y:
        # Match each nucleotide to its complementary pair
        if x == "A":
            species += "T"
        if x == "T":
            species += "A"
        if x == "C":
            species += "G"
        if x == "G":
            species += "C"
    print(species)


complementary(species_one)
complementary(species_two)


def RNA(y):
    """Convert a DNA strand into RNA.

    DNA → RNA rules:
        A → U
        T → A
        C → G
        G → C

    Args:
        y (str): DNA sequence.

    Returns:
        None: Prints the resulting RNA sequence.
    """
    species = ""
    for x in y:
        # DNA nucleotides converted to RNA complements
        if x == "A":
            species += "U"
        if x == "T":
            species += "A"
        if x == "C":
            species += "G"
        if x == "G":
            species += "C"
    print(species)


RNA(species_one)
RNA(species_two)


def zisti_RNA(x):
    """Check if a sequence is RNA or DNA.

    Args:
        x (str): A nucleotide sequence.

    Returns:
        None: Prints either "RNA" or "DNA".
    """
    if "U" in x:  # RNA contains Uracil (U)
        print("RNA")
    else:
        print("DNA")


zisti_RNA(species_one)
zisti_RNA(species_two)
