from util.space import Line, Plane
from util.space import vector_3d, zero_3d
from util.space import two_point_line, three_point_plane, line_plane_intersect

class Polygon( object ):

    # contains: list of vertices, list of edges (lines), polygon normal, list of edge normals

    def __init__( self, vertices = list(), precalculate = False ):
        self.normal = None
        if precalculate:
            # pre-calculate normal, edges, edge normals
            pass    
        
    def _precalculate( self ):
        
        num_vertices = len( self.vertices )
        # if n < 3, puke

        vert_list = list( self.vertices )
        vert_list.append( vert_list[0] )
        
        # calculate the polygon normal
        plane = three_point_plane( vert_list[0], vert_list[1], vert_list[2] )
        self.normal = vector_3d( plane.A, plane.B, plane.C )
        
        # calculate the (directed) edges
        self.edges = list()
        self.edge_normals = list()
        for x in range( num_vertices ):
            self.edges.append( two_point_line( vert_list[x], vert_list[x+1] ) )
            # self.edge_normals.append( ... )            
        
        
    # contains_point

    