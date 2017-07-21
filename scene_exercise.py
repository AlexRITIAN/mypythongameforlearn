'''exercise scene transition'''
import cocos
import pyglet
from cocos.scene import Scene
from cocos.scenes import *
from cocos.actions import *
from cocos.director import director


class ImgDisplay(cocos.layer.Layer):
    def __init__(self):
        super(ImgDisplay, self).__init__()
        sprite = cocos.sprite.Sprite("hello_world_action_sprite.jpg")
        sprite.position = 320, 240
        sprite.scale = 1
        self.add(sprite)
        sprite.do(Rotate(360, 5))


class KeyDisplay(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(KeyDisplay, self).__init__()
        self.key_pressed = set()

    def on_key_press(self, key, modifiers):
        if pyglet.window.key.symbol_string(key) is "A":
            director.push(FadeTRTransition(Scene(Img2Display(), KeyDisplay())))
        if pyglet.window.key.symbol_string(key) is "D":
            director.push(FadeTRTransition(Scene(ImgDisplay(), KeyDisplay())))


class Img2Display(cocos.layer.Layer):
    def __init__(self):
        super(Img2Display, self).__init__()
        sprite = cocos.sprite.Sprite("img2.jpg")
        sprite.position = 320, 240
        sprite.scale = 1
        self.add(sprite)
        sprite.do(Rotate(360, 5))


if __name__ == "__main__":
    director.init()
    director.run(Scene(ImgDisplay(), KeyDisplay()))
