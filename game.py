from board import Board

class Game(object):

    def __init__(self, rows=10, cols=10, ships=[5,4,3,2]):

        self.boards = (Board(rows, cols, ships),
                       Board(rows, cols, ships))

        self.nextplayer = 0

    def play(self, player, row, col):
        if player != self.nextplayer:
            return "That's not your turn!"

        otherplayer = 1 - player
        otherboard = self.boards[otherplayer]
        shipsize, shot = otherboard.shoot(row, col)

        # First, check for conditions that do not change the next player
        if shot:
            return ("Already shot that location (result was {}), try again"
                    .format(shipsize))
        stats = otherboard.stats()
        if stats["hits"] == stats["ships"]:
            return "You have won. Game is over."

        # Then, the conditions that *do* change who plays next
        self.nextplayer = otherplayer
        if shipsize == 0:
            return "Miss!"
        return "Hit on boat of size {}!".format(shipsize)

if __name__ == "__main__":
    import random
    import time
    names = ["Nelson", "Nimitz"]
    g = Game()
    while True:
        player = g.nextplayer
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        print("{} shoots {},{}!".format(names[player], row, col))
        result = g.play(player, row, col)
        print result
        print
        if "won" in result:
            break
        print names[0]
        print g.boards[0]
        print names[1]
        print g.boards[1]
