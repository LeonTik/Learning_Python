#The FizzBuzz Job interview question
#一班死𡃁仔玩FizzBuzz, 順時針一個個𡃁仔數1,2,3....
#當數到個個數可以比3除盡 個個𡃁仔要叫Fizz 當數到個個數可以比5除盡就叫Buzz
#當數到個個數既可以同時比3和5除盡 就叫FizzBuzz

shout = 0
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0: #記撚住第2行開始要用elif 而不是if
        print("Buzz")
    elif number % 3 and number % 5 == 0:
        print("FizzBuzz")
        shout += number
    else:
        print(number) #如果以上既條件都唔符合咁print返普通數字

