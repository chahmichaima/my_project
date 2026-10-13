#Given a tuple which value is integers, is it possible to add more integers to the tuple?
mytuple=(15,20,45,20,65,3)
print(mytuple)
var=list(mytuple)
print(type(var))
var.append(15)
mytuple=tuple(var)
print(mytuple)