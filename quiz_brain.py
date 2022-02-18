class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_output = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_output)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong!")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")