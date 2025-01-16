basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# ** operator rozpakowania
person = {**basic_data, **advanced_data}

print(person)
