#!/usr/bin/env python3

import os
import sys


# writes sorted files to output and returns sorted files
def output_sorted_files(inputDir, outputDir):
    files = os.listdir(inputDir)
    files.sort()

    # write sorted file names to file
    with open(outputDir + "/sorted_documents.txt", "w") as f:  # write mode
        for file in files[:-1]:
            f.write(file + "\n")
        f.write(files[-1])

    return files


def get_terms_frequency(files, inputDir):
    terms = set()

    # stores each item in a dict as key: filename, value: item (term and freq)
    file_term_map = {}

    for file in files:
        # get contents of each file
        with open(inputDir + "/" + file, "r") as f:
            contents = f.read()
            cur_items = contents.split("\n")
            for item in cur_items:
                # get the term and frequency number
                term = item.split(" ")[0]
                terms.add(term)
                file_term_map[file + term] = item

    return [terms, file_term_map]


# write sorted terms to file, returns sorted terms
def output_sorted_terms(terms, outputDir):
    sorted_terms = sorted(terms)
    with open(outputDir + "/sorted_terms.txt", "w") as f:
        for term in sorted_terms[:-1]:
            f.write(term + "\n")
        f.write(sorted_terms[-1])
    return sorted_terms


# returns the matrix given by sorted terms and files mapped in the file_term_map
def get_matrix(file_term_map, sorted_terms, files):
    # generate matrix
    matrix = {}
    for i, term in enumerate(sorted_terms):
        for j, file in enumerate(files):
            if file_term_map.get(file + term):
                freq = file_term_map[file + term].split(" ")[1]
                matrix[(i, j)] = freq
    return matrix


# write matrix to file
def output_matrix(outputDir, matrix, sorted_terms, files):
    with open(outputDir + "/td_matrix.txt", "w") as f:
        rows = len(sorted_terms)
        cols = len(files)

        f.write(str(rows) + " " + str(cols) + "\n")
        for i in range(rows):
            for j in range(cols):
                item = matrix.get((i, j))
                f.write(str(item or 0))
                if j != cols - 1:
                    f.write(" ")
            if i != rows - 1:
                f.write("\n")


def main():
    if len(sys.argv) < 3:
        print(
            "To use program, first argument is input directory, second is output directory"
        )
        return

    inputDir = sys.argv[1]
    outputDir = sys.argv[2]

    files = output_sorted_files(inputDir, outputDir)
    terms, file_term_map = get_terms_frequency(files, inputDir)

    sorted_terms = output_sorted_terms(terms, outputDir)

    matrix = get_matrix(file_term_map, sorted_terms, files)
    output_matrix(outputDir, matrix, sorted_terms, files)


if __name__ == "__main__":
    main()
