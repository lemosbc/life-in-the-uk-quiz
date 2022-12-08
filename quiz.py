#quiz.py


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

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    #answers are sorted so that the correct answer is not always displayed first
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f" {label} {alternative}")
    #takes user input and coverts to integer
    #uses integer as index for alternatives
    #compares alternative selected from user inputted index with correct_answer
    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

