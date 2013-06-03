import sympy as s
import unittest

from util.polyhedron import *
from util.space import zero_3d, v_x, v_y, v_z, two_point_line
from util.space import rot_x, rot_y, rot_z

class TestTetrahedron( unittest.TestCase ):

    def test_make_tetrahedron( self ):
        d4 = Tetrahedron()
        self.assertEqual( len( d4.vertices ), 4 )
        d4.make_faces()
        self.assertEqual( d4.faces[2].normal, \
            -4 * (v_x + v_y + v_z) \
            )
            
    def test_face_hits_tetrahedron( self ):
        d4 = Icosahedron( numeric = True )
        d4.make_faces()
        # start from outside the polyhedron!
        d4.face_hit( two_point_line( v_z, zero_3d))
        