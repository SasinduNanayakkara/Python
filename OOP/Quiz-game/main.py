# import classes
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create empty list to store new questions
question_bank = []

# loop through the question_data method and assign questions to question_bank
for question in question_data:
    question_text = question["text"] # get the question
    question_answer = question["answer"] # get the answer
    new_question = Question(question_text, question_answer)  # pass the values to the constructor
    question_bank.append(new_question) # add questions and answers into the question_bank

quiz = QuizBrain(question_bank) # create an object of QuizBrain

while quiz.still_has_question(): # until end of all the questions loop through it

    quiz.next_question() # print the next question

print("You've completed the quiz")
print(f"You're final score was : {quiz.score} / {quiz.question_number}") # print the final scored
