from game import Game


def main():
    print("=== SYNDROME STRIKE ===")
    print("Each player starts with:")
    print("- A RANDOM secret codeword")
    print("- EXACTLY 1 starting error")

    game = Game()
    game.run()


if __name__ == "__main__":
    main()