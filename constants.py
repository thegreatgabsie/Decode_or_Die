import numpy as np

from codingtheory import (
    calculate_syndrome,
    get_hamming_distance,
    GenerateCodespace,
    GetParityCheckMatrix
)


G_HAMMING = np.array([
    [1,0,0,0,1,1,0],
    [0,1,0,0,1,0,1],
    [0,0,1,0,0,1,1],
    [0,0,0,1,1,1,1]
])

G_CUSTOM = np.array([
    [1,0,0,0,0,0,0, 0,1,1,1,0,0,0,1],
    [0,1,0,0,0,0,0, 1,0,1,1,1,0,0,0],
    [0,0,1,0,0,0,0, 0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0, 0,0,1,0,1,1,1,0],
    [0,0,0,0,1,0,0, 0,0,0,1,0,1,1,1],
    [0,0,0,0,0,1,0, 1,0,0,0,1,0,1,1],
    [0,0,0,0,0,0,1, 1,1,0,0,0,1,0,1]
])

