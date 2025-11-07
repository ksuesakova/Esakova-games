import prompt
from VD_games import cli

def run_game(game_module):
    name = cli.welcome_user()
    print(game_module.RULES)

    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_round()
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
