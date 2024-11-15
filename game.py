import random
import operator

# Define arithmetic operations
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def generate_question():
    """Generates a random arithmetic question."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(list(OPERATIONS.keys()))

    # Avoid division by zero and ensure proper formatting for division
    if operation == "/":
        num1 = num1 * num2  # Ensure division results in an integer
    question = f"{num1} {operation} {num2}"
    answer = OPERATIONS[operation](num1, num2)
    return question, round(answer, 2)

def ask_question(question, correct_answer):
    """Asks a question and returns if the user's answer is correct."""
    try:
        user_answer = float(input(f"What is {question}? "))
        if abs(user_answer - correct_answer) < 0.01:  # Allow minor rounding errors
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            return False
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return False

def start_quiz():
    """Starts the arithmetic quiz."""
    print("Welcome to the Arithmetic Quiz!")
    num_questions = int(input("How many questions would you like to answer? "))
    
    score = 0
    for i in range(num_questions):
        print(f"\nQuestion {i + 1}/{num_questions}:")
        question, correct_answer = generate_question()
        if ask_question(question, correct_answer):
            score += 1

    print("\n--- Quiz Completed ---")
    print(f"You answered {score}/{num_questions} questions correctly!")
    print("Thanks for playing!")

if __name__ == "__main__":
    start_quiz()
