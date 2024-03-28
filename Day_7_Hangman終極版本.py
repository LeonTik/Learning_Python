import random 
import Day_7_hangman_art
from Day_7_hangman_art import logo
print(logo)

should_continue = True 
while should_continue: 
   stage = Day_7_hangman_art.stages 

   chosen_word = random.choice(Day_7_hangman_art.word_list)
   lives = 6 
   print(f'fuck, we got this {chosen_word}') #比自己出貓睇

   display = []

   word_length = len(chosen_word)
   for _ in range(word_length):
      display += "_"
   print(display)

   end_of_game = False

   while not end_of_game: 
      guess = input("Please guess a letter: ").lower()
      if guess in display: 
         print(f"You've already guessed {guess}")

      for position_alphabet in range(len(chosen_word)): 
         letter = chosen_word[position_alphabet] 
         if letter == guess: 
            display[position_alphabet] = letter
            print(display)
         
      if guess not in chosen_word: 
         print(f"You guessed {guess}, that's not in the word. You lose a life")
         lives = lives-1 
         if lives == 0: 
            end_of_game = True 
            print("You lose!!")

         if "_" not in display: 
            end_of_game = True 
            print("You are win")

         print(stage[lives])

   result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
   if result == "no":
      should_continue = False
      print("Bye Bye !!!")      

