#!/usr/bin/python3
 
import math

def write_file(file_write,drug_sorted, number_sorted, cost_sorted):
    fw = open(file_write,'w')
    header = 'drug_name' + ',' + 'num_prescriber' + ',' + 'total_cost'
    fw.write(header + '\n')

    for i in range(len(drug_sorted)):
        fw.write(drug_sorted[i]+','+str(number_sorted[i])+','+str(math.floor(cost_sorted[i]))+'\n')

    fw.close()
