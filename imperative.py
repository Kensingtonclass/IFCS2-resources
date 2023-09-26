print('💂🏰')
print("Welcome to the City Adventure Game!")
print("In this game, you'll embark on an exciting journey through different cities.")
print("To navigate through the story, simply type your choices as they appear.")

print("Let's start! Which city are you from?")
city = input("Type 'Manchester', 'London', or 'Bristol': ")

if city.lower() == "manchester":
    print("\nWelcome Mancunian! You find yourself at the heart of Manchester, surrounded by its iconic red-brick buildings.")
    print("Do you wish to explore the historic Manchester City Library or go watch a match at Old Trafford?")
    choice = input("Type 'Library' or 'Old Trafford': ")

    if choice.lower() == "library":
        print("\nYou head to the Manchester City Library. The building is teeming with knowledge and history.")
        print("Do you wish to explore the archives or read a rare book?")
        choice = input("Type 'Archives' or 'Book': ")

        if choice.lower() == "archives":
            print("\nYou delve into the archives and unearth Manchester's rich industrial history. It's a fulfilling day!")
        else:
            print("\nYou read a rare book about the culture of Manchester. It's fascinating!")

    else:
        print("\nYou head to Old Trafford and witness an exhilarating match! The crowd is electric.")
        print("Do you cheer for Manchester United or the visiting team?")
        choice = input("Type 'United' or 'Visiting': ")

        if choice.lower() == "united":
            print("\nYou cheer with the fans for Manchester United. It's a thrilling experience!")
        else:
            print("\nYou cheer for the visiting team. It's a bold move, but you enjoy the match!")

elif city.lower() == "london":
    print("\nWelcome Londoner! You find yourself amidst the hustle and bustle of the capital city.")
    print("Do you wish to visit the iconic Tower of London or relax at Hyde Park?")
    choice = input("Type 'Tower' or 'Park': ")

    if choice.lower() == "tower":
        print("\nYou head to the Tower of London. The historic castle on the north bank of the River Thames is awe-inspiring.")
        print("Do you explore the Crown Jewels or the White Tower?")
        choice = input("Type 'Jewels' or 'White Tower': ")

        if choice.lower() == "jewels":
            print("\nYou witness the dazzling Crown Jewels. It's a once-in-a-lifetime experience!")
        else:
            print("\nYou explore the White Tower and learn about its rich history. It's enlightening!")

    else:
        print("\nYou relax at Hyde Park, enjoying the serene environment amidst the city chaos.")
        print("Do you go for a boat ride or a stroll?")
        choice = input("Type 'Boat' or 'Stroll': ")

        if choice.lower() == "boat":
            print("\nYou enjoy a peaceful boat ride on the Serpentine. It's refreshing!")
        else:
            print("\nYou stroll through the park, taking in the beauty of nature. It's rejuvenating!")

else:  # Bristol
    print("\nWelcome Bristolian! You find yourself in Bristol, a city steeped in maritime history.")
    print("Do you wish to visit the SS Great Britain or explore the Clifton Suspension Bridge?")
    choice = input("Type 'SS Great Britain' or 'Bridge': ")

    if choice.lower() == "ss great britain":
        print("\nYou explore the SS Great Britain, a masterpiece of engineering by Isambard Kingdom Brunel.")
        print("Do you explore the ship or the dockyard?")
        choice = input("Type 'Ship' or 'Dockyard': ")

        if choice.lower() == "ship":
            print("\nYou explore the magnificent ship and learn about its voyages. It's exciting!")
        else:
            print("\nYou explore the historic dockyard and learn about Bristol's maritime heritage. It's fascinating!")

    else:
        print("\nYou head to the Clifton Suspension Bridge, another marvel by Brunel, spanning the Avon Gorge.")
        print("Do you walk across the bridge or explore the visitor centre?")
        choice = input("Type 'Walk' or 'Centre': ")

        if choice.lower() == "walk":
            print("\nYou walk across the bridge, enjoying the stunning views. It's breathtaking!")
        else:
            print("\nYou explore the visitor centre and learn about the bridge's construction. It's intriguing!")

print("\nThank you for playing the City Adventure Game! Hope you had fun exploring different cities and their landmarks.")
