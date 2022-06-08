import os
import glob

data_path = 'frames'
label_files = list(glob.glob(os.path.join(data_path, "[!classes]*.txt")))
for file in label_files:
    labels  = open(file).readlines()
    newlabels = []
    for label in labels:
        label = label.split()
        label[0] = '0'
        newlabels.append(" ".join(label))
        out_str = "\n".join(newlabels)
    with open(file, 'w') as outfile:
        outfile.write(out_str)
