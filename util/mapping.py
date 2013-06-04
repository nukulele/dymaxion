import sympy as s

from util.space import rot_x, rot_y, rot_z

def sx( x ):
    '''maps x from theoretical space to postscript pixel coords'''
    return 216 * x + 18
    
def sy( y ):
    '''maps y from theoretical space to postscript pixel coords'''
    return 216 * y + 144

class face_mappings( object ):
    
    def __init__( self, poly ):
        self.face_dict = _icosahedron_mapping()

    def map_point( self, face_name, point ):
        if face_name not in self.face_dict:
            return None
        face = self.face_dict[ face_name ]
        new_point = point.multiply( face[0] )
        return ( new_point[0] + face[1], -new_point[1] + face[2] )
                
def _icosahedron_mapping( ):

    th = (s.sqrt(3)/2).evalf()
        
    ret_dict = dict()
    ret_dict['a'] = ( rot_x( s.pi/2 ), 0.5, (th*7)/3 )
    ret_dict['e'] = ( rot_x( 0 ), 0.5, (th*5)/3 )
    return ret_dict
    
    