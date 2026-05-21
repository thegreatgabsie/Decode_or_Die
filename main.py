from game import Game


def main():
    print("""
    ====================================
            WELCOME TO
            SYNDROME STRIKE
    ====================================

    A two-player coding theory game
    where players repair and sabotage
    codewords using syndrome decoding.

    --------------- MECHANICS ---------------

    • Each player is given:
        - A correct codeword
        - A corrupted codeword with 1 error

    • Players take turns making moves.

    • Players can see:
        - The parity-check matrix
        - Their own current codeword
        - Their own Hamming distance
        - All player's color status

    • Players CANNOT see the exact
    Hamming distance of their opponent.

    • Instead, the opponent's condition
    is shown using a color status system.

    ------------- STATUS COLORS -------------

    GREEN
    • Opponent has exactly 1 error
    • Their codeword is very close
    to the correct codeword

    YELLOW
    • Opponent is still inside the
    decoding sphere
    • Recovery is still possible

    RED
    • Opponent is outside the
    decoding sphere
    • Their codeword is heavily corrupted

    --------------- MOVES -------------------

    1. ATTACK
    - Flip one bit in the opponent's codeword
    - Used to sabotage their progress

    2. REPAIR
    - Flip one bit in your own codeword
    - Used to fix errors

    3. CHECK SYNDROME
    - Displays the syndrome of your codeword
    - Helps identify possible error positions

    ------------- WIN CONDITION -------------

    You win if:
    • You completely repair your codeword

    OR

    • Your opponent becomes too corrupted
    to recover before you


    ====================================
                GOOD LUCK!
    ====================================
    """)

    game = Game()
    game.run()


if __name__ == "__main__":
    main()