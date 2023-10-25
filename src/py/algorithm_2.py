import random as rand
class game():
    def temple_game():
        a = rand.randrange(1, 100)
        guess = 0
        while (guess != a):
            guess = int(input("What's your guess stranger? "))
            if(guess > a):
                print("Too big")
            if(guess < a):
                print("Too small")
        print("Just right, welcome!")
            