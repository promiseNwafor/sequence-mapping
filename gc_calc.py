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
    code_obj = nucleotide_count(codes)
    total_code = sum(code_obj.values())
    total_gc = sum([code_obj["G"], code_obj["C"]])
    gc_content = total_gc / total_code
    return gc_content


print(GC_content(f))

f.close()
