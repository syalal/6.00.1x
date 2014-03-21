# -*- coding: utf-8 -*-
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
cumPayment = 0.0

# For each month:
for m in range(1, 13):
    
    myBalance = 0.0
    # Compute the monthly payment, based on the previous month’s balance.
    payment = balance * monthlyPaymentRate
    
    # Update the outstanding balance by removing the payment, then charging interest on the result.
    balance -= payment
    interest = balance * annualInterestRate / 12
    
    # Output the month, the minimum monthly payment and the remaining balance.
    print("Month: " + str(m))
    print("Minimum monthly payment: " + str(round(payment, 2)))
    print("Remaining balance: " + str(round(balance + interest, 2)))
    
    # Keep track of the total amount of paid over all the past months so far.
    myBalance = balance
    balance += interest
    cumPayment += payment
    
# Print out the result statement with the total amount paid and the remaining balance.
print("Total paid: " + str(round(cumPayment, 2)))
print("Remaining balance: " + str(round(myBalance + interest, 2)))
