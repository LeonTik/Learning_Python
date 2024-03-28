travel_log = [                                    
    {    "country" : "France",
      "我想去既地方":["Paris","Lille","Dijon"], 
        "去過既地方": 12 
    },

    {    "country" : "Germany",         
      "我想去既地方": ["Berlin", "Hamburg", "Stuttgart"],
      "去過既地方": 10
    }
    ] #以list為主

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#唔掂上而個list 但要加個dict入去 dict本身又有list

def add_new_country(country_visited, times_visited, cities_visited): 
    new_country = {} # new_country 係list 裡面既dict , 所以 new_country係dict 隸屬於 travel log 呢個list 
     #呢個dict 裡面既list 既 "country"(key) 既value係 = country_visited(parameter)       
    new_country["country"] = country_visited
    new_country["我想去既地方"]= cities_visited
    new_country["去過既地方"]= times_visited
    travel_log.append(new_country) #唔該加 new_country入travel_log 既list 

add_new_country ("Russia", 2, ["Moscow", "Saint Petersburg"]) 


print(travel_log)