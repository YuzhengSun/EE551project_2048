import curses
from random import randrange, choice
from collections import defaultdict


def get_user_action():
    pass


class GameField():
    def __init__(self):
        pass

    def reset(self):
        pass

    def draw(self):
        pass


def main(stdscr):
    # reset game board, get into state 'Game'
    def init():
        game_field.reset()
        return 'Game'

    # win state, lead to 'Init' or 'Exit'
    def win():
        # draw current state--win
        game_field.draw(stdscr)
        # get a user's action
        action = get_user_action(stdscr)
        # default the state as current state
        responses = defaultdict(lambda: win)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    # lose state, lead to 'Init' or 'Exit'
    def lose():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: lose)
        return responses[action]

    # game state, lead to 'Game', 'Init' or 'Exit'
    def game():
        # draw current state--game
        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_lose():
                return 'Lose'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': win,
        'Lose': lose,
        'Game': game
    }

    # set win number, default 2048
    game_field = GameField(win_num = 2048)

    state = 'Init'

    # loop
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)




