#quiz.py

import random
from string import ascii_lowercase


NUM_QUESTIONS_PER_QUIZ = 5

#Quiz questions in a dictionary
#Correct answer is always the first alternative in the list
QUESTIONS = {
    "Which king, who succeeded Henry VIII, died when he was 15 years old": [
        "Edward VI", "Charles I", "Harold", "Richard III"
        ], 
    "Is the statement below TRUE or FALSE? Charles II marched into England with a Scottish army to reclaim his throne.": [
        "True", "False"
        ],
    "Which country of the UK is not represented on the Union Flag": [
        "Wales", "Scotland", "Northern Ireland", "England"
        ],
    "Which of these people was a great British playwright": [
        "William Shakespeare", "Sir Francis Drake", "Geoffrey Chaucer", "William Caxton"
        ],
    "When were the first professional football clubs formed": [
        "19th Century", "The Middle Ages", "17th Century", "20th Century"
        ]
}



#sets the number of questions per session determined by which ever is lowest
#NUM_QUESTIONS_PER_QUIZ or the length of the QUESTIONS dictionary
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    #returns a list of random questions
    #k is the sample size determined by num_questions
    return random.sample(list(questions.items()), k=num_questions)


#interacts with user display a question, labeling alternatives with a lowercase
#letter and uses zip to pair label and alternatives into a dictionary
#returns labeled alternatives
def get_answer(question, alternatives):
    print(f"{question}?")
    #string.ascii_lowercase uses letters to label alternatives
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")
    #determines rather user input is a valid label and if not prompts user 
    #for a valid input
    #assigns user input to answer_label
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


#sets correct_answer as the correct answer within the alternatives
#calls get_answer() and compare user answer to correct_answer
#print outcome and return 1 for correct and 0 for incorrect for score keeping
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    #functionality to display alternatives in random order with each iteration
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    #Preprocess: prepares list of questions
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )
    #Process: main loop
    #sets score counter to zero
    num_correct = 0
    #enumerate numbers each question
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        #adds 1 for every correct answer returned by ask_questions()
        num_correct += ask_question(question, alternatives)
    
    #Post-process: print out score
    print(f"\nYou got {num_correct} correct out of {num} questions")



#Run quiz
if __name__ == "__main__":
    run_quiz()