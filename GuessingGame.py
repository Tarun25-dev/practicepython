import random

print("🎮 NUMBER GUESSING CHALLENGE")
print("Win all rounds to become the WINNER!\n")

max_number = 3
max_attempts = 3

while max_number <= 10:
    secret_number = random.randint(1, max_number)
    print(f"🔢 Round: Guess a number between 1 and {max_number}")
    print(f"🎯 Attempts allowed: {max_attempts}")

    won_round = False

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print("✅ Correct! You passed this round.\n")
            won_round = True

            # Reward logic
            if attempt == 1:
                max_attempts = 4
            else:
                max_attempts = 3
            break
        else:
            print("❌ Wrong guess")

    if not won_round:
        print("\n💀 Game Over!")
        print(f"The correct number was {secret_number}")
        break

    max_number += 1

if max_number > 10:
    print("🏆🏆🏆 CONGRATULATIONS! YOU ARE THE WINNER 🏆🏆🏆")
