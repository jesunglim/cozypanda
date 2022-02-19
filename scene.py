from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFileData




loadPrcFileData("", "window-title Scene") # window name
loadPrcFileData("", "icon-filename icon/scene.ico") # window icon


def create_axes_cross(name, size, has_labels):
    def create_axis_line(label, color, draw_to):
        coords.setColor(color)
        coords.moveTo(0, 0, 0)
        coords.drawTo(draw_to)

        # Put the axis' name in the tip
        if label != "":
            text = TextNode(label)
            text.setText(label)
            text.setTextColor(color)
            axis_np = coords_np.attachNewNode(text)
        else:
            axis_np = coords_np.attachNewNode("")
        axis_np.setPos(draw_to)
        return axis_np

    coords_np = NodePath(name)
    coords = LineSegs()
    coords.setThickness(2)
    axis_x_np = create_axis_line("X" if has_labels else "", (1, 0, 0, 1), (size, 0, 0))   # Red
    axis_y_np = create_axis_line("Y" if has_labels else "", (0, 1, 0, 1), (0, size, 0)) # Green
    axis_z_np = create_axis_line("Z" if has_labels else "", (0, 0, 1, 1), (0, 0, size))  # Blue
    node = coords.create(True)
    coords_np.attachNewNode(node)
    return coords_np, axis_x_np, axis_y_np, axis_z_np


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        base.disableMouse()
        base.oobe()   # debugging view



        # Load the environment model.
        box = self.loader.loadModel("models/box")
        box.reparentTo(self.render)
        #box.scene.setScale(1, 1, 1)
        box.setPos(0, 0, 0)

        axis = self.loader.loadModel("axis.egg")
        axis.reparentTo(self.render)
        box.setPos(0, 0, 0)

        print("posotion = " + str(box.get_pos() ) )
        

MyApp().run()


