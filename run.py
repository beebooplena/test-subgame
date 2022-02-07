class Spill():
    """
    Game
    """
    def __init__(self) -> None:
        self.brett = []
        self.pcbrett = []

        for row in range(5):
            rad = []
            for kolonne in range(5):
                rad.append('')
                self.brett.append(rad)

    def sjekk_kollisjon(self,x,y, retning):
        """
        Checking collision
        """
        if retning:
            if x > 3:
                print("out of board")
            for rute in range(3):
                if self.brett[y][x + rute] == "x":
                    print("rute opptatt")
        else:
            if y > 3:
                print("out of board")
            for rute in range(3):
                if self.brett[y+rute][x] == "x":
                    print("rute opptatt")
    
    def print_brett(self):
        """
        printing the game
        """
        for rad in self.brett:
            print(rad)


nyttspill = Spill()
nyttspill.print_brett()



