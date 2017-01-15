b = balance = 320000
r = annualInterestRate = .2

# monthlyInterestRate = annualInterestRate / 12
r12 = r / 12.0
lb = b / 12.0 #lowBound 
ub = (b * (1 + r12)**12) / 12.0 #lowBound 
#epsilon = 0.1
payOff = False

pay = (lb + ub)/2

while not payOff:
  for i in range(12):
    tempBalance = b
    tempPay = pay
    b -= pay
    b += b * r12

  if tempBalance - tempPay < 0:
    ub = pay

  elif tempBalance - tempPay > 0:
    lb = pay

  else:
    payOff = True

  if 0 < abs(tempBalance - tempPay) < .001:
    payOff = True

  pay = (lb + ub)/2
  b = balance

print('Lowest Payment: %.2f' % tempPay)