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
        return ( new_point[0] + face[1], new_point[1] + face[2] )
                
def _icosahedron_mapping( ):

    def _make_rot_matrix( pole_angle, long_angle ):
        ret_matrix = rot_x( -0.6523581397843681859 ) 
        ret_matrix = ret_matrix.multiply( rot_y( pole_angle ) ).multiply( rot_x( 0.6523581397843681859 ) )
        ret_matrix = ret_matrix.multiply( rot_x( long_angle ) )
        
        return ret_matrix

    th = (s.sqrt(3)/2).evalf()
        
    ret_dict = dict()
    ret_dict['a'] = ( _make_rot_matrix( 0, -s.pi/2 ), 0.5, (th*7)/3 )
    ret_dict['e'] = ( _make_rot_matrix( 0, -0.841068670567930 ), 0.5, (th*5)/3 )
    # ret_dict['j'] = ( _make_rot_matrix( s.pi/5, s.pi/2 ), 1, (th*2)/3 )
    # ret_dict['n'] = ( _make_rot_matrix( s.pi/5, 0.841068670567930 ), 1, (th*2)/3 )
    ret_dict['f'] = ( _make_rot_matrix( 2*s.pi/5, -s.pi/2 ), 1.5, (th*7)/3 )
    ret_dict['o'] = ( _make_rot_matrix( 2*s.pi/5, -0.841068670567930 ), 1.5, (th*5)/3 )
    ret_dict['k'] = ( _make_rot_matrix( 4*s.pi/5, -s.pi/2 ), 2.5, (th*7)/3 )
    ret_dict['p'] = ( _make_rot_matrix( 4*s.pi/5, -0.841068670567930 ), 2.5, (th*5)/3 )
    # ret_dict['r'] = ( _make_rot_matrix( s.pi, s.pi/2 ), 3, (th*2)/3 )
    # ret_dict['q'] = ( _make_rot_matrix( s.pi, 0.841068670567930 ), 3, (th*2)/3 )
    ret_dict['g'] = ( _make_rot_matrix( 6*s.pi/5, -s.pi/2 ), 3.5, (th*7)/3 )
    ret_dict['l'] = ( _make_rot_matrix( 6*s.pi/5, -0.841068670567930 ), 3.5, (th*5)/3 )
    ret_dict['b'] = ( _make_rot_matrix( 8*s.pi/5, -s.pi/2 ), 4.5, (th*7)/3 )
    ret_dict['c'] = ( _make_rot_matrix( 8*s.pi/5, -0.841068670567930 ), 4.5, (th*5)/3 )
    return ret_dict
    
    