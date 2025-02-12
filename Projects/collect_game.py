#Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("basket",0, -150)
player.set_size(0.3)
# object = codesters.Sprite("envelope")
stage.set_background("pink")

object_speed = random.randint(-7,-2)
valentines = 0


#Section 2 - Objects
def falling_object():
    global object_speed,object_speed, valentines
    if valentines < 10:
        x = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("envelope", x, y)
        # object.set_size(0.5)
        object.set_y_speed(object_speed)

stage.event_interval(falling_object, 2.5)

#Section 3 - Collision
def collision(player, object):
    global valentines

    if object.get_image_name() == "envelope":
        stage.remove_sprite(object)
        valentines += 1
        if valentines == 10:
            player.say(f"You got ten valentines, you win!",5)
        # else:
        #     player.say(f"You only got {valentines} valentines. You lose.", 0.5)

player.event_collision(collision)

#Section 4 - Controls

#Right Key
def go_right():
    player.move_right(8)

player.event_key("right", go_right)

#Left Key
def go_left():
    player.move_left(10)

player.event_key("left", go_left)