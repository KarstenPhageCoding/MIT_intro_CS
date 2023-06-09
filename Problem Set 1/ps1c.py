# In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
# and your annual raise affect how long it takes you to save for a down payment.  This is nice, but 
# suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years. 
# How much should you save each month to achieve this?  In this problem, you are going to write a 
# program to answer that question.  To simplify things, assume: 

# 1. Your semi­annual raise is .07 (7%) 
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M. 
 
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
# the required down payment.

# inputs    
#input_salary=float(input('Enter your Annual Salary in $/yr '))

# globals
portion_down_payment=0.25
total_cost=1000000
semi_annual_raise=0.07
annual_return=0.04
time_frame=36 #months
down_payment=portion_down_payment*total_cost

    
    



def savings(savings_rate, starting_salary):
    current_savings=0
    salary=starting_salary
    for month in range(1,time_frame+1):
        interest_income=current_savings*annual_return/12
        salary_saved=savings_rate*salary/12
        current_savings+=salary_saved+interest_income
        if month%6==0:
            salary+=semi_annual_raise*salary
    return current_savings
        


def bisection_search(input_salary):
    #return portion of salary saved a month to reach goal
    #Search range: savings_rate*10,000 from 0 to 10,000
    #goal: savings=250,000 +/- 100
    
    left_bound, right_bound = 0, 10000
    savings_rate=round((right_bound+left_bound)/2) #initial guess
    residual = savings(savings_rate/10000, input_salary)-down_payment
    bisect_count=0
    while not abs(residual)<100:
        if residual > 0:
            #savings rate is too high, so take lower half of interval
            right_bound=savings_rate
            savings_rate=round((right_bound+left_bound)/2)
            
        elif residual < 0:
            left_bound=savings_rate
            savings_rate=round((right_bound+left_bound)/2)
        bisect_count+=1
        residual = savings(savings_rate/10000, input_salary)-down_payment
        
        if savings_rate == 10000: 
            print('It is not possible to save for the house in three years.')
            break    
    return (savings_rate/10000, bisect_count, residual)

print(bisection_search(150000))

#Test cases pass, but the style with inputs/outputs makes it annoying to debug. 
# You can easily make this file match the hw by following the first two problems in the set. 
            