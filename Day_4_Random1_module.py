# Random Module (Randomization )
#Random都係用一抽公式 or code 去製造偽random, 因為computer 本身就是決定論
#所以有random module
import random 
import Day_4_my_module

#xyz 其實係random integer
xyz = random.randint(1,10) #賦予一個名比佢eg. xyz, 咁隨機咁由1-10 既range比個整數佢
print(xyz)


#module is responsible for a different bit of functionality
# Module like a part of car, a module for the engine....
#你可以開一個新file裡面可以打 pi=3.14159246, 之後係任何一個file可以import 呢個file (module)
print(Day_4_my_module.pi) #你想要Day_4_my_module 裡面既 pi

#如想佢出0至1之間的小數點 
zxy = random.random() #zxy其實係random_float     *random.random()* generates a random floating-point number between 0 and 1
print(zxy)

#how to create a random decimal number 由0至5之間出小數 (唔同上面, *random.random()* 係好似機率數學 0至1)
randomFloat = random.random()*5  #呢處乘5就得啦
print(randomFloat)

#special task 
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#adding an f before a string allows you to create an f-string, which lets you include variables, functions, and expressions inside the string by enclosing them in curly braces {}.