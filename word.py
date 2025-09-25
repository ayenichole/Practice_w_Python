secret_word = "chupacabra"
userr = input("Enter a word:")
while userr != secret_word:
    userr = input("Enter a word:")
    #break
else: 
     print("You have successfully guessed the word")