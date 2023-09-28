class CityAdventureGame:
    def __init__(self, name, city):
        self.name = name
        self.city = city.lower()
        self.city_greetings = {
            "manchester": "Welcome Mancunian! You find yourself at the heart of Manchester, surrounded by its iconic red-brick buildings.",
            "london": "Welcome Londoner! You find yourself amidst the hustle and bustle of the capital city.",
            "bristol": "Welcome Bristolian! You find yourself in Bristol, a city steeped in maritime history.",
        }
        self.city_landmarks = {
            "manchester": ["Manchester City Library", "Old Trafford"],
            "london": ["Tower of London", "Hyde Park"],
            "bristol": ["SS Great Britain", "Clifton Suspension Bridge"],
        }

    def greet_user(self):
        print(f"Hello, {self.name}!")

    def greet_city(self):
        if self.city in self.city_greetings:
            print(f"{self.city_greetings[self.city]}")
        else:
            print("Sorry, your city is not in our list.")
            self.city = None

    def discuss_landmarks(self):
        if self.city in self.city_landmarks:
            landmarks = " and ".join(self.city_landmarks[self.city])
            print(f"In {self.city.capitalize()}, you can explore landmarks like {landmarks}.")

    def start_game(self):
        self.greet_user()
        self.greet_city()
        if self.city:
            self.discuss_landmarks()
        print("\nThank you for playing the City Adventure Game! Hope you had a pleasant conversation.")


name = input("What's your name? ")
city = input("From which city are you? ")
game = CityAdventureGame(name, city)
game.start_game()
