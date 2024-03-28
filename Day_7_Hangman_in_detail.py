#有隻英文字要你估咁多個字母,估唔到就屌死個火柴人
#https://developers.google.com/edu/python/lists 參考

import random

#做個word_list []
word_list = ["ardvark", "baboon", "camel"]
# 係個word_list 隨機揀詞語  之後assign 呢個隨機揀詞語 成為variable 叫 chosen_word
chosen_word = random.choice(word_list)  

#打印出"所選的詞"以供測試, 測試時可以見到個system揀左咩字
print(f'Pssst, the solution is {chosen_word}.')

# Challenge 2 solution 如何 代替空格位 "_"

display = [] #顯示係 ["_"] 作為起點 
word_length = len(chosen_word) # word_length assign 比 len(chosen_word)==被揀詞語有幾多隻字母 即你有幾長 
for _ in range(word_length): # "_" 係 word_length 既範圍裡 loop入去
   display += "_" # display = display + "_" 直到loop哂成個chosen_word的字母 
print(display)   

guess = input("Please guess a letter: ").lower() #.lower() method 用於將字符串轉換為全部小寫字母

#估中左個字母係會代表"_" 呈現
for position_alphabet in range(len(chosen_word)): #position_alphabet == 你估中的字母 loop入呢個range到
    letter = chosen_word[position_alphabet]  #被揀詞語其中的一個位
    if letter == guess: # when the value is true or false 
        display[position_alphabet] = letter
print(display)      # Display          ["_", "_", "_", "_", "_"]


