import cocos
import pyglet
from cocos.director import director


class KeyDisplay(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(KeyDisplay,self).__init__()

        self.text = cocos.text.Label("",x=100,y=280)
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def on_key_press(self,key,modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_relase(self,key,modifiers):
        self.keys_pressed.remove(key)
        self.update_text()
    
    def update_text(self):
        key_name = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        text = "keys: " + ','.join(key_name)
        self.text.element.text = text

class MouseDisplay(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MouseDisplay,self).__init__()

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label(
            "no mouse event yet",
            font_size = 18,
            x = self.posx,
            y = self.posy
            )
        self.add(self.text)
    
    def update_text(self,x,y):
        text = "Mouse @ %d,%d" % (x,y)
        self.text.element.x = self.posx
        self.text.element.y = self.posy
        self.text.element.text = text

    def on_mouse_motion(self,x,y,dx,dy):
        self.update_text(x,y)
    
    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        self.update_text(x,y)

    def on_mouse_press(self,x,y,buttons,modifiers):
        self.posx,self.posy = director.get_virtual_coordinates(x,y)
        self.update_text(x,y)

if __name__ == "__main__":
    director.init(resizable=True)
    director.run(cocos.scene.Scene(KeyDisplay(),MouseDisplay()))