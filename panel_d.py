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

    def _sphere_to_cart( theta, phi, numeric = True ):
        ret_val = vector_3d( \
            s.sin( theta ) * s.cos( phi ), \
            s.cos( theta ), \
            s.sin( theta ) * s.sin( phi ) )
        if numeric:
            ret_val = ret_val.evalf()
        return ret_val

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

    face_plane = d20.faces[6].plane
    rot_mat = mappings.face_dict['g'][0]
  
    bag_o_points = dict()
    
    for lat in range( 35, 111, 5 ):
        for lon in range( 210, 271, 5 ):
            point = line_plane_intersect( two_point_line( \
                _sphere_to_cart( to_rad( lat ).evalf(), to_rad( lon ).evalf() ), zero_3d), face_plane, ray=True )
            mp = point.multiply( rot_mat )
            # c.circle( mp[0],mp[1],0.002,fill=1,stroke=0)
            bag_o_points[(lat,lon)] = mp
 
    for lat in range( 35, 109, 5 ):
        for lon in range( 210, 270, 5 ):
            p0 = bag_o_points[(lat, lon)]
            p1 = bag_o_points[(lat+5,lon)]
            p2 = bag_o_points[(lat,lon+5)]
            
            if lon % 5:
                c.setLineWidth( 0.0005 )
            else:
                c.setLineWidth( 0.001 )
            
            c.line( p0[0],p0[1],p1[0],p1[1] )
            
            if lat % 5:
                c.setLineWidth( 0.0005 )
            else:
                c.setLineWidth( 0.001 )
                
            c.line( p0[0],p0[1],p2[0],p2[1] )

    c.showPage()
    c.save()
    
if __name__ == '__main__':
    make_map( "panel_d.pdf" )        