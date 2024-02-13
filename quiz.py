import random

print("Welcome to the Quiz Game!")
print("You'll be asked several multiple-choice or fill-in-the-blank questions.")
print("Let's see how well you know the topics!")
print("NOTE:every answer should start with lowercase")
questions = {
    "What is the capital of INDIA?": "New Delhi",
    "Where is the Taj Mahal is located?": "Agra",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the full form of SBI": "State Bank of India",
    "Who is the father of AI": "John McCarthy"
}


def present_quiz_questions():
    score = 0
    for question, answer in questions.items():
        print("\nQuestion:", question)
        user_answer = input("Your answer: ").strip().capitalize()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)
    return score

def play_again():
    response = input("\nDo you want to play again? (yes/no): ").lower()
    return response.startswith('y')

def main():
    play = True
    while play:
        score = present_quiz_questions()
        print("\nYour final score is:", score, "out of", len(questions))
        play = play_again()

if __name__ == "__main__":
    main()
