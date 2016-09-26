initial_balance = balance = 3926 #360
anual_interest_rate = annualInterestRate = .2
fixed_payment = 10

while(balance > 0):
  balance = initial_balance
  for i in range(12):
    balance -= fixed_payment
    balance += balance * (anual_interest_rate / 12)
        
  fixed_payment += 10

print("Lowest Payment: %.f" % (fixed_payment - 10))
    