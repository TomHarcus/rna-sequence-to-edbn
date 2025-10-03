import re
from Bio import SeqIO
import time

HOTKNOTS_EXEC = '/home/tom/Downloads/HotKnots_v2.0/bin/HotKnots'
HOTKNOTS_DIRECTORY = '/home/tom/Downloads/HotKnots_v2.0/bin/'

INPUT = 'Rfam.fa'
OUTPUT = 'hotknots_output.csv'

count = 0

regex = "[BDEFHIJKLMNOPQRSTVWXYZ]"

start = time.perf_counter()

for record in SeqIO.parse(INPUT, 'fasta'):
    
    if re.search(regex, str(record.seq.upper())):
        count += 1
    

print(count)

end = time.perf_counter()

print(f"Time taken: {end-start}")
