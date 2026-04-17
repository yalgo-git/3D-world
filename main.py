from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.model = self.loader.loadModel('models/environment')
        self.model.reparentTo(self.render)

        self.model.setScale(0.5)
        self.model.setPos(0, 20, 21)
        self.camLens.setFov(75)

game = Game()
game.run()
