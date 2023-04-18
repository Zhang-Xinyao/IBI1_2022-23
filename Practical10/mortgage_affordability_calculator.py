#define a function that can calculate the mortgage affordavility
#"x" represents the salary and "y" represents the house value
def calculator(x, y):
#if you buy	a house	worth no more than five	times your annual salary
#output "yes"
#if more than five times 
#output "no"
    if x*5>=y:
        print('Yes')
    else:
        print('No')
#example: salary=3900 and value=18000
calculator(3900,18000)
