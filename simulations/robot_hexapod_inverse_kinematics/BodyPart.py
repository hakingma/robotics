from __future__ import division
from visual import *

class BodyPart:
    def RotateX(self, angle, orig):
        raise NotImplementedError( "Should have implemented this" )

    def RotateY(self, angle, orig):
        raise NotImplementedError( "Should have implemented this" )

    def RotateZ(self, angle, orig):
        raise NotImplementedError( "Should have implemented this" )

    def GetPosition(self):
        raise NotImplementedError( "Should have implemented this" )
