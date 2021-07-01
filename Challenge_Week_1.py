
# PART 1

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
number_of_loans=len(loan_costs)
print(number_of_loans)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!
sum_of_loans=sum(loan_costs)
print(sum_of_loans)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
average_loans=sum_of_loans/number_of_loans
print(average_loans)


#PART 2

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

loan_price=loan.get("loan_price")
print(loan_price)
remaining_months=loan.get("remaining_months")
print(remaining_months)
repayment_interval=loan.get("repayment_interval")
print(repayment_interval)
future_value=loan.get("future_value")
print(future_value)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate=.20

present_value = round((future_value) / ((1 + discount_rate/12) ** remaining_months),2)
print(present_value)

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
if present_value>=loan_price:
    print("The loan is worth at least the cost to buy it")
else:
    print("The loan is too expensive and not worth the price")


#PART 3



new_loan = {

    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def fair_value(future_value,discount_rate,remaining_months):
    present_value = round((future_value) / ((1 + discount_rate/12) ** remaining_months),2)
    return present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

remaining_months=new_loan.get("remaining_months")
future_value=new_loan.get("future_value")
discount_rate=.2

fair_value=round(fair_value(future_value,discount_rate,remaining_months),2)
print(f"The present value of the loan is: {fair_value}")


#PART 4

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans=[]
inexpensive_loans_sublist=[]

discount_rate=.2

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for loan in loans:
    loan_price=loan["loan_price"]
    remaining_months=loan["remaining_months"]
    repayment_interval=loan["repayment_interval"]
    future_value=loan["future_value"]
    if loan_price<=500:
        inexpensive_loans_sublist.append(loan_price)
        inexpensive_loans_sublist.append(remaining_months)
        inexpensive_loans_sublist.append(repayment_interval)
        inexpensive_loans_sublist.append(future_value)
        inexpensive_loans.append(inexpensive_loans_sublist)
        inexpensive_loans_sublist=[]

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print(inexpensive_loans)


#PART 5





# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

import csv
from pathlib import Path

# Set the output header
headerList = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headerList)
    for loans in inexpensive_loans :
        csvwriter.writerow(loans)