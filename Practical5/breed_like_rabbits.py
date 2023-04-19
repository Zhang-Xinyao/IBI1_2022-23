#How to get the population of rabbits in each genration andknow at which genration the number of rabbit exceeds 100
#give enough loops,and "n" refers to the generation
ans=2
n=1
while True:
#each generation has 2^n rabbits
	ans = 2*ans
	n=n+1
	if (ans > 100):
#when the "n" satisfies "ans>100",stop the loop and output this "n"
        	print('The generation exceeding 100 is', n,'th generation')
        	break
#output the amount of rabbits in each generations
	print(ans)



 
