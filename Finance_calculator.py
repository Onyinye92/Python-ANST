#Prompt user for their financial details
monthly_income =float(input("Enter your monthly income:"))       #Get user's monthly income
monthly_expenses =float(input("Enter your monthly expenses:"))   #Get user's monthly expenses


#Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses


#Calculate the annual savings with a 5% interest rate
annual_savings = monthly_savings * 12                             #Savings over 12 months
interest = annual_savings * 0.5                                   #Interest rate on annual savings
projected_savings = monthly_savings * 12 * 0.5                     #Project


#Print the result
print("your monthly savings are: ${:.2f}".format(monthly_savings))
print("your projected annual savings after interest are: ${:.2f}".format(projected_savings))