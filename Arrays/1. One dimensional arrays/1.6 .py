# Funkcja zwraca nazwę dnia tygodnia dla podanego numeru dnia (1-poniedziałek
#  ... 7-niedziela)

def weekday(n):
    # Lista nazw dni tygodnia
    
    weekdays = ["Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Zwracamy odpowiednią nazwę dnia
    return weekdays[n - 1] 


print("Day 1:", weekday(1))
print("Day 4:", weekday(4))
print("Day 7:", weekday(7))
