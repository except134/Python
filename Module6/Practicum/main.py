import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pong game"

class Pad(arcade.Sprite):
    def __init__(self):
        super().__init__("pad.png", 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 0.2)
        self.change_x = 5
        self.change_y = 5
        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
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
        
    def update(self, delta_time):
        if arcade.check_for_collision(self.pad, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.pad.update()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.pad.change_x = 8
        if key == arcade.key.LEFT:
            self.pad.change_x = -8

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.pad.change_x = 0

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
    
