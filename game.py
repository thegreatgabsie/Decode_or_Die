import random
import os
from constants import G_HAMMING, G_CUSTOM
from player import Player

from codingtheory import (
    calculate_syndrome,
    get_hamming_distance,
    GenerateCodespace,
    GetParityCheckMatrix,
    get_minimum_distance
)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Game:
    def __init__(self, difficulty):

        if difficulty == "1":
            G = G_HAMMING
            self.mode_name = "HAMMING"

        elif difficulty == "2":
            G = G_CUSTOM
            self.mode_name = "CUSTOM"

        else:
            print("Invalid choice. Defaulting to Hamming.")
            G = G_HAMMING
            self.mode_name = "HAMMING"

        self.H = GetParityCheckMatrix(G)
        self.valid_codewords = GenerateCodespace(G)

        # Auto-detect code length
        self.num_bits = G.shape[1]

        # Auto-detect minimum distance
        self.minimum_distance = get_minimum_distance(self.valid_codewords)

        # Error correction capability
        # For spheres of distance t
        self.max_correctable_errors = (self.minimum_distance - 1) // 2

        codewords = random.sample(self.valid_codewords, 2)

        self.p1 = Player("Player 1", codewords[0])

        self.p2 = Player("Player 2", codewords[1])

        self.current_player = self.p1
        self.opponent = self.p2

    def print_board(self):

        print("\n" + "=" * 60)

        print(f"MODE: {self.mode_name}")
        print("PARITY CHECK MATRIX (H):")

        for row in self.H:
            print(f"   {row.tolist()}")

        print("-" * 40)

        dist = get_hamming_distance(self.current_player.current_vector, self.current_player.secret_codeword)

        color_name, txt_color = (self.current_player.get_sphere_color(self.max_correctable_errors))

        print(
            f"YOUR CURRENT CODE: "
            f"{self.current_player.current_vector}"
        )

        print(
            f"YOUR HAMMING DISTANCE: "
            f"{dist} "
            f"({txt_color}{color_name}\033[0m)"
        )

        print("-" * 40)

        opp_color, opp_txt = (
            self.opponent.get_sphere_color(
                self.max_correctable_errors
            )
        )

        print(
            f"OPPONENT STATUS: "
            f"{opp_txt}{opp_color}\033[0m"
        )

        print("=" * 60)

    def take_turn(self):

        self.print_board()

        print(
            f"\n>>> "
            f"{self.current_player.name}'s TURN <<<"
        )

        print("1. ATTACK")
        print("2. REPAIR")
        print("3. CHECK SYNDROME")

        choice = input(
            "Select Action: "
        ).strip()

        if choice == "1":

            bit = int(
                input(
                    f"Bit to sabotage "
                    f"(1-{self.num_bits}): "
                )
            ) - 1

            self.opponent.current_vector[bit] ^= 1

        elif choice == "2":

            bit = int(
                input(
                    f"Bit to repair "
                    f"(1-{self.num_bits}): "
                )
            ) - 1

            self.current_player.current_vector[bit] ^= 1

        elif choice == "3":

            syndrome = calculate_syndrome(
                self.current_player.current_vector,
                self.H
            )

            print(
                f"\n[SYSTEM SCAN] "
                f"Syndrome: {syndrome}"
            )

            # input(
            #     "Press Enter to end turn..."
            # )

    def check_win(self):

        opp_dist = get_hamming_distance(
            self.opponent.current_vector,
            self.opponent.secret_codeword
        )

        if opp_dist > self.max_correctable_errors + 1:

            print("\n" + "=" * 60)
            print(f"{self.current_player.name} WINS!")
            print("Opponent moved too far outside the decoding sphere!")
            print("=" * 60)

            self.game_over_screen()
            return True

        curr_dist = get_hamming_distance(
            self.current_player.current_vector,
            self.current_player.secret_codeword
        )

        if curr_dist == 0:

            print("\n" + "=" * 60)
            print(f"{self.current_player.name} WINS!")
            print("They fully repaired their codeword!")
            print("=" * 60)

            self.game_over_screen()
            return True

        return False

    def switch_turn(self):

        self.current_player, self.opponent = (
            self.opponent,
            self.current_player
        )

    def run(self):

        while True:

            self.take_turn()

            if self.check_win():
                break

            self.switch_turn()

    def game_over_screen(self):

        print("\nFINAL REVEAL")
        print("=" * 60)

        for player in [self.p1, self.p2]:

            print(f"\n{player.name}")

            print(
                f"Secret Codeword   : "
                f"{player.secret_codeword}"
            )

            print(
                f"Final Codeword    : "
                f"{player.current_vector}"
            )

            dist = get_hamming_distance(
                player.current_vector,
                player.secret_codeword
            )

            print(
                f"Final Distance    : {dist}"
            )

        print("=" * 60)

    def run(self):

        while True:

            clear_screen()
            self.take_turn()

            if self.check_win():
                break

            input("\nPress Enter to continue...")
            clear_screen()

            self.switch_turn()