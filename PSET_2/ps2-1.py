b = balance # = 4213
r = annualInterestRate # = .2
m = monthlyPaymentRate # = .04

# monthlyInterestRate = annualInterestRate / 12
r12 = r / 12.0

# minMonthlyPayment = balance * monthlyPaymentRate
p = b * m

# monthlyUnpaidBalance =  balance - minMonthlyPayment
ub = b - p

# updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
newB = ub + r12 * ub

for i in range(11):
  # print('Month: ' + str(i + 1))
  # print('Minimum monthly payment: %.2f' % p)
  # print('Remaining balance: %.2f' % newB)
  # minMonthlyPayment = monthlyUnpaidBalance * monthlyPaymentRate
  p = newB * m

  #monthlyUnpaidBalance -= minMonthlyPayment
  ub = newB - p

  #updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
  newB = ub + r12 * ub
        
        
print('Remaining balance: %.2f' % newB)