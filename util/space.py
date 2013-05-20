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

def vector_3d( x, y, z ):
    return Matrix( (x,y,z) ).transpose()
    
# ---- some matrix manipulations
# a = Matrix( (1,2,3) )
# b = Matrix( (3,4,5) )
# a-b, a+b, a.dot(b), a.cross(b)

class Line( object ):

    def set_params( self, params_list ):
        
        '''definition of a line in 3-space, p0 + tv for real t'''
        self.p0, self.v = params_list

def two_point_line( p0, p1 ):
    ret_line = Line()
    ret_line.set_params( (p0, p1-p0 ) )
    return ret_line

class Plane( object ):
    
    '''Definition of a plane in 3-space, stored in the form Ax+By+Cz+D=0'''
    
    def set_params( self, params_list ):
        self.A, self.B, self.C, self.D = params_list
        
    def normal( self ):
        return vector_3d( self.A, self.B, self.C )

def three_point_plane( p0, p1, p2 ):
    # check for types, raise if bad?
    
    e1 = p1-p0
    e2 = p2-p1
    normal = e1.cross(e2)
    # check for degenerate case! normal == 0?
    
    d = p0.dot( normal )
    
    ret_plane = Plane()
    ret_plane.set_params( (normal[0], normal[1], normal[2], d) )
    return ret_plane
    
def line_plane_intersect( line, plane ):

    if type( line ) != Line:
        raise ValueError
    if type( plane ) != Plane:
        raise ValueError
        
    n = plane.normal()
    t = ( plane.D - n.dot( line.p0 )) / n.dot( line.v )
    return line.p0 + t * line.v
        
        
