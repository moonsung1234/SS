
from window import Window
from setter import Setter

width = 1000 # static
height = 700 # static

sr = Setter(6, 5, 30)

wd = Window(width, height, sr)
wd.init()
wd.show()