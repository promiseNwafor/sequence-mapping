# count the pattern occurence
def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count

# for V. cholerae
ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
pattern = "TGATCA"


# map out all patterns of length k in the whole text  
def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        for i in range(n-k+1):
            if text[i:i+k] == pattern:
                freq[pattern] += 1
    return freq


# find the most frequent occurring pattern
def frequent_words(text, k):
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


# find the reverse complement of pattern
def reverse(pattern):
    rev = ""
    for char in pattern:
        rev = char + rev
    return rev


def complement(pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    comp = ""
    for base in pattern:
        comp += basepairs.get(base)
    return comp


def reverse_complement(pattern):
    return complement(reverse(pattern))


# check for patterns in the entire genome and return the positions as a list
def pattern_matching(pattern, genome):
    positions = []
    for i in range(len(genome)-len(pattern) + 1):
        i_pattern = genome[i:i+len(pattern)]
        if i_pattern == pattern:
            positions.append(i)
    return positions
