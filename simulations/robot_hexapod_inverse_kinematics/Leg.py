from __future__ import division
from visual import *
from utils import *
from Joint import Joint
from Transformation import Transformation
from BodyPart import BodyPart

UPPER_LEG_LENGTH = 5
LOWER_LEG_LENGTH = 5
COXA_LENGHT = 2
LEG_RADIUS = .1
JOINT_RADIUS = .2
JOINT_COLOR = color.green

class Leg(BodyPart):
    def __init__(self, parent, pos, isLeftLeg):
        self.parent = parent
        self.isLeftLeg = isLeftLeg
        self.legJoint = Joint(pos, vector(0,1,0))
        self.coxa = cylinder(pos=pos,length = COXA_LENGHT, radius = LEG_RADIUS, axis = vector(0,0,1))
        self.coxaJoint = Joint(self.coxa.pos + vector(0,0,COXA_LENGHT),vector(1,0,0))
        self.upperLeg = cylinder(pos=self.coxaJoint.GetPosition(),length = UPPER_LEG_LENGTH, radius = LEG_RADIUS, axis = vector(0,0,1))
        self.kneeJoint = Joint(self.coxaJoint.GetPosition() + vector(0,0,UPPER_LEG_LENGTH), vector(1,0,0))
        self.lowerLeg = cylinder(pos=self.kneeJoint.GetPosition(),length = LOWER_LEG_LENGTH, radius = LEG_RADIUS, axis = vector(0,0,1))
        self.endPos = Joint(self.kneeJoint.GetPosition() + vector(0,0,LOWER_LEG_LENGTH), vector(0,0,1))
        self.targetPos = vector(self.endPos.GetPosition().x,self.endPos.GetPosition().y,self.endPos.GetPosition().z)
        self.coxaAngle = 0.0
        self.upperLegAngle = 0.0
        self.lowerLegAngle = 0.0
        
    def RotateX(self, angle, orig):
        self.legJoint.RotateX(angle, orig)  
        self.coxa.rotate(angle = radians(angle), origin = orig, axis = vector(1,0,0))     
        self.coxaJoint.RotateX(angle, orig)     
        self.upperLeg.rotate(angle = radians(angle), origin = orig, axis = vector(1,0,0))     
        self.kneeJoint.RotateX(angle, orig)     
        self.lowerLeg.rotate(angle = radians(angle), origin = orig, axis = vector(1,0,0))
        self.endPos.RotateX(angle, orig)

    def RotateY(self, angle, orig):
        self.legJoint.RotateY(angle, orig)     
        self.coxa.rotate(angle = radians(angle), origin = orig, axis = vector(0,1,0))     
        self.coxaJoint.RotateY(angle, orig)     
        self.upperLeg.rotate(angle = radians(angle), origin = orig, axis = vector(0,1,0))     
        self.kneeJoint.RotateY(angle, orig)     
        self.lowerLeg.rotate(angle = radians(angle), origin = orig, axis = vector(0,1,0))     
        self.endPos.RotateY(angle, orig)

    def RotateZ(self, angle, orig):
        self.legJoint.RotateZ(angle, orig)  
        self.coxa.rotate(angle = radians(angle), origin = orig, axis = vector(0,0,1))     
        self.coxaJoint.RotateZ(angle, orig)     
        self.upperLeg.rotate(angle = radians(angle), origin = orig, axis = vector(0,0,1))     
        self.kneeJoint.RotateZ(angle, orig)     
        self.lowerLeg.rotate(angle = radians(angle), origin = orig, axis = vector(0,0,1))     
        self.endPos.RotateZ(angle, orig)

    def GetPosition(self):
        return self.legJoint.GetPosition()

    def CopyEndPosition(self):
        x = self.endPos.GetPosition().x
        y = self.endPos.GetPosition().y
        z = self.endPos.GetPosition().z
        return vector(x,y,z)

    def ResetCoxaAngle(self):
        self.coxa.rotate(angle = radians(-self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.coxaJoint.Rotate(-self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())
        self.upperLeg.rotate(angle = radians(-self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.kneeJoint.Rotate(-self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())
        self.lowerLeg.rotate(angle = radians(-self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.endPos.Rotate(-self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())

    def ResetUpperLegAngle(self):
        self.upperLeg.rotate(angle = radians(-self.upperLegAngle), origin = self.coxaJoint.GetPosition(), axis = self.coxaJoint.GetAxle())
        self.kneeJoint.Rotate(-self.upperLegAngle, self.coxaJoint.GetPosition(), self.coxaJoint.GetAxle())
        self.lowerLeg.rotate(angle = radians(-self.upperLegAngle), origin = self.coxaJoint.GetPosition(), axis = self.coxaJoint.GetAxle())
        self.endPos.Rotate(-self.upperLegAngle, self.coxaJoint.GetPosition(), self.coxaJoint.GetAxle())

    def ResetLowerLegAngle(self):    
        self.lowerLeg.rotate(angle = radians(-self.lowerLegAngle), origin = self.kneeJoint.GetPosition(), axis = self.kneeJoint.GetAxle())
        self.endPos.Rotate(-self.lowerLegAngle, self.kneeJoint.GetPosition(), self.kneeJoint.GetAxle())

    def SetCoxaAngle(self, angle):
        self.coxaAngle = angle
        self.coxa.rotate(angle = radians(self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.coxaJoint.Rotate(self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())
        self.upperLeg.rotate(angle = radians(self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.kneeJoint.Rotate(self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())
        self.lowerLeg.rotate(angle = radians(self.coxaAngle), origin = self.legJoint.GetPosition(), axis = self.legJoint.GetAxle())
        self.endPos.Rotate(self.coxaAngle, self.legJoint.GetPosition(), self.legJoint.GetAxle())

    def SetUpperLegAngle(self, angle):
        self.upperLegAngle = angle
        self.upperLeg.rotate(angle = radians(self.upperLegAngle), origin = self.coxaJoint.GetPosition(), axis = self.coxaJoint.GetAxle())
        self.kneeJoint.Rotate(self.upperLegAngle, self.coxaJoint.GetPosition(), self.coxaJoint.GetAxle())
        self.lowerLeg.rotate(angle = radians(self.upperLegAngle), origin = self.coxaJoint.GetPosition(), axis = self.coxaJoint.GetAxle())
        self.endPos.Rotate(self.upperLegAngle, self.coxaJoint.GetPosition(), self.coxaJoint.GetAxle())

    def SetLowerLegAngle(self, angle):
        self.lowerLegAngle = angle
        self.lowerLeg.rotate(angle = radians(self.lowerLegAngle), origin = self.kneeJoint.GetPosition(), axis = self.kneeJoint.GetAxle())
        self.endPos.Rotate(self.lowerLegAngle, self.kneeJoint.GetPosition(), self.kneeJoint.GetAxle())

    def setTargetPos(self, targetPos):
        self.targetPos = targetPos

    def moveToTargetPos(self):
        tX = self.targetPos.x - self.legJoint.GetPosition().x
        tY = self.targetPos.y# - self.legJoint.GetPosition().y
        tZ = self.targetPos.z - self.legJoint.GetPosition().z

        #print self.targetPos
        #print self.legJoint.GetPosition()

        bodyHeight = self.parent.GetBodyHeight()
        #print "bodyHeight:%r" %bodyHeight
        yAngle = math.atan2(tX,tZ)

        if(self.isLeftLeg == True):
            #print degrees(yAngle) + 180
            self.SetCoxaAngle(degrees(yAngle) + 180)
        else:
            #print degrees(yAngle)
            self.SetCoxaAngle(degrees(yAngle))
            
        stretch = math.sqrt( (tZ*tZ) + (tX*tX) ) - COXA_LENGHT
        #print stretch
        c1 = math.sqrt((tY * tY) + (stretch*stretch))
        #print c1
        alpha1 = math.asin(tY/c1)
        #print alpha1
        beta2 = radians(90) - alpha1
        #print beta2
        c3 = math.sqrt( (bodyHeight * bodyHeight) + (c1*c1) - (2 * bodyHeight * c1 * math.cos(beta2)) )
        #print c3
        gamma2 = math.acos( ( (c1*c1) -  (bodyHeight*bodyHeight) - (c3*c3) ) / (-2*bodyHeight*c3) )
        #print gamma2
        beta3 = math.acos( ((UPPER_LEG_LENGTH * UPPER_LEG_LENGTH) - (LOWER_LEG_LENGTH*LOWER_LEG_LENGTH) - (c3*c3) ) / (-2*LOWER_LEG_LENGTH*c3) )
        #print beta3
        #print (degrees(gamma2+beta3))-90
        self.SetUpperLegAngle(-((degrees(gamma2+beta3))-90) )
        #print -((degrees(gamma2+beta3))-90)
        gamma3 = math.acos( ((c3*c3) -  (LOWER_LEG_LENGTH*LOWER_LEG_LENGTH) - (UPPER_LEG_LENGTH*UPPER_LEG_LENGTH)) / (-2*LOWER_LEG_LENGTH*UPPER_LEG_LENGTH) )
        #print gamma3
        self.SetLowerLegAngle(180-degrees(gamma3))
        #print 180-degrees(gamma3)
'''
        yAngle = degrees(yAngle)
#        if False == self.isLeftLeg:
#            yAngle = 180 - yAngle
        self.rotateHipY(yAngle)
'''
    
