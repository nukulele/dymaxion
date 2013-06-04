import sympy as s
import unittest

from util.polyhedron import *
from util.space import zero_3d, v_x, v_y, v_z
from util.space import two_point_line
from util.space import rot_x, rot_y, rot_z

class TestPolyhedron( unittest.TestCase ):

    def test_make_tetrahedron( self ):
        d4 = Tetrahedron()
        self.assertEqual( len( d4.vertices ), 4 )
        d4.make_faces()
        self.assertEqual( d4.faces[2].normal, \
            -4 * (v_x + v_y + v_z) \
            )
            
    def test_cube_hits( self ):
        d6 = Icosahedron( numeric = True )
        d6.rotate_vertices( rot_x( -s.atan2( s.GoldenRatio-1, s.GoldenRatio ).evalf() ) )
        d6.make_faces()
        print d6.face_hit( two_point_line( v_x, zero_3d))
        print d6.face_hit( two_point_line( -v_x, zero_3d))
        print d6.face_hit( two_point_line( v_y, zero_3d))
        print d6.face_hit( two_point_line( -v_y, zero_3d))
        print d6.face_hit( two_point_line( v_z, zero_3d))
        print d6.face_hit( two_point_line( -v_z, zero_3d))
        print d6.face_hit( two_point_line( v_x+v_y+v_z, zero_3d))
        print d6.face_hit( two_point_line( v_x+v_y-v_z, zero_3d))
        print d6.face_hit( two_point_line( v_x-v_y+v_z, zero_3d))
        print d6.face_hit( two_point_line( v_x-v_y-v_z, zero_3d))
        print d6.face_hit( two_point_line( -v_x+v_y+v_z, zero_3d))
        print d6.face_hit( two_point_line( -v_x+v_y-v_z, zero_3d))
        print d6.face_hit( two_point_line( -v_x-v_y+v_z, zero_3d))
        print d6.face_hit( two_point_line( -v_x-v_y-v_z, zero_3d))

        