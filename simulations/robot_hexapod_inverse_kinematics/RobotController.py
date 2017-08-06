from __future__ import division
from visual import *

from Body import Body
from Leg import Leg

class RobotController:
    def __init__(self, body):
        self.body = body
        self.body.SetBodyHeight(5)

        self.urlEndPos = self.body.upperRightLeg.CopyEndPosition()
        self.mrlEndPos = self.body.middleRightLeg.CopyEndPosition()
        self.lrlEndPos = self.body.lowerRightLeg.CopyEndPosition()

        self.ullEndPos = self.body.upperLeftLeg.CopyEndPosition()
        self.mllEndPos = self.body.middleLeftLeg.CopyEndPosition()
        self.lllEndPos = self.body.lowerLeftLeg.CopyEndPosition()

        self.animAngle = 0.0
        self.floorAnimAngle = 0.0
        self.bodyAngles = vector(0,0,15)

        self.rollXAngleUp = False
        self.rollZAngleUp = False
        

    def SetFloor(self,floor):
        self.floor = floor
        self.floorAngleX = 0.0
        self.floorAngleZ = self.bodyAngles.z
        self.floor.rotate(angle = radians(self.floorAngleZ), origin = self.body.bodyCentreVec, axis = vector(0,0,1))
    
    def control(self):
        #self.body.RotateX(self.bodyAngles.x,self.body.bodyCentreVec)
        self.floor.rotate(angle = radians(-self.floorAngleZ), origin = self.body.bodyCentreVec, axis = vector(0,0,1))
        self.floor.rotate(angle = radians(-self.floorAngleX), origin = self.body.bodyCentreVec, axis = vector(1,0,0))
        self.floor.pos = self.floor.pos + vector(0,self.body.GetBodyHeight(),0)

        self.floorAngleX = -self.bodyAngles.x
        self.floorAngleZ = self.bodyAngles.z
        self.body.SetBodyHeight(4 + (math.sin(radians(self.animAngle))*2))

        self.floor.pos = self.floor.pos - vector(0,self.body.GetBodyHeight(),0)
        self.floor.rotate(angle = radians(self.floorAngleX), origin = self.body.bodyCentreVec, axis = vector(1,0,0))
        self.floor.rotate(angle = radians(self.floorAngleZ), origin = self.body.bodyCentreVec, axis = vector(0,0,1))
        
        self.TripodGateSequence()
        self.body.ApplyTransformations()

        self.animAngle = (self.animAngle + 2) % 360
        self.floorAnimAngle = (self.floorAnimAngle + 1) % 360
        self.bodyAngles.x  = math.sin(radians(self.floorAnimAngle))*10
        self.bodyAngles.z  = math.cos(radians(self.floorAnimAngle))*10
        
        
