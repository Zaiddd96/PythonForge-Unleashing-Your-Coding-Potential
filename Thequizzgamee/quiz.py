class Quiz:
    """A class to represent a Quiz."""

    def __init__(self, questions):
        """Initialize the Quiz with a list of questions."""
        self.current_question_index = 0
        self.questions = questions
        self.total_score = 0

    def has_more_questions(self):
        """Check if there are more questions in the quiz."""
        return self.current_question_index < len(self.questions)

    def ask_next_question(self):
        """Ask the next question in the quiz."""
        current_question = self.questions[self.current_question_index]
        self.current_question_index += 1
        user_answer = input(f"Q.{self.current_question_index} {current_question.text} (True/False): ")
        self.verify_answer(user_answer, current_question.answer)

    def verify_answer(self, user_answer, correct_answer):
        """Verify the user's answer and update the score if it's correct."""
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer!")
            self.total_score += 1
        else:
            print(f"Incorrect answer, the correct answer is {correct_answer}.")
        print(f"Your current score is {self.total_score}/{self.current_question_index}\n")


