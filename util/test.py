import sympy as s
import unittest

from polygon import Polygon
from util.space import *


class TestAngleConversions( unittest.TestCase ):

    def test_to_rad_1( self ):
        self.assertEqual( to_rad( 90 ), s.pi/2 )

    def test_to_rad_2( self ):
        self.assertEqual( to_rad( -90 ), -s.pi/2 )
        
    def test_to_rad_3( self ):
        self.assertEqual( to_rad( 360 ), 2*s.pi )
 
    def test_to_deg_1( self ):
        self.assertEqual( to_deg( s.pi/2 ), 90 )

    def test_to_deg_2( self ):
        self.assertEqual( to_deg( -s.pi/2 ), -90 )
        
    def test_to_deg_3( self ):
        self.assertEqual( to_deg( 2*s.pi ), 360 )
        
class TestRotationMatricies(unittest.TestCase):

    def test_rot_x( self ):
        result = rot_x( 1 )
        cos1 = s.cos(1)
        sin1 = s.sin(1)
        self.assertEqual( \
            result, s.Matrix( ((1,0,0),(0,cos1,-sin1),(0,sin1,cos1)) ) \
            )
        
    def test_rot_y( self ):
        result = rot_y( 1 )
        cos1 = s.cos(1)
        sin1 = s.sin(1)
        self.assertEqual( \
            result, s.Matrix( ((cos1,0,sin1),(0,1,0),(-sin1,0,cos1)) ) \
            )
        
    def test_rot_z( self ):
        result = rot_z( 1 )
        cos1 = s.cos(1)
        sin1 = s.sin(1)
        self.assertEqual( \
            result, s.Matrix( ((cos1,-sin1,0),(sin1,cos1,0),(0,0,1)) ) \
            )
        
    def test_compound( self ):
        a = rot_z(1).multiply( rot_y(1) ).multiply( rot_x(1) )
        b = rot_x(-1).multiply( rot_y(-1) ).multiply( rot_z(-1) )
        self.assertTrue( a.multiply(b), rot_x(0) )

class TestLine( unittest.TestCase ):

    def test_good_line( self ):
        test_line = Line( vector_3d( 0,0,0 ), vector_3d( 1,1,1 ) )
        self.assertTrue( test_line.is_valid() )
        
    def test_bad_line( self ):
        test_line = Line( vector_3d( 1,1,1 ), vector_3d( 0,0,0 ) )
        self.assertFalse( test_line.is_valid() )
        
    def test_two_point_line_good( self ):
        a = vector_3d( 1,2,3 )
        b = vector_3d( 2,3,4 )
        test_line = two_point_line( a, b )
        self.assertTrue( test_line.is_valid() )

    def test_two_point_line_bad( self ):
        a = vector_3d( 1,2,3 )
        b = vector_3d( 1,2,3 )
        try:
            test_line = two_point_line( a, b )
            self.assertFalse( True )
        except LineInvalidError:
            self.assertTrue( True )
                
class TestPlane( unittest.TestCase ):

    def test_three_point_plane_good( self ):
        test_plane = three_point_plane( v_x, v_y, v_z )
        self.assertEqual( test_plane.A, 1 )
        self.assertEqual( test_plane.B, 1 )
        self.assertEqual( test_plane.C, 1 )
        self.assertEqual( test_plane.D, -1 )
        self.assertEqual( test_plane.normal, vector_3d( 1,1,1 ) )
        self.assertEqual( test_plane.norm_length, s.sqrt(3) )
        self.assertTrue( test_plane.is_valid() )
        self.assertTrue( test_plane.contains_point( \
            vector_3d( s.Rational(1,2),s.Rational(1,2),0 ) ))
        self.assertTrue( test_plane.contains_point( \
            vector_3d( 0, s.Rational(1,2),s.Rational(1,2) ) ))
        self.assertFalse( test_plane.contains_point( zero_3d ) )
        self.assertTrue( test_plane.contains_point( \
            vector_3d( s.Rational(1,3), s.Rational(1,3),s.Rational(1,3) ) ))
        self.assertEqual( test_plane.distance_to_point( zero_3d ), \
            -s.sqrt(3)/3)
        self.assertEqual( test_plane.distance_to_point( vector_3d( 1,1,1 ) ), \
            2*s.sqrt(3)/3)

    def test_three_point_plane_bad( self ):
        try:
            test_plane = three_point_plane( \
                vector_3d( 1,1,1 ), vector_3d( 2,2,2 ), vector_3d( 3,3,3 ) )
            self.assertFalse( True )
        except PlaneInvalidError:
            self.assertTrue( True )
            
if __name__ == '__main__':
    unittest.main()