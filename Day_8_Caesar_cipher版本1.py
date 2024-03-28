#Encryption (part 1 )
#古時加密 只不過將字母 向右移

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #你去到Z會發覺無位移 所以加多set字母

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n") #你加下想encode or decode?
text = input("Type your message: \n").lower() #你想encode or decode 邊隻字?
shift = int(input("Type the shift number: \n")) #你想移幾多個位



def encrypt(plain_text, shift_amount): #有兩個parameters, (user比既原初詞彙), (佢想移幾多個位)
    cipher_text = "" # 有for loop 就set 起點比佢 cipher_text->最終既encode個隻字
    for letter in plain_text:  #letter係 個隻word既每一個字母 加下我地要拆開佢每一隻字
        position = alphabet.index(letter) #原先某特定既字母既位置 用list.index() 顯示返字母係list到既第幾項
        new_position = position + shift_amount # 新位置係 == 原先既位置 + 移幾多個位,  呢到加1 
        new_letter = alphabet[new_position] #新個隻字母 = 字母表裡既新位置
        cipher_text += new_letter  #encode左個隻字 = encode緊個隻字 = 新個隻字母, 一隻一隻字入完呢個loop 加返埋一齊個個樣
    print(f"The encoded text is {cipher_text}")



def decrypt(cipher_text, shift_amount):#有兩個parameters,
    plain_text = ""
    for letter in cipher_text: 
        position = alphabet.index(letter)
        new_position = position - shift_amount #新位置係 == 原先既位置 - 移幾多個位,   呢到減1 
        plain_text += alphabet[new_position]
print("The decoded text is {plain_text}")

if direction == "encode": 
    encrypt(plain_text = text, shift_amount = shift) #如果user揀encode ,就用 encrypt() function
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift) #如果user揀decode ,就用 decrypt() function

