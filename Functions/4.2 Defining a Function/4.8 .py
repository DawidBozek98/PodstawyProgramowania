# Funkcja formatująca godzinę i minutę na podstawie podanego formatu

def time_string(hours, minutes, time_format):
    if time_format == '24':

        # Format 24-godzinny
        return f'{hours:02}:{minutes:02}'
    
    elif time_format == '12':
        # Format 12-godzinny doklejamy am jeśli mniejszy od 12, jeśli większy doklejamy pm
        period = 'am' if hours < 12 else 'pm'

        # Jeśli godzina to 0 (północ), to jest 12:00am
        if hours == 0:
            return f'12:{minutes:02}{period}'
        
        # Jeśli godzina to 12 (południe), to jest 12:00pm
        elif hours == 12:
            return f'12:{minutes:02}{period}'
        
        # Dla godzin większych niż 12, odejmujemy 12, aby uzyskać godziny w formacie 12-godzinnym
        else:
            return f'{hours % 12 if hours % 12 != 0 else 12}:{minutes:02}{period}'

# Testowanie funkcji time_string
print(time_string(15, 38, '24'))  # 15:38
print(time_string(8, 3, '24'))    # 08:03
print(time_string(0, 5, '24'))    # 00:05
print(time_string(11, 15, '12'))  # 11:15am
print(time_string(0, 7, '12'))    # 12:07am
print(time_string(7, 30, '12'))   # 7:30am
print(time_string(12, 46, '12'))  # 12:46pm
print(time_string(13, 10, '12'))  # 1:10pm
print(time_string(19, 2, '12'))   # 7:02pm
