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
num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))

#selects a random sample of questions in the QUESTIONS dict where 
#k is the sample size determined by num_questions
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

#Functionality that displays question, alternatives and compares user
#input with correct answer

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    #string.ascii_lowercase uses letters to label alternatives
    #zip() combines letters and alternatives into a dictionary
    #functionality to display alternatives in random order with each iteration
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
        )
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")
    
    #assigns user input to answer_label and prompts user to input valid
    #answer label until they do
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of the {', '.join(labeled_alternatives)}")
    
    #compares user input for answer label with label for correct answer
    #prints a message alerting the user if they were correct or not
    #updates num_correct counter
    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")
