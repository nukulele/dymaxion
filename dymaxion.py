import sympy as s

from reportlab.pdfgen import canvas

from util.polyhedron import Icosahedron
from util.mapping import sx, sy, face_mappings
from util.space import rot_x, rot_y, rot_z, vector_3d, zero_3d, to_rad
from util.space import two_point_line


def make_map( filename ):

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
    # helpers
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

    def _map_point( point ):
        line = two_point_line( point, zero_3d )
        for hit in  d20.face_hit( line ):
            mapped_point = mappings.map_point( hit[0], hit[1] )
            if mapped_point:
                new_x, new_y = mapped_point
                c.circle( sx(new_x), sy(new_y), 1./72 )

    def _sphere_to_cart( theta, phi ):
        return vector_3d( \
            s.sin( theta ) * s.cos( phi ), \
            s.cos( theta ), \
            s.sin( theta ) * s.sin( phi ) )
            
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
    # main
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
            
    c = canvas.Canvas( filename, pagesize=( 17*72, 11*72 ) )
    d20 = Icosahedron( numeric = True )
    d20.rotate_vertices( rot_x( -s.atan2( s.GoldenRatio-1, s.GoldenRatio ).evalf() ) )
    d20.make_faces()
    mappings = face_mappings( d20 )
    
    inc_factor = (s.pi/180).evalf()
    az_factor = (s.pi/180).evalf()
    
    for inc_percent in range( 0, 180, 5 ):
        for az_percent in range( 90, 120, 5 ):
            point = _sphere_to_cart( inc_percent * inc_factor, az_percent * az_factor )
            _map_point( point )
                    
    c.line( sx( 0 ), sy( s.sqrt(3).evalf() ), sx( 1 ), sy( s.sqrt(3).evalf() ) )
    c.line( sx( 1 ), sy( s.sqrt(3).evalf() ), sx( 0.5 ), sy( s.sqrt(3).evalf() * 1.5 ) )
    c.line( sx( 0.5 ), sy( s.sqrt(3).evalf() * 1.5 ), sx( 0 ), sy( s.sqrt(3).evalf() ) )


    c.showPage()
    c.save()

if __name__ == '__main__':
    make_map( "this.pdf" )