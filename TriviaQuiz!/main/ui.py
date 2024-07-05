from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#480607"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk("Quiz Trivia")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="𝐒𝐜𝐨𝐫𝐞: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=414, bg=THEME_COLOR, highlightbackground=THEME_COLOR)
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.text = self.canvas.create_text(150, 207, text="xxx", width=280, font=("Ariel", 15, "italic"),
                                            fill="black")
        self.canvas.grid(row=1, column=1)

        self.true = Button(text="𝐓𝐫𝐮𝐞", width=10, height=3, command=self.true_button)
        self.true.config(fg="black", bg="#ffde2e")
        self.true.grid(row=2, column=0)

        self.false = Button(text="𝐅𝐚𝐥𝐬𝐞", width=10, height=3, command=self.false_button)
        self.false.config(fg="black", bg="#ffde2e")
        self.false.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.label.config(text=f"𝐒𝐜𝐨𝐫𝐞: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)

    def true_button(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def false_button(self):
        self.quiz.check_answer("False")
        self.get_next_question()
