from random import randint

codons = ["GGU","GGC","GGA","GGG","TCT","TCC","TCA","TCG","AGT","AGC"]

length = input("What amino acid length flexible linker would you like a nucleotide sequence for?")

linker_sequence = ""
length = int(length)
for x in range(0,length):
    new_codon = codons[randint(0,9)]
    linker_sequence = linker_sequence + new_codon
    x = x + 1

print(linker_sequence)