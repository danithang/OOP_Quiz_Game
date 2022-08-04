class QuizBrain:
    # initializing to pass over list and create a value for question_number
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        # getting the length of the question_data list/dictionary and returning 12 because there are 12 questions
        # returning True or False to determine if user will go to the next question
        # same thing as writing an if/else statement to return True or False
        return self.question_number < len(self.question_list)

    def next_question(self):
        # getting hold of current question from question_list and getting hold of the current question number
        current_question = self.question_list[self.question_number]
        # making question number increase by 1 for each question
        self.question_number += 1
        # inputting Question number with current question passing in text from Question class and asking True or False
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        # identifying check_answer and inputting user_input and current_question.answer
        # because check_answer was called here, don't have to put it in main.py
        self.check_answer(user_input, current_question.answer)

    # receiving user input and correct_answer(current_question.answer) once we identified it in the next_question method
    # and use it as a parameter
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            # calculating the score to add 1 if user gets question right
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")















