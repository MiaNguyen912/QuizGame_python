import html  # help unescapte html entities (https://www.w3schools.com/html/html_entities.asp)


# example: double quotation mark " == entity '&quot'
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list  # list of object
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.curr_question = self.question_list[self.question_number]  # retrieve the current question
        self.question_number += 1
        self.correct_answer = self.curr_question.answer
        question_text = self.curr_question.text
        question_text = html.unescape(question_text)  # comment out this line and run program to see the difference

        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer, curr_question.answer)

        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer, correct_answser):
        if user_answer.lower() == correct_answser.lower():
            # print("    Your got it right")
            self.score += 1
            return True
        else:
            # print("    That's wrong.")
            return False
        # print(f"    The correct answer was: {correct_answser}")
        # print(f"    Your current score is: {self.score}/{self.question_number}\n")
