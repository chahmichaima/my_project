#Predict the output of the following code snippets
>>> 3 <= 3 < 9 #true:3<=3 & 3<9
>>> 3 == 3 == 3#true 3==3&3==3
>>> bool(0)#true 
>>> bool(5 == "5")#false:int != str
>>> bool(4 == 4) == bool("4" == "4")#true:bool(true)==bool(true)
>>> bool(bool(None))#false
x = (1 == True)#true 
y = (1 == False)#false 
a = True + 4#true==1 ,so 1+4=5 ,a==5
b = False + 10#false==0,0+10=10 so b==10

print("x is", x)#1
print("y is", y)#0
print("a:", a)#5
print("b:", b)#10