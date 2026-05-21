import random
from constants import H, VALID_CODEWORDS
from player import Player
from codingtheory import (
    calculate_syndrome,
    get_hamming_distance
)


class Game:
    def __init__(self):
        codewords = random.sample(VALID_CODEWORDS, 2)

        self.p1 = Player("Player 1", codewords[0])
        self.p2 = Player("Player 2", codewords[1])

        self.current_player = self.p1
        self.opponent = self.p2

    def print_board(self):
        print("\n" + "=" * 60)
        print("PARITY CHECK MATRIX (H):")

        for row in H:
            print(f"   {row.tolist()}")

        print("-" * 40)

        dist = get_hamming_distance(
            self.current_player.current_vector,
            self.current_player.secret_codeword
        )

        color_name, txt_color = (
            self.current_player.get_sphere_color()
        )

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
            self.opponent.get_sphere_color()
        )

        print(
            f"OPPONENT STATUS: "
            f"{opp_txt}{opp_color}\033[0m"
        )

        print("=" * 60)

    def take_turn(self):
        self.print_board()

        print(f"\n>>> {self.current_player.name}'s TURN <<<")
        print("1. ATTACK")
        print("2. REPAIR")
        print("3. CHECK SYNDROME")

        choice = input("Select Action: ").strip()

        if choice == "1":
            bit = int(
                input("Bit to sabotage (1-11): ")
            ) - 1

            self.opponent.current_vector[bit] ^= 1

        elif choice == "2":
            bit = int(
                input("Bit to repair (1-11): ")
            ) - 1

            self.current_player.current_vector[bit] ^= 1

        elif choice == "3":
            syndrome = calculate_syndrome(
                self.current_player.current_vector
            )

            print(
                f"\n[SYSTEM SCAN] Syndrome: "
                f"{syndrome}"
            )

            input("Press Enter to end turn...")

    def check_win(self):
        opp_dist = get_hamming_distance(
            self.opponent.current_vector,
            self.opponent.secret_codeword
        )

        if opp_dist >= 4:
            print(
                f"\n{self.current_player.name} Wins!"
            )
            return True

        curr_dist = get_hamming_distance(
            self.current_player.current_vector,
            self.current_player.secret_codeword
        )

        if curr_dist == 0:
            print(
                f"\n{self.current_player.name} "
                f"fully repaired their code!"
            )
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