from Day_8_art import logo 
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

should_continue = True 
while should_continue: 

    direction = input("Which one you wanna go, encode or decode?: ")
    text = input("Type your word here: ") #\n 下一行
    shift = int(input("Please type the shift number: "))

    shift = shift % 26
    def caesar(original_word, shift_amount, cipher_direction):
        final_word = ""
        if cipher_direction == "decode":
            shift_amount = shift_amount * -1
        for character in original_word:
            if character in alphabet:
                position = alphabet.index(character)
                new_position  = position + shift_amount 
                final_word += alphabet[new_position]
            else:
                final_word += character 
        print(f"The{cipher_direction}d text is{final_word}")


    caesar(original_word = text, shift_amount = shift, cipher_direction= direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Bye Bye !!!")