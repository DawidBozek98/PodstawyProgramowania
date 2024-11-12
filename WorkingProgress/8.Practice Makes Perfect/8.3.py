###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

#temperatura w Kelvinach K = C + 273.15
#temperatura w Fahrenheitach F = 9/5 * C + 32

celcius = float(input("Enter temperature in Celcius: ")) #pobieramy temperaturę w celciuszach poprzez funkcję input()

kelvin = celcius + 273.15 #temperatura w kelvinach obliczana jest przez użycie wzoru

fahrenheit = (9/5) * celcius + 32

print(f'Temperature in Kelvin: {kelvin:.2f}')#drukujemy wartość w kelvinach zaokrąglając do 2 miejsc po przecinku
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')