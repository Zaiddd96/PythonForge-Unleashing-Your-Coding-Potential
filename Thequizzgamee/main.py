from question_model import Question
from Database import quiz_questions
from quiz import Quiz

question_bank = []

# Iterate over the questions
for question in quiz_questions:
    # Extract the question and answer
    question_text = question["question"]
    answer = question["correct_answer"]

    # Create a Questions object and append it to the question bank
    question_and_answer = Question(question_text, answer)
    question_bank.append(question_and_answer)

# Create a Quiz object
quiz = Quiz(question_bank)

# While there are still questions in the quiz, ask the next question
while quiz.has_more_questions():
    quiz.ask_next_question()

# Print the final score after the quiz is completed
print(f"You have completed the quiz!\nYour final score was: {quiz.total_score}/{quiz.current_question_index}")


