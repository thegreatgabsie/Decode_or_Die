import numpy as np
import random

# --- ADVANCED CODING THEORY CONFIGURATION ---
# Custom [11, 6] Linear Code with d_min = 5.
H = np.array([
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
])

# Subset of valid codewords for players to choose from
VALID_CODEWORDS = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,1,0,1,1,0,0,0,0],
    [0,1,1,0,1,0,1,1,0,0,0],
    [0,0,1,1,0,1,0,1,1,0,0],
    [0,0,0,1,1,0,1,0,1,1,0],
    [0,0,0,0,1,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,1,0,0,1,0,1]
]

def calculate_syndrome(vector):
    """Calculates S = H * r^T over GF(2)"""
    syndrome = np.dot(H, np.array(vector).T) % 2
    return [int(x) for x in syndrome]

def get_hamming_distance(v1, v2):
    return sum(b1 != b2 for b1, b2 in zip(v1, v2))

class Player:
    def __init__(self, name, codeword_index):
        self.name = name
        self.secret_codeword = list(VALID_CODEWORDS[codeword_index])
        self.current_vector = list(self.secret_codeword)

        # Inject exactly 1 random initial error to start in the Green zone
        initial_error_bit = random.randint(0, 10)
        self.current_vector[initial_error_bit] ^= 1

    def get_sphere_color(self):
        dist = get_hamming_distance(self.current_vector, self.secret_codeword)
        if dist <= 1:
            return "GREEN", "\033[92m"
        elif dist <= 3:
            return "YELLOW", "\033[93m"
        else:
            return "RED", "\033[91m"

def print_restricted_board(current_player, opponent):
    """Enforces the strict Fog-of-War rules requested"""
    print("\n" + "="*60)
    print("1. PARITY CHECK MATRIX (H):")
    for row in H:
        print(f"   {row.tolist()}")
    print("-" * 40)

    # Current player details
    dist = get_hamming_distance(current_player.current_vector, current_player.secret_codeword)
    color_name, txt_color = current_player.get_sphere_color()
    clean_vector = [int(bit) for bit in current_player.current_vector]

    print(f"2. YOUR CURRENT CODE: {clean_vector}")
    print(f"3. YOUR HAMMING DISTANCE: {dist} ({txt_color}{color_name}\033[0m Zone)")
    print("-" * 40)

    # Opponent status tracking (Fog of War)
    opp_color_name, opp_txt_color = opponent.get_sphere_color()
    print(f"4. OPPONENT STATUS: {opp_txt_color}{opp_color_name}\033[0m")
    print("="*60)

def main():
    print("=== WELCOME TO SYNDROME STRIKE: ADVANCED CODESPACE ===")
    print("Available Codeword Indexes (1 to 8):")
    for i, cw in enumerate(VALID_CODEWORDS):
        print(f"Index {i + 1}: {cw}")

    p1_idx = int(input("\nPlayer 1, choose your secret codeword index (1-8): ")) - 1
    p2_idx = int(input("Player 2, choose your secret codeword index (1-8): ")) - 1

    p1 = Player("Player 1", p1_idx)
    p2 = Player("Player 2", p2_idx)

    current_player = p1
    opponent = p2

    while True:
        print_restricted_board(current_player, opponent)
        print(f"\n>>> {current_player.name}'s TURN <<<")
        print("1. ATTACK (Corrupt an opponent's bit)")
        print("2. REPAIR (Flip a bit in your own vector)")
        print("3. CHECK SYNDROME (Consumes your entire turn!)")

        choice = input("Select Action (1, 2, or 3): ").strip()

        if choice == "1":
            print(f"Select a bit index to sabotage (1-11): ")
            bit_to_flip = int(input()) - 1  # Convert 1-indexed input back to 0-index internally
            opponent.current_vector[bit_to_flip] ^= 1
            print(f"\n[!] Attack launched at index {bit_to_flip + 1}!")

        elif choice == "2":
            print(f"Select a bit index to repair/flip (1-11): ")
            bit_to_flip = int(input()) - 1  # Convert 1-indexed input back to 0-index internally
            current_player.current_vector[bit_to_flip] ^= 1
            print(f"\n[+] Vector modified at index {bit_to_flip + 1}!")

        elif choice == "3":
            syndrome = calculate_syndrome(current_player.current_vector)
            print(f"\n\033[94m[SYSTEM SCAN] Your Live Syndrome is: {syndrome}\033[0m")
            print("(Your turn ends immediately after analyzing the scan.)")
            input("Press Enter to end turn...")

        else:
            print("Invalid command! Your components stalled and you pass the turn.")

        # --- Evaluate Win/Loss Conditions ---
        opp_dist = get_hamming_distance(opponent.current_vector, opponent.secret_codeword)
        if opp_dist >= 4:
            print_restricted_board(current_player, opponent)
            print(f"\n\033[91mCRITICAL FAILURE! {opponent.name} entered the RED SPHERE (4+ errors). {current_player.name} Wins!\033[0m")
            break

        curr_dist = get_hamming_distance(current_player.current_vector, current_player.secret_codeword)
        if curr_dist == 0:
            print_restricted_board(current_player, opponent)
            print(f"\n\033[92mCOMPLETE CONVERGENCE! {current_player.name} restored their code to 0 errors and wins!\033[0m")
            break

        # Swap players
        current_player, opponent = opponent, current_player

if __name__ == "__main__":
    main()