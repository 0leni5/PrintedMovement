class Movement:
    def __init__(self):
        self.map = [["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-","-","-"]]
        self.positionX = 0
        self.positionY = 0
        print("Class 'Movement' loaded in.")
    def showMap(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if x == len(self.map[y]) - 1:
                    print(self.map[y][x], end="\n")
                else:
                    print(self.map[y][x], end="")

    def showPosition(self):
        print(f"""Position:
X: {self.positionX}
Y: {self.positionY}""")

    def createPlayer(self):
        self.map[0][0] = "+"
        self.positionX = 0
        self.positionY = 0
        self.showMap()

    def moveUp(self):
        self.map[self.positionY][self.positionX] = "-"
        self.positionY -= 1
        self.map[self.positionY][self.positionX] = "+"
        self.showPosition()
        self.showMap()

    def moveDown(self):
        self.map[self.positionY][self.positionX] = "-"
        self.positionY += 1
        self.map[self.positionY][self.positionX] = "+"
        self.showPosition()
        self.showMap()

    def moveLeft(self):
        self.map[self.positionY][self.positionX] = "-"
        self.positionX -= 1
        self.map[self.positionY][self.positionX] = "+"
        self.showPosition()
        self.showMap()

    def moveRight(self):
        self.map[self.positionY][self.positionX] = "-"
        self.positionX += 1
        self.map[self.positionY][self.positionX] = "+"
        self.showPosition()
        self.showMap()