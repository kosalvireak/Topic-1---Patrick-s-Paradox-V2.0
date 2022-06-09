print("For Josh")
josh_input = int(input("Enter the amount:"))
josh_interest_rate = int(input("Enter the interest rate:"))
josh_duration = int(input("Enter the duration(in month):"))
print("For Peyton")
Peyton_input = int(input("Enter the amount:"))
Peyton_high_interest_rate = float(input("Enter the high interest rate:"))
Peyton_low_interest_rate = float(input("Enter the low interest rate:"))
Peython_good_return_duration = int(input("Enter the good return duration(in month):"))
Peython_bad_return_duration = int(input("Enter the bad return duration(in month):"))

print("Duration: Money")
for i in range(1,josh_duration+1):
    money =josh_input*(1+(josh_interest_rate/100))**i
    print(format(i, "2"), format(money, "15.2f"))

print("----For Peyton----")
print("Duration: Money")
for i in range(1,Peython_bad_return_duration+1):
    money =Peyton_input*(1-(Peyton_low_interest_rate/100))**i
    print(format(i, "2"), format(money, "15.2f"))
    
for i in range(1,Peython_good_return_duration+1):
    money_remain =money*(1+(Peyton_high_interest_rate/100))**i
    print(format(i+9, "2"), format(money_remain, "15.2f"))