import os
import glob

data_path = 'frames/'
parent_path = 'data/Project2/'
image_files = list(glob.glob(os.path.join(data_path, "[!classes]*.txt")))
with open('train.txt', 'w') as outfile:
    for file in image_files:
        outfile.write(parent_path+data_path+os.path.splitext(os.path.basename(file))[0]+'.png\n')
