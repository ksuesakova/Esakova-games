import random
from VD_games import cli
import prompt

RULES = 'What is the result of the expression?'

def calculate(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case _:
            raise ValueError(f"Unknown operation: {operation}")

def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    answer = str(calculate(a, b, operation))
    question = f'{a} {operation} {b}'
    
    return question, answer

def run_calc_game():
    name = cli.welcome_user()
    print(RULES)
    
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')

def main():
    run_calc_game()

if __name__ == '__main__':
    main()
