from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(145, 130,
                                                     width=280,
                                                     text="Some text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, pady=20, padx=20, columnspan=2)

        self.score_label = Label(text=f"Score: 0",
                                 font=("Ariel", 16, "italic"),
                                 bg=THEME_COLOR,
                                 fg="white")
        self.score_label.grid(row=0, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img,
                                  highlightthickness=0,
                                  pady=20,
                                  padx=20,
                                  command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img,
                                   highlightthickness=0,
                                   pady=20,
                                   padx=20,
                                   command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        que_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=que_text)
        # if self.quiz.still_has_questions():
        #     self.get_next_question()

    def true_answer(self):
        self.quiz.check_answer("True")
        self.score_label["text"] = f"Score: {self.quiz.score}"
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.window.quit()

    def false_answer(self):
        self.quiz.check_answer("False")
        self.score_label["text"] = f"Score: {self.quiz.score}"
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.window.quit()