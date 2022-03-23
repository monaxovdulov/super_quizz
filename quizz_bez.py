import json

from game import Game, FLAG_GAME_STARTED
from question import Question


def test_console_run():
    # read json file
    with open('quizz.json') as json_file:
        data = json.load(json_file)

    # parse questions
    questions = []
    for q in data:
        questions.append(Question(q['text'], q['correct'], q['category'], q['score'], q['options']))

    # create game
    game = Game(questions)

    # start game
    game.start()

    # game loop
    while game.status == FLAG_GAME_STARTED:
        question = game.get_current_question()

        # print question and answer options
        print(question.question)
        counter = 1
        for option in question.get_answer_options():
            print(f"{counter}: {option}")
            counter += 1

        # get user answer
        answer = int(input("Select answer: "))

        # check answer
        is_correct = game.answer(answer)
        if is_correct:
            print(f"Correct! score: {game.score}")
        else:
            print(f"Wrong! correct answer was: {question.get_correct_answer()}")

    # game is finished, show final score
    print(f"Total score: {game.score}")


def main():
    pass


if __name__ == '__main__':
    # main()
    test_console_run()
