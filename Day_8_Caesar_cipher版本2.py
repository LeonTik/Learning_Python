#版本2
#Day_8_Caesar_cipher版本1 太多重覆 加下將encrypt and decrypt 二合為一
from Day8_art import logo  #import module which you have created 
print(logo) # I wanna use the variable inside the module

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
#你去到Z會發覺無位移 所以加多set字母

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n") #user家下想encode or decode?
text = input("Type your message: \n").lower() #use想encode or decode 邊隻字?
shift = int(input("Type the shift number: \n")) #use想移幾多個位

#有三個parameters, (一開始user輸入既text), (佢想移幾多個位), (佢係想encode or decode) 
def caesar(start_text, shift_amount, cipher_direction):
    end_text = "" # 有for loop 就set 起點比佢 end_text->最終既encode or decode個隻字
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
  #呢句if statement要擺係呢處, 不能放入for loop裡面
    if cipher_direction == "decode": 
        shift_amount *= -1 #shift = shift_amount * -1 , 如user輸入5 此句使其變成 -5
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------        
    for letter in start_text:  #letter係 個隻word既每一個字母 加下我地要拆開佢每一隻字
        position = alphabet.index(letter) #原先某特定既字母既位置 用list.index() 顯示返字母係list到既第幾項
        new_position = position + shift_amount  # 新位置係 == 原先既位置 + 移幾多個位
        end_text += alphabet[new_position] # end_text == end_text + alphabet[new_position] #字母表裡既新位置
        #最終既encode or decode個隻字 一隻一隻字入完呢個loop 加返埋一齊個個樣

    print(f"The {cipher_direction}d text is {end_text}")



caesar(start_text = text, shift_amount = shift, cipher_direction = direction) #呢個係function 


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#後續問題

# 1)what if the user enters a shift that is greater than the number of letters in the alphabet? 

shift = shift % 26 # 如果個user輸入多過26個英文字母大數 咁我地要用% 去除返個勁大既數 用remainder作為移幾多個位shift_amount

# 2)what happens if the user enters a number數字/symbol符號/ space隔行? eg. He types "meet me at 3" 

if cipher_direction == "decode":
    shft_amount *= -1 
for char in start_text: 
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount 
        end_text += alphabet[new_position]
    else:
        end_text += char 


# 3) Can you figure out a way to ask the user if tey want to restart the cipher program? 
#     Type "yes" if you want to go again. otherwise type "no".
#      if they type "yes" then ask them for the direction/text/ shift again and call the caesar() function again? 
# Hint: Try creating a new function that calls itself if they type "yes" 

should_continue = True 
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower() 
    shift = int(input("Type the shift number: \n")) 
    .
    .
    .
    .
    .
    .
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Goodbye")