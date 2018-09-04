# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:24:53 2018

@author: USER
"""
"""time_taken and current_savings is initialised to zero"""
time_taken = 0
r = 0.04
current_savings = 0
#user responses.
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
#portion_saved is a percentage of the monthly salary
portion_saved = portion_saved * (annual_salary/12)
#portion_down_payment is 25% of the total cost.
portion_down_payment = 0.25 * total_cost
# the current savings is increased till it is equal to down payment before we break out of the loop
while current_savings<= portion_down_payment:
 #time_taken = portion_down_payment/portion_saved
    current_savings += (current_savings*r/12) + (portion_saved)
    
    time_taken += 1

print(time_taken)
    