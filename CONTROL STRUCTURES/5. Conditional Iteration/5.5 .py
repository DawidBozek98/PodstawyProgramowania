###
# Sums numbers entered by user
#calculates the arithmetic mean of the numbers.
#
total_sum = 0 #  suma wynosi 0.
count = 0 # liczymy ile liczb zostało wprowadzonych
mean = 0 # inicjalizujemy pole średniej

while True:
    number = int(input("Enter a number (0 to stop): ")) #nieskończona pętla która będzie działać do momentu wprowadznia 0
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1 #zwiększamy licznik po każdej liczbie wprowadzonej

    if count > 0:
        mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {round(mean)}")

