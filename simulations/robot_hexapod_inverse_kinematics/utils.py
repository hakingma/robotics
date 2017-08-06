from __future__ import division
from visual import *

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

#example usage below:
##v = 'ten'
##for case in switch(v):
##    if case('one'):
##        print 1
##        break
##    if case('two'):
##        print 2
##        break
##    if case('ten'):
##        print 10
##        break
##    if case('eleven'):
##        print 11
##        break
##    if case(): # default, could also just omit condition or 'if True'
##        print "something else!"
##        # No need to break here, it'll stop anyway   

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def rotateAxlePos(rotationPos,rotationAxle, axlePosToRotate, angle):
    #translate to rotation origin
    axlePosToRotate = axlePosToRotate - rotationPos
    #rotate
    axlePosToRotate = rotate(axlePosToRotate, radians(angle),rotationAxle)
    #translate back
    axlePosToRotate = axlePosToRotate + rotationPos
    return axlePosToRotate
