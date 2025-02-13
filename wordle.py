import random  # Imports the random module, which includes functions for generating random numbers

file = open("words.txt", "r")  # Opens the file "words.txt" in read mode

possible_words = file.read().split('\n')  # Reads the entire file content and splits it into a list at newline characters

file.close()  # Closes the file to free up system resources

answer = random.choice(possible_words)  # Randomly selects one word from the list of possible words as the answer


lives = 6  # Sets the initial number of lives or attempts the player has

while lives > 0:  # Continues the game loop as long as the player has more than 0 lives
  guess = input("Guess a 5 letter word: ")  # Prompts the user to input a guess and stores it
  if len(guess) < 5:  # Checks if the guessed word is shorter than 5 letters
    print("Not enough letters, try again!")  # Informs the user the guess is too short
    continue  # Skips the rest of the loop and starts the next iteration
  if len(guess) > 5:  # Checks if the guessed word is longer than 5 letters
    print("Too many letters, try again!")  # Informs the user the guess is too long
    continue  # Skips the rest of the loop and starts the next iteration
  if guess not in possible_words:  # Checks if the guessed word is not in the list of possible words
    print("Not a valid guess, try again.")  # Informs the user the guess is invalid
    continue  # Skips the rest of the loop and starts the next iteration

  
  colors = ["⬛️"] * 5  # Initializes a list of black square emojis, one for each letter in the word
  answer_list = list(answer)  # Converts the answer word into a list of characters
  guess_list = list(guess)  # Converts the guessed word into a list of characters

  
  for i in range(5):  # Iterates over the indices of the word
    guess_letter = guess_list[i]  # Retrieves the current letter from the guessed word
    answer_letter = answer_list[i]  # Retrieves the corresponding letter from the answer word
    if guess_letter == answer_letter:  # Checks if the guessed letter matches the answer letter at the same position
      guess_list[i] = " "  # Marks the guessed letter as processed by replacing it with a space
      answer_list[i] = "."  # Marks the answer letter as correctly guessed by replacing it with a dot
      colors[i] = "🟩"  # Updates the color to green for a correct guess at the correct position

  
  for i in range(5):  # Iterates again over the indices for letters that were not green to check for yellow
    guess_letter = guess_list[i]  # Retrieves the current letter from the guessed word
    if guess_letter in answer_list:  # Checks if the guessed letter is anywhere in the answer word
      guess_list[i] = " "  # Marks the guessed letter as processed by replacing it with a space
      index = answer_list.index(guess_letter)  # Finds the index of the guessed letter in the answer word
      answer_list[index] = "."  # Marks the letter in the answer list as found by replacing it with a dot
      colors[i] = "🟨"  # Updates the color to yellow for a correct guess but in the wrong position


  print(colors)  # Prints the list of colors indicating the result of the guess
  print("")  # Prints a newline for better readability
  lives -= 1  # Decreases the number of lives by 1 because the player has used one attempt
  
  if colors == ["🟩"] * 5:  # Checks if all letters are correctly guessed (all green)
    print("You guessed it!")  # Congratulates the player for guessing the word
    break  # Exits the loop since the game is won
  else:  # If not all letters are green
    if lives >= 1:  # Checks if the player still has lives left
      continue  # Continues to the next iteration of the loop
    else:  # If no lives are left
      print("You couldn't guess it. The answer was: " + answer)   # Informs the player that they have run out of attempts
      break  # Exits the loop since the game is over