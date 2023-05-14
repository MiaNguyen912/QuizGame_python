class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list  #list of object
        self.score = 0
        

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_number] #retrieve the current question
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False): ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, correct_answser):
        if user_answer.lower() == correct_answser.lower():
            print("    Your got it right")
            self.score += 1
        else:
            print("    That's wrong.")
        print(f"    The correct answer was: {correct_answser}")
        print(f"    Your current score is: {self.score}/{self.question_number}\n")

