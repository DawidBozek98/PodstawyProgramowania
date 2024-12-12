# Funkcja, która usuwa wszystkie spacje z podanego zdania

def f(sentence):
    # Usuwamy wszystkie spacje za pomocą metody replace()
    return sentence.replace(" ", "")

# Testowanie 
print(f("integrated development environment"))  # Zwróci "integrateddevelopmentenvironment"
print(f("A programming language is a system of notation for writing computer programs"))  
# Zwróci "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
