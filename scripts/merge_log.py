import os

import pandas as pd

#dir_path = 'conv2d_result/'
#dir_path = 'conv3d_result/'
dir_path = 'matmul2d_result/'
file_names = os.listdir(dir_path)

lists = []
file_nums = 0
for name in file_names:
    f = open(dir_path+name,"r")
    lines = f.readlines()
    for n, fields in enumerate(lines):
        fields=fields.strip();
        fields=fields.split(",");
        if file_nums == 0:
            # for first file
            lists.append(fields)
            continue
        if fields[-1] != '%0Gflops%' and len(fields) > 1:
            lists[n][-1] = float(fields[-1]) + float(lists[n][-1])
    file_nums+=1

for j in range(len(lines)):
    if lists[j][-1] != '%0Gflops%' and len(lists[j]) > 1:
        lists[j][-1] /= file_nums

df = pd.DataFrame(lists[:-2])
df.to_excel(dir_path+"test.xlsx", index=False)
