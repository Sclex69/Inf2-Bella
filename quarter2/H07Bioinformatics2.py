input_file = './Human_FMR1_Protein_UniProt.fasta'

# Open our input file for reading
f = open(input_file)

# Before we start reading the file,
# set up an empty dict to hold our mappings
# between gene ids and their sequence
parsed_seqs = {}

# Set up variables to keep track of our
# current sequence id (a string),
# and our current sequence (as a list of smaller sequences)
# (we glue these smaller sequences together later on)

curr_seq_id = None
curr_seq = []

for line in f:

    # remove newline characters ("\n")
    line = line.strip()

    if line.startswith(">"):
        # We only execute this code IF we're in
        # an identifier line!

        # Even though the next if statement appears
        # early in the code, it is the final step in the
        # process of parsing an entry.

        # curr_seq_id starts as None, so if it is not None,
        # (i.e. it already holds an identifier)
        # AND we are in an identifier line,
        # then we must have finished reading an entry
        # and be just starting a new one. We should glue together
        # all the sequences for the current entry (with ''.join(curr_seq))
        # and save it to our dictionary, keyed based on the current
        # identifier
        if curr_seq_id is not None:
            parsed_seqs[curr_seq_id] = ''.join(curr_seq)

        # Regardless of whether we just saved an entry,
        # We're in a label line that starts a new entry,
        # so we should set the current sequence id to whatever it
        # says on the line, except for the '>' symbol
        curr_seq_id = line[1:]

        # empty out the current sequence, since we're starting
        # a new entry
        curr_seq = []

        # If we started a new entry, skip the stuff we'd normally
        # do to process sequence data and go on to the next line
        continue

    # If we got here, it means we are NOT in an identifier
    # line, and instead we've got sequence! We should add
    # the current sequence to the
    curr_seq.append(line)

# Join the sequences for the final entry and add them to the dict
parsed_seqs[curr_seq_id] = ''.join(curr_seq)

# Print out the final result!
print(parsed_seqs)

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
    return species

f=spocitanie(parsed_seqs[curr_seq_id])
print(f)
if len(f)> 6:
    print("PROTEIN")
else:
    if "T" in f:
        print("DNA")
    else:
        print("RNA")


print(len(f))