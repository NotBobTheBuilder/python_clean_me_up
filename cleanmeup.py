"""
CleanMeUp - an exercise in reading bad code and writing good code.

Refactor this code so it's readable, testable (bonus points for writing tests),
and has sensibly named functions with clear purpose.

The overall behaviour of the program should be the same - you are *only* to
change the implementation, not the behaviour.

Submit your solution in a Pull Request.

"""
class GuessingGame:
    import random
    def __init__(self, rounds, read=input, write=print, source=random.random):
        self.rounds = rounds
        self.read   = read
        self.write  = write

        self.name   = self.read("What is your name? :: ")
        self.write("Ok, hello there " + self.name)
        self.secrets = (int(source() * 100) for _ in range(self.rounds))

    def __iter__(self):
        return self

    def __next__(self):
        secret = next(self.secrets)
        self.write("starting a new round")
        guess = secret + 1
        while not int(guess) == secret:
            guess = self.read(self.name + ", guess what the number might be :: ")
            self.write(self.guess_clue(secret, int(guess)))

    def guess_clue(self, secret, guess):
        def compare_guess(secret, guess):
            return (guess > secret) - (guess < secret)

        return {
            1: "No, that number is too big",
            0: "That's right, the number is " + str(guess),
           -1: "No, that number is too small"
        }[compare_guess(secret, guess)]

if __name__ == "__main__":
  list(GuessingGame(2))
  print("bye bye")
