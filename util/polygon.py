from util.space import Line, Plane
from util.space import vector_3d, zero_3d
from util.space import two_point_line, three_point_plane, line_plane_intersect

class InvalidPolygon( Exception ):
    pass

class Polygon( object ):

    # contains: list of vertices, list of edges (lines), polygon normal, list of edge normals

    def __init__( self, vertices = list(), precalculate = False ):
        self.normal = None
        self.vertices = vertices
        if precalculate:
            self._precalculate()
            
    def _precalculate( self ):
        
        num_vertices = len( self.vertices )
        if num_vertices < 3:
            raise InvalidPolygon
            # we don't check for planarity

        vert_list = list( self.vertices )
        vert_list.append( vert_list[0] )
        
        # calculate the polygon normal
        self.plane = three_point_plane( vert_list[0], vert_list[1], vert_list[2] )
        self.normal = self.plane.normal
        
        # calculate the (directed) edges
        self.edges = list()
        self.edge_normals = list()
        for x in range( num_vertices ):
            self.edges.append( two_point_line( vert_list[x], vert_list[x+1] ) )
            self.edge_normals.append( self.edges[x].v.cross( self.normal ) )            
                
    def contains_point( self, point ):
        if abs( self.plane.distance_to_point( point ).evalf() ) > self.plane.epsilon:
            return False
        for index in range( len( self.vertices ) ):
            if self.edge_normals[index].dot( point ) > \
                    self.edge_normals[index].dot( self.vertices[index] ):
                return False
        return True
        

    
