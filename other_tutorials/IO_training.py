##### Step 1
# Open the file , read through it and close the file
import os
import numpy as np

os.listdir("./other_tutorials/")
filename = "SAFI_results.csv"
filepath = os.path.join("./other_tutorials", filename)

# open the file,
# the 'r' means we want to read from the file
# the open function returns what is called a file handle.
# we use this to refer to the file
f = open(filepath, "r")

# We use a for loop to iterate through the file one line at a time
for line in f:
    # we simply print the line
    print(np.array(line))

f.close()


##### Step 2
# Select a specific ‘column’ from the records in the file
f = open(filepath, "r")

# first line is a header so ignore it
# f.readline()

for line in f:
    print(line.split(",")[0])

f.close()
