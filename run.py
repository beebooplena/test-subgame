class Spill():
    """
    Game submarine
    """

    def __init__(self) -> None:
        self.brett = []

        for row in range(5):
            rad = []
            for kolonne in range(5):
                rad.append('')
            self.brett.append(rad)

    def sjekk_kollisjon(self, x, y, retning):
        """
        Checking collision
        """
        if retning:
            if x > 3:
                print("out of board")
            for rute in range(3):
                if self.brett[y][x + rute] == 'x':
                    print("rute opptatt")
        else:
            if y > 3:
                print("out of board")
            for rute in range(3):
                if self.brett[y+rute][x] == 'x':
                    print("rute opptatt")

    def place_ship(self, x, y, retning):
        """
        placing the ships
        """
        self.sjekk_kollisjon(x, y, retning)
        if retning:
            for rute in range(3):
                self.brett[y][x+rute] = 'x'
        else:
            for rute in range(3):
                self.brett[y+rute][x] = 'x'
    
    def shoot(self, x, y):
        """
        hit
        """
       
        if self.brett[y][x] == 'x':
                    print("hit")
        
        else:
            print("missed")



    def print_brett(self):
        """
        printing the game
        """
        for rad in self.brett:
            print(rad)


nyttspill = Spill()
nyttspill.print_brett()
nyttspill.place_ship(0, 1, 0)
nyttspill.print_brett()
nyttspill.shoot(0, 0)
nyttspill.print_brett()
