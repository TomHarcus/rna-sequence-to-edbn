from Bio import SeqIO

HOTKNOTS_EXEC = "/home/tom/Downloads/HotKnots_v2.0/bin/HotKnots"
HOTKNOTS_DIRECTORY = "/home/tom/Downloads/HotKnots_v2.0/bin/"

INPUT = "Rfam.fa"
OUTPUT = "hotknots_output.csv"

count = 0

for record in SeqIO.parse(INPUT, "fasta"):
    count += 1

print(count)