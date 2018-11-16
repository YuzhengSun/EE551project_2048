import random
import curses
from itertools import chain
class Action(object):
    UP='up'
    LEFT='left'
    DOWN='down'
    RIGHT='right'
    RESTART='restart'
    EXIT='exit'
    letter_codes =[ord(ch) for ch in 'WASRQwasdrq']
    actions=[UP,LEFT,DOWN,RIGHT,RESTART,EXIT]
    actions_dict=dict(zip(letter_codes,actions*2))
    def __init__(self,stdscr):
        self.stdscr = stdscr
    def get(self):
        char='N'
        while char not in self.action_dict:
            char= self.stdscr.getch()
        return self.action_dict[char]
class Grid(object):
    def __init__(self,size):
        self.size=size
        self.cells=None
        self.reset()
    def reset(self):
        self.cells = [[0 for i in range(self.size)] for j in range(self.size)]
        self.add_random_item()
        self.add_random_irem()
    def add_rnadom_item(self):
        empty_cells=[(i,j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0 ]
    def transpose(self):
        self.cells = [list(row) for row in zip(*self.cells)]
    def invert(self):
        self.cells = [row[::-1] for row in self.cells]