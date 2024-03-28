#整個bidding 既遊戲 
#價高者得 但不知對方出價
import os 
from Day_9_gavel import logo 
print(logo)

def clear_console(): #清走console既野 去返初始問題
    os.system('cls') # "cls" 係os 裡面既command

bid = {} #起一個 bid 既dictionary
bidding_finished = False  
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def find_highest_bidder(bidding_record):# 計邊個出價最高 "bid = {} 變成了 bidding_record = {}"
    highest_bid = 0       #最高價由零開始
    winner = ""          #最高價者 由無人開始

  # Bidding_record = {name:price}

    for bidder in bidding_record:   #在bidding_record(Dictionary) 裡面既叫價者, loop入去
        bid_amount = bidding_record[bidder] #委派bid_amount 成 bidder(key)既value
        if int(bid_amount) > highest_bid: # int 超重要, 攞bid_amount既integer 同 highest_bid 比較
            highest_bid = int(bid_amount)# 當函數 find_highest_bidder() 嘗試將 bid_amount 與 highest_bid 進行比較時，會引發 TypeError，因為一個是字符串，另一個是整數。
            winner = bidder
    print(f"The winner {winner} with a bid of ${highest_bid}")
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

while not bidding_finished: #上面定義了bidding_finished = False, 如果不是false -> 即是True
    name = input("what is your name?: ")  # 要求user 打個名
    price = input("what is your bid?: $") # 要求user 打個投價
    #建構緊個dictionary bid = {}
    
    bid[name] = int(price)  #委派name(key)一個price(value)  #bid = {name: price, name: price, name: price, name: price} 
    
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n") #user 選擇繼續定點
    
    if should_continue == "no": # should_continue, user 選擇no
        bidding_finished = True  # 上面定義了的bidding_finished 變成了True, 以下就可以用上面寫好既function
        find_highest_bidder(bid)  # 呢個function 比左個 bid既dictionary佢 

    elif should_continue == "yes": # should_continue, user 選擇yes
        clear_console()          #清左個console 變返第一條question出黎 "what is your name?"
