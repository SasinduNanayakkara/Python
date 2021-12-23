# handle the quiz game
class QuizBrain:
    def __init__(self, q_list):  # constructor
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):  # next question function
        current_question = self.question_list[self.question_number]  # get the current question
        self.question_number += 1  # increase the question number by 1
        user_answer = input(f"{self.question_number} : {current_question.text} (true/false) : ") # get the user's answer
        self.check_answer(user_answer, current_question.answer)  # call check_answer function

    def still_has_question(self):  # check whether there more question
        return self.question_number < len(self.question_list)  # check length of the question list
        # greater than current question number

    def check_answer(self, user_answer, correct_answer):  # check answer function
        if user_answer.lower() == correct_answer.lower():  # match user input answer and question list answer
            self.score += 1  # increase score by 1
            print("You got it right!")

        else:  # if answer is wrong
            print("That's wrong!")
        print(f"The correct answer id {correct_answer}")  # print the correct answer
        print(f"Your current score is {self.score} / {self.question_number}")  # print the current score
        print("\n")
