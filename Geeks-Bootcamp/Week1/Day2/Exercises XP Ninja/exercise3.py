#Find an interesting paragraph of text online.
#(Please keep it appropriate to the social context of our class.)
#Paste it to your code, and store it in a variable.
#Let’s analyze the paragraph. 
# Print out a nicely formatted message saying:
#How many characters it contains (this one is easy…).
#How many sentences it contains.
#How many words it contains.
#How many unique words it contains.
#Bonus: How many non-whitespace characters it contains.
#Bonus: The average amount of words per sentence in the paragraph.
#Bonus: the amount of non-unique words in the paragraph.
var="L'intelligence artificielle (IA) est l'ensemble des systèmes informatiques capables d'effectuer des tâches typiquement associées à l'intelligence, telles que l'apprentissage, le raisonnement, la résolution de problèmes, la perception ou la prise de décision. L'intelligence artificielle est également le champ de recherche visant à développer de tels systèmes,"
print (len(var), " characters")
print(len(var.split(","))," sentences")
print(len(var.split(" "))," words")
print(len(set(var.split(" ")))," unique words")