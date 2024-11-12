###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
#BPKOPLPW, CHASUS33, DEUTDEFF.

swift = input('Enter SWIFT code: ')
bank_code = swift[:4] #wycinamy pierwsze 4 znaki
country_code = swift[4:6] #wycinamy kolejne 2 znaki
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')#brakowało f