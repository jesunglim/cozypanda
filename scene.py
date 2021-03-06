from math import pi, sin, cos
from turtle import forward

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from pandac.PandaModules import *
from panda3d.core import loadPrcFileData

from panda3d.core import Point3



loadPrcFileData("", "window-title Scene") # window name
loadPrcFileData("", "icon-filename icon/scene.ico") # window icon


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        base.disableMouse() 
        self.camera.setPos(-5,-30,10)
        self.camera.setHpr(-20,-20,-20)


        # Load the environment model.
        box = self.loader.loadModel("models/box")
        box.reparentTo(self.render)
        #box.scene.setScale(1, 1, 1)
        box.setPos(0, 0, 0)


        # 모델 불러오기
        z = self.loader.loadModel("z.egg")
        z.reparentTo(self.render)
        x = self.loader.loadModel("x.egg")
        x.reparentTo(self.render)
        y = self.loader.loadModel("y.egg")
        y.reparentTo(self.render)

        # mouse picker
        self.picker = CollisionTraverser()
        self.picker.showCollisions(render)
        self.pq = CollisionHandlerQueue() 

        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        # colliders
        box.setCollideMask(BitMask32.bit(1)) 
        z.setCollideMask(BitMask32.bit(1))
        x.setCollideMask(BitMask32.bit(1))
        y.setCollideMask(BitMask32.bit(1))

        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP,self.pq)

        self.accept("mouse1",self.mouseClick)


    def mouseClick(self):
        print('mouse click')
        # check if we have access to the mouse
        if base.mouseWatcherNode.hasMouse():

            # get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
            mpos_x = mpos.getX()

            # set the position of the ray based on the mouse position
            self.pickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())
            self.picker.traverse(render)
            # if we have hit something sort the hits so that the closest is first and highlight the node
            if self.pq.getNumEntries() > 0:
                self.pq.sortEntries()
                pickedObj = self.pq.getEntry(0).getIntoNodePath()
                print('click on ' + pickedObj.getName())



                
    

MyApp().run()


