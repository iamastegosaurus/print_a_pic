from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty
from kivy.config import Config
from random import randint, random

class Puzzle(Camera):

    w = 5
    h = 4
    bs = 150

    blocksize = NumericProperty(bs)
    width = NumericProperty(w)
    height = NumericProperty(h)

    emptySquare = ( (w-1)*bs, (h-1)*bs )

    def on_texture_size(self, instance, value):
        self.build()

    def on_blocksize(self, instance, value):
        self.build()

    def build(self):
        texture = self.texture
        bs = self.blocksize
        for x in range(self.width): 
            for y in range(self.height):
                bx = x * bs
                by = y * bs
                subtexture = texture.get_region(bx, by, bs, bs)
                node = Scatter(pos=(bx, by), size=(bs, bs))
                with node.canvas:
                    Color(1, 1, 1)
                    Rectangle(size=node.size, texture=subtexture)
                if x+1 == self.width and y == 0:
                    pass
                else:
                    self.add_widget(node)
        self.shuffle()


    def shuffle(self):
        count = (self.width * self.height) - 1
        indices = list(range(count))
        childindex = 0
        while indices:
            index = indices.pop(randint(0, len(indices) - 1))
            x = self.blocksize * (index % self.width)
            y = self.blocksize * int(index / self.width)
            child = self.children[childindex]
            a = Animation(d=random() / 4.) + Animation(pos=(x, y), t='out_quad', d=.4)
            a.start(child)
            childindex += 1
    

    def on_touch_down(self, touch):
        x = int(touch.pos[0] / self.blocksize) * self.blocksize
        y = int(touch.pos[1] / self.blocksize) * self.blocksize

        for c in range( (self.width * self.height) - 1 ):
            child = self.children[c]
            if child.pos[0] == x and child.pos[1] == y:
                a = Animation(d=random() / 4.) + Animation(pos=self.emptySquare, t='out_quad', d=.4)
                a.start(child)
                self.emptySquare = (x, y)
                break

        if touch.is_double_tap:
            self.shuffle()
            return True

class PuzzleApp(App):
    def build(self):
        Config.set('graphics', 'width', '750')
        Config.write()
        root = Widget()
        puzzle = Puzzle(resolution=(900, 900), play=True)
        root.add_widget(puzzle)

        return root

PuzzleApp().run()