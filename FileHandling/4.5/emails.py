import re

# Funkcja do pobrania adresu email nadawcy
def email_sender(email_content):
    # adres nadawcy
    match = re.search(r"^From:\s*(.*?)(?:\s*<(.+?)>)?$", email_content, re.MULTILINE)
    if match:
        return match.group(2) if match.group(2) else match.group(1)  # Zwracamy adres e-mail nadawcy
    return None  # Jeśli nie znaleziono, zwrócimy None

# Funkcja do pobrania adresu 
def email_recipient(email_content):
    match = re.search(r"^To:\s*(.*?)(?:\s*<(.+?)>)?$", email_content, re.MULTILINE)
    if match:
        return match.group(2) if match.group(2) else match.group(1)  
    return None  

# Funkcja do pobrania tematu wiadomości
def email_subject(email_content):
    # Wzorzec do znalezienia tematu
    match = re.search(r"^Subject:\s*(.*)$", email_content, re.MULTILINE)
    if match:
        return match.group(1)  
    return None 

# Funkcja do pobrania treści wiadomości
def email_body(email_content):
    
    match = re.search(r"\r?\n\r?\n(.*)", email_content, re.DOTALL)  # Szukamy tekstu po dwóch pustych liniach
    if match:
        return match.group(1).strip()  
    return None 
