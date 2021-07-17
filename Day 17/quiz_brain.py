# The main class that is responsible for asking the questions and evaluating the user's answers
# the list of Question(class) objects is passed during initialization, and the questions are picked from here


# 


class QuizBrain:

    def __init__(self,q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    # this method will return True if there are still questions available.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    # this method will evaluate the user's input and increment score if correct. 
    def check_answer(self,user_answer,actual_answer):
        if user_answer == actual_answer.lower():
            self.score += 1
            print("Correct !")
        else:
            print("Wrong !!!")
        
        print(f"your score is {self.score}/{self.question_number}\n\n")


    # This method will ask the next question and increment the question number. 
    # will get the user input and call check_answer() for evaluation
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number}. {question.text} True or False : ").strip().lower()
        if user_input == 't':
            user_input = 'true'
        elif user_input == 'f':
            user_input = 'false'

        self.check_answer(user_input,question.answer)
    