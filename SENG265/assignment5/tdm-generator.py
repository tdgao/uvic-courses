#!/usr/bin/env python3

import os
import sys

# writes sorted files to output and returns sorted files
def output_sorted_files(inputDir, outputDir):
    files = os.listdir(inputDir)
    files.sort()

    # write sorted file names to file
    with open(outputDir + "/sorted_documents.txt", "w") as f: # write mode
        for file in files:
            f.write( file + "\n")

    return files

def main():
    if len(sys.argv) < 3:
        print("To use program, first argument is input directory, second is output directory")
        return
    
    inputDir = sys.argv[1]
    outputDir = sys.argv[2]

    files = output_sorted_files(inputDir, outputDir)
    terms = set()

    # stores each item in a dict as key: filename, value: item (term and freq)
    temp_file_items = {}

    for file in files:
        # get contents of each file
        with open(inputDir + "/" +file, "r") as f:
            contents = f.read()
            cur_items = contents.split('\n')
            for item in cur_items:
                # get the term and frequency number
                term = item.split(" ")[0]
                terms.add(term)
                temp_file_items[file+term] = item

    # write sorted terms to file
    sorted_terms = sorted(terms)
    with open(outputDir + "/sorted_terms.txt", "w") as f:
        for term in terms:
            f.write(term + "\n")

    # generate matrix
    matrix = {}
    for i, term in enumerate(sorted_terms):
        for j, file in enumerate(files):
            if temp_file_items.get(file+term):
                freq = temp_file_items[file+term].split(" ")[1]
                matrix[(i,j)] = freq

    # write matrix to file
    with open(outputDir + "/td_matrix.txt", "w") as f:
        rows = len(sorted_terms)
        cols = len(files)

        f.write(str(rows) + " " + str(cols) + "\n")
        for i in range(rows):
            for j in range(cols):
                item = matrix.get((i,j))
                f.write( str(item or 0) + " " )
            f.write("\n")

if __name__ == "__main__":
    main()
