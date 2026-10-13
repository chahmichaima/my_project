#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers={7, 14, 21, 28}
my_fav_numbers.add(42)
my_fav_numbers.add(36)
my_fav_numbers.remove(36)
friend_fav_numbers={10, 20, 30, 40}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
