# 無return

def add_numbers(num1, num2):
    result = num1 + num2

sum = add_numbers(5, 7) 
print(sum)

#============================================

#有return
def add_numbers(num1, num2):
    result = num1 + num2
    return(result) #本來係 call個 function -> add_numbers(argument 1, argument 2)  --- 就完撚左


#涉及運算 就用return 如果無return 你用上面既function 都出唔到個result  
sum = add_numbers(5, 7) #屌你老母 呢到call 返個 add_numbers 既function, 加兩個argument入去 先可以出到答案
print(sum)

sum2 = add_numbers(6,9)
print(sum2)

asshole = add_numbers(10000220, 382483289423)
print(asshole)