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
        ret_matrix = rot_x( -axis_skew ) 
        ret_matrix = ret_matrix.multiply( rot_y( pole_angle ) ).multiply( rot_x( axis_skew ) )
        ret_matrix = ret_matrix.multiply( rot_x( long_angle ) )
        
        return ret_matrix.evalf()

    # some magic constants
    axis_skew = (s.pi/2 - s.atan2( s.GoldenRatio-1, s.GoldenRatio ) - s.atan2( 1, s.GoldenRatio )).evalf()
    th = (s.sqrt(3)/2).evalf()        
    face_angle = s.atan( s.sqrt( 5 )/2 ).evalf()

    ret_dict = dict()
    
    ret_dict['a'] = ( _make_rot_matrix( 0, -s.pi/2 ), 0.5, (th*7)/3 )
    ret_dict['e'] = ( _make_rot_matrix( 0, -face_angle ), 0.5, (th*5)/3 )
    ret_dict['f'] = ( _make_rot_matrix( 2*s.pi/5, -s.pi/2 ), 1.5, (th*7)/3 )
    ret_dict['o'] = ( _make_rot_matrix( 2*s.pi/5, -face_angle ), 1.5, (th*5)/3 )
    ret_dict['k'] = ( _make_rot_matrix( 4*s.pi/5, -s.pi/2 ), 2.5, (th*7)/3 )
    ret_dict['p'] = ( _make_rot_matrix( 4*s.pi/5, -face_angle ), 2.5, (th*5)/3 )
    ret_dict['g'] = ( _make_rot_matrix( 6*s.pi/5, -s.pi/2 ), 3.5, (th*7)/3 )
    ret_dict['l'] = ( _make_rot_matrix( 6*s.pi/5, -face_angle ), 3.5, (th*5)/3 )
    ret_dict['b'] = ( _make_rot_matrix( 8*s.pi/5, -s.pi/2 ), 4.5, (th*7)/3 )
    ret_dict['c'] = ( _make_rot_matrix( 8*s.pi/5, -face_angle ), 4.5, (th*5)/3 )
    
    flip_y = rot_y( s.pi )
    
    ret_dict['j'] = ( ret_dict['l'][0].multiply( flip_y ), 1, (th*4)/3 )
    ret_dict['n'] = ( ret_dict['g'][0].multiply( flip_y ), 1, (th*2)/3 )
    ret_dict['t'] = ( ret_dict['c'][0].multiply( flip_y ), 2, (th*4)/3 )
    ret_dict['s'] = ( ret_dict['b'][0].multiply( flip_y ), 2, (th*2)/3 )
    ret_dict['q'] = ( ret_dict['e'][0].multiply( flip_y ), 3, (th*4)/3 )
    ret_dict['r'] = ( ret_dict['a'][0].multiply( flip_y ), 3, (th*2)/3 )
    ret_dict['h'] = ( ret_dict['o'][0].multiply( flip_y ), 4, (th*4)/3 )
    ret_dict['m'] = ( ret_dict['f'][0].multiply( flip_y ), 4, (th*2)/3 )
    ret_dict['d'] = ( ret_dict['p'][0].multiply( flip_y ), 5, (th*4)/3 )
    ret_dict['i'] = ( ret_dict['k'][0].multiply( flip_y ), 5, (th*2)/3 )
    
    return ret_dict
    
    