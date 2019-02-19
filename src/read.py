#!/usr/bin/python3

def read_file(file_name):
   f = open(file_name,'r')
   f.readline()

   list_drug = []
   list_number = []
   list_cost = []

   while True:
        line = f.readline()
        if not line:
           break

        content = line.split(',')
        if content[3] in list_drug:
            # add the cost if the drug name already exists
            dex = list_drug.index(content[3])
            list_number[dex] += 1
            list_cost[dex] += float(content[4])
        else: 
            # add the new drug name to the list
            list_drug.append(content[3])
            list_number.append(1)
            list_cost.append(float(content[4]))
   f.close()

   return list_drug, list_number, list_cost

