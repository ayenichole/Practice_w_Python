secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess_number = int(input("Enter an integer to guess the secret number:)"))
while guess_number != secret_number:
        
    if guess_number == secret_number:
        print("Well done, muggle you're free now!")
    else: 
          print("Ha! Ha! You're stuck in my loop.")
