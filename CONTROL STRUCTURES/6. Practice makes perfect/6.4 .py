# Password length has a significant impact on the level of data protection. 
# Write a program that checks whether the new password provided 
# is at least 12 characters long.

###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')
if len(new_password) < 12: #przypisujemy zmienną i ustawiamy długość < 12
   print('Password too short (min. 12 chars)') 
else:
   print('Password is long enough')