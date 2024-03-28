#點樣可以令個名既字頭變大楷
# .title() 可以令個名既字既大細楷亂左 都變得返正常

def format_name(f_name, l_name): # family_name  &  last_name 
    print(f_name.title())   #string轉換為title case, 即string中每個單詞的首字母大寫
    print(l_name.title())

format_name("john", "choi")


#點樣可以令個名既字既大細楷亂左 都變得返正常

def format_name(f_name, l_name): # family_name  &  last_name 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("jOHn", "cHOI")

# return_________________________________________________________________________________________________________________________________________________________

def format_name(f_name, l_name): # family_name  &  last_name 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}" #return係同個電腦講緊 this is the end of the function, 離開個function
 # 所以你return 之後print野係唔work 架!!!!!!!!!!!

output = len("Angela")
print(output)

print(format_name("joE", "lEe"))

#_____________________________________________________________________________________________________________________________________
# check第幾年第幾個月
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0: 
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

def day_in_month(year, month): 
    month_day = [31, 28, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_day[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = day_in_month(year, month)
print(days)
