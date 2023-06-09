#Part A: House Hunting
#Goal of part A is to determine how long 
#it will take to save enough money to make the down payment to a house.

#Inputs: 
# total_cost of dream home. 
# portion_down_payment (assume 25%) 
# current_savings =0
# annual return of r, so that monthly return is current_savings*r/12
# annual_salary
# portion_saved, portion of monthly income saved

# Return time in months it will take to save up the down payment

starting_salary=float(input('Enter your Annual Salary in $/yr '))
portion_saved=float(input('Enter the fraction of your monthly income dedicated to savings '))
total_cost=float(input('Enter the cost your dream house in $ '))

month_count=0
current_savings=0
portion_down_payment=0.25
annual_return=0.04

down_payment=portion_down_payment*total_cost

while current_savings<=down_payment:
    
    interest_income=current_savings*annual_return/12
    salary_saved=portion_saved*starting_salary/12
    current_savings+=salary_saved+interest_income
    month_count+=1
print(f'Number of months: {month_count}')

#Both test cases pass, and this matches the style that seems to be request. 
#Could probably do this with exact equation from typical acounting/actuarial math
#But tbh, the loops here are so quick that it's barely worth it, 
# and you can customize this loop in a number of ways

#Verdict, pretty easy. 



