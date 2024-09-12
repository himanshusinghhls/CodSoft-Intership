import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.u = 0
        self.c = 0
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")

        self.points_label = tk.Label(self.root, text=f"Your Points : {self.u} | Computer Points : {self.c}\n")
        self.points_label.pack()

        self.user_label = tk.Label(self.root, text="Enter a choice (rock, paper, scissors):")
        self.user_label.pack()
        self.user_entry = tk.Entry(self.root)
        self.user_entry.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.root.mainloop()

    def play(self):
        user = self.user_entry.get().lower()
        options = ["rock", "paper", "scissors"]
        comp = random.choice(options)

        if user in options:
            result = f"You chose {user}, computer chose {comp}.\n"
        else:
            result = "INVALID CHOICE!!!\n"
            self.result_label.config(text=result)
            return

        if user == comp:
            result += f"Both players selected {user}. It's a tie!\n"
        elif user == "rock":
            if comp == "scissors":
                result += "Rock beats scissors! You win!\n"
                self.u += 1
            else:
                result += "Paper beats rock! You lose.\n"
                self.c += 1
        elif user == "paper":
            if comp == "rock":
                result += "Paper beats rock! You win!\n"
                self.u += 1
            else:
                result += "Scissors beats paper! You lose.\n"
                self.c += 1
        elif user == "scissors":
            if comp == "paper":
                result += "Scissors beats paper! You win!\n"
                self.u += 1
            else:
                result += "Rock beats scissors! You lose.\n"
                self.c += 1

        self.points_label.config(text=f"Your Points : {self.u} | Computer Points : {self.c}\n")
        self.result_label.config(text=result)

        self.user_entry.delete(0, tk.END)

if __name__ == "__main__":
    game = RockPaperScissors()
