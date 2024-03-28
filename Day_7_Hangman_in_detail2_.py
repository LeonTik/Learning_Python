#how to check if the player Won 
#no more blank 
import random 

word_list = ["important", "golden", "foul", "apple"]
chosen_word = random.choice(word_list)

print(f'fuck, we got this {chosen_word}')

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False # 一定要大階 # (遊戲結束 = false) == 遊戲未結束

while not end_of_game: #如果 遊戲未結束 不是真 (遊戲仲繼續) 就 loop 落去 
   guess = input("Please guess a letter: ").lower()

   for position_alphabet in range(len(chosen_word)): 
      letter = chosen_word[position_alphabet] 
      if letter == guess: 
         display[position_alphabet] = letter
         print(display)
      else:
         print("No match") #如果估撚錯就 print no match 
         #但都不是我們想要的

   if "_" not in display: # 如果到估中洗d字 咁display[] 裡面無哂"_"
      end_of_game = True  #就(遊戲結束 = True) -> 遊戲結束
      print("You are win") #你win
     
     
#記撚著有indentation 