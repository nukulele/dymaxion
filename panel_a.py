import sympy as s

from util.pdf import get_letter_canvas, draw_hexes

from util.circle import three_point_circle

from util.polyhedron import Icosahedron
from util.mapping import sx, sy, face_mappings
from util.space import rot_x, rot_y, rot_z, vector_3d, zero_3d, to_rad
from util.space import two_point_line
from util.space import line_plane_intersect


_rt3 = s.sqrt(3).evalf()
_pi = s.pi.evalf()

def make_map( filename ):

    def _sphere_to_cart( theta, phi ):
        return vector_3d( \
            s.sin( theta ) * s.cos( phi ), \
            s.cos( theta ), \
            s.sin( theta ) * s.sin( phi ) )

    def _draw_this_circle( c, Circle ):
        pass
    
    def _draw_latitude_circle( c, latitude ):    
        pass
    
    def _draw_longitude_circle( c, longitude ):
        pass


    # set up our triangle
    c = get_letter_canvas( filename )

    # hex grid
    c.setStrokeColor( (0.75, 0.75, 1) )
    # c.setLineWidth( 0.001 )
    # draw_hexes( c, 2 )
    c.setLineWidth( 0.0005 )
    draw_hexes( c, 10 )

    c.setStrokeColor( (0.75,0.75,0.75) )
    d20 = Icosahedron( numeric = True )
    d20.rotate_vertices( rot_x( -s.atan2( s.GoldenRatio-1, s.GoldenRatio ).evalf() ) )
    d20.make_faces()
    mappings = face_mappings( d20 )

    face_plane = d20.faces[0].plane
    rot_mat = mappings.face_dict['a'][0]
 
    for lat in range( 0, 40, 5 ):
        if lat % 5:
            c.setLineWidth( 0.0005 )
        else:
            c.setLineWidth( 0.001 )

        lat_rad = to_rad( lat ).evalf()
        try:
            point = line_plane_intersect( two_point_line( zero_3d, _sphere_to_cart( lat_rad, 0 ) ), face_plane )
            mp1 = point.multiply( rot_mat )
            point = line_plane_intersect( two_point_line( zero_3d, _sphere_to_cart( lat_rad, _pi/2 ) ), face_plane )
            mp2 = point.multiply( rot_mat )
            point = line_plane_intersect( two_point_line( zero_3d, _sphere_to_cart( lat_rad, -_pi/2 ) ), face_plane )
            mp3 = point.multiply( rot_mat )
            
            the_circle = three_point_circle( mp1[0], mp1[1], mp2[0], mp2[1], mp3[0], mp3[1] )
            c.circle( the_circle.x0, the_circle.y0, the_circle.radius, fill=0, stroke=1 )
            
        except:
            pass
  
    for lon in range( 0, 360, 5 ):
    
        if lon % 5:
            c.setLineWidth( 0.0005 )
        else:
            c.setLineWidth( 0.001 )
        
        try:
            point = line_plane_intersect( two_point_line( _sphere_to_cart( _pi/4, to_rad( lon).evalf() ), zero_3d ), face_plane )
            mp1 = point.multiply( rot_mat )
            
            end_pt = _pi/9
            if (lon % 5) == 0:
                end_pt = _pi/18
            if (lon % 10) == 0:
                end_pt = _pi/36
            if (lon % 30) == 0:
                end_pt = 0
            
            point = line_plane_intersect( two_point_line( _sphere_to_cart( end_pt, to_rad( lon).evalf() ), zero_3d ), face_plane )
            mp2 = point.multiply( rot_mat )
            c.line( mp1[0], mp1[1], mp2[0], mp2[1] )
            
        except:
            pass
            
        


    c.showPage()
    c.save()
    
if __name__ == '__main__':
    make_map( "panel_a.pdf" )        
