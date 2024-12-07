###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
i = 1  # Początkowa wartość zmiennej i, zero nic nie zmienia więc startuje od 1

# Calculate the sum of even numbers 
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1  # Zwiększamy wartość zmiennej i o 1 w każdej iteracji

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
