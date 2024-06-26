from typing import List

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data["results"]:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
