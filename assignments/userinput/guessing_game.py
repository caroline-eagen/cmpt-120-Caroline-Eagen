def start():
    print("Guess the animal in 3 guesses. To exit the game enter 'quit'.")
    answer = "monkey"
    guess_count = 0
    guess_limit = 3
    quit = "quit"
    
    while guess_count < guess_limit:
        guess = input("guess an animal: ").lower()
        guess_count += 1
        
        if guess == answer:
            print("Congratulations! You guessed correctly!")
            break
        
        elif guess == quit:
            break
        
        else:
            print("Your answer is incorrect. Please guess again. You have ", guess_limit - guess_count, "tries left!")

    
    return None

start()