import numpy as np
import itertools


def calculate_syndrome(vector, H):
    syndrome = np.dot(H, np.array(vector).T) % 2
    return [int(x) for x in syndrome]



def get_hamming_distance(v1, v2):
    return sum(
        b1 != b2
        for b1, b2 in zip(v1, v2)
    )



def GetParityCheckMatrix(G):
    k, n = G.shape

    P = G[:, k:]

    identity_nk = np.eye(n - k, dtype=int)

    H = np.hstack((P.T, identity_nk))

    return H


def GenerateCodespace(generator_matrix):
    G = np.array(
        generator_matrix,
        dtype=int
    )

    k, n = G.shape

    messages = np.array(
        list(
            itertools.product(
                [0, 1],
                repeat=k
            )
        )
    )

    codewords = (messages @ G) % 2

    return codewords.tolist()


def get_minimum_distance(codewords):
    min_dist = float("inf")

    for codeword in codewords:

        weight = sum(codeword)

        if weight > 0:
            min_dist = min(
                min_dist,
                weight
            )

    return min_dist