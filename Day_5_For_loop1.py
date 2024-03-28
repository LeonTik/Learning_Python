fruits = ["Apple", "Peach", "Pear"]
for X in fruits: #如我想Print out list裡面所有items, 我可以比個統稱佢地 eg. X
    print(X)   #indentation 是非常重要 (tab隔兩個格)
    print(X + " pie")



#用for loop
the_entire_list = [180, 124, 165, 173, 189, 169, 146]
start_from_scratch = 0
for each_item_in_the_list in the_entire_list:
    start_from_scratch += each_item_in_the_list
    print(start_from_scratch)

# start_from_scratch += each_item_in_the_list (for the sum up of all items)
# start_from_scratch += 1 (for how many items in the list)

#task 1 搵總和
    total_height = sum(student_heights) #一般sum function情況
  
 #task 1 For loop
student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0  #由零開始
for height in student_heights: #入呢個list加呢堆height 
    total_height += height #由list裡面第一項加上去，加返height個個數
    print(total_height) 

#task 2 搵list裡面有幾多個items 
    number_of_students = len(student_heights) #一般len function情況

#task 2 for loop
student_heights = [180, 124, 165, 173, 189, 169, 146]
number_of_students = 0
for student in student_heights: #list裡面有幾多個items(有幾多個學生)
    number_of_students += 1 #每loop一次加1
    print(number_of_students)

#最後就計 average_height, 將上面計好的總身高除以學生人數
average_height = round(total_height/ number_of_students) # round --> 四捨五入
print(average_height)