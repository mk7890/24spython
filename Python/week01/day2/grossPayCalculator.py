# Write a program that prompts the user for hours and rate per hour to compute gross pay

hoursWorked = input("Enter Hours: ") # prompt the user to enter hours worked
ratePerHour = input("Enter Rate: ") # prompt the user to enter the rate of pay per hour

pay = int(hoursWorked) * float(ratePerHour) # calculate gross pay by multiplying rate by hours
pay = round(pay, 2) # using round function to set pay to two decimal places
print(f"Pay: {pay}") # pring the gross pass using a formated string
