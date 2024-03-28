# keeping track of the player's lives 
#如果條友揀撚錯左 我地要減少一個"live"(生命值) 一根火柴
#if guess is not a letter in the chosen_word, then reduce "live" by 1

import random 
#'''xxxxxxx''' 係大括

stages = ['''
      +-----+
      |     |
      O     |
     /|\    |
     / \    |
            |
==============''',
'''
      +-----+
      |     |
      O     |
     /|\    |
     /      |
            |
==============''',
'''
      +-----+
      |     |
      O     |
     /|\    |
            |
            |
==============''',
'''
      +-----+
      |     |
      O     |
     /|     |
            |
            |
==============''',
'''
      +-----+
      |     |
      O     |
      |     |
            |
            |
==============''',
'''
      +-----+
      |     |
      O     |
            |
            |
            |
==============''']  #砌個圖出黎 


word_list = ["important", "golden", "foul", "apple"]
chosen_word = random.choice(word_list)
lives = 6 #outside the while loop #生命值
print(f'fuck, we got this {chosen_word}')

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game: 
   guess = input("Please guess a letter: ").lower()

   for position_alphabet in range(len(chosen_word)): 
      letter = chosen_word[position_alphabet] 
      if letter == guess: 
         display[position_alphabet] = letter
         print(display)
      
   if guess not in chosen_word: #佢呢到個if 要同個for 排齊 否則生命值會好少
      lives = lives-1 #生命值減1
      if lives == 0: #當個生命值去到零
         end_of_game = True #遊戲結束 == 真
         print("You lose!!")

      if "_" not in display: 
         end_of_game = True 
         print("You are win")

      print(stages[lives]) #stages[] 係一個list , live係值 , stages 裡面既items 對應一個值 
                           #print the stages, and corresponding to the current number of lives
