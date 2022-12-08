#quiz.py

from string import ascii_lowercase

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

#Functionality that displays question, alternatives and compares user
#input with correct answer

num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    #string.ascii_lowercase uses letters to label alternatives
    #zip() combines letters and alternatives into a dictionary
    #answers are sorted so that the correct answer is not always displayed first
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")
    #takes user input and coverts to integer
    #uses integer as index for alternatives
    #compares alternative selected from user inputted index with correct_answer
    answer_label = input(f"\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

#New: Step 2: Make your application user-friendly
#Handle user errors
#https://realpython.com/python-quiz-application/#handle-user-errors
