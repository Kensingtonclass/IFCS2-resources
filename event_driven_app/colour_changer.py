import tkinter as tk
import random


class ColourChanger(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class, tk.Tk
        
        # Set initial window properties
        self.geometry("300x300")  # Approximate size for a palm-sized screen
        self.configure(bg='purple')  # Bright purple background
        
        # Create a button with gray background and transparent outline
        self.button = tk.Button(self, text="Click me to change screen colour",
                                command=self.change_colour,  # Link button click to change_colour method
                                bg="gray", fg="black", highlightthickness=0, font=("Helvetica", 16))
        self.button.pack(side="top", expand=True)  # Place the button in the centre of the screen
    
    def change_colour(self):  # Event handler for button click event
        colours = ['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'cyan', 'white', 'black']
        colour = random.choice(colours)  # Choose a random colour from the list
        self.configure(bg=colour)  # Set the background colour of the window to the chosen colour


if __name__ == "__main__":
    app = ColourChanger()
    app.mainloop()  # Start the Tkinter event loop
