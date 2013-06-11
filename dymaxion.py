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
                c.circle( sx(new_x), sy(new_y), 0.5, stroke=0, fill=1  )

    def _sphere_to_cart( theta, phi ):
        return vector_3d( \
            s.sin( theta ) * s.cos( phi ), \
            s.cos( theta ), \
            s.sin( theta ) * s.sin( phi ) )
            
    def _arc_azimuth( start_az, end_az, inclin, step ):
        for azimuth in range( start_az, end_az, step ):
            _map_point( _sphere_to_cart( to_rad( inclin ).evalf(), to_rad(azimuth).evalf() ))
    
    def _arc_inclin(  start_inc, end_inc, azimuth, step ):
        for inclin in range( start_inc, end_inc, step ):
            _map_point( _sphere_to_cart( to_rad( inclin ).evalf(), to_rad(azimuth).evalf() ))
            
    def _plot_skeleton():
        th = (s.sqrt(3)/2).evalf()

        c.line( sx(0), sy(2 * th) , sx(0.5), sy(3 * th) )
        c.line( sx(0.5), sy(th) , sx(1.5), sy(3 * th) )
        c.line( sx(1), sy(0) , sx(2.5), sy(3 * th) )
        c.line( sx(2), sy(0) , sx(3.5), sy(3 * th) )
        c.line( sx(3), sy(0) , sx(4.5), sy(3 * th) )
        c.line( sx(4), sy(0) , sx(5), sy(2 * th) )
        c.line( sx(5), sy(0) , sx(5.5), sy(th) )

        c.line( sx(0), sy( 2 * th ), sx(1), sy(0) )        
        c.line( sx(0.5), sy( 3 * th ), sx(2), sy(0) )        
        c.line( sx(1.5), sy( 3 * th ), sx(3), sy(0) )        
        c.line( sx(2.5), sy( 3 * th ), sx(4), sy(0) )        
        c.line( sx(3.5), sy( 3 * th ), sx(5), sy(0) )        
        c.line( sx(4.5), sy( 3 * th ), sx(5.5), sy( th ) )   
        
        c.line( sx(0), sy( 2 * th), sx( 5 ), sy( 2*th ) )     
        c.line( sx(0.5), sy(th), sx( 5.5 ), sy( th ) )     
            
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
    
    for azimuth in range( 0, 360, 5 ):
         _arc_inclin( 20, 161, azimuth, 1 )
    
    for inclin in range( 20, 161, 5 ):
         _arc_azimuth( 0, 360, inclin, 1 )
    
    c.setStrokeColorRGB( .5,.5, .5 )    
    _plot_skeleton()

    c.showPage()
    c.save()

if __name__ == '__main__':
    make_map( "this.pdf" )