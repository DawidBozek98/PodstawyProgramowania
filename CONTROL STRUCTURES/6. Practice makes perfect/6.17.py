# Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm


time_24hr = input("Enter time (24-hour format): ") #wpisujemy godzinę w formacie 24h


hours, minutes = map(int, time_24hr.split(':')) #oddzielamy godziny od minut tą funkcję znalazłem w internecie

# ustalamy AM lub PM
if hours >= 12:
    period = "pm"
else:
    period = "am"

# zmieniamy na format 12h
if hours == 0:
    hours_12hr = 12  # przypadek pólnocy (00:xx)
elif hours > 12:
    hours_12hr = hours - 12  # przypadek popołudnia (13:xx to 23:xx)
else:
    hours_12hr = hours  # przypadek poranka (01:xx to 11:xx)

time_12hr = f"{hours_12hr}:{minutes:02d}{period}" # zmieniamy czas na format 12h


print(f"Time in 12-hour format: {time_12hr}")
