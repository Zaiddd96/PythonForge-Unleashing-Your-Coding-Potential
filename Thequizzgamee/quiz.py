class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user, current_question.answer)

    def check_answer(self, user, correct_answer):
        if user.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"You got it wrong, its {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")


