import random

# Important note: row and column numbers go from 1 to N, not 0 to N-1.

class Board(object):

    def __init__(self, rows=10, cols=10, ships=[5,4,3,2]):
        self.rows = rows
        self.cols = cols
        self.board = {} # maps (x,y) to (size of ship, has_been_shot)
        for ship in ships:
            self.place(ship)

    def place(self, ship):
        # ship = size of the ship
        # try random placement, but if after 10 times, we cannot find
        # something that doesn't overlap with another ship, give up
        for i in range(10):
            row = random.randint(1, self.rows - ship)
            col = random.randint(1, self.cols - ship)
            r, c = random.choice([(0, 1), (1, 0)])
            for s in range(ship):
                if (row + s*r, col + s*c) in self.board:
                    break
            else:
                for s in range(ship):
                    self.board[(row + s*r, col + s*c)] = (ship, False)
                return
        raise Exception("failed to place ship after {} attempts"
                        .format(i+1))

    def __str__(self):
        s = ""
        for r in range(1, self.rows+1):
            for c in range(1, self.cols+1):
                shipsize, shot = self.board.get((r, c), ('~', False))
                mark = '!' if shot else ' '
                s += ("{mark}{shipsize}{mark} "
                      .format(mark=mark, shipsize=shipsize))
            s += '\n'
        s += ("shots: {shots}, hits: {hits}, total ships: {ships}\n"
              .format(**self.stats()))
        return s

    def shoot(self, row, col):
        # returns (size of ship, was_already_shot) tuple
        shipsize, shot = self.board.get((row, col), (0, False))
        self.board[row, col] = shipsize, True
        return shipsize, shot

    def stats(self):
        shots, hits, ships = 0, 0, 0
        for (shipsize, shot) in self.board.values():
            if shipsize>0:
                ships += 1
            if shot:
                shots += 1
            if shipsize>0 and shot:
                hits += 1
        return dict(shots=shots, hits=hits, ships=ships)

        
if __name__ == "__main__":
    b = Board()
    print("Initial board:")
    print(b)
    for i in range(10):
        r = random.randint(1, b.rows)
        c = random.randint(1, b.cols)
        shipsize, shot = b.shoot(r, c)
        print("Shooting {},{}: ship size {}, was{}shot before:"
              .format(r, c, shipsize, " " if shot else " never "))
        print(b)
