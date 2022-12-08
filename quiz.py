#quiz.py

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

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f" - {alternative}")
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

