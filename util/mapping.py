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

    axis_skew = (s.pi/2 - s.atan2( s.GoldenRatio-1, s.GoldenRatio ) - s.atan2( 1, s.GoldenRatio )).evalf()

    def _make_rot_matrix( pole_angle, long_angle ):
        ret_matrix = rot_x( -axis_skew ) 
        ret_matrix = ret_matrix.multiply( rot_y( pole_angle ) ).multiply( rot_x( axis_skew ) )
        ret_matrix = ret_matrix.multiply( rot_x( long_angle ) )
        
        return ret_matrix.evalf()

    th = (s.sqrt(3)/2).evalf()
        
    ret_dict = dict()
    
    maladjust_q = -.454790578009723
    maladjust_r = .27
    
    ret_dict['a'] = ( _make_rot_matrix( 0, -s.pi/2 ), 0.5, (th*7)/3 )
    ret_dict['e'] = ( _make_rot_matrix( 0, -0.841068670567930 ), 0.5, (th*5)/3 )
    ret_dict['j'] = ( _make_rot_matrix( s.pi/5, maladjust_q ), 1, (th*4)/3 )
    ret_dict['n'] = ( _make_rot_matrix( s.pi/5, maladjust_r ), 1, (th*2)/3 )
    ret_dict['f'] = ( _make_rot_matrix( 2*s.pi/5, -s.pi/2 ), 1.5, (th*7)/3 )
    ret_dict['o'] = ( _make_rot_matrix( 2*s.pi/5, -0.841068670567930 ), 1.5, (th*5)/3 )
    ret_dict['t'] = ( _make_rot_matrix( 3*s.pi/5, maladjust_q ), 2, (th*4)/3 )
    ret_dict['s'] = ( _make_rot_matrix( 3*s.pi/5, maladjust_r ), 2, (th*2)/3 )
    ret_dict['k'] = ( _make_rot_matrix( 4*s.pi/5, -s.pi/2 ), 2.5, (th*7)/3 )
    ret_dict['p'] = ( _make_rot_matrix( 4*s.pi/5, -0.841068670567930 ), 2.5, (th*5)/3 )
    ret_dict['q'] = ( _make_rot_matrix( s.pi, maladjust_q ), 3, (th*4)/3 )
    ret_dict['r'] = ( _make_rot_matrix( s.pi, maladjust_r ), 3, (th*2)/3 )
    ret_dict['g'] = ( _make_rot_matrix( 6*s.pi/5, -s.pi/2 ), 3.5, (th*7)/3 )
    ret_dict['l'] = ( _make_rot_matrix( 6*s.pi/5, -0.841068670567930 ), 3.5, (th*5)/3 )
    ret_dict['h'] = ( _make_rot_matrix( 7*s.pi/5, maladjust_q ), 4, (th*4)/3 )
    ret_dict['m'] = ( _make_rot_matrix( 7*s.pi/5, maladjust_r ), 4, (th*2)/3 )
    ret_dict['b'] = ( _make_rot_matrix( 8*s.pi/5, -s.pi/2 ), 4.5, (th*7)/3 )
    ret_dict['c'] = ( _make_rot_matrix( 8*s.pi/5, -0.841068670567930 ), 4.5, (th*5)/3 )
    ret_dict['d'] = ( _make_rot_matrix( 9*s.pi/5, maladjust_q ), 5, (th*4)/3 )
    ret_dict['i'] = ( _make_rot_matrix( 9*s.pi/5, maladjust_r ), 5, (th*2)/3 )
    return ret_dict
    
    