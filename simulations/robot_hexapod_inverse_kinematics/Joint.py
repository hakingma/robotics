from __future__ import division
from visual import *
from utils import *
from Transformation import Transformation
from BodyPart import BodyPart

JOINT_RADIUS = .2
JOINT_COLOR = color.green

class Joint(BodyPart):
    def __init__(self, pos, rotationAxle):
        self.rotationAxle = rotationAxle
        self.joint = sphere(pos = pos, radius = JOINT_RADIUS, axis = self.rotationAxle, color = JOINT_COLOR)
        
    def RotateX(self, angle, orig):
        self.joint.rotate(angle = radians(angle), origin = orig, axis = vector(1,0,0))
        self.rotationAxle.rotate(radians(angle),vector(1,0,0))

    def RotateY(self, angle, orig):
        self.joint.rotate(angle = radians(angle), origin = orig, axis = vector(0,1,0))
        self.rotationAxle.rotate(radians(angle),vector(0,1,0))

    def RotateZ(self, angle, orig):
        self.joint.rotate(angle = radians(angle), origin = orig, axis = vector(0,0,1))
        self.rotationAxle.rotate(radians(angle), vector(0,0,1))

    def Rotate(self, angle, orig, ax):
        self.joint.rotate(angle = radians(angle), origin = orig, axis = ax)
        self.rotationAxle.rotate(radians(angle), ax)
        
    def GetAxle(self):
        return self.joint.axis

    def GetPosition(self):
        return self.joint.pos

    def AddNode(child):
        self.child = child

    def GetNode(name):
        if self.child.name == name:
            return name
        else:
            return self.child.GetNode(name)
        
    def GetPosition(self):
        return self.joint.pos

    def CopyPosition(self):
        return vector(self.joint.pos.x,self.joint.pos.y,self.joint.pos.z)
    
    def SetPosition(self, pos):
        self.joint.pos = pos
