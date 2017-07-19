import cocos
from cocos.actions import *


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super(HelloWorld, self).__init__(64, 64, 224, 225)
        label = cocos.text.Label(
            'Hello World',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)
        sprite = cocos.sprite.Sprite("hello_world_action_sprite.jpg")
        sprite.position = 320, 240
        sprite.scale = 1
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))
        sprite.do(Repeat(Reverse(scale) + scale))

if __name__ == "__main__":
    cocos.director.director.init()
    hello_world = HelloWorld()
    hello_world.do(RotateBy(360,duration=10))
    main_scene = cocos.scene.Scene(hello_world)
    cocos.director.director.run(main_scene)
