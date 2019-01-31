'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount=float(input('What amount will you invest?'))
interest_rate=float(input('What is the interest rate in percentage?'))/100
years=float(input('For how may years would you like to invest?'))

future_value=investment_amount*(1+interest_rate)**years

print('This will result in a future value of ', future_value)