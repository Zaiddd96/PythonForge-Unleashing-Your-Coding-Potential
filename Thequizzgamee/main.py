from question_model import Questions
from data import questions
from quiz import Quiz

question_bank = []
for question in questions:
    ques = question["question"]
    ans = question["correct_answer"]
    ques_ans = Questions(ques, ans)
    question_bank.append(ques_ans)

quizz = Quiz(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print(f"You have completed the quiz!\nYour final score was: {quizz.score}/{quizz.question_number}")

