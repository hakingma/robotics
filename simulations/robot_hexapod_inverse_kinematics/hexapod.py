from __future__ import division
from visual import *

from Body import Body
from RobotController import RobotController

body = Body(vector(0,5,-10))
controller = RobotController(body)
#bodyCentreVisual = cylinder(pos = body.bodyCentre, axis =  vector(0,2,0), radius=.1)
angle = 0
angleUp = True
coxaAngle = 0
coxaAngleUp = True;

floor = box(pos=body.bodyCentreVec - (0,5,0),length=40,width=40,height=.1,color = color.blue)
floorAxleX = vector(1,0,0)
floorAxleY = vector(0,1,0)
floorAxleZ = vector(0,0,1)

controller.SetFloor(floor)

while True:
##    if coxaAngleUp == True:
##        coxaAngle = coxaAngle + 1
##        if coxaAngle == 45:
##            coxaAngleUp = False
##    else:
##        coxaAngle = coxaAngle - 1
##        if coxaAngle == 0:
##            coxaAngleUp = True
##
##    if angleUp == True:
##        angle = angle + 1
##        if angle == 45:
##            angleUp = False
##    else:
##        angle = angle - 1
##        if angle == 0:
##            angleUp = True            

    #floor.rotate(angle = radians(angle), origin = body.bodyCentreVec, axis = vector(1,0,0))
    #floor.rotate(angle = radians(angle), origin = body.bodyCentreVec, axis = vector(0,1,0))
    #floor.rotate(angle = radians(angle), origin = body.bodyCentreVec, axis = vector(0,0,1))

    #body.RotateX(angle,body.bodyCentreVec)
    #body.RotateY(angle,body.bodyCentreVec)
    #body.RotateZ(angle,body.bodyCentreVec)
            
##    body.SetURLCoxaAngle(coxaAngle)
##    body.SetURLUpperLegAngle(-coxaAngle)
##    body.SetURLLowerLegAngle(coxaAngle)
##
##    body.SetULLCoxaAngle(-coxaAngle)
##    body.SetULLUpperLegAngle(-coxaAngle)
##    body.SetULLLowerLegAngle(coxaAngle)

    controller.control()

#    angle = (angle + 1) % 20


    #body.ApplyTransformations()

    rate(100)

    #floor.rotate(angle = radians(-angle), origin = body.bodyCentreVec, axis = vector(0,0,1))
    #floor.rotate(angle = radians(-angle), origin = body.bodyCentreVec, axis = vector(0,1,0))  
    #floor.rotate(angle = radians(-angle), origin = body.bodyCentreVec, axis = vector(1,0,0))  

