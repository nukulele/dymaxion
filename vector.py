#! /usr/bin/python

from sympy.matrices import Matrix
from sympy import sin, cos
from sympy import pi

def to_rad( angle ):
    return angle * pi / 180
    
def to_deg( angle ):
    return angle * 180 / pi

def rot_x( angle ):
    return Matrix([[1,0,0],[0,cos(angle),-sin(angle)],[0,sin(angle),cos(angle)]])
    
def rot_y( zangle ):
    return Matrix([[cos(angle),0,sin(angle)],[0,1,0],[-sin(angle),0,cos(angle)]])

def rot_z( angle ):
    return Matrix([[cos(angle),-sin(angle),0],[sin(angle),cos(angle),0],[0,0,1]])
    
# ---- some matrix manipulations
# a = Matrix( (1,2,3) )
# b = Matrix( (3,4,5) )
# a-b, a+b, a.dot(b), a.cross(b)

class Plane( object ):
    pass
    
    