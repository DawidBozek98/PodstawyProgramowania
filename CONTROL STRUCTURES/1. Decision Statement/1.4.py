###
# Credit card payment 
#
account_balance = 500
total_payment = float(input('Enter amount of payment: ')) #Dajemy float bo płatność możę być zmiennoprzecinkowa

if total_payment <= account_balance: #
    print('Payment completed')
else:
    print('No funds')