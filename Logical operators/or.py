high_income =True
good_credit =True

if (high_income or good_credit):
    print('Eligible for loan')
else:
    print('Not eligible')   #eligible


high_income =True
good_credit =False

if (high_income or good_credit):
    print('Eligible for loan')
else:
    print('Not eligible')    #eligible


high_income =False
good_credit =False

if (high_income or good_credit):
    print('Eligible for loan')
else:
    print('Not eligible')    #not eligible