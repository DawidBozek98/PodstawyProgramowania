###
# A program that prints your height both in cm and in feet and inches.
#
# 1 stopa = 30.48 cm
# 1 cal = 2.54 cm

cm = 191
feet = cm // 30 #dzielenie bez reszty
remaining_cm = cm % 30 #reszta z dzielenia przez 30
inches = remaining_cm // 2.54 #liczba pełnych cali



print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
#nadal nie rozumiem dlaczego ludzie używają tego systemu metrycznego