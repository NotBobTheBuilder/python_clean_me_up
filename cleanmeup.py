"""
CleanMeUp - an exercise in reading bad code and writing good code.

Refactor this code so it's readable, testable (bonus points for writing tests),
and has sensibly named functions with clear purpose.

The overall behaviour of the program should be the same - you are *only* to
change the implementation, not the behaviour.

Submit your solution in a Pull Request.

"""
from __future__ import print_function

def get_name(inp=raw_input, out=print):
    """
    get_name - ask the user for their name, say hello and return it

    in  - input stream overriding raw_input
    out - output stream overriding print

    """
    name = inp("What is your name? :: ")
    out("Ok, hello there " + name)
    return name

def random_numbers(count):
    """
    random_numbers  - return a sequence of random numbers

    count           - the length of the desired sequence

    """
    import random
    return (random.randint(0, 1000) for i in xrange(count))

def compare_round(secret, guess):
    """
    compare_round - return 1 if secret > guess, -1 if secret < guess or
                    0 when values are equal

    secret        - number being guessed
    guess         - users attempt at guessing

    """
    return (guess > secret) - (guess < secret)

def round(secret, name, inp=raw_input, out=print):
    """
    round   - keep prompting the user to guess a number, giving them clues until
              they're correct

    secret  - the secret value for this round
    name    - name of the user we're prompting
    in  - input stream overriding raw_input
    out - output stream overriding print

    """
    out("starting a new round")
    while True:
        guess = inp(name + ", guess what the number might be :: ")
        result = compare_guess(int(guess), secret)
        out({
            1: "No, that number is too big",
            0: "That's right, the number is " + guess,
           -1: "No, that number is too small"
        }[result])
        if result == 0: return

if __name__ == "__main__":
    name = get_name()
    for n in random_numbers(3):
      round(n, name)
    print("bye bye")
