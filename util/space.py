#! /usr/bin/python

# -----------------------------------------------------------------
# Do something about verifying types
# Do something about exceptions on degenerate cases
# -----------------------------------------------------------------

from sympy.matrices import Matrix
from sympy import sin, cos, sqrt
from sympy import pi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# exceptions

class WrongMathObject( Exception ):
    pass

class LineInvalidError( Exception ):
    pass

class PlaneInvalidError( Exception ):
    pass
    
class NoInterceptError( Exception ):
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# angle measure conversions

def to_rad( angle ):
    return angle * pi / 180
    
def to_deg( angle ):
    return angle * 180 / pi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# rotation matrices

def rot_x( angle ):
    return Matrix([[1,0,0],[0,cos(angle),-sin(angle)],[0,sin(angle),cos(angle)]])
    
def rot_y( zangle ):
    return Matrix([[cos(angle),0,sin(angle)],[0,1,0],[-sin(angle),0,cos(angle)]])

def rot_z( angle ):
    return Matrix([[cos(angle),-sin(angle),0],[sin(angle),cos(angle),0],[0,0,1]])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# shortcut for making 3D vectors

def vector_3d( x, y, z ):
    return Matrix( (x,y,z) ).transpose()
    
zero_3d = vector_3d( 0,0,0 )
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Line
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
class Line( object ):

    '''definition of a line in 3-space, p0 + tv for real t'''

    def __init__( self, p0 = zero_3d, v = zero_3d ):
        self.p0, self.v = ( p0, v )
        
    def is_valid( self ):
        return not ( v == zero_3d )
        
    # contains_point( self, point )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Plane
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Plane( object ):
    
    '''Definition of a plane in 3-space, stored in the form Ax+By+Cz+D=0'''
    
    def __init__( self, a = 0, b = 0, c = 0, d = 0 ):
        self.epsilon = 1e-50
        self.A, self.B, self.C, self.D = [ a,b,c,d ]
        self.normal = vector_3d( self.A, self.B, self.C )
        self.norm_length = sqrt( self.normal.dot( self.normal ) )

    def is_valid( self ):
        return not( self.normal == zero_3d )

    def distance_to_point( self, point ):
        if not self.is_valid():
            raise PlaneInvalidError()
        n = self.normal
        return ( n.dot( point ) + self.D ) / self.norm_length 
        
    def contains_point( self, point ):
        if not self.is_valid():
            raise PlaneInvalidError()
        return abs(self.distance_to_point( point )) < self.epsilon
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# geometric utilities
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
def two_point_line( p0, p1 ):
    if p0 == p1:
        raise LineInvalidError
    return Line( ( p0, p1-p0 ) )

def three_point_plane( p0, p1, p2 ):
    e1 = p1-p0
    e2 = p2-p1
    normal = e1.cross(e2)
    if normal == zero_3d:
        raise PlaneInvalidError
    d = p0.dot( normal )
    return Plane( normal[0], normal[1], normal[2], -d )    
 
def line_plane_intersect( line, plane ):
    n = plane.normal
    if n.dot( line.v ) == 0:
        raise NoInterceptError
    t = ( -plane.D - n.dot( line.p0 )) / n.dot( line.v )
    return line.p0 + t * line.v
        
