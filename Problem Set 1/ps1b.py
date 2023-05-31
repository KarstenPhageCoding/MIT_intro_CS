#Part B: Saving with a raise
#Goal of part A is to determine how long 
#it will take to save enough money to make the down payment to a house.

#Inputs: 
# total_cost of dream home. 
# portion_down_payment (assume 25%) 
# current_savings =0
# annual return of r, so that monthly return is current_savings*r/12
# annual_salary
# portion_saved, portion of monthly income saved
# semi-annual raise, 
# so that annual salary will be increased by semi_annual_raise*annual_raise after 6th month, and so on

# Return time in months it will take to save up the down payment

salary=float(input('Enter your Annual Salary in $/yr '))
portion_saved=float(input('Enter the fraction of your monthly income dedicated to savings '))
total_cost=float(input('Enter the cost your dream house in $ '))
semi_annual_raise=float(input('Enter your expected semi_annual_raise '))

month_count=0
current_savings=0
portion_down_payment=0.25
annual_return=0.04

down_payment=portion_down_payment*total_cost

while current_savings<=down_payment:
    
    interest_income=current_savings*annual_return/12
    salary_saved=portion_saved*salary/12
    current_savings+=salary_saved+interest_income
    month_count+=1
    
    if month_count%6==0:
        salary+=semi_annual_raise*salary
        
    
print(f'Number of months: {month_count}')

#Relatively easy to extend, but I'm surprised that the remainder thing 
#worked so easily.