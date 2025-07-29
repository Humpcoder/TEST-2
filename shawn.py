import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print(f"I'm thinking of a number between 1 and 100. Can you guess it in {max_attempts} tries?")
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"🎊 Congratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("⬆️ Too low! Try a higher number.")
            else:
                print("⬇️ Too high! Try a lower number.")
                
            # Show remaining attempts
            print(f"You have {max_attempts - attempts} attempts remaining.")
            
        except ValueError:
            print("⚠️ Please enter a valid number between 1 and 100.")
    
    # If player runs out of attempts
    print(f"\nGame over! The number was {secret_number}.")
    print("Better luck next time! 😊")

# Start the game
if __name__ == "__main__":
    number_guessing_game()