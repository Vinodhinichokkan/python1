high_income =True
good_credit =False 

if (high_income and not good_credit):
    print('Eligible for loan')
else:
    print('Not eligible')    #eligible


high_income =True
good_credit =True

if (high_income and not good_credit):
    print('Eligible for loan')
else:
    print('Not eligible')    #not eligible