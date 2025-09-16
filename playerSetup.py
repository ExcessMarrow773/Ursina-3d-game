from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def playerStart():
    player = FirstPersonController()
    player.speed = 100 #4.45
    player.jump_height = 1
    player.scale  = 0.9

    player.x_setter(7)
    player.y_setter(10)
    player.z_setter(7)

    return player
