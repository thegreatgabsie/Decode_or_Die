import numpy as np
from constants import H


def calculate_syndrome(vector):
    syndrome = np.dot(H, np.array(vector).T) % 2
    return [int(x) for x in syndrome]


def get_hamming_distance(v1, v2):
    return sum(b1 != b2 for b1, b2 in zip(v1, v2))