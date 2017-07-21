import cocos
import pyglet
from cocos.actions import *
from cocos.scenes import *
from cocos.director import director

class StartDisplay(cocos.layer.Layer):
    def __init__(self):
        super(StartDisplay,self).__init__()
        sprite = cocos.sprite.Sprite("hello_world_action_sprite.jpg")
        sprite.position = 320,240
        sprite.scale = 1
        self.add(sprite)

if __name__ == "__main__":
    director.init()
    start_Scene = cocos.scene.Scene(StartDisplay())
    start_Scene.do(Twirl(grid=(16,12),duration=2))
    director.run(start_Scene)