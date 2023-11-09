#!/usr/bin/env python3
import sys


# returns a list of 1 and 0 based on existance of term in query words
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


# returns the list of sorted terms
def get_sorted_terms(indexDir):
    terms = []
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


# returns the list of relavent sorted file names
def get_file_names(indexDir):
    names = []
    with open(indexDir + "/sorted_documents.txt", "r") as f:
        contents = f.read()
        for name in contents.split("\n"):
            name = name.strip()
            if name:
                names.append(name)

    return names


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

    file_names = get_file_names(indexDir)

    rankings = []
    for i, m_vector in enumerate(matrix_vectors):
        result = cosine_similarity(query_vector, m_vector)
        rank = "{:.4f}".format(round(result, 4))
        rankings.append((rank, file_names[i]))

    rankings.sort(reverse=True)

    for rank in rankings:
        print(rank[0] + " " + rank[1])


if __name__ == "__main__":
    main()
