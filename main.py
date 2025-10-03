import time
import os

DBN_DIR = 'dbnFiles'

OUTPUT = 'bprna_dataset_output.csv'

count = 0

STRAND_CHARS = ('A', 'C', 'G', 'U')
SEQUENCE_CHARS = ('.', '(', '[', '{')

num_pseudoknots = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

start = time.perf_counter()

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

        if '[' in current_sequence:
            num_pseudoknots += 1

        if len(current_strand) == len(current_sequence):
            count+=1

        if len(current_strand) >= 1000:
            count1 += 1

        if len(current_strand) < 1000 and len(current_strand) >= 800:
            count2 += 1

        if len(current_strand) < 800 and len(current_strand) >= 500:
            count3 += 1
        
        if len(current_strand) < 500 and len(current_strand) >= 200:
            count4 += 1

        if len(current_strand) < 200:
            count5 += 1
        
print(f'Count: {count}')
print(f'Number of pseudoknots: {num_pseudoknots}')
print(f'Number of examples over 1000: {count1}')
print(f'Number of examples between 800 and 1000: {count2}')
print(f'Number of examples between 500 and 800: {count3}')
print(f'Number of examples between 200 and 500: {count4}')
print(f'Number of examples under 200: {count5}')

end = time.perf_counter()

print(f"Time taken: {end-start}")



