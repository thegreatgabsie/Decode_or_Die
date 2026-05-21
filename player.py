import random
from constants import VALID_CODEWORDS
from codingtheory import get_hamming_distance


class Player:
    def __init__(self, name, codeword):
        self.name = name
        self.secret_codeword = list(codeword)
        self.current_vector = list(codeword)

        # EXACTLY 1 starting error
        error_bit = random.randint(0, 10)
        self.current_vector[error_bit] ^= 1

    def get_sphere_color(self):
        dist = get_hamming_distance(
            self.current_vector,
            self.secret_codeword
        )

        if dist <= 1:
            return "GREEN", "\033[92m"
        elif dist <= 3:
            return "YELLOW", "\033[93m"
        else:
            return "RED", "\033[91m"