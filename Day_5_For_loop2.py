#[Interactive Coding Exercise] High Score
student_scores = [78, 65, 89, 86, 55,1000, 64, 89,]
print(max(student_scores)) #一般搵最大既方法
#用for loop 搵最大
highest_scores = 0          #將最高既分數設定 由零開始作為起點 (入左個List會慢慢攞d數來代)             
for score in student_scores:   #進入student_scores 個list 而裡面的item我稱之為score
    if score > highest_scores: #假設 <1st> 當第一個數係 78 係大過個初設值=0       // <2nd>當第二個數係 65 係細過個 78 (個初設值經過第一次條件已成為78) //
        highest_score = score  #     <1st> 咁就會使 highest_score 等於 score (True)// <2nd>咁就不能符合呢個條件(False)                            //
print(f"The highest score in the class is: {highest_score}")
#f 比python知道string裡有value要顯示

# For loop and the range function 
for number in range(1,11,2): #range() 裡面永遠只有兩個數, 第三個數 講緊1-10既range係跳著幾多上 
    print(number) #eg 我想佢顯示1,3,5,7,9 --> range(1,10, 2)

# 知唔知有咩方法係最快計到 1+2+3+4+5+6.......+97+98+99+100 = ?
# Carl Gauss: (第一 + 第尾一) or (第二 + 第尾二) ... 都會等於101, 所以 101 x 50 = sum 

total = 0 #記撚著 相加個總和 會初設其數為0 

for number in range(1,101): #0 進入呢個loop
    total += number #total初設為0 不斷入loop加哂成個range既數 至總和
print(total)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# task to sum up 2+4+6.....+100
total_even_number = 0 
for number in range(2,101,2):
    total_even_number += number
print(total_even_number) #if having indentation, it will show every single step below 

# another way to do the same thing: sum up 2+4+6.....+100
total2 = 0
for number in range(1,101):
    if number % 2 == 0: # remainder is 0, then can add up, otherwise if remainder is 1,2, it will skip them 
        total2 += number 
print(total2)



