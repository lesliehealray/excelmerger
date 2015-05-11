import os
import sys


with open("~/Desktop/suspense_merge.xlsx","a+") as fout:
	folder_path = sys.argv
	for filename in os.listdir(folder_path):
		fpath = os.path.join(folder_path, filename)
    	with open(fpath) as f:
    		#f.next() # skip the header
    		#for line in f:
        #		fout.write(line)
        	print fpath

