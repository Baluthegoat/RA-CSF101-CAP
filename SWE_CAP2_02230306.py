############################
# Tashi Penjor 
# Section A
# 02230306
############################
# REFERENCES
# https://www.geeksforgeeks.org/maximum-number-of-overlapping-intervals/
# https://docs.eyesopen.com/toolkits/python/shapetk/shape_examples.html
# https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
# https://github.com/ctphoenix/CDR_Overlap/blob/master/CDR_Overlap.py
# https://www.geeksforgeeks.org/python-find-overlapping-tuples-from-list/
# Solution 
# Task 1: There were 14 people assigned and there are 12 of overlapping space assignments
# Task 2: There were 4734 assignments that overlap completely.  
###########################
# Function to read the input file.
def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

# task 1
def calculate_overlap(file_lines):
    assignments = set()
    people = set()
    overlap = set()

    for line in file_lines:
        line = line.strip()
        elf1, elf2 = line.split(',')
        start1, end1 = map(int, elf1.split('-'))
        start2, end2 = map(int, elf2.split('-'))

        people.add(elf1[:-2])
        people.add(elf2[:-2])

        if start1 <= start2 and end1 >= end2:
            assignments.add(elf1[:-2])
        elif start2 <= start1 and end2 >= end1:
            assignments.add(elf2[:-2])
        elif start1 <= start2 and end1 <= end2:
            overlap.add(elf1[:-2])
            assignments.add(elf1[:-2])
        elif start2 <= start1 and end2 <= end1:
            overlap.add(elf2[:-2])
            assignments.add(elf2[:-2])

    print(f"There were {len(people)} people assigned and there are {len(overlap)} of overlapping space assignments")


# task 2
def calculate_total_complete_overlap(file_lines):
    complete_overlap_count = 0

    for line in file_lines:
        line = line.strip()
        elf1, elf2 = line.split(',')
        start1, end1 = map(int, elf1.split('-'))
        start2, end2 = map(int, elf2.split('-'))

        if start1 <= start2 and end1 >= end2:
            complete_overlap_count += 1
        elif start2 <= start1 and end2 >= end1:
            complete_overlap_count += 1

    print(f"There were {complete_overlap_count} assignments that overlap completely.")

# Reading the input file.
file_path = 'input_2_cap2.txt'
file_lines = read_input(file_path)
calculate_overlap(file_lines)
calculate_total_complete_overlap(file_lines)


