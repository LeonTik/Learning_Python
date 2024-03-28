#1) Dict 
#   Dictionary = { key: value, key: value}
list = []
tuple = ()
Dict = {}
#2) nesting 可以係個dict 裡面加list / Dict
#   nesting = {key 1 : [list],
#              key 2 : {dictionary}    }


[{[]}, {[]}]
#先比個list[] {}  好似下面咁有組織 
travel_log = [                                    
    {    "country" : "France",
      "我想去既地方":["Paris","Lille","Dijon"], 
        "去過既地方": 12 
    },

    {    "country" : "Germany",         
      "我想去既地方": ["Berlin", "Hamburg", "Stuttgart"],
      "去過既地方": 10
    }
               
        ]

print(travel_log)