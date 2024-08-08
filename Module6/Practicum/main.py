import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pong game"

class Pad(arcade.Sprite):
    def __init__(self):
        super().__init__("pad.png", 0.2)

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 0.2)
        self.change_x = 3
        self.change_y = 3
        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.pad = Pad()
        self.ball = Ball()
        self.setup()
        
    def on_draw(self):
        self.clear((0, 0, 0))
        self.pad.draw()
        self.ball.draw()
        
    def setup(self):
        self.pad.center_x = SCREEN_WIDTH / 2
        self.pad.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        
    def update(self):
        self.ball.update()    

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
    
