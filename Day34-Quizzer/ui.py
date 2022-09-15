from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text=f"{quiz}", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_mark = PhotoImage(file="images/true.gif")
        self.right_button = Button(image=right_mark, highlightthickness=0, command=self.check_right)
        self.right_button.grid(row=2, column=0)
        wrong_mark = PhotoImage(file="images/false.gif")
        self.wrong_button = Button(image=wrong_mark, highlightthickness=0, command=self.check_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end./nYour final score is: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)



