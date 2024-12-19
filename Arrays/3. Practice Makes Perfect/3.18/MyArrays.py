
# Funkcja zwracająca drugi największy element w tablicy
def second_largest(arr):
    arr = list(set(arr))  # Usuwamy duplikaty
    arr.sort()  # Sortujemy tablicę rosnąco
    if len(arr) < 2:
        return None  # Jeśli w tablicy jest mniej niż 2 elementy
    return arr[-2]  # Zwracamy przedostatni element

# Funkcja zwracająca różnicę między największą a najmniejszą wartością w tablicy
def difference_largest_smallest(arr):
    arr.sort()  
    return arr[-1] - arr[0]  # Różnica między największym a najmniejszym

# Funkcja zwracająca medianę liczb w tablicy
def median(arr):
    arr.sort()  # Sortujemy tablicę
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]  # Jeśli liczba elementów jest nieparzysta, zwracamy środkowy element
    else:
        # Jeśli liczba elementów jest parzysta, zwracamy średnią dwóch środkowych
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

# Funkcja zwracająca tablicę z najmniejszą i największą wartością
def smallest_largest(arr):
    arr.sort()  # Sortujemy tablicę
    return [arr[0], arr[-1]]  # Zwracamy tablicę z najmniejszą i największą wartością

# Funkcja zwracająca tablicę jako ciąg znaków oddzielonych myślnikiem
def array_to_string(arr):
    return "-".join(map(str, arr))  # Łączymy elementy tablicy w ciąg znaków
