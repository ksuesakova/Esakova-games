import random


def generate_progression(length, start, step):
    return [start + i * step for i in range(length)]


def play_progression_game():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        length = random.randint(5, 10)
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        progression = generate_progression(length, start, step)

        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."

        question = " ".join(map(str, progression))
        print(f"Question: {question}")

        user_answer = input("Your answer: ").strip()

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()
