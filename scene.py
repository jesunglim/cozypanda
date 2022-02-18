from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFileData

loadPrcFileData("", "window-title Scene") # window name
loadPrcFileData("", "icon-filename icon/scene.ico") # window icon

class MyApp(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        box = self.loader.loadModel("models/box")
        # Reparent the model to render.
        box.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        #box.scene.setScale(1, 1, 1)
        box.setPos(0, 10, 0)


        panda = self.loader.loadModel("models/panda")
        panda.setPos(-2, 10, 0)
        panda.setScale(0.2, 0.2, 0.2)
        panda.reparentTo(self.render)



MyApp().run()