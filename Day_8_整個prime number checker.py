# 整個prime number checker
#質數 == 只有 1 同自身除個陣 remainder係0

def prime_checker(number):
    is_prime = True   #我們設置 “is_prime” 為 True，我們假設輸入數字是質數 除非另有證明
    for i in range(2, number): #創建一個循環，遍歷 2 和"給定數字"（不包括）之間的所有數字，並將該範圍內的每個數字依次分配給變量 i。
                            #例如，如果用戶輸入 10，則循環將遍歷數字 2、3、4、5、6、7、8 和 9，變量 i 將依次取這些值中的每一個。
                            #該循環用於檢查給定數字是否為質數。 如果 2 到 number（不包括）範圍內的任何數字恰好整除給定數字（即沒有餘數）
                            # 則"給定數字"不是質數，並且變量 is_prime 設置為 False。 如果範圍內的數字都不能整除"給定的數字"，則"給定的數字"是質數，變量 is_prime 保持為 True。
        if number % i == 0:  # eg 10 = "給定的數字" 10/2, 10/3, 10/4, 10/5, 10/6, 10/7, 10/8, 10/9   
            is_prime = False

    if is_prime == True:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
         

n = int(input("check this number: "))
prime_checker(number = n)

#當我們說“inclusive”時，意味著the endpoint包含在範圍內。eg，如果我們說“從 1 數到 10”，這意味著我們將數字 10 作為計數的一部分，並且我們最終得到總共 10 個數字。
#當我們說“exclusive”時，意味著the endpoint不包含在範圍內。 例如，如果我們說“從 1 數到 10 不包括”，這意味著我們不包括數字 10 作為計數的一部分，並且我們最終得到總共 9 個數字。