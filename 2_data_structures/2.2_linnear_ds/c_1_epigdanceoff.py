# EpigDanceOff - Kattis

# Reasoning:
#
# For each line, discard the columns that have 
# other character than "_" at that line.
# The surviving columns are blank columns.
# A blank column is a column where all the characters are "_"


from sys import stdin
n_lines, m_chars = map(int, stdin.readline().split())
blank_columns = [*range(m_chars)]
for _ in range(n_lines):
    line = stdin.readline()
    blank_columns = [i for i in blank_columns if line[i] == "_"]
print(len(blank_columns)+1)