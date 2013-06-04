from util.space import Line, Plane
from util.space import line_plane_intersect
from util.space import vector_3d, zero_3d

from util.polygon import Polygon

from util.space import NoInterceptError

from sympy import GoldenRatio, Rational

class Hedron( object ):

    def __init__( self, numeric = False ):
        self._set_vertices()
        if numeric:
            float_verts = [v.evalf() for v in self.vertices]
            self.vertices = float_verts
        
    def _set_vertices( self ):
        pass

    def rotate_vertices( self, rot_matrix ):
        self.vertices = [v.multiply( rot_matrix ) for v in self.vertices]

    def face_hit( self, line ):
    
        ret_list = list()
        for face in self.faces:
            try: 
                intersect = line_plane_intersect( line, face.plane, ray=True )
                if face.contains_point( intersect ):
                    ret_list.append( (face.name, intersect ) )
                    pass
            except NoInterceptError:
                continue
        return ret_list

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
            Polygon( ( self.vertices[0], self.vertices[1], self.vertices[2]), name="a" ),
            Polygon( ( self.vertices[3], self.vertices[0], self.vertices[2]), name="b"),
            Polygon( ( self.vertices[3], self.vertices[1], self.vertices[0]), name="c" ),
            Polygon( ( self.vertices[2], self.vertices[1], self.vertices[3]), name="d" ),
        )            

class Cube( Hedron ):
    
    def _set_vertices( self ):
        self.vertices = (
            vector_3d( -1,-1,-1 ),
            vector_3d( -1,-1,1 ),
            vector_3d( -1,1,-1 ),
            vector_3d( -1,1,1 ),
            vector_3d( 1,-1,-1 ),
            vector_3d( 1,-1,1 ),
            vector_3d( 1,1,-1 ),
            vector_3d( 1,1,1 ),
        )
        
    def make_faces( self ):
        self.faces = (
            Polygon( ( self.vertices[1], self.vertices[5], self.vertices[7], self.vertices[3]), name="a" ),
            Polygon( ( self.vertices[4], self.vertices[6], self.vertices[7], self.vertices[5]), name="b" ),
            Polygon( ( self.vertices[2], self.vertices[3], self.vertices[7], self.vertices[6]), name="c" ),
            Polygon( ( self.vertices[0], self.vertices[2], self.vertices[6], self.vertices[4]), name="d" ),
            Polygon( ( self.vertices[0], self.vertices[4], self.vertices[5], self.vertices[1]), name="e" ),
            Polygon( ( self.vertices[0], self.vertices[1], self.vertices[3], self.vertices[2]), name="f" ),
        )            

class Icosahedron( Hedron ):

    def _set_vertices( self ):
        half = Rational(1,2)
        half_phi = (GoldenRatio / 2)
        # half = .5
        # half_phi = (GoldenRatio / 2).evalf()
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
            Polygon( ( self.vertices[0], self.vertices[1], self.vertices[2]), name="a" ),
            Polygon( ( self.vertices[0], self.vertices[2], self.vertices[3]), name="b" ),
            Polygon( ( self.vertices[0], self.vertices[3], self.vertices[4]), name="c" ),
            Polygon( ( self.vertices[0], self.vertices[4], self.vertices[5]), name="d" ),
            Polygon( ( self.vertices[0], self.vertices[5], self.vertices[1]), name="e" ),

            Polygon( ( self.vertices[1], self.vertices[6], self.vertices[2]), name="f" ),
            Polygon( ( self.vertices[2], self.vertices[7], self.vertices[3]), name="g" ),
            Polygon( ( self.vertices[3], self.vertices[8], self.vertices[4]), name="h" ),
            Polygon( ( self.vertices[4], self.vertices[9], self.vertices[5]), name="i" ),
            Polygon( ( self.vertices[5], self.vertices[10], self.vertices[1]), name="j" ),

            Polygon( ( self.vertices[6], self.vertices[7], self.vertices[2]), name="k" ),
            Polygon( ( self.vertices[7], self.vertices[8], self.vertices[3]), name="l" ),
            Polygon( ( self.vertices[8], self.vertices[9], self.vertices[4]), name="m" ),
            Polygon( ( self.vertices[9], self.vertices[10], self.vertices[5]), name="n" ),
            Polygon( ( self.vertices[10], self.vertices[6], self.vertices[1]), name="o" ),

            Polygon( ( self.vertices[6], self.vertices[11], self.vertices[7]), name="p" ),
            Polygon( ( self.vertices[7], self.vertices[11], self.vertices[8]), name="q" ),
            Polygon( ( self.vertices[8], self.vertices[11], self.vertices[9]), name="r" ),
            Polygon( ( self.vertices[9], self.vertices[11], self.vertices[10]), name="s" ),
            Polygon( ( self.vertices[10], self.vertices[11], self.vertices[6]), name="t" )
        )

