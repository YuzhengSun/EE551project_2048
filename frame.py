
def init():  # reset the game board and return to state game
    pass


def win():  # shows the game points and goes to init/quit
    pass


def lose():  # shows the game points and goes to init/quit
    pass


def game():  # W,A,S,D,R,Q can be used in this state and goes to  win/lose/init/quit
    pass


# This dictionary is created for calling functions in loops
state_actions = {'INIT': init, 'WIN': win, ' LOSE': lose, 'GAME': game}

# This is a list for users' actions
actions = ['up', 'down', 'left', 'right', 'restart', 'quit']

'''attributes should be added into this class. 
1.reset gameboard 
2.actions be processed 
3.return to other states'''


class Gameboard(object):  # initializes the gameboard which is a n*n(4?6?) matrix
    pass


state = 'Init'
while state != 'Exit':
    state = state_actions[state]()

