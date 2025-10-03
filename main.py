import re
from Bio import SeqIO
import time
import subprocess

HOTKNOTS_EXEC = '/home/tom/Downloads/HotKnots_v2.0/bin/HotKnots'
HOTKNOTS_DIRECTORY = '/home/tom/Downloads/HotKnots_v2.0/bin/'

INPUT = 'Rfam.fa'
OUTPUT = 'hotknots_output.csv'

count = 0

regex = "[^ACGU]"

start = time.perf_counter()

for record in SeqIO.parse(INPUT, 'fasta'):
    current_strand = str(record.seq.upper()).replace('T', 'U')

    
    if not re.search(regex, current_strand) and len(current_strand) <= 20:
        count+=1
        
   
    """
    command = [HOTKNOTS_EXEC, '-s', current_strand]
    out = subprocess.run(command, cwd=HOTKNOTS_DIRECTORY, capture_output=True, text=True)
    result = out.stdout.split('\n')
    """
    
  
    #print(out)
    

print(count)

end = time.perf_counter()

print(f"Time taken: {end-start}")



