student_scores = {"Harry": 81,
                  "Ron": 78,
                  "Hermione" : 99,
                  "Draco": 78,
                  "Neville": 62}
for 學生 in student_scores:
           #key
    print(學生)
           #  value     [key]
    print(student_scores[學生])


#__________________________________________________________________________________________________________________________________
#Q1) create an empty dict called student_grade 
student_grades = {}  #對下面好重要 因為佢assign左下面student_grades 新既dict

#Q2) 試寫下如何分類 dictionary 裡既key 且重新比個value佢
student_grades = {} #開左個新Dictionary
for 學生 in student_scores: #攞返舊dict 落黎 loop入去 再用返裡面既key
    score = student_scores[學生] # score = (舊dict裡既key)'s value 
    if score > 90:            #假設 score 達到某個條件 咁就比個新value 佢
        student_grades[學生] = "Outstanding"
    elif score > 80:            # 新value
        student_grades[學生] = "Exceeds Expectations"
    elif score > 70:            # 新value
        student_grades[學生] = "Acceptable"
    else:                       # 新value
        student_grades[學生] = "Fail"

print(student_grades) #print 新Dict