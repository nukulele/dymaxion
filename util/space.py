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
    
    '''Definition of a plane in 3-space, stored in the form Ax+By+Cz+D=0'''
    
    def set_params( self, params_list )
        self.A, self.B, self.C, self.D = params_list
        
def plane_from_points( p0, p1, p2 ):
    # check for types, raise if bad?
    
    e1 = p1-p0
    e2 = p2-p1
    normal = e1.cross(e2)
    # check for degenerate case!
    
    # solve for D
    ret_plane = Plane()
    ret_plane.set_params( normal[0], normal[1], normal[2], 4 )
    return ret_plane