from util.space import Line, Plane
from util.space import vector_3d, zero_3d

from util.polygon import Polygon

from sympy import GoldenRatio, Rational

class Hedron( object ):
    def __init__( self ):
        self._set_vertices()
        
    def _set_vertices( self ):
        pass

    def rotate_vertices( self, rot_matrix ):
        self.vertices = [v.multiply( rot_matrix ) for v in self.vertices]

class Tetrahedron( Hedron ):
    
    def _set_vertices( self ):
        self.vertices = ( 
            vector_3d( -1,-1,1 ),
            vector_3d( 1,-1,-1 ),
            vector_3d( 1,1,1 ),
            vector_3d( -1,1,-1 )
        )
            
    def make_faces( self ):
        self.faces = (
            Polygon( ( self.vertices[0], self.vertices[1], self.vertices[2]), precalculate=True ),
            Polygon( ( self.vertices[3], self.vertices[0], self.vertices[2]), precalculate=True ),
            Polygon( ( self.vertices[3], self.vertices[1], self.vertices[0]), precalculate=True ),
            Polygon( ( self.vertices[2], self.vertices[1], self.vertices[3]), precalculate=True ),
        )            

class Icosahedron( Hedron ):

    def _set_vertices( self ):
        half = Rational(1,2)
        half_phi = (GoldenRatio / 2)
        self.vertices = ( 
            vector_3d( -half, half_phi, 0 ),
            vector_3d( half, half_phi, 0 ),
            vector_3d( 0, half, -half_phi ),
            vector_3d( -half_phi, 0, -half ),
            vector_3d( -half_phi, 0, half  ),
            vector_3d( 0, half, half_phi ),
            vector_3d( half_phi, 0, -half ),
            vector_3d( 0, -half, -half_phi ),
            vector_3d( -half, -half_phi, 0 ),
            vector_3d( 0, -half, half_phi ),
            vector_3d( half_phi, 0, half ),
            vector_3d( half, -half_phi, 0 )
        )
            
    def make_faces( self ):
        self.faces = (
            Polygon( ( self.vertices[0], self.vertices[1], self.vertices[2]), precalculate=True ),
            Polygon( ( self.vertices[0], self.vertices[2], self.vertices[3]), precalculate=True ),
            Polygon( ( self.vertices[0], self.vertices[3], self.vertices[4]), precalculate=True ),
            Polygon( ( self.vertices[0], self.vertices[4], self.vertices[5]), precalculate=True ),
            Polygon( ( self.vertices[0], self.vertices[5], self.vertices[1]), precalculate=True ),

            Polygon( ( self.vertices[1], self.vertices[6], self.vertices[2]), precalculate=True ),
            Polygon( ( self.vertices[2], self.vertices[7], self.vertices[3]), precalculate=True ),
            Polygon( ( self.vertices[3], self.vertices[8], self.vertices[4]), precalculate=True ),
            Polygon( ( self.vertices[4], self.vertices[9], self.vertices[5]), precalculate=True ),
            Polygon( ( self.vertices[5], self.vertices[10], self.vertices[1]), precalculate=True ),

            Polygon( ( self.vertices[6], self.vertices[7], self.vertices[2]), precalculate=True ),
            Polygon( ( self.vertices[7], self.vertices[8], self.vertices[3]), precalculate=True ),
            Polygon( ( self.vertices[8], self.vertices[9], self.vertices[4]), precalculate=True ),
            Polygon( ( self.vertices[9], self.vertices[10], self.vertices[5]), precalculate=True ),
            Polygon( ( self.vertices[10], self.vertices[6], self.vertices[1]), precalculate=True ),

            Polygon( ( self.vertices[6], self.vertices[11], self.vertices[7]), precalculate=True ),
            Polygon( ( self.vertices[7], self.vertices[11], self.vertices[8]), precalculate=True ),
            Polygon( ( self.vertices[8], self.vertices[11], self.vertices[9]), precalculate=True ),
            Polygon( ( self.vertices[9], self.vertices[11], self.vertices[10]), precalculate=True ),
            Polygon( ( self.vertices[10], self.vertices[11], self.vertices[6]), precalculate=True )
        )

