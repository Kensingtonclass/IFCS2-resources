def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}!")

def greet_city():
    city = input("From which city are you? ").lower()
    city_greetings = {
        "manchester": "Welcome Mancunian! You find yourself at the heart of Manchester, surrounded by its iconic red-brick buildings.",
        "london": "Welcome Londoner! You find yourself amidst the hustle and bustle of the capital city.",
        "bristol": "Welcome Bristolian! You find yourself in Bristol, a city steeped in maritime history.",
    }
    if city in city_greetings:
        print(f"{city_greetings[city]}")
        return city
    else:
        print("Sorry, your city is not in our list.")
        return None

def discuss_landmarks(city):
    city_landmarks = {
        "manchester": ["Manchester City Library", "Old Trafford"],
        "london": ["Tower of London", "Hyde Park"],
        "bristol": ["SS Great Britain", "Clifton Suspension Bridge"],
    }
    if city in city_landmarks:
        landmarks = " and ".join(city_landmarks[city])
        print(f"In {city.capitalize()}, you can explore landmarks like {landmarks}.")

def start_game():
    greet_user()
    city = greet_city()
    if city:
        discuss_landmarks(city)
    print("\nThank you for playing the City Adventure Game! Hope you had a pleasant conversation.")

start_game()
