from __future__ import division
from visual import *
from BodyPart import BodyPart

class Transformation:
    def __init__(self):
        self.rotX = 0.0
        self.rotXOrig = vector(0,0,0)
        self.rotY = 0.0
        self.rotYOrig = vector(0,0,0)
        self.rotZ = 0.0
        self.rotZOrig = vector(0,0,0)
        self.transX = 0.0
        self.transY = 0.0
        self.transZ = 0.0
        self.elemList = []

    def AddElement(self, elem):
        self.elemList.append(elem)

    def ResetTrans(self):
        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateZ(-self.rotZ, self.rotZOrig)
            else:
                elem.rotate(angle = radians(-self.rotZ), origin = self.rotZOrig, axis = vector(0,0,1))
        
        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateY(-self.rotY, self.rotYOrig)
            else:
                elem.rotate(angle = -radians(self.rotY), origin = self.rotYOrig, axis = vector(0,1,0))

        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateX(-self.rotX, self.rotXOrig)
            else:
                elem.rotate(angle = radians(-self.rotX), origin = self.rotXOrig, axis = vector(1,0,0))

    def RotateX(self, angle, orig):
        self.rotX = angle
        self.rotXOrig = orig

        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateX(self.rotX, self.rotXOrig)
            else:
                elem.rotate(angle = radians(self.rotX), origin = self.rotXOrig, axis = vector(1,0,0))

    def RotateY(self, angle, orig):
        self.rotY = angle
        self.rotYOrig = orig

        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateY(self.rotY, self.rotYOrig)
            else:
                elem.rotate(angle = radians(self.rotY), origin = self.rotYOrig, axis = vector(0,1,0))

    def RotateZ(self, angle, orig):
        self.rotZ = angle
        self.rotZOrig = orig

        for elem in self.elemList:
            if isinstance(elem, BodyPart):
                elem.RotateZ(self.rotZ, self.rotZOrig)
            else:
                elem.rotate(angle = radians(self.rotZ), origin = self.rotZOrig, axis = vector(0,0,1))
