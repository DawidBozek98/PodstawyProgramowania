import queue

# Tworzenie kolejki 
visited_websites = queue.LifoQueue()


visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    # Jeśli użytkownik chce wrócić do poprzedniej strony
    if website == '0':
        if visited_websites.empty():
            print('No previous website to go back to.')
            break
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get()  # Pobiera ostatnią odwiedzoną stronę

    # jeśli wprowadza nazwę 
    elif website != "":
        visited_websites.put(website)  

    
    print('You are currently viewing:', website)
    print()
