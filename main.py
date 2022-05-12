
from window import Window
from setter import Setter

width = 700 # static
height = 700 # static

sr = Setter(6, 5, 30)

wd = Window(width, height, sr)
wd.set(sr.list)
wd.show()