import math
import random
from VD_games import cli
import prompt

RULES = 'Find the greatest common divisor of given numbers.'

def find_gcd(a, b):
    return math.gcd(a, b)

def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'{a} {b}'
    correct_answer = str(find_gcd(a, b))
    return question, correct_answer

def run_gcd_game():
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
    run_gcd_game()

if __name__ == '__main__':
    main()
