import random
import logging
logging.basicConfig(level=logging.INFO)

"""to pick a random number and store in guess"""
guess=random.randint(1,100)

logging.info("\nwelcome to the guess the number game:\n")

while True:
    user_guess=int(input("guess a number between 1 to 100:"))
    if user_guess==guess:
        logging.info("congratulation, you guess the right number")
        break
    elif (guess - 10) <= user_guess <= (guess + 10):
        logging.info("you are so close")
    elif user_guess<guess:
        logging.info("your guess is to low")
    elif user_guess>guess:
        logging.info("your guess is to high")
    else:
        logging.info("enter a valid number between 1-100")

        
