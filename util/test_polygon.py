import sympy as s
import unittest

from util.space import vector_3d, v_x, v_y, v_z
from util.polygon import *

class TestPolygonConstruction( unittest.TestCase ):

    def test_poly_create( self ):
        '''create a polygon from a list of three vertices'''
        poly = Polygon( ( v_x, v_y, v_z ), precalculate = False )
        self.assertTrue( True )
        self.assertEqual( poly.normal, None )
        
    def test_poly_normal_1( self ):
        '''make sure normal is correct and oriented properly'''
        poly = Polygon( ( v_x, v_y, v_z ) )
        self.assertEqual( poly.normal, vector_3d(1,1,1) )
        
    def test_poly_normal_2( self ):
        '''make sure normal is reversed for polygon facing other way'''
        poly = Polygon( ( v_z, v_y, v_x ) )
        self.assertEqual( poly.normal, vector_3d(-1,-1,-1) )
        
    def test_precalculateds( self ):
        '''test the precalculated values for accuracy'''
        poly = Polygon( ( v_x, v_y, zero_3d ) )
        # coefficients of the plane
        self.assertEqual( poly.plane.A, 0 )
        self.assertEqual( poly.plane.B, 0 )
        self.assertEqual( poly.plane.C, 1 )
        self.assertEqual( poly.plane.D, 0 )
        # check third edge: p0 and v
        self.assertEqual( poly.edges[2].p0, zero_3d )
        self.assertEqual( poly.edges[2].v, v_x )
        # edge normals
        self.assertEqual( poly.edge_normals[2], vector_3d( 0,-1, 0 ) )
        
    def test_contains_point( self ):
        '''Check to see whether points are inside or outside the polygon'''    
        poly = Polygon( ( v_x, v_y, zero_3d ) )
        # include the vertices
        self.assertTrue( poly.contains_point( v_x ) )
        self.assertTrue( poly.contains_point( v_y ) )
        self.assertTrue( poly.contains_point( zero_3d ) )
        # check for out of plane
        self.assertFalse( poly.contains_point( v_z ) )
        self.assertFalse( poly.contains_point( v_z/10000 ) )
        self.assertFalse( poly.contains_point( v_x + v_z/10000 ) )
        self.assertFalse( poly.contains_point( v_x - v_z/10000 ) )
        # pairs straddle edges
        self.assertTrue( poly.contains_point( 50*(v_x+v_y)/101 ) )
        self.assertFalse( poly.contains_point( 51*(v_x+v_y)/101 ) )
        self.assertTrue( poly.contains_point( v_y/2 + v_x/101 ) )
        self.assertFalse( poly.contains_point( v_y/2 - v_x/101 ) )
        self.assertTrue( poly.contains_point( v_x/2 + v_y/101 ) )
        self.assertFalse( poly.contains_point( v_x/2 - v_y/101 ) )
 
