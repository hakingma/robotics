from __future__ import division
from visual import *
from Leg import Leg
from Joint import Joint
from Transformation import Transformation
from BodyPart import BodyPart

BODY_LENGTH = 16
BODY_WIDTH = 3
BODY_RADIUS = .1
JOINT_RADIUS = .2
JOINT_COLOR = color.green
LEG_SPACING = 6


class Body(BodyPart):
    def __init__(self, bodyCentre):
        self.bodyCentreVec = bodyCentre
        self.bodyHeight = self.bodyCentreVec.y
        self.worldTransform = Transformation()
        self.angleX = 0.0;
        self.angleXOrig = vector(0,0,0);
        self.angleY = 0.0;
        self.angleYOrig = vector(0,0,0);
        self.angleZ = 0.0;
        self.angleZOrig = vector(0,0,0);

        self.URLCoxaAngle = 0.0
        self.URLUpperLegAngle = 0.0
        self.URLLowerLegAngle = 0.0

        self.ULLCoxaAngle = 0.0
        self.ULLUpperLegAngle = 0.0
        self.ULLLowerLegAngle = 0.0

        self.MRLCoxaAngle = 0.0
        self.MRLUpperLegAngle = 0.0
        self.MRLLowerLegAngle = 0.0

        #self.bodyCentreVis = sphere(pos = self.bodyCentreVec, radius = JOINT_RADIUS, color = JOINT_COLOR)
        ##draw body
        self.bodyLE = cylinder(pos = self.bodyCentreVec - vector(BODY_LENGTH/2,0,BODY_WIDTH/2), length=BODY_LENGTH, radius = BODY_RADIUS, axis = vector(1,0,0), color = color.white)
        self.bodyRI = cylinder(pos = self.bodyCentreVec - vector(BODY_LENGTH/2,0,-BODY_WIDTH/2), length=BODY_LENGTH, radius = BODY_RADIUS, axis = vector(1,0,0), color = color.white)
        self.bodyUP = cylinder(pos = self.bodyCentreVec - vector(BODY_LENGTH/2,0,BODY_WIDTH/2), length=BODY_WIDTH, radius = BODY_RADIUS, axis = vector(0,0,1), color = color.white)
        self.bodyLO = cylinder(pos = self.bodyCentreVec - vector(-(BODY_LENGTH/2),0,BODY_WIDTH/2), length=BODY_WIDTH, radius = BODY_RADIUS, axis = vector(0,0,1), color = color.white)

        self.worldTransform.AddElement(self.bodyLE)
        self.worldTransform.AddElement(self.bodyRI)
        self.worldTransform.AddElement(self.bodyUP)
        self.worldTransform.AddElement(self.bodyLO)

        self.upperRightLeg = Leg(self, self.bodyCentreVec + vector((BODY_LENGTH/2) - 2,0,BODY_WIDTH/2),False)
        self.worldTransform.AddElement(self.upperRightLeg)

        self.middleRightLeg = Leg(self, self.upperRightLeg.GetPosition() - vector(LEG_SPACING,0,0),False)
        self.worldTransform.AddElement(self.middleRightLeg)

        self.lowerRightLeg = Leg(self, self.middleRightLeg.GetPosition() - vector(LEG_SPACING,0,0),False)
        self.worldTransform.AddElement(self.lowerRightLeg)

        self.upperLeftLeg = Leg(self, self.bodyCentreVec + vector((BODY_LENGTH/2) - 2,0,-(BODY_WIDTH/2)),True)
        self.upperLeftLeg.RotateY(180, self.upperLeftLeg.GetPosition())
        self.worldTransform.AddElement(self.upperLeftLeg)

        self.middleLeftLeg = Leg(self, self.upperLeftLeg.GetPosition() - vector(LEG_SPACING,0,0),True)
        self.middleLeftLeg.RotateY(180, self.middleLeftLeg.GetPosition())
        self.worldTransform.AddElement(self.middleLeftLeg)

        self.lowerLeftLeg = Leg(self, self.middleLeftLeg.GetPosition() - vector(LEG_SPACING,0,0),True)
        self.lowerLeftLeg.RotateY(180, self.lowerLeftLeg.GetPosition())
        self.worldTransform.AddElement(self.lowerLeftLeg)

    def SetBodyHeight(self, height):
        self.bodyHeight = height

    def GetBodyHeight(self):
        return self.bodyHeight
    
    def RotateX(self,angle, orig):
        self.angleX = angle
        self.angleXOrig = orig

    def RotateY(self,angle, orig):
        self.angleY = angle
        self.angleYOrig = orig

    def RotateZ(self,angle, orig):
        self.angleZ = angle
        self.angleZOrig = orig


    def SetURLCoxaAngle(self, angle):
        self.URLCoxaAngle  = angle

    def SetURLUpperLegAngle(self, angle):
        self.URLUpperLegAngle = angle

    def SetURLLowerLegAngle(self, angle):
        self.URLLowerLegAngle = angle


    def SetULLCoxaAngle(self, angle):
        self.ULLCoxaAngle  = angle

    def SetULLUpperLegAngle(self, angle):
        self.ULLUpperLegAngle = angle

    def SetULLLowerLegAngle(self, angle):
        self.ULLLowerLegAngle = angle


    def SetMRLCoxaAngle(self, angle):
        self.MRLCoxaAngle  = angle

    def SetMRLUpperLegAngle(self, angle):
        self.MRLUpperLegAngle = angle

    def SetMRLLowerLegAngle(self, angle):
        self.MRLLowerLegAngle = angle        
        

    def ApplyTransformations(self):
        self.lowerLeftLeg.ResetLowerLegAngle()
        self.lowerLeftLeg.ResetUpperLegAngle()
        self.lowerLeftLeg.ResetCoxaAngle()
        
        self.lowerRightLeg.ResetLowerLegAngle()
        self.lowerRightLeg.ResetUpperLegAngle()
        self.lowerRightLeg.ResetCoxaAngle()

        self.middleLeftLeg.ResetLowerLegAngle()
        self.middleLeftLeg.ResetUpperLegAngle()
        self.middleLeftLeg.ResetCoxaAngle()
        
        self.middleRightLeg.ResetLowerLegAngle()
        self.middleRightLeg.ResetUpperLegAngle()
        self.middleRightLeg.ResetCoxaAngle()

        self.upperLeftLeg.ResetLowerLegAngle()
        self.upperLeftLeg.ResetUpperLegAngle()
        self.upperLeftLeg.ResetCoxaAngle()

        self.upperRightLeg.ResetLowerLegAngle()
        self.upperRightLeg.ResetUpperLegAngle()
        self.upperRightLeg.ResetCoxaAngle()

        self.worldTransform.ResetTrans()
        
        self.worldTransform.RotateX(self.angleX, self.angleXOrig)
        self.worldTransform.RotateY(self.angleY, self.angleYOrig)
        self.worldTransform.RotateZ(self.angleZ, self.angleZOrig)

        self.upperRightLeg.moveToTargetPos()
        self.middleRightLeg.moveToTargetPos()
        self.lowerRightLeg.moveToTargetPos()

        self.upperLeftLeg.moveToTargetPos()
        self.middleLeftLeg.moveToTargetPos()
        self.lowerLeftLeg.moveToTargetPos()

##        self.upperRightLeg.SetCoxaAngle(self.URLCoxaAngle)
##        self.upperRightLeg.SetUpperLegAngle(self.URLUpperLegAngle)
##        self.upperRightLeg.SetLowerLegAngle(self.URLLowerLegAngle)
##        
##        self.upperLeftLeg.SetCoxaAngle(self.ULLCoxaAngle)
##        self.upperLeftLeg.SetUpperLegAngle(self.ULLUpperLegAngle)
##        self.upperLeftLeg.SetLowerLegAngle(self.ULLLowerLegAngle)
##
##        self.middleRightLeg.SetCoxaAngle(self.MRLCoxaAngle)
##        self.middleRightLeg.SetUpperLegAngle(self.MRLUpperLegAngle)
##        self.middleRightLeg.SetLowerLegAngle(self.MRLLowerLegAngle)
    
