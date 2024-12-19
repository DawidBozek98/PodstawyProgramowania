# Plan posiłków na cały tydzień [śniadanie, obiad, kolacja]
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],  # Poniedziałek
   ["Pancakes", "Sandwich", "Steak"],                  # Wtorek
   ["Smoothie", "Chicken Wrap", "Salmon"],             # Środa
   ["Eggs", "Pasta", "Soup"],                          # Czwartek
   ["Toast", "Burrito", "Pizza"],                      # Piątek
   ["Cereal", "Salad", "Fish Tacos"],                  # Sobota
   ["Bagel", "Rice and Beans", "Stir-fry"]             # Niedziela
]

# Funkcja zwracająca nazwę dnia tygodnia
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Funkcja zwracająca plan posiłków dla danego dnia
# Posiłki oddzielone przecinkami
def day_meal_plan(meal_plan, day_number):
   day_meals = meal_plan[day_number - 1]  # Wybieramy posiłki dla danego dnia
   return ", ".join(day_meals)  # Łączymy posiłki w jeden ciąg znaków

# Wypisanie planu posiłków na cały tydzień
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for i in range(7):
   day_name = weekday(i + 1)  # Pobieramy nazwę dnia tygodnia
   meals = day_meal_plan(meal_plan, i + 1)  # Pobieramy posiłki dla danego dnia
   print(f"{day_name}: {meals}")
