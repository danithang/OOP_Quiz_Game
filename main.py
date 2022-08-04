from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating question bank, using for loop to get a question in question_data
question_bank = []
for question in question_data:
    # creating variables for text and answer and passing the dictionary text and answer from question_data
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # creating a new question variable and calling the Question class with new question and answer
    new_question = Question(question_text, question_answer)
    # appending question_bank with new_question variable to create new questions and answers
    question_bank.append(new_question)

# calling QuizBrain class and passing in question_bank which will be inside question_list attribute and get question
quiz = QuizBrain(question_bank)
# quiz object will call next question while still_has_questions method returns True
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
# adding score and question_number to quiz variable to get final score
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

