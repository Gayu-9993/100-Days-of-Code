print("Welcome to the tip calculator...")
bill_amount = float(input("What was the total bill? $"))
tip_percent = int(input("what percentage tip would you like to give? 10,12 or 15 ? "))
num_people  = int(input('How many people to split the bill into? '))


total_bill = bill_amount + (bill_amount * (tip_percent / 100))

amount_per_person = round((total_bill / num_people),2)
print("Each person should pay $",amount_per_person," as final amount is ",round(total_bill,2))