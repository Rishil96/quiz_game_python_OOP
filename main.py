# Use OpenTrivia DB to get more questions for this quiz program

from data import question_data, question_data2_cleaned
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# We have 2 choices for questions ,use question_data or question_data2_cleaned
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

game_on = True
print("Welcome to Quiz Master!\n")
while game_on:
    while quiz.still_has_questions():
        quiz.next_question()
    print("You have completed the quiz!")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")

    play_again = input("Would you like to take the quiz again? (y/n): ")
    if play_again == 'n':
        game_on = False

