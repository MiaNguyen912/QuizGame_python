from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain object of datatype QuizBrain
        # (datatype specializing can be eliminate, but it helps vscode be able to suggest methods and attributes of that datatype)

        self.quiz = quiz_brain

        # set up window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # set up score label
        score = 0
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Courier", 15, "bold"))
        self.score_label.grid(column=2, row=1, sticky="e")

        # set up question canvas
        self.question_box = Canvas(bg="white", width=300, height=250)
        self.question_text = self.question_box.create_text(150, 125, text="Some questions", fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=280)
        self.question_box.grid(column=1, columnspan=2, row=2, pady=50)

        self.get_next_question()  # call this to initialize 1st question

        # set up buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=3)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=3)

        # keep screen on
        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")  # if quiz done, disable the buttons
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True", self.quiz.correct_answer)
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False", self.quiz.correct_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")

        self.window.after(1000, self.get_next_question)
