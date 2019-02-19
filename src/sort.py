#!/usr/bin/python3

def sorting(list_drug, list_number, list_cost):
    #sort the list based on total value
    List = zip(list_cost, list_drug)
    list_drug = [x for _, x in sorted(List, reverse=True)]
    List = zip(list_cost, list_number)
    list_number = [x for _, x in sorted(List, reverse=True)]
    list_cost.sort(reverse=True)


    dex_start = 0
    while dex_start < len(list_cost):
         cost = list_cost[dex_start]
         #find the drugs with the same cost
         for i in range(dex_start,len(list_cost)):
             if cost != list_cost[i]: 
                 dex_end = i
                 break
             if i == (len(list_cost)-1):
                 dex_end = len(list_cost)
         #sort the list based on drug name alphabetically     
         List = zip(list_drug[dex_start:dex_end], list_number[dex_start:dex_end])
         list_number[dex_start:dex_end] = [x for _, x in sorted(List)]
         list_drug[dex_start:dex_end] = sorted(list_drug[dex_start:dex_end])
          
         dex_start = dex_end

    return list_drug, list_number, list_cost
