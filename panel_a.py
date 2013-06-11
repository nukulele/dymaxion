import sympy as s

from util.pdf import get_letter_canvas

from util.circle import three_point_circle

from util.polyhedron import Icosahedron
from util.mapping import sx, sy, face_mappings
from util.space import rot_x, rot_y, rot_z, vector_3d, zero_3d, to_rad
from util.space import two_point_line

rt3 = s.sqrt(3).evalf()

def make_map( filename ):


    def _draw_this_circle( c, Circle ):
        pass
    
    def _draw_latitude_circle( c, latitude ):    
        pass
    
    def _draw_longitude_circle( c, longitude ):
        pass

    c = get_letter_canvas( filename )
        
    c.showPage()
    c.save()
    
if __name__ == '__main__':
    make_map( "panel_a.pdf" )        