#Section 1: Setup
import codesters 
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



#Section 2: define controls
def move_up(sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_left(sprite):
    sprite.move_left(10)
    
def move_right(sprite):
    sprite.move_right(10)

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)

def forward(sprite):
    sprite.forward(1)

def draw(sprite):
    sprite.pen_down()

def stop_drawing(sprite):
    sprite.pen_up()

#Section 2: define hide and show
def hide (sprite):
    sprite.hide()

def show(sprite):
    sprite.show()

#Section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)
s1.event_key("h", hide)
s1.event_key("g", show)
s1.event_key("j", turn_left)
s1.event_key("k", turn_right)
s1.event_key("u", forward)
s1.event_key("b", draw)
s1.event_key("v", stop_drawing)

#Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")
    

