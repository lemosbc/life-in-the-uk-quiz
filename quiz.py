#quiz.py

import random
from string import ascii_lowercase
import pathlib
#uses tomllib if available if not falls back on toml
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 6
#uses pathlib to tell script that questions.toml is in the same folder
#as quiz.py
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
#reads the questions.toml file then loads the parsed strings into a dictionary
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

#sets the number of questions per session determined by which ever is lowest
#NUM_QUESTIONS_PER_QUIZ or the length of the QUESTIONS dictionary
def prepare_questions(path, num_questions):
    #read toml file and pick-out the questions list
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    #returns a list of random questions
    #k is the sample size determined by num_questions
    return random.sample(questions, k=num_questions)


#interacts with user display a question, labeling alternatives with a lowercase
#letter and uses zip to pair label and alternatives into a dictionary
#returns labeled alternatives
def get_answers(question, alternatives, num_choices = 1):
    print(f"{question}?")
    #string.ascii_lowercase uses letters to label alternatives
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    # Changes the wording according to the number of choices
    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handles invalid answers
        # Assigns user input to answer_label
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue
        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue
         

        return [labeled_alternatives[answer] for answer in answers]


#sets correct_answer as the answer in the question dictionary in the toml table
#calls get_answer() and compare user answer to correct_answer
#print outcome and return 1 for correct and 0 for incorrect for score keeping
def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    #functionality to display alternatives in random order with each iteration
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question = question["question"], 
        alternatives = ordered_alternatives,
        num_choices = len(correct_answers),
    )
    if set(answers) == set(correct_answers):
        print("⭐ Correct! ⭐")
        return 1
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}: "] + correct_answers))
        return 0


def run_quiz():
    #Preprocess: prepares list of questions
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )
    #Process: main loop
    #sets score counter to zero
    num_correct = 0
    #enumerate numbers each question
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        #adds 1 for every correct answer returned by ask_questions()
        num_correct += ask_question(question)
    
    #Post-process: print out score
    print(f"\nYou got {num_correct} correct out of {num} questions")



#Run quiz
if __name__ == "__main__":
    run_quiz()


#Next-step
#Step 5: Expand Your Quiz Functionality
    # Add Hints to Help the User
#https://realpython.com/python-quiz-application/#add-hints-to-help-the-user