f = open("./rattusbrca1.txt", "r")
f.readline()


#count the nucleotides
def nucleotide_count(sequence):
    codes = {"A": 0, "T": 0, "G": 0, "C": 0}
    for line in f:
        for code in line:
            if code.upper() in codes:
                codes[code] += 1
    return codes

# calculate the GC content
def GC_content(codes):
    total_code = sum(codes.values())
    total_gc = sum([codes["G"], codes["C"]])
    gc_content = total_gc / total_code
    print(gc_content)


GC_content(nucleotide_count(f))

f.close()
