"""A Program to Create a Wordle"""

__author__: str = "730543747"


def contains_char(word: str, character: str) -> bool:
    """Testing if a letter is found in the secret word."""
    assert len(character) == 1, f"len('{character}') is not 1"
    index = 0
    while index < len(word):  # stop loop at the last character of the word
        if word[index] == character:  # when character is in word
            return True
        index += 1  # checks every character in the wword
    return False  # when character is not in word


# defining emoji variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis that codify the reuslts of a Wordle Guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    index = 0  # so we can check every character in the word
    result = ""  # keep track of emojis
    while index < len(guess):  # stop at the last character of the word
        if secret[index] == guess[index]:  # letter is in the right place
            result += GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # letter is in the word but in a different place
            result += YELLOW_BOX
        else:  # letter is not in the word
            result += WHITE_BOX
        index += 1  # to iterate through every character
    return result


def input_guess(n: int) -> str:
    """Prompt user to enter a word with a specified number of characters"""
    guess = input(f"Enter a {n} character word:")
    while len(str(guess)) != int(n):  # make sure word is the right lenght
        guess = input(
            f"That wasn't {n} chars! Try again:"
        )  # if not have them try agian
    return str(guess)


def main(secret: str) -> None:
    """The entry point of the program and main game loop"""
    turns = 1  # keeps track of how many guesses they have made
    print(f"===Turn {turns}/6===")
    guess = input_guess(
        len(secret)
    )  # prompt user to give guess same length as secret word
    while guess != secret and turns < 6:
        print(emojified(guess, secret))  # print result of guess
        turns += 1  # add one to turn count
        print(f"===Turn {turns}/6===")
        guess = input_guess(len(secret))
    if guess == secret:  # for when they win
        print(emojified(guess, secret))  # print result of guess
        print(f"You won in {turns}/6 turns!")
    else:  # for when they loose
        print(emojified(guess, secret))
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
