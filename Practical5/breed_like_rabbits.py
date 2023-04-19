#How to get the population of rabbits in each genration andknow at which genration the number of rabbit exceeds 100
#give enough loops,and "n" refers to the generation
for n in range(1,100):
#each generation has 2^n rabbits
	ans = 2**n
	if (ans > 100):
#when the "n" satisfies "ans>100",stop the loop and output this "n"
        	print('The generation exceeding 100 is', n)
        	break
#output the amount of rabbits in each generations
	print(ans)



 
