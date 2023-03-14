# What does this piece of code do?
# Answer:It draws a random number between 1 and 100 for ten times,and it outputs the largest number among these ten numbers. 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
