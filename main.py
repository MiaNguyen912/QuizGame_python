from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])  # object of class Question
    question_bank.append(new_question)
# print(question_bank)

quiz = QuizBrain(question_bank)  # initialize
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You're completed the quiz")
print(f"Your final score was: {quiz.score}/{len.question_bank()}")
