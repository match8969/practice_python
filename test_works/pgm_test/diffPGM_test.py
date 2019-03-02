
import os
import sys


argvs = sys.argv

first_path = argvs[1]
second_path = ''
if len(argvs) == 3:
    second_path = argvs[2]





def is_pgm_file(filepath):
    with open(first_path, 'r') as f:
        line = f.read()
        rows = line.rstrip().split(' ')
        c


