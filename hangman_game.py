import random
import logging
logging.basicConfig(level=logging.INFO)

words_list = ["hello","hii","python"]
guess = random.choice(words_list)
chance=6
word = "_" * len(guess)

logging.info("\nwelcome to hangman game")
logging.info(f"\nguess the word:{word}")

while True:
    try:
        user_guess=str(input("\nEnter your guess letter:"))
    except:
        logging.info("Enter valid letter a-z")
        continue

    if user_guess in guess:
        new_word=""
        for i in range (len(guess)):
            if user_guess==guess[i]:
                new_word+=user_guess
            else:
                new_word+=word[i]
        logging.info(f"current word:{new_word}")
        word=new_word

    else:
        chance-= 1
        logging.warning(f"word is wrong:\n{chance}")
        if chance==0:
            logging.info("you are loss the game")
            break

    if guess==word:
        logging.info("you are win the game")
        break