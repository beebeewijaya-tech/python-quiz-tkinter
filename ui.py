from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#fff"
RED_COLOR = "#FF6D6D"
GREEN_COLOR = "#B4FE98"


class QuizInterface(Tk):
    def __init__(self, quiz: QuizBrain):
        super().__init__()
        self.title("Quizzer")
        self.config(width=300, height=300, padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz

        self.init_score()
        self.init_canvas()
        self.init_button_right()
        self.init_button_left()
        self.get_next_question()
        self.mainloop()

    def init_canvas(self):
        self.canvas = Canvas(width=300, height=300, bg=WHITE_COLOR)
        self.question_text = self.canvas.create_text(150, 150, text="Quiz", font=("Arial", 20, "bold", "italic"), fill=THEME_COLOR, width=250)
        self.canvas.grid(column=0, row=1, columnspan=3)


    def init_score(self):
        self.score = Label(text=f"Score = {self.quiz.score}", fg=WHITE_COLOR, bg=THEME_COLOR)
        self.score.grid(column=2, row=0, pady=20)

    def init_button_right(self):
        self.button_right_image = PhotoImage(file="images/true.png")
        self.button_right = Button(
            image=self.button_right_image,
            bg=THEME_COLOR,
            fg=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=THEME_COLOR,
            highlightbackground=THEME_COLOR,
            command=self.true_answer
        )
        self.button_right.grid(column=2, row=3, pady=20)

    def init_button_left(self):
        self.button_left_image = PhotoImage(file="images/false.png")
        self.button_left = Button(
            image=self.button_left_image,
            bg=THEME_COLOR,
            fg=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=THEME_COLOR,
            highlightbackground=THEME_COLOR,
            command=self.false_answer
        )
        self.button_left.grid(column=0, row=3, pady=20)

    def true_answer(self):
        is_true = self.quiz.check_answer("True")
        self.change_canvas_color(is_true)
        self.score.config(text=f"Score = {self.quiz.score}")
        self.after(1000, self.reset_canvas_color)

    def false_answer(self):
        is_true = self.quiz.check_answer("False")
        self.change_canvas_color(is_true)
        self.score.config(text=f"Score = {self.quiz.score}")
        self.after(1000, self.reset_canvas_color)

    def change_canvas_color(self, is_true):
        if is_true:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)

    def reset_canvas_color(self):
        self.canvas.config(bg=WHITE_COLOR)
        self.get_next_question()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{self.question}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've finished the quiz")
            self.button_left.config(state="disabled")
            self.button_right.config(state="disabled")
