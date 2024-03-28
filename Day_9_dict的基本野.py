#  Dictionary 
#                  key      :    Value 
suck_my_dict = {"distraught": "extremely worried, nervous, or upset:",  
                "antelope":"羚羊", 
                "otter": "水獺", 
                "llama":"大羊駝" , 
                "cobra":"眼鏡蛇", 
                "hyena":"鬣狗", 
                "raccoon" : "浣熊", 
                "sloth" : "樹懶", 
                "ostrich": "鴕鳥",
                "platypus":"鴨嘴獸" }
print(suck_my_dict[ "cobra"])

suck_my_dict["hyena"]="警察" #轉呢個dictionary key既value 
print(suck_my_dict)



#----------------------------------------------------------------------------------------------------------------------------------------
#如何抹去已存在的dictionary 
suck_my_dict = {"distraught": "extremely worried, nervous, or upset:",  
                "antelope":"羚羊", 
                "otter": "水獺", 
                "llama":"大羊駝" , 
                "cobra":"眼鏡蛇", 
                "hyena":"鬣狗", 
                "raccoon" : "浣熊", 
                "sloth" : "樹懶", 
                "ostrich": "鴕鳥",
                "platypus":"鴨嘴獸" }


suck_my_dict = {} #創建多個{}係呢到
print(suck_my_dict[ "cobra"]) #print() 移左落黎

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#如何loop though 個dictionary
suck_my_dict = {"distraught": "extremely worried, nervous, or upset:",  
                "antelope":"羚羊", 
                "otter": "水獺", 
                "llama":"大羊駝" , 
                "cobra":"眼鏡蛇", 
                "hyena":"鬣狗", 
                "raccoon" : "浣熊", 
                "sloth" : "樹懶", 
                "ostrich": "鴕鳥",
                "platypus":"鴨嘴獸" }

for thing in suck_my_dict:  
    print(thing)#但只會比你 key 無value
    print(suck_my_dict[thing]) #舯所以要加多呢行落去  suck my dict裡面既key 都print埋出黎 唔該
