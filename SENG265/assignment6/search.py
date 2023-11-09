#!/usr/bin/env python3
import sys


# returns a list of the relavant words to query
def get_query_vector(terms):
    query_words = []
    for line in sys.stdin:
        word = line.strip().split(" ")[0]
        if word:
            query_words.append(word)

    query_vector = []
    for term in terms:
        if term in query_words:
            query_vector.append(1)
        else:
            query_vector.append(0)

    return query_vector


def get_sorted_terms(indexDir):
    terms = []
    # todo - replace with param
    with open(indexDir + "/sorted_terms.txt", "r") as f:
        contents = f.read()
        for term in contents.split("\n"):
            term = term.strip().split(" ")[0]
            if term:
                terms.append(term)

    return terms


# returns a list of lists, with each list being the column in the matrix
def get_matrix_vectors(indexDir):
    vectors = []
    # todo - replace with param
    with open(indexDir + "/td_matrix.txt", "r") as f:
        contents = f.read()
        lines = contents.split("\n")

        indexes = lines.pop(0).strip().split(" ")
        columns = int(indexes[1])
        for i in range(columns):
            vectors.append([])

        for line in lines:
            if not line:
                break
            values = line.split(" ")
            for i in range(columns):
                value = int(values[i])
                vectors[i].append(value)
    return vectors


# Does the dot products of vectors A and B
# A and B must be of equal length
def dot(A, B):
    if len(A) != len(B):
        print(A, B)
        return
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i] * B[i]
    return sum


# returns the magnitude of vector A
def magnitude(A):
    sum = 0
    for num in A:
        sum = sum + num**2

    return sum ** (1 / 2)


def cosine_similarity(A, B):
    return dot(A, B) / (magnitude(A) * magnitude(B))


def main():
    if len(sys.argv) < 2:
        print("To use program, first argument is input directory")
        return
    indexDir = sys.argv[1]

    terms = get_sorted_terms(indexDir)
    query_vector = get_query_vector(terms)
    matrix_vectors = get_matrix_vectors(indexDir)

    for m_vector in matrix_vectors:
        result = cosine_similarity(query_vector, m_vector)

        print(f"{result:.2f}")


if __name__ == "__main__":
    main()
