# One dimensional dodger atm
import random

class Player(object):
    """docstring for Player"""
    def __init__(self, start):
        super(Player, self).__init__()
        self.pos = start
    def update(self, danger_ind):
        ''' Choose a new location '''
        x = random.randint(-1,1)
        self.pos += x
        self.pos = max(0, min(9, self.pos))
        return self.pos

class CleverPlayer(Player):
    """docstring for GeneticPlayer"""
    def update(self, dangers):
        if dangers[self.pos]:
            if self.pos > 5:
                if dangers[self.pos - 1]:
                    self.pos += 1
                else:
                    self.pos -= 1
            else:
                if dangers[self.pos + 1]:
                    self.pos -= 1
                else:
                    self.pos += 1
        self.pos = max(0, min(9, self.pos))
        return self.pos

class LessCleverPlayer(Player):
    """docstring for LessCleverPlayer"""
    def update(self, dangers):
        possib = [-1,0,1]
        for i in range(-1,2):
            try:
                if dangers[self.pos + i]:
                    possib.remove(i)
            except:
                pass
        if len(possib) == 0:
            pass
        else:
            self.pos = self.pos + random.choice(possib)
        self.pos = max(0, min(9, self.pos))
        return self.pos

        

class GeneticPlayer(Player):
    """docstring for GeneticPlayer"""
    def update(self, danger_ind):
        pass
def game(board_size, player):
    board_size = board_size
    BOARD = list(range(board_size))
    DANGERS = [0 for _ in range(board_size)]
    score = 0
    while True:
        # s = ""
        # for i in DANGERS:
            # s += str(i)
        # print(s)
        # print("_"*player.pos + "o" + "_"*(board_size - player.pos -1))
        # print()

        # Update player
        player.update(DANGERS)

        # Move danger onto board and check for death
        if DANGERS[player.pos] == 1:
            break

        # Reset dangers, and add a danger
        DANGERS = [0 for _ in range(board_size)]
        for i in range(score//10):
            danger = random.randint(0,9)
            DANGERS[danger] = 1

        score += 1
    return score
bob = LessCleverPlayer(5)
l = [game(10, bob) for _ in range(10000)]
print(sum(l)/len(l))