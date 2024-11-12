###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))#odległość
fuel_price = float(input('Enter fuel price per liter: '))#cena paliwa
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))#zużycie paliwa
total_fuel_consumption = (distance / 100) * fuel_consumption #dystans/100 * zużycie 
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total transport cost: {total_cost:.2f} currency units')