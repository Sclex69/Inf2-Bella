def read_fasta(input_file):
    """
    Read a FASTA file and separate sequences by identifiers.
    """
    parsed_seqs = {}
    curr_seq_id = None
    curr_seq = []

    with open(input_file) as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if curr_seq_id is not None:
                    parsed_seqs[curr_seq_id] = ''.join(curr_seq)
                curr_seq_id = line[1:]
                curr_seq = []
                continue

            curr_seq.append(line)

    if curr_seq_id is not None:
        parsed_seqs[curr_seq_id] = ''.join(curr_seq)

    return parsed_seqs


def sequence_identity(seq1, seq2):
    """
    Calculate identity between two aligned sequences.
    """
    identical = 0
    different = 0
    diff_pairs = {}

    for a, b in zip(seq1, seq2):
        if a == b:
            identical += 1
        else:
            different += 1
            pair = a + b
            diff_pairs[pair] = diff_pairs.get(pair, 0) + 1

    identity = identical / min(len(seq1), len(seq2)) * 100
    return identity, identical, different, diff_pairs


def most_frequent_pair(diff_pairs):
    """
    Find most frequent differing nucleotide pair.
    """
    return max(diff_pairs.items(), key=lambda x: x[1])


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Global alignment using Needleman–Wunsch algorithm.
    """
    n, m = len(seq1), len(seq2)
    score = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        score[i][0] = i * gap
    for j in range(m+1):
        score[0][j] = j * gap

    for i in range(1, n+1):
        for j in range(1, m+1):
            diag = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            score[i][j] = max(diag, up, left)

    aligned1, aligned2 = "", ""
    i, j = n, m

    while i > 0 and j > 0:
        current = score[i][j]
        if current == score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1
        elif current == score[i-1][j] + gap:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1
        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    return aligned1, aligned2, score[n][m]


# ---------- MAIN ----------

sequences = read_fasta("sequences.fasta")

# choose two sequences for alignment
seq_ids = list(sequences.keys())
seq1 = sequences[seq_ids[0]]
seq2 = sequences[seq_ids[1]]

identity, same, diff, diff_pairs = sequence_identity(seq1, seq2)

print("Aligned sequence IDs:", seq_ids[0], "vs", seq_ids[1])
print("Sequence identity (%):", identity)
print("Identical positions:", same)
print("Different positions:", diff)

pair, count = most_frequent_pair(diff_pairs)
print("Most frequent differing pair:", pair, count)

a1, a2, score = needleman_wunsch(seq1, seq2)
print("\nAligned sequences:")
print(a1)
print(a2)
print("Alignment score:", score)
