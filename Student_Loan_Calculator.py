"""
This program calculates total amount owed after graduation on student loans,
determines if a given monthly payment is feasible, and determines how long it will
take to pay off your student loans if monthly payment is feasible

@author: Matteo Hernandez

"""

#Part A: Calculating total amount owed after graduation
years = int(input("Enter number of years: "))
loan_per_year = float(input("Enter loan amount per year: "))
interest_rate = float(input("Enter interest rate: "))


total_owed = 0
counter = 0

#While loop that calculates the total amount owed based on previous user input
while counter<years:
    total_owed = (total_owed + loan_per_year) + ((total_owed + loan_per_year)* interest_rate)
    counter += 1
    
    
#typecasts total_owed variable into an integer
total_owed = int(total_owed)
print("\nTotal Owed At Graduation:\n$", total_owed)



#Part B: Determine if monthly payment is feasible
monthly_payment = 0
interest = 0

#Boolean variable for while loop. Loop keeps running until a valid monthly payment is entered
valid = False

while valid != True:
    
    monthly_payment = float(input("Name a monthly payment: "))
    interest = (interest_rate*total_owed)/12
    
    #If/else statement that checks feasibility of monthly payment amount based on user input
    if interest>monthly_payment :
        print("A monthly payment of $",int(monthly_payment)," won't work! You'll be paying your loans forever.")
        valid = False
        
    else:
        print("A monthly payment of $",int(monthly_payment),"will work!")
        valid = True
    print("The minimum monthly payment for this loan would be",int(interest),"dollars.\n")



#Part C: Determine how long it will take to pay off student loans
month = 0

#While loop that calculates the total months to pay off debt based on previous input
while total_owed>0:
    total_owed = (total_owed - monthly_payment)* (1 + (interest_rate / 12) )
    month += 1
    
#to determine years accurately with accrued interest and monthly payments
years = month/12
print("It will take",month,"months to pay off your student loans.")
print("It will take",years,"years to pay off your student loans.")