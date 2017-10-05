import pandas as pd
import numpy as np

syn_table = {}
list_pairs_ppi = []

'''
toy = pd.read_csv("ToyPPIData.txt", "\t")
ppi_1 = np.array(toy.values[:, 0:1])
ppi_2 = np.array(toy.values[:, 1:2])
for index in range(ppi_1.shape[0]):
    if ppi_1[index, 0] not in list_ppi:
        list_ppi.append(ppi_1[index, 0])
for index in range(ppi_2.shape[0]):
    if ppi_2[index, 0] not in list_ppi:
        list_ppi.append(ppi_2[index, 0])
'''

df = pd.read_csv("BIOGRID-ALL-3.4.152.tab2.txt", "\t")
ppi = np.array(df.values[:, 7:9])
name = np.array(df.values[:, 15:17])


with open("ppi_biogrid.txt", "w") as f:
    for index in range(ppi.shape[0]):
        if name[index, 0] == 9606 and name[index, 1] == 9606:
            print("9606!!!")
            if [ppi[index, 0], ppi[index, 1]] not in list_pairs_ppi or [ppi[index, 1], ppi[index, 0]] not in list_pairs_ppi:
                f.write(ppi[index, 0] + "\t" + ppi[index, 1] + "\t1\n")
                list_pairs_ppi.append([ppi[index, 0], ppi[index, 1]])
                print("Added " + ppi[index, 0] + "\t" + ppi[index, 1] + "\t1")
            else:
                print("Duplicate!")
f.close()


'''
ppi_A = np.array(df.values[:, 7:8])
syn_A = np.array(df.values[:, 9:10])
ppi_B = np.array(df.values[:, 8:9])
syn_B = np.array(df.values[:, 10:11])
for index in range(ppi_A.shape[0]):
    if ppi_A[index, 0] not in syn_table.keys():
        syn_table[ppi_A[index, 0]] = syn_A[index, 0].split("|")
        print("Split!")
    if ppi_B[index, 0] not in syn_table.keys():
        syn_table[ppi_B[index, 0]] = syn_B[index, 0].split("|")
        print("Split!")    
'''

'''
with open("ToyPPIData.txt", "w") as f:
    for index in range(ppi_A.shape[0]):
        write_A = ppi_A[index, 0]
        for syn in syn_table[ppi_A[index, 0]]:
            if syn in list_ppi:
                write_A = syn
                print("Synonym Found!_A")
        write_B = ppi_B[index, 0]
        for syn in syn_table[ppi_B[index, 0]]:
            if syn in list_ppi:
                write_B = syn
                print("Synonym Found!_B")
        f.write(write_A + "\t" + write_B + "\t1\n")
f.close()
'''


