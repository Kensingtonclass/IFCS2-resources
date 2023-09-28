import tkinter as tk
import csv

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        
        self.master.geometry("400x300")
        self.master.configure(bg='fuchsia')

        # Load questions from CSV file
        self.questions = self.load_questions("questions.csv")
        self.current_question = 0
        self.score = 0

        # Create GUI components
        self.question_label = tk.Label(master, text="", wraplength=300)
        self.question_label.pack()

        self.var = tk.StringVar()
        self.option_buttons = [tk.Radiobutton(master, text="", variable=self.var, value=str(i)) for i in range(4)]
        for btn in self.option_buttons:
            btn.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Display the first question
        self.display_question()

    def load_questions(self, filename):
        questions = []
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
        return questions
    
    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'])
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=question[f'option {i + 1}'])
        self.var.set(None)
        self.result_label.config(text="")

    def check_answer(self):
        selected_option = self.var.get()
        if selected_option:
            correct_answer = self.questions[self.current_question]['correct answer']
            selected_answer = self.questions[self.current_question][f'option {int(selected_option) + 1}']
            if selected_answer == correct_answer:
                self.score += 1
                self.result_label.config(text="Correct!")
            else:
                self.result_label.config(text=f"Wrong! The correct answer is {correct_answer}.")
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.master.after(2000, self.display_question)
            else:
                self.master.after(2000, self.display_result)

    def display_result(self):
        self.result_label.config(text=f"You scored {self.score} out of {len(self.questions)}!")
        for btn in self.option_buttons:
            btn.pack_forget()
        self.submit_button.pack_forget()
        self.question_label.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
