#! /usr/bin/python

# -----------------------------------------------------------------
# Do something about exceptions and verifying types and degenerate
# cases
# -----------------------------------------------------------------

from sympy.matrices import Matrix
from sympy import sin, cos, sqrt
from sympy import pi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# exceptions

class WrongMathObject( Exception ):
    pass

class ObjectDegenerateCase( Exception ):
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

    def __init__( self, params_list  = (zero_3d, zero_3d ) ):
        self.p0, self.v = params_list
        
    # is_valid (i.e. is self.v zero )
    # contains_point( self, point )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Plane
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Plane( object ):
    
    '''Definition of a plane in 3-space, stored in the form Ax+By+Cz+D=0'''
    
    def __init__( self, params_list = (0,0,0,0) ):
        self.A, self.B, self.C, self.D = params_list
        
    def normal( self ):
        return vector_3d( self.A, self.B, self.C )

    def is_valid( self ):
        return not( (self.A, self.B, self.C) == (0,0,0) )

    def distance_to_point( self, point ):
        n = self.normal()
        return ( n.dot( point ) + self.D ) / sqrt( sum( [x*x for x in n] ) )
        
    def contains_point( self, point ):
        return self.distance_to_point( point ) == 0
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# geometric utilities
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
def two_point_line( p0, p1 ):
    return Line( ( p0, p1-p0 ) )

def three_point_plane( p0, p1, p2 ):
    e1 = p1-p0
    e2 = p2-p1
    normal = e1.cross(e2)
    d = p0.dot( normal )
    return Plane( (normal[0], normal[1], normal[2], -d) )    
 
def line_plane_intersect( line, plane ):
    n = plane.normal()
    t = ( plane.D - n.dot( line.p0 )) / n.dot( line.v )
    return line.p0 + t * line.v
        
# --------------------------------------------------

# tired of typing these!

a = vector_3d( 1,0,0 )
b = vector_3d( 0,1,0 )
c = vector_3d( 0,0,1 )
P = three_point_plane( a,b,c )