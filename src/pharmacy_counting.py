#!/usr/bin/python3 

from read import read_file
from sort import sorting
from write import write_file


# read in the input dataset
file_name = './input/itcont.txt'
list_drug, list_number, list_cost = read_file(file_name)

# sort the list
drug_sorted, number_sorted, cost_sorted = sorting(list_drug, list_number, list_cost)

# write the output dataset
file_write = './output/top_cost_drug.txt'
write_file(file_write, drug_sorted, number_sorted, cost_sorted)
