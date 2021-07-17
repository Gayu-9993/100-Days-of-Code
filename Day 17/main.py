from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
import keyboard


# This is a program for a Quiz game. 
# The questions are in data.py under question_data.
# This program converts the dictionary items into Question(class) objects, which are appended to a list
# This list will be passed to the QuizBrain(class) object. This will ask the questions
# As long as there are questions in the list, the user will be quizzed. 
# At the end of the question bank list, the final score is displayed.


# list of Question(class) objects. 
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))
    
    # use the following line instead of the one above if using the questions from Trivia DB. 
    
    #question_bank.append(Question(question['question'],question['correct_answer']))


#just shuffling the list to get a bit of randomness
random.shuffle(question_bank)

#QuizBrain(class) object will ask the questions and evaluate. 
quiz = QuizBrain(question_bank)

# use the following line to limit the number of questions if using Trivia DB and dont want the entire 50.

#quiz = QuizBrain(question_bank[:10])


# if there are questions left in the list, we can go on. 
while quiz.still_has_questions():
    quiz.next_question()

# at the end of the game, the final score is displayed.
print(f"Well done. You've completed the quiz. your score was {quiz.score}/{quiz.question_number}")

print("Press escape to exit...")

keyboard.wait('esc')