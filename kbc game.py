import random

def select_question(questions):
    # Select a random question from the list of questions
    return random.choice(questions)

def main():
    questions = [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "B"},
        {"question": "What is the chemical symbol for water?", "options": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"], "answer": "A"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Leo Tolstoy"], "answer": "A"}
    ]

    score = 0

    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win!")

    for i in range(1, 5):
        print("\nQuestion", i)
        question = select_question(questions)
        print(question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer was", question["answer"])

    print("\nQuiz is over!")
    print("Your final score is", score)

if __name__ == "__main__":
    main()
