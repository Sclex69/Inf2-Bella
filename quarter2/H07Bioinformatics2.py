def read_fasta(input_file):
    """
    Read a FASTA file and separate sequences by identifiers.

    Args:
        input_file (str): Path to FASTA file.

    Returns:
        dict: {sequence_id: sequence}
    """
    parsed_seqs = {}
    curr_seq_id = None
    curr_seq = []

    with open(input_file) as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"): #fasta header
                if curr_seq_id is not None: #If a previous sequence exists: Save it into the dictionary ,Join all sequence lines into one string
                    parsed_seqs[curr_seq_id] = ''.join(curr_seq)
                curr_seq_id = line[1:]
                curr_seq = []
                continue

            curr_seq.append(line)

    if curr_seq_id is not None:
        parsed_seqs[curr_seq_id] = ''.join(curr_seq)

    return parsed_seqs


def spocitanie(sequence):
    """
    Count occurrences of each character in a sequence.
    """
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts


def detect_fasta_type(char_dict):
    """
    Detect whether a sequence is DNA, RNA, or PROTEIN.
    """
    if len(char_dict) > 6:
        return "PROTEIN"
    if "T" in char_dict:
        return "DNA"
    return "RNA"


def dinucleotide_count(sequence):
    """
    Count dinucleotide frequencies in a DNA sequence.
    """
    dinucs = {}
    for i in range(len(sequence) - 1):
        pair = sequence[i:i+2]
        dinucs[pair] = dinucs.get(pair, 0) + 1
    return dinucs


def cg_observed_expected(sequence):
    """
    Calculate observed/expected CpG ratio.
    """
    mono = spocitanie(sequence)
    di = dinucleotide_count(sequence)

    c = mono.get("C", 0)
    g = mono.get("G", 0)
    cg = di.get("CG", 0)
    length = len(sequence)

    expected = (c * g) / length if length > 0 else 0
    if expected == 0:
        return 0

    return cg / expected


# ---------- MAIN ----------

input_files = [
    "Human_FMR1_Protein_UniProt.fasta",
    "Human_X_Chromosome_FMR_Region_NCBI.fasta",
    "sequences.fasta"
]

for file in input_files:
    print("\nProcessing file:", file)
    sequences = read_fasta(file)

    for seq_id, seq in sequences.items():
        counts = spocitanie(seq)
        seq_type = detect_fasta_type(counts)

        print("\nSequence ID:", seq_id)
        print("Type:", seq_type)
        print("Unique characters:", len(counts))

        # Dinucleotide analysis ONLY for DNA
        if seq_type == "DNA":
            dinucs = dinucleotide_count(seq)
            print("CG dinucleotide count:", dinucs.get("CG", 0))
            print("CpG observed/expected:", cg_observed_expected(seq))
