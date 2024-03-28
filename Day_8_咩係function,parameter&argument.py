def my_infor():
    print("My name is john")
    print("I love girls")

my_infor()

def my_information(name, preference):  # name/ preference= parameter ,  
    print(f"My name is {name}")
    print(f"I love {preference}")

my_information("leon", "sex")  #   leon/ sex = argument  記撚著加" ", 次序係跟著上面既parameter (Positional argument)


def my_language(lan1, lan2):
    print(f"My mother tongue is {lan1}")
    print(f"My second language is {lan2}")
my_language (lan2="English" , lan1="Cantonese" ) #如掉轉了次序 請跟據parameter 去assign 個正確position 比argument

