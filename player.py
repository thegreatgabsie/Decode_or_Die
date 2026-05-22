import random

from codingtheory import (
    get_hamming_distance
)


class Player:

    def __init__(self, name, codeword):

        self.name = name

        self.secret_codeword = (list(codeword))

        self.current_vector = (list(codeword))

        # EXACTLY 1 starting error
        error_bit = random.randint(0, len(self.current_vector) - 1)

        self.current_vector[error_bit] ^= 1

    def get_sphere_color(self, max_correctable_errors):

        dist = get_hamming_distance(self.current_vector, self.secret_codeword)

        # Fully repaired or 1 error
        if dist <= 1:
            return (
                "GREEN",
                "\033[92m"
            )

        # One error before losing
        elif dist == (max_correctable_errors + 1):
            return (
                "RED",
                "\033[91m"
            )

        # Everything in-between
        else:
            return (
                "YELLOW",
                "\033[93m"
            )