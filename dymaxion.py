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
        for hit in d20.face_hit( line ):
            # print hit[0]
            mapped_point = mappings.map_point( hit[0], hit[1] )
            if mapped_point:
                new_x, new_y = mapped_point
                c.circle( sx(new_x), sy(new_y), 1, stroke=0, fill=1  )

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
    
    c.setFillColorRGB( .5,.5, 1 )
    
    for inc_percent in range( 0, 90, 5 ):
        for az_percent in range( 0, 360, 5 ):
            point = _sphere_to_cart( inc_percent * inc_factor, az_percent * az_factor )
            _map_point( point )
    
    #_map_point( vector_3d( 0, 0.645497224367903, 0.577350269189626 ) )
    
    sr3 = s.sqrt(3).evalf()
    
    c.setLineWidth( 0.25 )                
    c.line( sx( 0 ), sy( sr3 ), sx( 1 ), sy( sr3 ) )
    c.line( sx( 1 ), sy( sr3 ), sx( 0.5 ), sy( sr3 * 1.5 ) )
    c.line( sx( 0.5 ), sy( sr3 * 1.5 ), sx( 0 ), sy( sr3 ) )
    c.line( sx( 0 ), sy( sr3 ), sx( 0.5 ), sy( sr3 *.5 ) )
    c.line( sx( 0.5 ), sy( sr3 *.5 ), sx( 1), sy( sr3 ) )


    c.showPage()
    c.save()

if __name__ == '__main__':
    make_map( "this.pdf" )