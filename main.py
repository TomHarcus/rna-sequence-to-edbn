import time
import os

DBN_DIR = 'dbnFiles'

OUTPUT = 'bprna_dataset_output.csv'

count = 0

STRAND_CHARS = ('A', 'C', 'G', 'U')
SEQUENCE_CHARS = ('.', '(', '[', '{')

start = time.perf_counter()

max = 0
min = 999999

for name in os.listdir(DBN_DIR):
    with open(os.path.join(DBN_DIR, name)) as f:
        current_strand = ''
        current_sequence = ''
        for line in f:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if line.startswith(STRAND_CHARS):
                current_strand += line
            elif line.startswith(SEQUENCE_CHARS):
                current_sequence += line

        if len(current_strand) == len(current_sequence) and len(current_strand) <= 500:
            count+=1

        
         
        
print(f'Count: {count}')



end = time.perf_counter()

print(f"Time taken: {end-start}")



