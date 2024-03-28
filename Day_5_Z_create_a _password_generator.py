#create a password_generator
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
           , "n", "o", "p", "q", "r", "s", "t", "u", "v" ,"w", "x", "z"
           ,"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"
           ,"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your passwords? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

#The random.choice() function 會係個你造既list中隨機地選擇item

#Easy level 造一組Password 含letters/ numbers/ symbols
password = "" 

for char in range (1, nr_letters + 1): #個user 想要幾多個英文字母 char = character, +1 係指 eg. 佢想要5個字母, 但輸入個陣個range只得1-4, 所以+1

    random_char = random.choice(letters) #random.choice係個(letter)呢個list到隨機選擇 就等於 [random_char= 隨機的5個字母]  
    password += random_char # password = password + random_char   
    #password = random_char(1st item, eg.a )+ random_char(2nd item, eg.c) + random_char (3rd item, eg.f) + random_char (4th item, eg.F) + random_char (5th item, eg.E)
    #loop入個list 到直到組成到5 個字母 (acfFE)

for char in range (1,nr_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range (1,nr_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

print(password)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#harder level 造一組Password 含letters/ numbers/ symbols, 不過其中的組合要隨機搞亂 eg. numbers/ letters/ symbols or eg. symbols/ letters/ numbers
password_list = []   # []裡面將會係兜亂的密碼

for char in range (1, nr_letters + 1): 

    random_char = random.choice(letters)
    password_list += random_char

for char in range (1,nr_numbers + 1):
    random_char = random.choice(numbers)
    password_list += random_char

for char in range (1,nr_symbols + 1):
    random_char = random.choice(symbols)
    password_list += random_char

print(password_list)
random.shuffle(password_list) #random.shuffle 將呢個小list 裡面既組合兜亂

password = ""  #D密碼兜亂左喇 咁我想拼返個靚仔D既string
for char in password_list: #入去上面個(password_list) loop著咁generate 個PW
    password += char 

print(f"Your password is: {password}") #"f" 係令{ }裡面個數 可以加埋個string咁print出黎