##        if self.rollXAngleUp == True:
##            if self.bodyAngles.x < 15:
##                self.bodyAngles.x = self.bodyAngles.x + .2 
##            else:
##                self.rollXAngleUp = False
##        else:
##            if self.bodyAngles.x > -15:
##                self.bodyAngles.x = self.bodyAngles.x - .2 
##            else:
##                self.rollXAngleUp = True            
##
##        if self.rollZAngleUp == True:
##            if self.bodyAngles.z < 15:
##                self.bodyAngles.z = self.bodyAngles.z + .2 
##            else:
##                self.rollZAngleUp = False
##        else:
##            if self.bodyAngles.z > -15:
##                self.bodyAngles.z = self.bodyAngles.z - .2 
##            else:
##                self.rollZAngleUp = True            

    def RotateVectorX(self, vec, angle, origin):
        vectorTrans = vec - origin
        vectorRot = vector(vectorTrans)
        vectorRot.z = vectorTrans.z*math.cos(radians(angle)) - vectorTrans.y*math.sin(radians(angle))
        vectorRot.y = vectorTrans.y*math.cos(radians(angle)) + vectorTrans.z*math.sin(radians(angle))
        vectorRot = vectorRot + origin
        return vectorRot

    def RotateVector(self, vec, angles, origin):
        #translate to origin
        vectorTrans = vec - origin
        vectorTmp1 = vector(0,0,0)
        vectorTmp2 = vector(0,0,0)
        #first rotate over the x axis
        vectorTmp1.z = vectorTrans.z*math.cos(radians(angles.x)) - vectorTrans.y*math.sin(radians(angles.x))
        vectorTmp1.y = vectorTrans.y*math.cos(radians(angles.x)) + vectorTrans.z*math.sin(radians(angles.x))
        vectorTmp1.x = vectorTrans.x#x is unchanged
        #then rotate over z axis
        vectorTmp2.x = vectorTmp1.x*math.cos(radians(angles.z)) - vectorTmp1.y*math.sin(radians(angles.z))
        vectorTmp2.y = vectorTmp1.y*math.cos(radians(angles.z)) + vectorTmp1.x*math.sin(radians(angles.z))
        vectorTmp2.z = vectorTmp1.z#z is unchanged
        #TODO: rotate over y axis
        
        #translation to original position
        vectorRot = vectorTmp2 + origin
        return vectorRot
    
    def CalcRotationOffsets(self, targetPos, origin, angles):
        if angles.x != 0:
            targetPosRot = self.RotateVectorX(targetPos,angles.x,origin)
            rotXOffset = vector(targetPosRot.x - targetPos.x, targetPosRot.y - targetPos.y, targetPosRot.z - targetPos.z)
            return rotXOffset
        else:
            return vector(0,0,0)

    def CalcRotationOffsetsNew(self, targetPos, origin, angles):
        targetPosRot = self.RotateVector(targetPos,angles,origin)
        rotOffsets = vector(targetPosRot.x - targetPos.x, targetPosRot.y - targetPos.y, targetPosRot.z - targetPos.z)
        return rotOffsets

    def TripodGateSequence(self):
        self.animAngle1 = self.animAngle
        self.animAngle2 = (self.animAngle + 180) % 360
        tripodOffset = vector(0,0,0)
        
        self.xOffset1 = math.sin(radians(self.animAngle1)) * 2
        if (self.animAngle1 >= 90 and self.animAngle1 <= 270):
            self.yOffset1 = 0.0
        else:
            self.yOffset1 = math.cos(radians(self.animAngle1)) * 2

        self.xOffset2 = math.sin(radians(self.animAngle2)) * 2
        if (self.animAngle2 >= 90 and self.animAngle2 <= 270):
            self.yOffset2 = 0.0
        else:
            self.yOffset2 = math.cos(radians(self.animAngle2)) * 2

        #self.xOffset1 = 0.0
        #self.yOffset1 = 0.0
        #self.xOffset2 = 0.0
        #self.yOffset2 = 0.0
        

        urlTargetPos = vector(self.urlEndPos.x, self.urlEndPos.y-5, self.urlEndPos.z-5) + vector(self.xOffset1,self.yOffset1,0)
        urlTargetPos = urlTargetPos + self.CalcRotationOffsetsNew(urlTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.upperRightLeg.setTargetPos(urlTargetPos)

        mrlTargetPos = vector(self.mrlEndPos.x, self.mrlEndPos.y-5, self.mrlEndPos.z-5) + vector(self.xOffset2,self.yOffset2,0)
        mrlTargetPos = mrlTargetPos + self.CalcRotationOffsetsNew(mrlTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.middleRightLeg.setTargetPos(mrlTargetPos)

        lrlTargetPos = vector(self.lrlEndPos.x, self.lrlEndPos.y-5, self.lrlEndPos.z-5) + vector(self.xOffset1,self.yOffset1,0)
        lrlTargetPos = lrlTargetPos + self.CalcRotationOffsetsNew(lrlTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.lowerRightLeg.setTargetPos(lrlTargetPos)
        
        
        ullTargetPos = vector(self.ullEndPos.x, self.ullEndPos.y-5, self.ullEndPos.z+5) + vector(self.xOffset2,self.yOffset2, 0)
        ullTargetPos = ullTargetPos + self.CalcRotationOffsetsNew(ullTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.upperLeftLeg.setTargetPos(ullTargetPos)

        mllTargetPos = vector(self.mllEndPos.x, self.mllEndPos.y-5, self.mllEndPos.z+5) + vector(self.xOffset1,self.yOffset1, 0)
        mllTargetPos = mllTargetPos + self.CalcRotationOffsetsNew(mllTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.middleLeftLeg.setTargetPos(mllTargetPos)

        lllTargetPos = vector(self.lllEndPos.x, self.lllEndPos.y-5, self.lllEndPos.z+5) + vector(self.xOffset2,self.yOffset2, 0)
        lllTargetPos = lllTargetPos + self.CalcRotationOffsetsNew(lllTargetPos,self.body.bodyCentreVec,self.bodyAngles)
        self.body.lowerLeftLeg.setTargetPos(lllTargetPos)

    #def ApplyBodyRotationOffsets(self, targetVector):
        
