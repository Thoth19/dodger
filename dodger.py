# One dimensional dodger atm
import random
HALF_BOARD_SIZE = 5 
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
            if self.pos > HALF_BOARD_SIZE:
                if dangers[self.pos - 1]:
                    self.pos += 1
                else:
                    self.pos -= 1
            else:
                if dangers[self.pos + 1]:
                    self.pos -= 1
                else:
                    self.pos += 1
        else:
            if self.pos > HALF_BOARD_SIZE and not dangers[self.pos-1]:
                self.pos -= 1
            elif self.pos < HALF_BOARD_SIZE and not dangers[self.pos+1]:
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

class LearningPlayer(Player):    
    # Note imcompat with this files gameplay
    def update(self, dangers):
        # call external code
        action = model.evaluate(state)\
        self.pos += action
        
        if self.pos < 0:
            self.pos = 0
        if self.pos > 9:
            self.pos = 9

    def init_model(model):
        self.model = model

class GeneticPlayer(Player):
    """docstring for GeneticPlayer"""
    def update(self, danger_ind):
        pass

class Game(object):
    """docstring for Game"""
    def __init__(self, board_size, player):
        super(Game, self).__init__()
        self.board_size = board_size
        self.player = player
        self.reset()

    def reset():
        self.player.pos = HALF_BOARD_SIZE
        self.score = 0
        self.dangers = [0 for _ in range(board_size)]
        self.alive = True

    def step():
        if not self.alive:
            return -1
        player.update(self.dangers)       

        # Move danger onto board and check for death
        if DANGERS[player.pos] == 1:
            self.alive = False
            return self.score

        # Reset dangers, and add a danger
        self.dangers = [0 for _ in range(board_size)]
        for i in range(score//10 + 1):
            danger = random.randint(0,9)
            self.dangers[danger] = 1
        score += 1

        return 0 # For no error

def game(board_size, player):
    BOARD = list(range(board_size))
    DANGERS = [0 for _ in range(board_size)]
    score = 0
    while True:
        # s = ""
        # for i in DANGERS:
        #     s += str(i)
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
        for i in range(score//10 + 1):
            danger = random.randint(0,9)
            DANGERS[danger] = 1

        score += 1
    return score
if __name__ == '__main__':
    
    # Run single time
    # bob = CleverPlayer(HALF_BOARD_SIZE)
    # print(game(10, bob))

    # Run the whole averaging thing
    bob = CleverPlayer(HALF_BOARD_SIZE)
    l = [game(10, bob) for _ in range(10000)]
    print(sum(l)/float(len(l)))