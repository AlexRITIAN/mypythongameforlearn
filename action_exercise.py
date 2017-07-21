'''action exercise'''
import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import *


class DoAction(cocos.layer.Layer):
    def __init__(self):
        super(DoAction, self).__init__()
        sprite = cocos.sprite.Sprite("hello_world_action_sprite.jpg")
        sprite.position = 320, 240
        sprite.scale = 1
        self.add(sprite)
        #bezier = cocos.path.Bezier((0,0),(300,0),(50,500),(200,100))
        # def my_call(sprite):
        #     print("this function be called")
        action_result = (MoveBy((-100,-200),2) | RotateBy(180,2)) + (MoveBy((100,200),2) | RotateBy(180,2))
        sprite.do(action_result)



class KeyDisplay(cocos.layer.Layer):
    def __ini__(self):
        super(KeyDisplay,self).__init__()
        self.text = cocos.text.Label("",x=320,y=240)
        self.key_pressed = set()
        self.update_text()
        self.add()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(key) for key in self.key_pressed]
        text = "keys : " + ','.join(key_names)
        self.text.element.text = text

    def on_key_press(self,key,modifiers):
        self.key_pressed.add(key)
        self.update_text()

if __name__ == "__main__":
    director.init()
    director.run(Scene(DoAction()))
